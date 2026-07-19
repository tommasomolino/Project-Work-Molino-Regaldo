### Progettazione del DNSLookup

La classe `DNSLookup` è stata implementata come sottoclasse di `Tool`. Il dominio da interrogare viene passato al metodo polimorfico `execute(target)`, mentre i tipi di record DNS vengono forniti al costruttore come configurazione dell’oggetto.

Abbiamo scelto questa distinzione perché il dominio rappresenta il bersaglio dell’operazione e può cambiare a ogni esecuzione, mentre l’elenco dei record stabilisce il comportamento del particolare oggetto `DNSLookup`. La stessa istanza può quindi interrogare domini diversi mantenendo la stessa configurazione.

Per effettuare le interrogazioni DNS abbiamo scelto la libreria `dnspython`, utilizzando il modulo `dns.resolver`. La libreria permette di interrogare direttamente diversi tipi di record e fornisce eccezioni specifiche per i principali errori di risoluzione.

La prima versione del componente supportava solamente i record `A`. In seguito il funzionamento è stato esteso ai record:

* `A`, per gli indirizzi IPv4;
* `AAAA`, per gli indirizzi IPv6;
* `MX`, per i server di posta;
* `TXT`, per i record testuali.

L’utente può richiedere un solo record, più record separati da virgola oppure tutti i record supportati tramite l’opzione `ALL`.

I tipi richiesti vengono conservati in una lista. Durante `execute()` la classe esegue una query per ogni tipo e costruisce due dizionari paralleli:

* `esito`, contenente lo stato di ogni interrogazione;
* `risultato`, contenente le liste di valori restituiti per ciascun record.

Questa struttura è stata preferita a un unico messaggio generale perché una query multipla può riuscire per alcuni record e fallire per altri. Per esempio, un dominio può possedere record `A` ma non record `MX`.

I valori restituiti da `dnspython` vengono convertiti in stringhe tramite `to_text()`. In questo modo il report contiene dati leggibili e utilizzabili anche per una futura esportazione in JSON.

### Gestione degli errori DNS

Gli errori vengono distinti in base alla loro portata.

`NXDOMAIN` indica che il dominio non esiste. Poiché il problema riguarda il dominio e non un singolo tipo di record, il metodo interrompe subito l’esecuzione e restituisce un errore generale.

`NoAnswer` indica invece che il dominio esiste ma non contiene il record richiesto. In questo caso l’esecuzione continua sugli altri record, l’esito del singolo record segnala l’assenza e il relativo risultato viene rappresentato con una lista vuota.

Anche `Timeout` e `NoNameservers` vengono associati al singolo record, permettendo al programma di tentare comunque le altre interrogazioni richieste.

Abbiamo deciso che `risultato` deve contenere esclusivamente dati DNS o liste vuote. I messaggi di errore e i dettagli tecnici vengono quindi conservati in `esito`, evitando di mescolare risultati validi e oggetti eccezione.

### Validazione dell’input

La validazione dell’input dell’utente viene svolta nel file principale prima della creazione di `DNSLookup`.

Il programma:

* converte la scelta in maiuscolo;
* separa più record tramite la virgola;
* elimina gli spazi superflui;
* verifica che ogni valore appartenga all’elenco dei record supportati;
* rifiuta input vuoti o record sconosciuti;
* converte `ALL` nell’elenco completo dei record disponibili.

Abbiamo mantenuto questa validazione nel livello di interazione con l’utente perché la classe `DNSLookup` deve occuparsi della risoluzione DNS e non della lettura da terminale.

### Alternative scartate

Inizialmente avevamo considerato di passare il dominio direttamente al costruttore. Abbiamo scartato questa soluzione perché avrebbe reso l’interfaccia di `DNSLookup` meno coerente con le altre sottoclassi di `Tool`: il bersaglio deve essere passato uniformemente tramite `execute(target)`.

Abbiamo inoltre evitato di inserire chiamate a `input()` dentro `DNSLookup`. In questo modo la classe può essere utilizzata anche da test automatici, da altri moduli o da una futura interfaccia diversa dalla CLI.

