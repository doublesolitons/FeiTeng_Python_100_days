import heapq
import itertools
import collections
import random
'''
list generation
'''
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
#
# prices2 = {key: value for key, value in prices.items() if value > 100}
# print(prices2)
#

#####################################################################
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'input {name} score in {course}'))
#     print(scores[row], end='\n')


#####################################################################

# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(3, list1))
# print(heapq.nsmallest(2, list2, key=lambda x: x['price']))
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))

#####################################################################
# all permutations
# print(list(itertools.permutations('ABCD')), sep='\n')
#
# # partial permutations
# print(list(itertools.permutations('ABCD', 3)), sep='\n')
#
# print(list(itertools.product('ABCD', '123')))

# print(list(itertools.cycle(('A', 'B', 'C'))))

#####################################################################
# from collections import Counter
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))

#####################################################################

'''
Data structure & algorithm
- select sorting 
    
'''
def select_sort(items, comp = lambda x, y: x < y):
    # items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


if __name__ == '__main__':
    items = [random.randint(1, 20) for _ in range(10)]
    print(items)
    print(select_sort(items))



#####################################################################

#####################################################################