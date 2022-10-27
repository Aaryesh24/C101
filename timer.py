#importing modules
import time

#import time in seconds
seconds = input("Enter time in seconds")

#define the countdown timer function
def countdownTimer(seconds):
    while (seconds > 0):
        mins = int(seconds/60)
        secondss = int(seconds % 60)
        timer = f'{ mins } : { secondss}'
        print(timer)
        seconds -= 1
        time.sleep(1)
    print("time's up")

countdownTimer(int(seconds))