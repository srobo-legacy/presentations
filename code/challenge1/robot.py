from sr import *
import look.py

R=Robot()

while True
    if look.look_at_things():
        R.motors[0].m0 = 25
        R.motors[1].m0 = 25
        time.sleep(2,5)
        R.motors[0].m0 = 0
        R.motors[1].m0 = 0
        time.sleep(1)
        R.motors[0].m0 = -25
        R.motors[1].m0 = -25
        time.sleep(2,5)
        R.motors[0].m0 = 0
        R.motors[1].m0 = 0
        time.sleep(1)
