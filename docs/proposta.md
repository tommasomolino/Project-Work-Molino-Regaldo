# Proposta di progetto

> Una pagina, da far approvare al docente **prima** di scrivere codice. Una volta
> approvata, resta nel repository come traccia del punto di partenza (e si confronta
> con quello che hai effettivamente realizzato).

## Titolo provvisorio

Network Toolkit

## Gruppo

- Tommaso Molino
- Marco Giacomo Regaldo

## Cosa fa (5-6 righe)

La nostra idea è quella di scrivere un programma che faccia da "coltellino svizzero" per l'analisi di un indirizzo in rete.

Perciò l'idea è di avere un singolo tool che possa eseguire diverse funzioni di scanning e che vengano salvati in un formato strutturato JSON. La scaletta delle varie funzionalità è ambiziosa e in ordine di difficoltà crescente, partiamo dal basso e vediamo quanto riusciamo a spingerci oltre.

Network Toolkit:
-  PingTool
-  PortScanner
- DNSLookup
- HTTPHeaders
- WhoisLookup
- IPCalculator
- HashCalculator

## A chi serve / quale problema reale risolve

Crediamo che questo progetto possa anche servirci in futuro (se tutto va come lo abbiamo immaginato) e che tocchi argomenti specifici del nostro corso.


## Competenze del corso messe in gioco

- Versioning di Git
- Programmazione ad oggetti ed ereditarietà (il tool può subire implementazioni)
- Gestione di eccezioni
- JSON

## Gerarchia di ereditarietà prevista

- Classe base Toolkit
	- Una sottoclasse per Tool
	- PingTool
	- PortScannerTool
	- DNSTool
	- HTTPHeadersTool
	- .....

Il metodo polimorfico principale sarà:
>execute(target)

Così ogni sottoclasse lo ridefinisce in base al tool.

## Piano di massima (fasi)

### Fase 1

- struttura del progetto
- classe base Tool
### Fase 2

- PingTool
### Fase 3

- PortScannerTool

### Fase 4

- DNSTool
### Fase 5

- HTTPHeadersTool
### Fase 6

- Gestione errori
### Fase 7

- Test con pytest

**A metà percorso conto di avere pronto:** _…_

## Estensione avanzata che vorrei tentare

_Almeno una, per puntare sopra la sufficienza._
