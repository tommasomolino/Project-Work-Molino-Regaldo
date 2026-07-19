# Network Toolkit

## Cosa fa

Network Toolkit è uno strumento da riga di comando pensato per svolgere operazioni di rete.
Il programma permette di eseguire lookup DNS su diversi tipi di record, effettuare scansioni di porte su un host e calcolare la suddivisione di una rete in sottoreti (VLSM) a partire dagli host richiesti.
L’obiettivo è fornire un toolkit semplice ma concreto, con risultati organizzati in formato JSON.
La struttura a classi rende il progetto estendibile: nuovi strumenti potranno essere aggiunti senza modificare il funzionamento generale del programma.

## Strumenti disponibili

- **DNS Lookup** — interrogazione di record `A`, `AAAA`, `MX`, `TXT` (o `ALL`) su un dominio.
- **Port Scanner** — scansione TCP di un intervallo di porte su un host.
- **IP Calculator** — suddivisione di una rete in sottoreti secondo VLSM, a partire dal numero di host richiesti per ciascuna.

## Membri del gruppo

- Tommaso Molino — [@tommasomolino](https://github.com/tommasomolino)
- Marco Giacomo Regaldo — [@marcogia1512](https://github.com/marcogia1512)

Corso: Programmazione Python — Cybersecurity Specialist.

## Installazione

```bash
git clone https://github.com/tommasomolino/Project-Work-Molino-Regaldo.git
cd Project-Work-Molino-Regaldo/
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Richiede **Python 3.11+**.

## Come si usa

```bash
cd src
python -m project
```

Il programma mostra un menu interattivo per scegliere lo strumento da usare. Vedi
`docs/manuale-utente.md` per la guida completa.

## Test

```bash
pytest
```

## Struttura del repository

```
.
├── src/project/       ← SORGENTE: il codice del programma
├── tests/             ← test pytest
├── docs/              ← METAINFORMAZIONI: documentazione, proposta, devlog, uso IA
├── requirements.txt
└── README.md
```

Approfondimenti in `docs/manuale-tecnico.md` (architettura e gerarchia delle classi) e
`docs/scelte.md` (giustificazione delle scelte di progettazione).
