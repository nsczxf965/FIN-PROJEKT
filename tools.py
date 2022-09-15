import pandas as pd
import yfinance as yf

def insert_symbol(con, ticker):
    # Daten aus Ticker auslesen
    symbol = ticker.info["symbol"]
    name = ticker.info["longName"]
    country = ticker.info["country"]
    # Prüfen, ob Symbol schon vorhanden
    query = f"""select count(1) from finance.symbols 
                where symbol = '{symbol}';"""
    df = pd.read_sql(query,con)
    vorhanden = df.iloc[0,0] == 1
    # Daten in Datenbank schreiben
    if not vorhanden:
        query = f"""insert into finance.symbols values
        ('{symbol}', '{name}', '{country}');"""    
        con.execute(query)
    else:
        print("Eintrag existiert schon")