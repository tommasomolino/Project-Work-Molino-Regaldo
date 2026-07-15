# Devlog

---

## Entry

### Settimana 1 — [21 - 28 giugno]

Prima di tutto abbiamo cercato di capire con chi fare gruppo.
Abbiamo deciso di lavorare insieme (Marco & Tommaso) perché condividiamo le stesse problematiche a livello di programmazione.
Condividiamo la stessa curiosità e voglia di metterci in gioco. 
Abbiamo letto le proposte indicate dal professore e abbiamo scelto di sviluppare uno strumento che ci possa tornare utile nel futuro.

### Settimana 2 — [29 giugno - 5 luglio]

La nostra idea per il progetto è stata visionata dal professore.
Basandoci sulle sue considerazioni abbiamo scelto di ridurre lo scope dei 7 tool ipotizzati in proposta.md a 3 ben strutturati.
L'obiettivo è approfondire i seguenti tool invece di farne tanti superficiali: PortScanner, IPCalculator, DNSLookup. 
Scartati i seguenti tool: HTTPHeaders, WhoisLookup, PingTool, HashCalculator.

### Settimana 3 — [6 - 12 luglio]

Creata classe base in tool.py e imbastita sottoclasse port_scanner.py.
Imparato a utilizzare il costruttore super()__init__ per una sottoclasse.
Implementazione nella sottoclasse PortScanner il metodo execute() sull'analisi di una porta specifica.

### Settimana 4 — [13 -19 luglio]

Implementato il tool DNSLookup con record A come sottoclasse di Tool. Aggiunti record AAAA, MX e TXT.
Generato il __main__.py e in seguito modificato a mano.
Difficoltà nell'evitare che gli errori si sovrascrivessero, risolto tramite dizionari distinti (record_status e dns_results).
Gestione degli errori di query DNS. Validazione degli input e test su entrambi i tool (Portscanner e DNS Lookup).


---

## Bilancio finale

Alla consegna, una entry di bilancio (30-50 righe). Spunti: di cosa siete più soddisfatti,
cosa avete capito di nuovo, cosa avete sottovalutato all'inizio, cosa rifareste diversamente,
se la divisione del lavoro è stata equa, cosa avreste aggiunto con un'altra settimana, e —
onestamente — che voto dareste al vostro progetto e perché.
