## Sintesi

Abbiamo utilizzato ChatGPT e Claude come strumenti di supporto allo studio, alla progettazione e alla revisione del codice.

Gli assistenti sono stati configurati per lavorare principalmente come tutor: porre domande, spiegare i concetti, indicare problemi e proporre piccoli passi, senza fornire immediatamente la soluzione completa.

Il codice del componente `DNSLookup` è stato scritto e modificato progressivamente da noi, verificando manualmente il comportamento dopo ogni modifica.

## Dettaglio per parte

| Parte del progetto            | Cosa abbiamo chiesto                                                                   | Cosa abbiamo accettato, modificato o rifiutato                                          | Perché                                                                         |
|-------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Struttura di `DNSLookup`      | Chiarimenti sull’ereditarietà da `Tool` e sul ruolo di `execute(target)`               | Abbiamo adottato `DNSLookup(Tool)` e mantenuto il dominio come parametro di `execute()` | Per rispettare il contratto polimorfico comune agli strumenti                  |
| Import relativi               | Spiegazione della sintassi `from .tool import Tool`                                    | Abbiamo adottato l’import relativo                                                      | I moduli appartengono allo stesso package `project`                            |
| Libreria DNS                  | Indicazioni sul modulo da utilizzare con `dnspython`                                   | Abbiamo utilizzato `dns.resolver` e `dns.exception`                                     | Offrono query DNS ed eccezioni specifiche                                      |
| Supporto multi-record         | Discussione su come aggiungere `AAAA`, `MX` e `TXT`                                    | Abbiamo trasformato il singolo tipo di record in una lista di tipi                      | Consente una o più interrogazioni con la stessa esecuzione                     |
| Validazione della CLI         | Supporto per interpretare `A,MX`, spazi, input non validi e `ALL`                      | Abbiamo implementato personalmente parsing e controlli nel main                         | La classe rimane indipendente dall’interazione con l’utente                    |
| File `__main__.py` temporaneo | Richiesta esplicita di una versione pronta per testare DNSLookup e PortScanner         | Abbiamo accettato una struttura iniziale del menu, riservandoci di modificarla          | Serviva a eseguire subito test integrati senza deviare dal lavoro sul DNSLookup|
| Test manuali                  | Richiesta di casi utili per verificare successo, record mancanti e dominio inesistente | Abbiamo eseguito personalmente i test e controllato gli output                          | Per confermare la correttezza del comportamento reale                          |
| Aggiunta automatica di .json  | Richiesta su come aggiungere automaticamente .json al percorso specificato             | Abbiamo accettato e applicato quanto consigliato                                        | Perchè un utente potrebbe scordare l'estensione del file                       |

## Cosa non abbiamo delegato all’IA

Non abbiamo delegato all’IA la comprensione finale del codice, l’esecuzione dei test, la verifica degli output, la scelta definitiva delle modifiche da conservare e la gestione della repository Git.

Le entry del devlog e le riflessioni personali sul lavoro del gruppo non sono interamente scritte da noi, per una questione di tempi: le prime settimane non sono state sfruttate al massimo date le mille verifiche, nell'ultima settimana abbiamo dedicato tanto tempo al progetto ma non siamo riusciti anche a scrivere tutte le documentazioni a mano
