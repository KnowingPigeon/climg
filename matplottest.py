import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axis = plt.subplots()

climg_u = [[0x0FFFFFFF, 0xFF7F27FF, 0x00A2E8FF, 0xFF7F27FF, 0xFF7F27FF], 
           [0x22B14CFF, 0xED1C24FF, 0xA349A4FF, 0xFF7F27FF, 0xFF7F27FF], 
           [0x00A2E8FF, 0xFFF200FF, 0x000000FF, 0xFF7F27FF, 0xFF7F27FF],
           [0x00A2E8FF, 0xFFF200FF, 0x000000FF, 0xFF7F27FF, 0xFF7F27FF]]

def rgba_to_rgbs(rgba):
    rgbs = hex(rgba // (0x1 * 0x10 **2))[2:]
    rgbs = '#' + '0' * (6 - len(rgbs)) + rgbs
    return rgbs

def plot_pixel(x, y, color):
    axis.add_patch(Rectangle((x, y+len(climg_u)-1), 1, 1, facecolor=color))

def main():
    axis.set_xlim(left = 0, right = len(climg_u[0]))
    axis.set_ylim(bottom = 0, top = len(climg_u))
    for i in range(len(climg_u)):
        for j in range(len(climg_u[0])):
            color = rgba_to_rgbs(climg_u[i][j])
            plot_pixel(j, -i, color)

main()
plt.show()