Per i record mancanti avevamo inizialmente previsto di sostituire l’intero risultato con un messaggio di errore. Questa soluzione è stata abbandonata perché, durante una ricerca multipla, avrebbe cancellato i record già trovati

### Validazione dell'input per PortScanner e IpCalculator

Anche per `PortScanner` e `IpCalculator`, come già per `DNSLookup`, una parte della validazione dell'input resta in `__main__.py` invece di essere spostata nelle classi — ma non tutta, e per motivi diversi da tool a tool.

Per `PortScanner`, `__main__.py` verifica che la porta iniziale non sia maggiore di quella finale **prima** di costruire l'intervallo (`range(start_port, end_port + 1)`): se questo controllo mancasse, `range()` non solleverebbe alcun errore ma produrrebbe silenziosamente un intervallo vuoto, e la scansione richiesta dall'utente verrebbe ignorata senza alcuna spiegazione. Il controllo sui singoli valori di porta (0-65535) e sul timeout, invece, resta nel costruttore di `PortScanner`: è configurazione dello strumento, non dipende dall'input testuale dell'utente, e deve restare valida anche se lo strumento viene creato da un contesto diverso dalla CLI (per esempio un test automatico).

Per `IpCalculator`, il controllo "il numero di host deve essere maggiore di zero" è presente **sia** in `__main__.py` **sia** dentro `IpCalculator.execute()` — è una duplicazione voluta, non una svista. In `__main__.py` il controllo produce un messaggio mirato al singolo valore che ha fallito (es. `-5 non è un valore valido: deve essere maggiore di zero.`); dentro `execute()` lo stesso controllo viene rifatto e intercettato come `ValueError` generico (con il messaggio meno preciso descritto sopra in "Comportamento noto"). Il controllo in `__main__.py` esiste per dare all'utente da terminale un errore chiaro e immediato; quello dentro `execute()` resta comunque necessario perché la classe deve rimanere corretta anche se chiamata da un contesto che non passa dalla validazione di `__main__.py` — come, appunto, i test automatici in `tests/test_ip_calculator.py`.

### Progettazione di IpCalculator

`IpCalculator` è stata implementata come sottoclasse di `Tool`. A differenza di `DNSLookup`, il costruttore non riceve alcuna configurazione fissa oltre al `tool_name`: sia l'indirizzo di rete (`target`) sia l'elenco degli host richiesti per ogni sottorete cambiano a ogni calcolo, quindi vengono passati entrambi al metodo `execute(target, host_requirements)` invece di essere fissati all'istanziazione.

Per la manipolazione degli indirizzi abbiamo scelto il modulo standard `ipaddress`, che fornisce già la rappresentazione di reti/indirizzi IPv4 e i controlli di validità sintattica, evitando di reimplementare da zero il parsing della notazione CIDR.

L'algoritmo di suddivisione segue la tecnica VLSM (Variable Length Subnet Masking): gli host richiesti vengono ordinati in ordine decrescente e per ciascun valore si calcola il numero minimo di bit necessari a ospitarlo (`math.ceil(math.log2(host + 2))`, il `+2` tiene conto degli indirizzi di rete e broadcast riservati in ogni sottorete). Si parte dal requisito più grande per evitare frammentazione dello spazio di indirizzi: partire dalle sottoreti più piccole lascerebbe spesso "buchi" troppo piccoli per i requisiti più grandi rimasti da allocare.

Un "cursore" (`cursor`) tiene traccia del primo indirizzo libero e avanza dopo ogni sottorete allocata (`subnet.broadcast_address + 1`), garantendo che le sottoreti calcolate non si sovrappongano.

### Gestione degli errori in IpCalculator

Il metodo usa un blocco `try/except/else`: il ramo `try` esegue il calcolo, `except ValueError` intercetta sia un `target` non valido (sollevato da `ipaddress.ip_network`) sia un numero di host ≤ 0 (controllo esplicito), `else` imposta l'esito di successo solo se nessuna eccezione è stata sollevata. Il caso di spazio esaurito (la sottorete calcolata non rientra più nella rete di partenza) non è un'eccezione ma un ritorno anticipato con esito di fallimento, perché è una condizione prevista del dominio del problema, non un errore di programmazione.

