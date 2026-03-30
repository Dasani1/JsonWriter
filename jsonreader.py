import json
import matplotlib.pyplot as plt
import jsonwriter

#Read a json file, then graph it.
with open('random.json') as f:
    data = json.load(f)

values = [item['value'] for item in data] #ooh list comprehension ish
times = [item['Time'] for item in data]

plt.plot(times,values)
plt.ylabel("Values")
plt.xlabel("Time")
plt.title("Values over time")
plt.show()

    


