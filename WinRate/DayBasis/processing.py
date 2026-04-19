import random

import tushare as ts
from datetime import datetime, timedelta
from mathUtils import *

ts.set_token('5ac0e1fb3ac124721f1b11bab7e8d368593aaf47653c4bf071a9d3f8')
pro = ts.pro_api()

def judgeBasisBefore(code,date):
    date = datetime.strptime(date, '%Y%m%d')
    info = ts.pro_bar(ts_code=code,adj='qfq',start_date=date.strftime('%Y%m%d'),end_date=datetime.now().strftime('%Y%m%d'))
    l = len(info)
    high = info.iloc[l-1]['high']
    low = info.iloc[l-1]['low']
    buyPrice = round(random.uniform(high,low),2)
    while (datetime.now() > date):
        date = date +timedelta(days=1)
        curInfo = ts.pro_bar(ts_code=code,adj='qfq',start_date=date.strftime('%Y%m%d'),end_date=date.strftime('%Y%m%d'))
        cur = pro.daily(ts_code=code,adj='qfq',trade_date=date.strftime('%Y%m%d'))
        if curInfo is not None:
            price = curInfo['close'][0]
            if win(buyPrice,price,0.1):
                print(buyPrice,price,date)
                return 1
            elif lose(buyPrice,price,0.05):
                print(buyPrice,price,date)
                return -1
    return 0

if __name__=='__main__':
    print(judgeBasisBefore('000001.SZ','20250307'))