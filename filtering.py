import zmq
import json

def filterByKey(data, keyphrases):
    if isinstance(keyphrases, str):
        keyphrases = [keyphrases] # filters data using the key(s)
    return [item for item in data if item["key"] in keyphrases]

def main():
    context = zmq.Context()
    print("Client connecting to server...")
    socket = context.socket(zmq.REP) #reply socket being used
    socket.connect("tcp://localhost:5554")
    print(f"Client connected, receiving data from server")

    while True:
        keyphrases = socket.recv_string() #the way the user wants to sort the data
        try:
            with open("data.txt", "r") as f:
                data = json.load(f) #gets the unfiltered data
        except FileNotFoundError:
            print("Error: Could not find data.txt file")
            data = []
        except json.JSONDecodeError:
            print("Error: data.txt is not valid JSON")
            data = []       
        if not data:
            socket.send_string("Data file could not open please try again later")
        else:
            filteredData = filterByKey(data, keyphrases)
            if not filteredData:
                socket.send_string("No items were found using the given filters")
            else:
                socket.send_string(f"filtered data: {filteredData}\nKeys Used: {keyphrases}")#sends the data to the server/user

if __name__ == "__main__":
    main()