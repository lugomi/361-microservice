import zmq
import time
import os

# clear console out after printing welcome message
clear = lambda: os.system('clear')

context = zmq.Context()

#  Socket to talk to server
print("Connecting to fitness2tacos microservice...")
time.sleep(3)
clear()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

requests = ["1350 cal", "600 cal", "1150 cal", "300 cal", "900 cal"]
for request in requests:
    print(f"Sending request '{request}'...")
    socket.send_string(request)

#  Get the reply.
    message = socket.recv()
    message = message.decode('UTF-8')
    workout = message.split(',')
    print(f"Your workout to burn off your tacos-------->")
    for exercise in workout:
        print(exercise)