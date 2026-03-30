import json
import random

#This file is just for me to learn how to write json files, it's not important for the actual project

time = 0
data = []
n = 4

for i in range(24*n):
    if i % 24 <= 12 and not 0: #1,2,3,4...24 also night and day
        num = random.randint(1,25)
    else:
        num = random.randint(75,100)
    time += 1
    light = {
    "value": num,
    "Time": time
    }
    data.append(light)

with open("random.json","w") as f:
    json.dump(data,f, indent = 2)
    print("works!")