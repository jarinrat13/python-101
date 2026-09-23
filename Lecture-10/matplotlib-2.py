<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.linespace(0, 2 * np.pi, 100)
y = np.sin(x)

line, = ax.plot(x,y)

def update(frame):
    line.set_ydate(np.sin(x + frame / 10.0))
    return line ,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

=======
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.linespace(0, 2 * np.pi, 100)
y = np.sin(x)

line, = ax.plot(x,y)

def update(frame):
    line.set_ydate(np.sin(x + frame / 10.0))
    return line ,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

>>>>>>> 36e2367c506c94705546caf13817ba0e32d9cbfa
plt.show()