input_str = input("nhap x,y:")
dimension=[int(x) for x in input_str.split(',')]
rownum=dimension[0]
colnum=dimension[1]
mul=[[0 for col in range(colnum)] for row in range(rownum)]
for row in range(rownum):
    for col in range(colnum):
        mul[row][col]=row*col
print(mul)