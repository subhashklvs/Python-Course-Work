rows = 5
cols = 10
top = ' '.join(['*'] * cols)
for i in range(rows):
    if i == 0 or i == rows - 1:
        print(top)
    else:
        print('*' + ' ' * (2 * cols - 3) + '*')
