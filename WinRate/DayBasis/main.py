
from mathUtils import changeRate
from  dateUtils import *
from datetime import datetime
import tushare as ts
from processing import *

ts.set_token('5ac0e1fb3ac124721f1b11bab7e8d368593aaf47653c4bf071a9d3f8')
pro = ts.pro_api()

total=pro.stock_basic(list_status="L")
stockLen = len(total)

win=0
lose=0
holding=0

for index in range(1000):
    code = total.iloc[index]['ts_code']
    date = randomDate(total.iloc[index]['list_date'],dateToString(datetime.now()))
    status = judgeBasisBefore(code,date)
    if status == 1:
        win+=1
    elif status == -1:
        lose+=1
    else :
        holding+=1
    index+=1
print(win,lose,holding)