**Comportamento noto**: il controllo `host <= 0` si trova all'interno dello stesso blocco `try` che gestisce la validità dell'indirizzo di rete, quindi la sua eccezione viene catturata dallo stesso `except ValueError`. Di conseguenza il messaggio finale in `risultato` inizia sempre con il prefisso `"L'indirizzo di rete inserito non è valido: "`, anche quando il problema riguarda gli host. Il messaggio fa inoltre riferimento all'intera lista `host_requirements`, non al singolo valore che ha fallito il controllo. Abbiamo scelto di non modificare questo comportamento in questa fase del progetto, documentandolo qui e verificandolo esplicitamente nei test automatici (`tests/test_ip_calculator.py`).

### Progettazione di PortScanner

`PortScanner` è stata implementata come sottoclasse di `Tool`. Il costruttore riceve, oltre al `tool_name`, l'intervallo di porte da scandire (`port_range`) e il timeout di connessione (`timeout`): entrambi sono considerati configurazione dello strumento (valgono per tutta la vita dell'oggetto), mentre il `target` viene passato a `execute()`, coerentemente con l'interfaccia comune di `Tool`.

Il costruttore valida subito i parametri ricevuti: ogni valore in `port_range` deve stare nell'intervallo 0-65535 (i limiti delle porte TCP), e `timeout` deve essere positivo. Validare in `__init__` invece che in `execute()` fa fallire subito la creazione di uno scanner mal configurato, prima di qualunque tentativo di connessione.

Per la scansione abbiamo usato il modulo standard `socket`, aprendo una connessione TCP per ogni porta dell'intervallo, con timeout impostato tramite `settimeout()`. Il parametro `verbose` di `execute()` controlla solo la stampa a schermo porta per porta durante la scansione, ma non influisce sul contenuto del report restituito.

### Gestione degli errori in PortScanner

Le eccezioni sollevate durante la connessione vengono distinte per tipo: `ConnectionRefusedError` indica una porta chiusa (l'host ha risposto rifiutando la connessione), `TimeoutError` indica che non è arrivata risposta entro il timeout (porta filtrata o host irraggiungibile), `OSError` copre altri errori di rete generici e viene trattata come porta chiusa. Le porte vengono classificate in tre liste separate (aperte, chiuse, in timeout) e riassunte in un unico messaggio testuale in `risultato`.

### Perché report_exporter.py non è una classe né una sottoclasse di Tool

`export_report(report, file_path)` è rimasta una funzione libera, non un metodo di `Tool` né una classe a sé stante. La domanda ce la siamo posti esplicitamente, usando lo stesso criterio con cui valutiamo se serve una classe: un oggetto ha senso quando esiste uno **stato** (attributi che devono essere ricordati tra una chiamata e l'altra) e un **comportamento polimorfico** (più varianti dello stesso metodo che si comportano diversamente). `export_report` non ha né l'uno né l'altro: riceve tutto ciò che le serve tramite i parametri a ogni chiamata, e fa sempre la stessa identica cosa (serializzare un dizionario in JSON con `json.dump`), qualunque sia lo strumento che ha prodotto quel dizionario.

Questo è anche il motivo per cui `report_exporter.py` non importa `Tool` né alcuna sua sottoclasse. Il metodo `execute()` di ogni sottoclasse di `Tool` restituisce sempre un semplice `dict` (mai `self`, come esplicitato dall'annotazione `-> dict`): una volta che `__main__.py` ha ricevuto quel dizionario, l'oggetto `Tool`/`DNSLookup`/`PortScanner`/`IpCalculator` che l'ha generato non serve più. `export_report` lavora quindi su un dato "puro" — un dizionario fatto di stringhe, numeri e liste — e non sull'istanza che lo ha prodotto.

Questa scelta realizza un **basso accoppiamento** tra l'esportazione e la gerarchia degli strumenti: il contratto di `export_report` è "dammi un dizionario serializzabile in JSON", non "dammi un `Tool`". Aggiungere un quarto strumento in futuro non richiederà nessuna modifica a `report_exporter.py`, perché la funzione non sa (e non ha bisogno di sapere) da dove arrivi il report.

