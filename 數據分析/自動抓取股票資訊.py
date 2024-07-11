import pandas
import requests as req
import schedule
import time


def stock_info():
    localtime = time.localtime()
    result = time.strftime("%Y-%m-%d %I-%M-%S", localtime)
    print(f"{result} 取得股票資訊")
    res = req.get("https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL")
    stock = pandas.DataFrame(res.json())
    stock.to_csv(f"{result}.csv", encoding="utf_8_sig", index=False)


schedule.every().day.at("08:00:00").do(stock_info)

while True:
    schedule.run_pending()
    time.sleep(5)
