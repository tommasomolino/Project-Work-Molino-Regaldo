# Manuale utente

> Guida all’installazione e all’utilizzo di Network Toolkit da terminale.

## Requisiti

Sono necessari:

* Python 3.11 o superiore;
* accesso a Internet per le query DNS;
* Git, se il progetto viene scaricato dalla repository;
* un terminale Linux, macOS o Windows con ambiente Python configurato.

## Installazione

Clonare la repository:

```bash
git clone https://github.com/tommasomolino/Project-Work-Molino-Regaldo.git
```

Entrare nella cartella del progetto:

```bash
cd Project-Work-Molino-Regaldo
```

Creare un ambiente virtuale:

```bash
python -m venv .venv
```

Attivarlo su Linux o macOS:

```bash
source .venv/bin/activate
```

Su Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Installare le dipendenze:

```bash
pip install -r requirements.txt
```

Quando l’ambiente virtuale è attivo, il prompt dovrebbe mostrare:

```text
(.venv)
```

## Avvio

Dalla cartella principale del progetto eseguire:

```bash
PYTHONPATH=src python -m project
```

Verrà mostrato il menu:

```text
=== NETWORK TOOLKIT ===
1. DNS Lookup
2. Port Scanner
3. Ip Calculator
0. Esci
Seleziona uno strumento:
```

Inserire il numero corrispondente alla funzione desiderata e premere Invio.

## DNS Lookup

Il DNS Lookup permette di interrogare i record DNS associati a un dominio.

### Record supportati

| Record | Significato                                             |
| ------ | ------------------------------------------------------- |
| `A`    | Indirizzi IPv4 associati al dominio                     |
| `AAAA` | Indirizzi IPv6 associati al dominio                     |
| `MX`   | Server che ricevono la posta elettronica                |
| `TXT`  | Informazioni testuali, spesso usate per SPF e verifiche |
| `ALL`  | Interroga tutti i tipi supportati                       |

### Ricerca di un singolo record

Dal menu selezionare:

```text
1
```

Inserire il dominio:

```text
example.com
```

Inserire il tipo di record:

```text
A
```

Esempio:

```text
Inserisci il dominio da risolvere: example.com
Scegli uno o più tipi di record (['A', 'AAAA', 'MX', 'TXT'] oppure ALL): A
```

Output indicativo:

```python
{
    'tool': 'DNSLookup',
    'target': 'example.com',
    'esito': {
        'A': 'Risolto con successo'
    },
    'risultato': {
        'A': ['104.20.23.154', '172.66.147.243']
    }
}
```

Gli indirizzi restituiti possono cambiare nel tempo in base alla configurazione DNS del dominio.

### Ricerca di più record

Separare i tipi con una virgola:

```text
A,AAAA,MX
```

Sono accettati anche spazi:

```text
A, AAAA, MX
```

Esempio:

```text
Inserisci il dominio da risolvere: google.com
Scegli uno o più tipi di record (['A', 'AAAA', 'MX', 'TXT'] oppure ALL): A,MX
```

Il programma eseguirà una query separata per ogni tipo selezionato.

## Port Scanner

Il Port Scanner verifica lo stato delle porte TCP comprese in un intervallo.

### Avvio della scansione

Dal menu selezionare:

```text
2
```

Il programma richiede:

1. indirizzo IP o hostname;
2. porta iniziale;
3. porta finale.

Esempio:

```text
Inserisci IP o hostname da scansionare: 127.0.0.1
Inserisci la porta iniziale: 20
Inserisci la porta finale: 25
```

Il programma prova ogni porta inclusa nell’intervallo, comprese le due estremità.

Nell’esempio vengono quindi controllate:

```text
20, 21, 22, 23, 24, 25
```

### Output della scansione

Esempio indicativo:

```text
Connessione rifiutata sulla porta 20
Connessione rifiutata sulla porta 21
Porta 22 aperta
Connessione rifiutata sulla porta 23
Connessione rifiutata sulla porta 24
Connessione rifiutata sulla porta 25
```

Report finale:

```python
{
    'tool': 'PortScanner',
    'target': '127.0.0.1',
    'esito': 'Scansione effettuata',
    'risultato': 'Le porte aperte sono:[22]\n'
                 'Le porte chiuse sono:[20, 21, 23, 24, 25]\n'
                 'Le porte andate in timeout sono:[]'
}
```

### Interpretazione degli stati

**Porta aperta**

Un servizio accetta connessioni TCP su quella porta.

**Porta chiusa**

Il dispositivo ha risposto rifiutando la connessione. La macchina è raggiungibile, ma non è presente un servizio in ascolto su quella porta.

**Timeout**

Non è stata ricevuta una risposta entro il tempo configurato. Il risultato può dipendere da firewall, filtri di rete, problemi di connessione o host non raggiungibile.

## Uscita dal programma

Per chiudere Network Toolkit selezionare:

```text
0
```

Il programma mostrerà:

```text
Chiusura del Network Toolkit.
```
## Errori comuni e cosa fare

### `ModuleNotFoundError: No module named 'project'`

Il programma è stato avviato senza indicare la cartella `src`.

Eseguire dalla radice della repository:

```bash
PYTHONPATH=src python -m project
```

### `ModuleNotFoundError: No module named 'dns'`

La dipendenza `dnspython` non è installata nell’ambiente attivo.

Attivare il virtual environment e installare le dipendenze:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Il dominio è vuoto

Il programma richiede un dominio non vuoto. Ripetere l’operazione inserendo solamente il nome, senza protocollo o percorso.

Corretto:

```text
example.com
```

Da evitare:

```text
https://example.com/pagina
```

### Il record non è valido

Sono accettati solamente:

```text
A
AAAA
MX
TXT
ALL
```

Per più record usare la virgola:

```text
A,MX,TXT
```

### La porta iniziale è maggiore della finale

Inserire un intervallo crescente.

Corretto:

```text
20
100
```

Errato:

```text
100
20
```

### Errore nei dati delle porte

Le porte devono essere numeri interi.

Corretto:

```text
22
```

Errato:

```text
ssh
```

### Tutte le porte risultano in timeout

Possibili cause:

* target non raggiungibile;
* firewall che scarta le connessioni;
* indirizzo errato;
* problemi di rete;
* scansione bloccata dal sistema remoto.

Verificare prima la raggiungibilità del target e utilizzare il programma solamente su sistemi per i quali si dispone dell’autorizzazione.

## Uso responsabile

Il Port Scanner deve essere utilizzato esclusivamente:

* sui propri dispositivi;
* in reti di laboratorio;
* su sistemi per i quali è stata ottenuta un’autorizzazione esplicita.

La scansione non autorizzata di sistemi di terzi può violare regolamenti, contratti o norme applicabili.
