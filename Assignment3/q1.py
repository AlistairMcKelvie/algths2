from collections import namedtuple
import numpy as np

Item = namedtuple('Item', ['value', 'weight'])


def q1(file):
    with open(file, 'r') as f:
        knapsackSize, itemCount = f.readline().split()
        knapsackSize = int(knapsackSize)
        itemCount = int(itemCount)
        items = ['']
        for row in f:
            value, weight = row.split()
            items.append(Item(int(value), weight = int(weight)))
            
    # print items
    A = np.zeros([knapsackSize + 1, len(items)])
    for x in range(knapsackSize + 1):
        A[x][0] = 0
    for i in range(1, len(items)):
        for x in range(knapsackSize + 1):
            # print 'i', i
            # print 'x', x
            # print 'item', items[i]
            # print 'A[x[i - 1]]', A[x][i - 1]
            # print 'A[x - items[i].weight][i - 1] + items[i].value', A[x - items[i].weight][i - 1] + items[i].value
            if items[i].weight > x:
                A[x][i] = A[x][i - 1]
                # print 'items[i].weight > x'
                # print 'setting A[{1}][{0}] to {2}'.format(x, i, A[i - 1][x])
            else:
                A[x][i] = max(A[x][i - 1],
                              A[x - items[i].weight][i - 1] + items[i].value)
                # print 'setting A[{0}][{1}] to {2}'.format(i, x, max(A[x][i - 1],
                #              A[x - items[i].weight][i - 1] + items[i].value))
            # print '-----------------------------'
    # print A
    np.savetxt('test1_out.txt', A, '%.0f')
    return A[knapsackSize][len(items) - 1]
