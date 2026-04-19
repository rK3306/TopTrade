import random
from datetime import datetime, date, timedelta


def randomDate(dFrom,dEnd): # Both are String format
    df=datetime.strptime(dFrom,'%Y%m%d')
    de=datetime.strptime(dEnd,'%Y%m%d')
    days = (de-df).days
    random_days= random.randint(0,days) #include 0 and days
    random_day = df+timedelta(days=random_days)
    return random_day.strftime('%Y%m%d')

def dateToString(date):
    date_str = date.strftime('%Y%m%d')
    return date_str


if __name__=='__main__':
    print(randomDate('20150123','20150128'))
    print(dateToString(datetime.now()))
    print(datetime.now())
    print(randomDate('20250123',dateToString(datetime.now())))


