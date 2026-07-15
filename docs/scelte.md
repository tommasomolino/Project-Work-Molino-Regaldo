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

Per i record mancanti avevamo inizialmente previsto di sostituire l’intero risultato con un messaggio di errore. Questa soluzione è stata abbandonata perché, durante una ricerca multipla, avrebbe cancellato i record già trovati.
