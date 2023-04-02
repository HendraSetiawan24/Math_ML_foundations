#This introduction of Linear Algebra started with some overview example of bank robber cather. 
#The bank robber run with car about 2.5km/second where sherif 3km/s late 5 mins than the robbers.
#to simplify the model we could solve the equations with python code

import numpy as np
import matplotlib.pyplot as plt 

t = np.linspace(0 , 40 , 1000) # start, finish and points 

# we create variable name to identify the robber 
d_r = 2.5 * t

# we also create variable for sherif who trying to catch the rober at 3.5km/s
d_s = 3 * (t-5)


# we build the plot to solve the equation using below
fig, ax = plt.subplots()
plt.title("A Bank Robber Caught")
plt.xlabel("Time(in minutes)")
plt.ylabel("distance(in km)")
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c="green")
ax.plot(t, d_s, c="blue")
plt.axvline(x=30, color="purple", linestyle="--")
plt.axhline(y=75, color="purple", linestyle="--")
plt.legend()
plt.show()