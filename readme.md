# cs361-filtering
Created for CS 361 Software Engineering 1

To Use:

Use ZeroMQ listening on port 5554

Store data that you want to be filterable in a data.txt file in this format:

[
    {"someDataName": "", "key": ""},
    {"someDataName": "", "key": ""},
    {"someDataName": "", "key": ""},
] 

Or for multiple keys:

[
    {"someDataName": "", "keys": ["", ""]},
    {"someDataName": "", "keys": ["", ""]},
    {"someDataName": "", "keys": ["", ""]},
] 

Send the microservice just the key(s) the data file should be filtered by.

The microservice will return the filteredData of the data.txt file with the keys that were used to get the filtered data. If it did not find any data that could be filtered with the given keys, then returns a "No items were found using the given filters".

# Example Code
Use this example code to send the keys to the microservice and recieve the data filtered by the keys from the microservice:

#Create ZeroMQ context
    context = zmq.Context()
#Create REQ (request) socket
    socket = context.socket(zmq.REQ)
    socket.bind("tcp://*:5554")
#Send the keys to filter data request
    keys = [“TODO”, “OVERDUE”]
    for k in keys:
#Send each key 
        socket.send_string(key)
#Receive each thing that was filtered
        response = socket.recv_string() 
        print(f”Received: {response}”)

# UML Diagram:
![alt text](<Filtering Microservice UML Diagram.drawio.png>)