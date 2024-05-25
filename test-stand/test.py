import csv
import numpy as np
 
 
burn = np.random.randint(1, 10 + 1, 1000)
thrust = burn * 200 + 2000 + np.random.randint(1, 400 + 1, 1000)
pressure = np.random.randint(1, 10 + 1, 1000)
impulse = 0
rssi = np.random.randint(1, 10 + 1, 1000)
 
with open('salaries.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(zip(burn, thrust,pressure,impulse,rssi))