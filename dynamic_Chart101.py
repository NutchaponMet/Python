import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
# from IPython import display
import time

# Create random number generator
rng = default_rng()

x = np.array([], dtype=int)
y = np.array([], dtype=int)
accum_data = np.array([], dtype=int)

# Initialize tracking variables
lastest_num_points = 10
count = 1

# Initialize chart
fig = plt.figure(figsize=(6,4))
plt.ylim(0,11)
plt.xlabel('Step Series')
plt.ylabel('Data value')

# Create main loop
for i in range(0,1000):
     # Random sampling - simulate generating and reading streaming data
     data = rng.choice(np.arange(1,11))

     # Add a new data to x and y array
     x = np.concatenate((x, np.array([i])))
     y = np.concatenate((y, np.array([data])))

     # Accumulate data
     accum_data = np.concatenate((accum_data, np.array([data])))

     # Check if we need to shift x-axis series
     if count > lastest_num_points:
          x = x[1:]
          y = y[1:]
          plt.xlim(np.min(x), np.max(x))
     # Increment the counter
     count += 1

     # Calculate mean of data series
     mean = np.mean(accum_data)

     # Set title chart
     plt.title('Random Integers (mean = ' + '{:.2f}'.format(mean)+ ')', color='red')

     plt.plot(x, y, color='deepskyblue', linewidth=1)

     # display.clear_output(wait=True)
     # display.display(plt.gcf())

     # Sleep for 1 second
     # time.sleep(.0001)
     plt.pause(0.001)
plt.show()

# display.clear_output(wait=True)