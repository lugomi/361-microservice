# Fitness2Tacos Microservice
Microservice for OSU CS 361: Software Engineering I

# Communication Contract
1. Communication Method:
   - Discord
   
2. Response to partnet must be made within:
   - 24 hours

3. Misc:
   - If unsure (about anything), ask.
   - If something is unclear, clarify.
   - If there are any anticipated problems/challenges that can affect partner, share as soon as possible.


# HOW TO Request Data
In order to request data you need to ensure a few things:
  - First you need to make sure that you have python3 installed.
  
  - Then you will need to install the ZeroMQ library by entering the following command in terminal: 
    - `pip install zmq`
    
  - A Socket will have to be created (this is how the request will be made) and then you will need to send a string to the microservice.
    - The string must be composed of three things: a number, whitepsace, the word 'cal'.
    - An example string: '1234 cal'
    
  - Here's an example call (make sure to have socket created already):
  ```
  client_request = '1230 cal'
  
  socket.send_string(client_request)
  ```
  
 # HOW TO Receive Data
In order to receive data you need to ensure a few things:
  - First you need to make sure that you have python3 installed.
  
  - Then you will need to install the ZeroMQ library by entering the following command in terminal: 
    - `pip install zmq`

  - Make sure to use the same socket that was used to request data from the microservice.
    The data that is sent from the client will be in the form of a string that uses commas to separate data.

  - Here's an example for receiving data that carries on from the example of requesting data:
  ```
  # '1230 cal' sent to the microservice
  
  message = socket.recv()
  message = message.decode('UTF-8')
  
  # need to parse response to get data requested
  formatted_response = message.split(',')
  ```
  
# UML Diagram
<img width="661" alt="Screen Shot 2022-07-25 at 8 49 44 PM" src="https://user-images.githubusercontent.com/68767288/180918988-0c2f00c9-f160-4f37-bb12-681d38adf5c0.png">




    
   
