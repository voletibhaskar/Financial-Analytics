import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
st.set_page_config(layout="wide")


def stock_api_generator(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'OVERVIEW'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    title_list = title.split(',')
    for title_iterator in title_list:
        new_url = url+function+symbol
        r = requests.get(new_url)
        data = r.json()
        json_data_processing(data)

def json_data_processing(data):
    
    dataframe = pd.DataFrame({
    'Ticker': data['Symbol'],
    'Name': data['Name'],
    'Sector': data['Sector'],
    'Market Cap': data['MarketCapitalization'],
    'PE Ratio': data['PERatio'],
    'PEG Ratio': data['PEGRatio'],
    'Book Ratio': data['BookValue'],
    'Dividends Per Share': data['DividendPerShare'],
    'Earnings Per Share': data['EPS'],
    'Revenue Per Share TTM': data['RevenuePerShareTTM'],
    '52WeekHigh': data['52WeekHigh'],
    '52WeekLow': data['52WeekLow'],
    '50DayMovingAverage': data['50DayMovingAverage'],
    '200DayMovingAverage': data['200DayMovingAverage'],
    'SharesOutstanding': data['SharesOutstanding'],
},index=[0])
    st.write(dataframe)


def company_overview_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'OVERVIEW'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    json_data_processing(data)
    
def income_statement_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'INCOME_STATEMENT'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    print(data)
    
def balance_sheet_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'BALANCE_SHEET'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    print(data)
    
def cash_flow_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'CASH_FLOW'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    
    print(data)
    
def earnings_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'EARNINGS'
    symbol = '&symbol='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    print(data)
    
def news_sentiments_req(ALPHA_VANTAGE_KEY,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+'NEWS_SENTIMENT'
    symbol = '&tickers='+title+'&apikey='+ALPHA_VANTAGE_KEY
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    print(data)
    

def stock_selector(ALPHA_VANTAGE_KEY,OPTIONS):
    st.sidebar.title('Financial Analytics')
    title = st.text_input('Tickr Selector', 'TD')
    st.write('The current ticker selected:', title)
    
    option = st.sidebar.selectbox("",(OPTIONS),0)
    
    if option == 'Company Overview':
        company_overview_req(ALPHA_VANTAGE_KEY,title)
        
    if option == 'Income Statement':
        income_statement_req(ALPHA_VANTAGE_KEY,title)

    if option == 'Balance Sheet':
        balance_sheet_req(ALPHA_VANTAGE_KEY,title)

    if option == 'Cash Flow':
        balance_sheet_req(ALPHA_VANTAGE_KEY,title)

    if option == 'Earnings':
        balance_sheet_req(ALPHA_VANTAGE_KEY,title)

    if option == 'News & Sentiments':
        balance_sheet_req(ALPHA_VANTAGE_KEY,title)
        
    

if __name__ == "__main__":
    ALPHA_VANTAGE_KEY = 'WYIFLCPADSDLDB4V'
    OPTIONS = ['Company Overview','Income Statement','Balance Sheet','Cash Flow','Earnings','News & Sentiments']
    stock_selector(ALPHA_VANTAGE_KEY,OPTIONS)