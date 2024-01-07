import time
from datetime import date
from datetime import datetime
def aika():
    #PÄIVÄMÄÄRÄ TÄNÄÄN
    today = date.today()

    datetime_month = today.month
    datetime_day = today.day
    #YHDISTETÄÄN PÄIVÄ JA KUUKAUSI
    aika_tänään = (f'{datetime_day}.{datetime_month}')
    #MUUTETAAN STRING MUOTOON
    inputText = aika_tänään
    return inputText