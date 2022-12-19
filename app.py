from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')

def data_split_zero(d1):
    zerosp = d1.split('-')
    return(zerosp)

def data_split_today(d2):
    todaysp = d2.split('-')
    return(todaysp)

def zero_datatime(zerosp):
    zerodt = datetime.date(int(zerosp[0]),int(zerosp[1]),int(zerosp[2]))
    return(zerodt)

def today_datatime(todaysp):
    todaydt = datetime.date(int(todaysp[0]),int(todaysp[1]),int(todaysp[2]))
    return(todaydt)

def calc(d1, d2):
    res = abs(d2-d1).days
    res=int(res/7)
    return res


zero = "2022-01-01" #y-m-d
today = "2022-12-19"
zerosp=data_split_zero(zero)
todaysp=data_split_today(today)

zerodt=zero_datatime(zerosp)
print(zerodt)
todaydt=today_datatime(todaysp)

final=calc(zerodt, todaydt)

if __name__ == '__main__':
    app.run(debug=True)