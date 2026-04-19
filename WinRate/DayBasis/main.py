
from mathUtils import changeRate
from  dateUtils import *
from datetime import datetime
import tushare as ts

ts.set_token('5ac0e1fb3ac124721f1b11bab7e8d368593aaf47653c4bf071a9d3f8')
pro = ts.pro_api()

total=pro.stock_basic(list_status="L")
# print(total)
# for index in total.index:
stock = total.loc[0]
    # print(total.iloc[index]['name'])
bDate=total.loc[0]['list_date']
print(bDate)
rDate = randomDate(bDate,dateToString(datetime.now()))
print(rDate)

print(hey)