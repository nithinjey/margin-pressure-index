# Margin Pressure Index (MPI)

Stock price drawdowns are rarely explained by a single cause. When a stock drops 15%, 
how much of that is genuine loss of confidence in the company vs 
forced selling from margin calls cascading through leveraged positions?

This project aims to build a data pipeline and model to:
- Construct a per-stock **Margin Pressure Index** from public market signals 
  (short interest, volume anomalies, options skew, aggregate margin debt)
- Decompose historical drawdown events into estimated **mechanical** (margin-driven) 
  vs. **fundamental** components
- Serve results through a live interactive dashboard where you can explore any ticker's 
  margin pressure history and drawdown breakdowns

## Motivation

## Tech Stack
- **Data:** yfinance, FINRA public datasets, pandas-datareader  
- **Storage:** PostgreSQL / AWS S3  
- **Modeling:** scikit-learn, XGBoost, statsmodels  
- **Dashboard:** Streamlit + Plotly  
- **Deployment:** AWS EC2  

## Status
🚧 In active development — data pipeline in progress