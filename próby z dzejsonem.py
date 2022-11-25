import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")


try:
    tasks = r.jason()
except json.decoder.JASONDecodeError:
    print("Niepoprawny format")
else:
    completedTasksByUser = dict()
    for entry in tasks:
        if (entry["completed"]  == True):
            try:
                completedTasksByUser[entry["UserID"]] += 1
            except KeyError:
                completedTasksByUser[entry["UserID"]] = 1

