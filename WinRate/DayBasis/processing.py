import math
import random

import tushare as ts
from datetime import datetime, timedelta
from mathUtils import *
import logging

logging.basicConfig(
    filename='result.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' # 格式：时间 - 级别 - 信息
)

ts.set_token('5ac0e1fb3ac124721f1b11bab7e8d368593aaf47653c4bf071a9d3f8')
pro = ts.pro_api()

def judgeBasisBefore(code,date,wr,lr):
    date = datetime.strptime(date, '%Y%m%d')
    info = ts.pro_bar(ts_code=code,adj='qfq',start_date=date.strftime('%Y%m%d'),end_date=datetime.now().strftime('%Y%m%d'))
    if info is None: # exception
        return 0
    l = len(info)
    high = info.iloc[l-1]['high']
    low = info.iloc[l-1]['low']
    l -= 1
    buyPrice = round(random.uniform(high,low),2)

    while math.isnan(buyPrice):
        high = info.iloc[l - 1]['high']
        low = info.iloc[l - 1]['low']
        buyPrice = round(random.uniform(high, low), 2)
        date = info.iloc[l-1]['trade_date']
        l -= 1
        if l-1 < 0:
            break
    win = buyPrice*(1+wr)
    lose = buyPrice*(1-lr)

    while l>=0:
        close = info.iloc[l]['close']
        if close >= win:
            logging.info('code:' + code + ',' + 'dateBegin:' + str(date) + ',buyPrice:' + str(buyPrice) + ',endDate:' + str(
                info.iloc[l]['trade_date']) +
                  ',endPrice:' + str(close) + '.result:win')
            print('code:'+code+','+'dateBegin:'+str(date)+',buyPrice:'+ str(buyPrice) +',endDate:'+str(info.iloc[l]['trade_date'])+
                  ',endPrice:'+str(close)+'.result:win')
            return 1
        elif close <= lose:
            logging.info('code' + code + ',dateBegin:' + str(date) + ',buyPrice:' + str(buyPrice) + ',endDate:' + str(
                info.iloc[l]['trade_date']) +
                  ',endPrice:' + str(close) + '.result:lose')
            print('code:'+code+',dateBegin:' + str(date) + ',buyPrice:' + str(buyPrice) + ',endDate:' + str(info.iloc[l]['trade_date']) +
                  ',endPrice:' + str(close) + '.result:lose')
            return -1
        l-=1
    logging.info('code'+code+',dateBegin:' + str(date) + ',buyPrice:' + str(buyPrice) + '.result:holding')
    return 0

    # while (datetime.now() > date):
    #     date = date +timedelta(days=1)
    #     curInfo = ts.pro_bar(ts_code=code,adj='qfq',start_date=date.strftime('%Y%m%d'),end_date=date.strftime('%Y%m%d'))
    #     cur = pro.daily(ts_code=code,adj='qfq',trade_date=date.strftime('%Y%m%d'))
    #     if curInfo is not None:
    #         price = curInfo['close'][0]
    #         if win(buyPrice,price,0.1):
    #             print(buyPrice,price,date)
    #             return 1
    #         elif lose(buyPrice,price,0.05):
    #             print(buyPrice,price,date)
    #             return -1
    # return 0

if __name__=='__main__':
    print(judgeBasisBefore('000001.SZ','20250307'))