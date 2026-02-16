# portfolio_optimization

Piccola app **Streamlit** per visualizzare la performance di un portafoglio (line chart), la sua allocazione (pie chart) e alcune metriche di rischio base (**volatilità annualizzata** e **Sharpe ratio**) a partire da una serie storica di prezzi salvata in un file CSV. :contentReference[oaicite:0]{index=0}

---

## Cosa fa

- Legge i prezzi da `portfolio_data.csv` (con colonna `Date` come indice temporale). :contentReference[oaicite:1]{index=1}  
- Permette di inserire da UI:
  - i **ticker** (comma-separated)
  - i **pesi** del portafoglio (comma-separated)
- Calcola:
  - **portfolio value** (prezzi normalizzati * pesi)
  - **cumulative return**
  - **volatilità annualizzata** (std dei rendimenti giornalieri × √252)
  - **Sharpe ratio** (mean/std × √252, senza risk-free) :contentReference[oaicite:2]{index=2}
- Visualizza:
  - andamento del portafoglio (line chart)
  - grafico a torta dell’allocazione (Plotly) :contentReference[oaicite:3]{index=3}

---

## Struttura repo

- `interactive.py` — app Streamlit :contentReference[oaicite:4]{index=4}  
- `portfolio_data.csv` — dataset prezzi (da popolare) :contentReference[oaicite:5]{index=5}  
- `requirements.txt` — dipendenze :contentReference[oaicite:6]{index=6}  

---

## Requisiti

Python 3.9+ consigliato.

Dipendenze minime (come da `requirements.txt`):  
- `streamlit`
- `pandas`
- `plotly` :contentReference[oaicite:7]{index=7}

> Nota: nello script viene importato anche `yfinance`, quindi se vuoi usarlo senza modifiche, installalo:
> `pip install yfinance` :contentReference[oaicite:8]{index=8}

---

## Installazione

```bash
git clone https://github.com/fantuf/portfolio_optimization.git
cd portfolio_optimization
python -m venv .venv
source .venv/bin/activate  # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install yfinance  # opzionale ma consigliato (vedi nota sopra)
