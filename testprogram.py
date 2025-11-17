import zmq
import json

def test_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.bind("tcp://*:5554")
    print("Test client running...")

    test_keys = [
        "TODO"
    ]

    for key in test_keys:
        socket.send_string(key)
        response = socket.recv_string()
        print("Response:")
        print(response)

if __name__ == "__main__":
    test_microservice()