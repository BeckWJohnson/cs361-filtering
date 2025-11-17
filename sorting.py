import zmq
import json

context = zmq.Context()
print("Client connecting to server...")
socket = context.socket(zmq.REQ) #request socket being used
socket.connect("tcp://localhost:5554")

print(f"Client connected, receiving data from server")
keyphrases = socket.recv() #the way the user wants to sort the data
with open("data.txt", "r") as f:
    data = json.load(f) #gets the unfiltered data

def filterByKey(data, keyphrases):
    return [item for item in data if any(k in keyphrases for k in item["key"])] # filters data using the key(s)

filteredData = filterByKey(data, keyphrases)
socket.send_string("filtered data: %s\nKeys Used: %s\n", filteredData, keyphrases) #sends the data to the server/user
socket.send_string("Q") #exit server, could be deleted depending on exit strategy
context.destroy()