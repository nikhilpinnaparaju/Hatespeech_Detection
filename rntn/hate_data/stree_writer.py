f = open('./SOStr.txt','r')
g = open('./STree.txt','w+')

while (1):

    curline = f.readline()

    if not curline:
        break

    data = curline.split('|')
    n = len(data)
    m = 2*n-1

    string = ''
    x = m
    y = n-2

    # print(n,m)
    for i in range(m-1):
        # print(x, y)
        string += str(x)+'|'

        if y > 0:
            x -= 1
            y -= 1
            # print('f1')
        elif y == 0:
            x += 0
            y -= 1
            # print('f2')

        elif y < 0:
            x += 1
            # print('f3')
        # string += str(x)+'|'

    string += str(0)+'\n'
    g.write(string)

f.close()
g.close()
