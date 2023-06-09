import mouse
import time
import os
import keyboard
from colorama import init, Fore, Style
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# initialize "colorama" to handle the color of the text in the console
init()

# set the bright green color of the text in the console
print(Style.BRIGHT + Fore.GREEN)

pd = "\npressed: "

# outputs the program header
print("####################")
print("# Activity Tracker #")
print("####################")

time.sleep(2)

# clear the screen
os.system('cls')


# create the "MyHandler" class that will track changes to files in the directory
class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # if it is not a file change, then output the event information
        if event.event_type != 'modified':
            print(f'{event.event_type}: {event.src_path}')


# function called by pressing a key on the keyboard
def on_key_press(event):
    print(pd + event.name)


def on_left_click():
    print(pd + 'Left Mouse Button')


def on_right_click():
    print(pd + 'Right Mouse Button')


def on_middle_click():
    print(pd + 'Middle Mouse Button')


# set mouse button handlers
mouse.on_click(on_left_click)
mouse.on_right_click(on_right_click)
mouse.on_middle_click(on_middle_click)

mouse.wait()

# create an "Observer" object and start monitoring file changes in the C:/ directory
observer = Observer()
observer.schedule(MyHandler(), path='C:/', recursive=True)
observer.start()

# set the handler for key presses on the keyboard
keyboard.on_press(on_key_press)

try:
    # an infinite loop that waits 0.01 second between iterations
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# version: 1.0
# code by G02m0n1k
