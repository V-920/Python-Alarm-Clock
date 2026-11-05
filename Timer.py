import time
from playsound import playsound
import datetime

GREEN = "\033[32m"
CYAN = "\033[36m"

def set_alarm(duration):
    print(f"Alarm set for {duration} seconds from now." + GREEN)
    sound_file = "sound.wav"
    is_running = True
    while is_running == True:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"Current time: {current_time}" + CYAN)
        time.sleep(1)
        if current_time == duration:
            print("Alarm! Time's up!" + GREEN)
            playsound(sound_file)
            is_running = False

if __name__ == "__main__":
    duration = input("Enter the duration of the alarm in seconds (HH:MM:SS):  " + GREEN)
    set_alarm(duration)