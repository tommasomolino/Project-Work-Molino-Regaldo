# Network Toolkit

## Cosa fa

Network Toolkit è uno strumento da riga di comando pensato per svolgere operazioni di rete.
Il programma permette di eseguire lookup DNS su diversi tipi di record, effettuare scansioni di porte su un host e calcolare informazioni su indirizzi e sottoreti IP.
L’obiettivo è fornire un toolkit semplice ma concreto, con risultati organizzati in formato JSON.
La struttura a classi rende il progetto estendibile: nuovi strumenti potranno essere aggiunti senza modificare il funzionamento generale del programma.

## Membri del gruppo

- Tommaso Molino — handle GitHub
- Marco Giacomo Regaldo — handle GitHub

Corso: Programmazione Python — Cybersecurity Specialist.

## Installazione

```bash
git clone https://github.com/tommasomolino/Project-Work-Molino-Regaldo.git
cd Network\ ToolKit/
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Richiede **Python 3.11+**.

## Come si usa

```bash
python -m progetto --help
```

(Sostituisci `progetto` con il nome reale del tuo pacchetto. Vedi `docs/manuale-utente.md`
per la guida completa.)

## Test

```bash
pytest
```

## Struttura del repository

```
.
├── src/progetto/      ← SORGENTE: il codice del programma
├── tests/             ← test pytest
├── docs/              ← METAINFORMAZIONI: documentazione, proposta, devlog, uso IA
├── requirements.txt
└── README.md
```

Approfondimenti in `docs/manuale-tecnico.md` (architettura) e `docs/architettura` (gerarchia
delle classi).
