import streamlit as st
import streamlit.components.v1 as components
import requests
from collections import defaultdict
import pandas as pd
st.set_page_config(layout="wide", initial_sidebar_state='auto')

def A_operations_processing(ProcessMapping,operation,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+ProcessMapping['process_type_A'][operation]
    symbol = '&symbol='+title+'&apikey='+ProcessMapping['ALPHA_VANTAGE_KEY']
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    
    if operation == 'Company Overview':
        st.dataframe(pd.json_normalize(data).transpose())
    
    elif operation == 'Earnings':
        print('My Earnings: ',data)
        
        start_year, end_year = st.sidebar.select_slider(
            'Select the range of your years',
            options=list(range(0, len(data["annualEarnings"]))),
            value=(0,len(data["annualEarnings"])))
                
        # selectedAnnualYear = st.sidebar.selectbox("Year Selector",(list(range(0, len(data["annualEarnings"])))),0)
        selectedQuaterlyReport = st.sidebar.selectbox("Quater Selector",(list(range(0, len(data["quarterlyEarnings"])))),0)
        col1, col2 = st.columns([4,4])
        col1.header("Annual Earnings")
        col1.dataframe(pd.json_normalize(data['annualEarnings'][start_year:end_year]).transpose())
        col2.header("Quaterly Earnings")
        col2.dataframe(pd.json_normalize(data['quarterlyEarnings'][selectedQuaterlyReport]).transpose())
  
    else:
        print('My data: ',data)
        selectedAnnualYear = st.sidebar.selectbox("Annual Reports",(list(range(0, len(data["annualReports"])))),0)
        selectedQuaterlyReport = st.sidebar.selectbox("Quaterly Reports",(list(range(0, len(data["quarterlyReports"])))),0)
        col1, col2 = st.columns([4,4])
        col1.header("Annual Reports")
        col1.dataframe(pd.json_normalize(data['annualReports'][selectedAnnualYear]).transpose())
        col2.header("Quaterly Reports")
        col2.dataframe(pd.json_normalize(data['quarterlyReports'][selectedQuaterlyReport]).transpose())

        # st.write(data)
        
    # json_data_processing(data)
    
def B_operations_processing(ProcessMapping,operation,title):
    url = 'https://www.alphavantage.co/query?'
    function = 'function='+ProcessMapping['process_type_B'][operation]
    symbol = '&tickers='+title+'&apikey='+ProcessMapping['ALPHA_VANTAGE_KEY']
    new_url = url+function+symbol
    r = requests.get(new_url)
    data = r.json()
    st.dataframe(pd.json_normalize(data))

# def stock_selector(ALPHA_VANTAGE_KEY,OPTIONS):
def stock_selector(ProcessMapping):
    st.sidebar.title('Financial Analytics')
    st.markdown('API Limit **500 Calls/Day** OR **5 Calls/Min**')
    st.markdown('**EVERY ACTION NEW CALL**')
    
    title = st.text_input('Tickr Selector')
    st.write('The current ticker selected:', title)
    
    optionsList = list(ProcessMapping["process_type_A"].keys()) + list(ProcessMapping["process_type_B"].keys())
    option = st.sidebar.selectbox("",(optionsList),0)
    if option == 'News & Sentiments':
        B_operations_processing(ProcessMapping,option,title)
        # balance_sheet_req(ALPHA_VANTAGE_KEY,title)
    else:
        A_operations_processing(ProcessMapping,option,title)
        
    

if __name__ == "__main__":
    ProcessMapping = {
        'ALPHA_VANTAGE_KEY' : 'WYIFLCPADSDLDB4V',
        'process_type_A' : {
            'Company Overview': 'OVERVIEW',
            'Income Statement': 'INCOME_STATEMENT',
            'Balance Sheet': 'BALANCE_SHEET',
            'Cash Flow' : 'CASH_FLOW',
            'Earnings' : 'EARNINGS',
                            },
        'process_type_B' : {
            'News & Sentiments' : 'NEWS_SENTIMENT'
        }
        
    }
    # stock_selector(ALPHA_VANTAGE_KEY,OPTIONS)
    stock_selector(ProcessMapping)