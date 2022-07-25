import zmq
import time
import os

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

workouts = [
    "For 2 rounds:,10 Air Squats,10 Push Ups,10 Sit-ups,Run 400m",
    "For 3 rounds:,10 Kettbell Swings,10 Box Jumps,10 Burpees",
    "Run 800m,25 Pull Ups,50 Push Ups,100 Air Squats,Run 800m",
    "For 3 rounds:,10 Power Cleans,10 Push Press,50 Jump Rope"
]

# clear console out after printing welcome message
clear = lambda: os.system('clear')

# check if substring present in request
# if string contains 'cal', then a request has been sent
# ****** didn't use this but leave here for now ********
cutoff = "cal"

#  Socket to talk to client
print("Connecting to fitness2tacos client...")
time.sleep(3)
clear()

def main():
    while True:
        msg = socket.recv()
        print("Awaiting request from client...")
        print(f'Receive request: {msg}')

        msg = msg.decode('UTF-8')
        params = msg.split(' ')
        cals = int(params[0])
        
        # 0 - 300 calories returns first item in workout list
        if 0 <= cals <= 300:
            i = 0
        
        # 301 - 900 calories returns second item in workout list
        elif 301 <= cals <= 900:
            i = 1

        # 901 - 1200 calories returns third item in workout list
        elif 901 <= cals <= 1200:
            i = 2

        # 1200+ returns final item in workout list
        else:
            i = 3

        socket.send_string(workouts[i])
        print(f'Sending working #{i+1} to client.')
        print("Response sent to client...")
        print("--------------------------------")

if __name__ == "__main__":
    main()