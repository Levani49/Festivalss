
import requests
import json
import sqlite3

conn = sqlite3.connect('holiday_db.sqlite')
cursor = conn.cursor()

country_code = input("შეიტანეთ ქვეყნის კოდის დასახელება: ") #მაგალითად: USA = US, Greece=GR, Germany=DE
year = int(input("შეიყვანეთ სასურველი წელი: "))
month = int(input("შეიყვანეთ სასურველი თვე(რიცხობრივად): "))
day = int(input("შეიყვანეთ სასურველი კალენდარული რიცხვი: "))

key = "93b4639cef00445bbc3feda2c9c888ad"
r = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=93b4639cef00445bbc3feda2c9c888ad&country={country_code}&year={year}&month={month}&day={day}")
print(r.status_code)
res = r.json()
print(json.dumps(res, indent=4))
res = json.loads(r.text)
print(res)

# with open('new.json', 'w') as f:
#     json.dump(res, f, indent=4)



for each in res:
    place = (each["location"])
    hol_name = (each["name"])
    d_ate = (each["date"])
    nat_type = (each["type"])
    day_week = (each["week_day"])

summary = ("თარიღი:",each["date"],"კვირის დღე:",each["week_day"],"ქვეყანა:",each["location"],"დღესასწაული:",each["name"],"დღესასწაულის ტიპი",each["type"])
print(summary)

# row = (place, hol_name, d_ate, nat_type, day_week)
# cursor.execute('''CREATE TABLE IF NOT EXISTS festivals
#                (location VARCHAR(50),
#                 name VARCHAR(50),
#                 date DATE
#                 type VARCHAR(50),
#                 weekDay VARCHAR(50))''' )   #კოდის ამ ნაწილში იქმნება ქვეყნის, დღესასწაულის დასახელების,ტიპის, კვირის დღის შესაბამისი სვეტები.
#
# cursor.execute('INSERT INTO festivals(location, name, date, type, weekDay) VALUES (?, ?, ?, ?, ?)', row)
#
# conn.commit()
# conn.close()






