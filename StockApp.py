import streamlit as st
import pandas as pd
from PIL import Image

st.write( """

Stock Market Web Application
**Visually** show data on a stock! Date rage from Jan 2, 2020 - Dec 20, 2020


""")
st.sidebar.header('User Input')

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-12-20")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'APPL':
        return 'Apple'
    elif symbol == 'FB':
        return 'Facebook'
    elif symbol == 'MSFT':
        return 'Microsoft'
    else: 
        'None'

def get_data(symbol, start, end):

    if symbol.upper() == 'AMZN':
        df = pd.read_csv("C:/Users/ozair/OneDrive/Desktop/Stock Analysis Web App/AppleStockPrices.csv")
    elif symbol.upper() == 'APPL':
        df = pd.read_csv("C:/Users/ozair/OneDrive/Desktop/Stock Analysis Web App/AppleStockPrices.csv")
    elif symbol.upper() == 'FB':
        df = pd.read_csv("C:/Users/ozair/OneDrive/Desktop/Stock Analysis Web App/FacebookStockPrices.csv")
    elif symbol.upper() == 'MSFT':
        df = pd.read_csv("C:/Users/ozair/OneDrive/Desktop/Stock Analysis Web App/MicrosoftStockPrices.csv")
    else: 
        df = pd.DataFrame(columns = ['Date', 'Close/Last', 'Volume', 'Open', 'High, Low'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    for j in range (0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

start, end, symbol = get_input()

df = get_data(symbol, start, end)

company_name = get_company_name(symbol.upper())

st.header(company_name+" Close Price\n")
st.line_chart(df[' Close/Last'])

st.header(company_name+" Volume\n")
st.line_chart(df[' Volume'])

st.header(' Data Statistics')
st.write(df.describe())
