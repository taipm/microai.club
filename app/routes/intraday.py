from flask import Blueprint, render_template, jsonify
from threading import Thread
from . import intraday_bp
from vnstock import *
import pandas as pd

def GetIntradayData(symbol):
    _page_num = 0
    _page_size = 5000
    df =  stock_intraday_data (symbol=symbol, page_num=_page_num, page_size=_page_size)    
    while True:
        _page_num += 1
        df_next =  stock_intraday_data(symbol=symbol, 
                            page_num=_page_num, 
                           page_size=_page_size)
        if df_next.empty:
            break
        else:
            df = df.append(df_next)
    df = df[['price', 'volume', 'time']]  # Keep only relevant columns
    df['time'] = pd.to_datetime(df['time']) 
    return df

@intraday_bp.route('/')
def intraday():
    print(f'Đang vào hàm Intraday')
    return render_template('intraday.html')

@intraday_bp.route('/intraday_data')
def intraday_data(symbol):        
    print(f'Đang vào hàm Intraday_data')    
    intraday_data = GetIntradayData(symbol=symbol.upper()).to_json(orient='records')
    return jsonify({'data': intraday_data})

