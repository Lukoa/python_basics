import datetime
import time
import winsound

def set_alarm():
    print('Set the alarm for:')
    hours=input(f"Input hours between 0hrs-23hrs: ")
    minutes=int(input("Input minutes btwn 0-59"))
    alarm_time=datetime.time(hour=hours, minute=minutes)
    return alarm_time

def play_alarm():
    frequency=1000
    duration=1000
    for i in range(3):
        winsound.Beep(frequency, duration)
        time.sleep(0.5)

def main():
    alarm_time=set_alarm()
    while True:
        now=datetime.datetime.now().time()
        if now>=alarm_time:
            print("Time to wake up!")
            play_alarm()
            break
        time.sleep(1)

if __name__=="__main__":
    main()