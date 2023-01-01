from user import User
import datetime as dt
from time import sleep

user = [
    User("고등학교", "이름", "230101", "0000")
]

print("\n자가진단 매크로 V1.1\n")

while True:
    now = dt.datetime.now().strftime("%H:%M:%S")
    if now == "00:00:00" or now == "00:00:01":
        for i in user:
            i.start()
    sleep(1)