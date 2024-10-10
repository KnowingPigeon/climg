import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

cwd = os.getcwd()
file = open(cwd + '\\' + input('File name>'), 'wb')

length = int(input('Length>'))
height = int(input('Height>'))

file.write(length.to_bytes(4, 'little'))
file.write(height.to_bytes(4, 'little'))
file.write(int(input('Transparency background (HEX)>'), 16).to_bytes(3, 'little'))

for i in range(length):
    for j in range (height):
        file.write(int(input('Color (HEX+A)>'), 16).to_bytes(4, 'little'))
        