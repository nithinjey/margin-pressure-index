import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

tickers = ["GME", "SPY", "QQQ", "NVDA"]

def load_data(tickers, range=5*365):
    end_date = datetime.today()
    start_date = end_date - timedelta(range)
    data = yf.download(tickers, start=start_date, end=end_date, group_by="ticker")

    dfs = []
    for ticker in tickers:
        df = data[ticker].copy()
        df["ticker"] = ticker
        df.reset_index(inplace=True)
        dfs.append(df)
    
    final_df = pd.concat(dfs, ignore_index=True)
    final_df.columns = [col.lower().replace(" ", "_") for col in final_df.columns]

    engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
    final_df.to_sql("stock_prices", engine, if_exists="replace", index=False)
    
    print(f"Saved {len(final_df)} rows across {len(tickers)} tickers")
    return final_df

data = load_data(tickers)
print(data)