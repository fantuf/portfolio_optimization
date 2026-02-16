# Portfolio Optimization & Interactive Dashboard 📈

Questo progetto combina algoritmi di **Portfolio Management** con un'interfaccia utente interattiva. Permette di analizzare le performance storiche di un portafoglio azionario, calcolare metriche di rischio e visualizzare l'allocazione degli asset in tempo reale.

## 🚀 Caratteristiche principali

* **Dashboard Interattiva**: Sviluppata con **Streamlit** per una gestione dinamica dei ticker e dei pesi del portafoglio.
* **Visualizzazione Dati**: Grafici interattivi della performance storica e della composizione del portafoglio tramite **Plotly**.
* **Metriche di Rischio**: Calcolo automatico della **Volatilità Annualizzata** e dello **Sharpe Ratio**.
* **Analisi Multi-Asset**: Supporto per qualsiasi ticker disponibile su Yahoo Finance.

## 🛠️ Requisiti

Il progetto utilizza le seguenti librerie Python:

* `pandas` - Manipolazione dati
* `yfinance` - Download dati finanziari
* `plotly` - Grafici interattivi
* `streamlit` - Web App framework

Installa tutto con:

```bash
pip install pandas yfinance plotly streamlit

```

## 💻 Come avviare la Dashboard

Per lanciare l'interfaccia interattiva, esegui il seguente comando nel terminale dalla cartella del progetto:

```bash
streamlit run interactive.py

```

## 📊 Utilizzo dell'App

Una volta avviata l'app nel browser, potrai:

1. **Inserire i Ticker**: Digita i simboli azionari separati da virgola (es. `AAPL, MSFT, TSLA`).
2. **Definire i Pesi**: Inserisci la quota di capitale per ogni asset (es. `0.4, 0.3, 0.3`).
3. **Analizzare i Risultati**:
* Il grafico **Portfolio Performance** mostrerà l'andamento del valore nel tempo.
* Il **Pie Chart** mostrerà visivamente la distribuzione del capitale.
* La sezione **Risk Metrics** fornirà un feedback immediato sull'efficienza del portafoglio.



## 📁 Struttura della Repository

* `interactive.py`: Il cuore dell'applicazione Streamlit.
* `portfolio_data.csv`: File di dati storici utilizzato per l'analisi (assicurati che sia presente o generato dagli script di download).
* `requirements.txt`: Elenco delle dipendenze per facilitare l'installazione.

---

**Sviluppato da:** [fantuf](https://www.google.com/search?q=https://github.com/fantuf)

**Licenza:** MIT
