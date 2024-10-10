import os
import random

cwd = os.getcwd()

file = open(cwd + '\\' + input('in>'), 'rb')

file.read(0x0a)
pix_loc = int.from_bytes(file.read(4), 'little')
file.read(0x12-0x0a)
length = int.from_bytes(file.read(2), 'little')
height = int.from_bytes(file.read(2), 'little') 
file.read(pix_loc - 0x16)

file2 = open(cwd + '\\' + input('out>'), 'wb')

file2.write(length.to_bytes(4, 'little'))
file2.write(length.to_bytes(4, 'little'))
file2.write((0xffffff).to_bytes(3, 'little'))
print(str(length) + ' ' + str(height))

stack = []
stack2 = []

for i in range(length):
    for j in range(length):
        stack2.append(file.read(1))
        stack2.append(file.read(1))
        stack2.append(file.read(1))
        stack.append(stack2.pop())
        stack.append(stack2.pop())
        stack.append(stack2.pop())


for i in range(length):
    for j in range(length):
        file2.write(stack.pop())
        file2.write((0xff).to_bytes(1, 'little'))