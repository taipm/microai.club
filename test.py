from vnstock import *
def GetIntradayData(symbol):
    _page_num = 0
    _page_size = 5000
    df =  stock_intraday_data(symbol=symbol, page_num=_page_num, page_size=_page_size)    
    while True:
        _page_num += 1
        df_next =  stock_intraday_data(symbol=symbol, 
                            page_num=_page_num, 
                           page_size=_page_size)
        if df_next.empty:
            break
        else:
            df = df.append(df_next)
    return df
print(GetIntradayData('VND'))