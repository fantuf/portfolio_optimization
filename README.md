# Portfolio Optimization 📈

Questo repository contiene un set di strumenti in Python per l'analisi finanziaria e l'ottimizzazione di portafogli azionari. Il progetto utilizza modelli matematici per calcolare l'allocazione ottimale degli asset, confrontando diverse strategie basate sul profilo rischio-rendimento.

## 🚀 Funzionalità

* **Analisi Statistica**: Calcolo dei rendimenti attesi, della volatilità (deviazione standard) e della matrice di covarianza degli asset.
* **Strategie di Ottimizzazione**:
* **Maximum Sharpe Ratio**: Identifica il portafoglio che massimizza il rendimento per unità di rischio.
* **Minimum Volatility**: Trova la combinazione di asset con il minor rischio possibile.


* **Visualizzazione**:
* Generazione della **Frontiera Efficiente**.
* Plotting dei portafogli ottimali rispetto a una simulazione Monte Carlo.


* **Integrazione Dati**: Supporto per il download automatico dei dati storici tramite l'API di Yahoo Finance (`yfinance`).

## 🛠️ Requisiti

Il progetto richiede Python 3.x e le seguenti librerie:

* `numpy`
* `pandas`
* `matplotlib`
* `scipy`
* `yfinance`

Puoi installarle tutte tramite pip:

```bash
pip install numpy pandas matplotlib scipy yfinance

```

## 💻 Come utilizzare il progetto

1. **Clona il repository**:
```bash
git clone https://github.com/fantuf/portfolio_optimization.git
cd portfolio_optimization

```


2. **Configurazione**:
All'interno dello script principale (o del notebook), definisci i ticker degli asset che desideri analizzare:
```python
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

```


3. **Esecuzione**:
Esegui lo script per visualizzare i risultati dell'ottimizzazione e i grafici della frontiera efficiente:
```bash
python main.py

```



## 📊 Concetti Implementati

### Markowitz Efficient Frontier

Il nucleo del progetto si basa sulla **Modern Portfolio Theory (MPT)**. La frontiera efficiente rappresenta l'insieme dei portafogli che offrono il massimo rendimento atteso per ogni livello di rischio.

### Sharpe Ratio

Viene calcolato per misurare l'efficienza di un portafoglio:



*(Dove  è il rendimento del portafoglio,  il tasso risk-free e  la volatilità).*

## 📂 Struttura della Repo

* `main.py` / `optimization.py`: Logica principale per il calcolo dei pesi e l'ottimizzazione.
* `requirements.txt`: Elenco delle dipendenze.
* `Notebooks/`: Eventuali esempi interattivi (.ipynb).

---

**Autore:** [fantuf](https://www.google.com/search?q=https://github.com/fantuf)

**Licenza:** MIT
