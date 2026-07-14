# Devlog

> Diario di bordo del gruppo. **Una entry a settimana** (minimo tre nel corso del progetto),
> 15-30 righe l'una, in prima persona plurale, **scritte da voi** (non dall'IA).

## Come si scrive

Tecnico e onesto: cosa avete fatto (fatti, non aspirazioni), cosa vi ha fatto perdere tempo,
cosa avete imparato, quali decisioni avete preso e perché, come vi siete divisi il lavoro.
Se una settimana non avete combinato niente, scrivetelo. Se vi siete bloccati tre giorni su
un bug, raccontate il bug. Le date delle entry vengono confrontate con il `git log`.

Ogni entry dovrebbe toccare almeno tre di questi punti:

- cosa abbiamo fatto questa settimana;
- cosa ci ha fatto perdere tempo e perché;
- cosa abbiamo imparato di nuovo (tecnicamente o organizzativamente);
- decisioni prese: cosa abbiamo scelto, perché, cosa abbiamo scartato;
- cosa pianifichiamo per la settimana prossima;
- divisione del lavoro: chi sta facendo cosa.

---

## Entry

### Settimana 1 — [fine giugno]

Prima di tutto abbiamo cercato di capire con chi fare gruppo.
Abbiamo deciso di lavorare insieme (Marco & Tommaso) perchè condividiamo le stesse problematiche a livello di programmazione.
Condividiamo la stessa curiosità e voglia di metterci in gioco. 
Abbiamo letto le proposte indicate dal professore e abbiamo scelto di sviluppare uno strumento che ci possa tornare utile nel futuro.

### Settimana 2 — [inizio luglio]

La nostra idea per il progetto è stata visionata dal professore.
Basandoci sulle sue condiderazioni abbiamo scelto di ridurre lo scope dei 7 tool ipotizzati in proposta.md a 3 ben strutturati.
L'obiettivo è approfondire ciascuno di questi tool invece di fare tanti tool superficiali: PortScanner, IPCalculator, DNSLookup. 
Scartati i seguenti tool: HTTPHeaders, WhoisLookup, PingTool, HashCalculator.

### Settimana 3 — [seconda settimana - luglio]

Creata classe base in tool.py e imbastita sottoclasse port_scanner.py.
Imparato a utilizzare il costruttore super()__ini__ per una sottoclasse.
Implementazione nella sottoclasse PortScanner il metodo execute() sull'analisi di una porta specifica.

---

## Bilancio finale

Alla consegna, una entry di bilancio (30-50 righe). Spunti: di cosa siete più soddisfatti,
cosa avete capito di nuovo, cosa avete sottovalutato all'inizio, cosa rifareste diversamente,
se la divisione del lavoro è stata equa, cosa avreste aggiunto con un'altra settimana, e —
onestamente — che voto dareste al vostro progetto e perché.
