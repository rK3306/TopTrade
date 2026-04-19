import logging

from mathUtils import changeRate
from  dateUtils import *
from datetime import datetime
import tushare as ts
from processing import *

logging.basicConfig(
    filename='result.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s' # 格式：时间 - 级别 - 信息
)

ts.set_token('5ac0e1fb3ac124721f1b11bab7e8d368593aaf47653c4bf071a9d3f8')
pro = ts.pro_api()

total=pro.stock_basic(list_status="L")
stockLen = len(total)

win=0
lose=0
holding=0

wr = 0.1
lr = 0.05

logging.info("================begin=================")
logging.info("WR:"+str(wr)+",LR:"+str(lr))

for index in range(100):
    code = total.iloc[index]['ts_code']
    date = randomDate(total.iloc[index]['list_date'],dateToString(datetime.now()))
    status = judgeBasisBefore(code,date,0.01,0.005)
    if status == 1:
        win+=1
    elif status == -1:
        lose+=1
    else :
        holding+=1
    index+=1
logging.info(str(win)+","+str(lose)+","+str(holding))
print(win,lose,holding)
logging.info("================end=================")