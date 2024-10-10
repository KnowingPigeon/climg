import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

fig, axis = plt.subplots()

def rgba_to_rgbs(rgba):
    rgbs = hex(rgba // (0x1 * 0x10 **2))[2:]
    rgbs = '#' + '0' * (6 - len(rgbs)) + rgbs
    return rgbs

def plot_pixel(x, y, color, offset):
    axis.add_patch(Rectangle((x, y+offset), 1, 1, facecolor=color))


cwd = os.getcwd()

file = open(cwd + '\\' + input('File name>'), 'rb')

length = int.from_bytes(file.read(4), 'little')
height = int.from_bytes(file.read(4), 'little')
bg_color = int.from_bytes(file.read(3), 'little')

axis.set_xlim(left = 0, right = height)
axis.set_ylim(bottom = 0, top = length)

climgu = []

for i in range(length):
    climgu.append([])
    for j in range(height):
    
        color = int.from_bytes(file.read(4), 'big')
        
        climgu[i].append(color)

file.close()

for i in range(len(climgu)):
    for j in range(len(climgu[0])):
        color = rgba_to_rgbs(climgu[i][j])
        plot_pixel(j, -i, color, len(climgu)-1)
plt.gca().set_aspect('equal')
plt.show()