# cs361-sorting
Created for CS 361 Software Engineering 1

To Use:

Use ZeroMQ listening on port 5554

Store data in a data.txt file in this format:

[
    {"someDataName": "", "key": ""},
    {"someDataName": "", "key": ""},
    {"someDataName": "", "key": ""},
] 

OR

[
    {"someDataName": "", "keys": ["", ""]},
    {"someDataName": "", "keys": ["", ""]},
    {"someDataName": "", "keys": ["", ""]},
] 

Send the microservice just the key(s) the data file should be filtered by.

The microservice will return the filteredData of the data.txt file with the keys that were used to get the filtered data. If it did not find any data that could be filtered with the given keys, then returns a "No items were found using the given filters".