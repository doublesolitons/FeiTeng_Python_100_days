import time
import math
import json
import requests
#######################################################
# def main():
#     f = None
#     try:
#         f = open('test.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('can not open the file')
#     except LookupError:
#         print('unknown encoding')
#     except UnicodeDecodeError:
#         print('Error in decoding')
#     finally:
#         if f:
#             f.close()
#
#
# if __name__ == '__main__':
#     main()

#################################################
# def main():
#     try:
#         with open('text.txt', 'r', encoding='utf-8') as f:
#             print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#
#
# if __name__ == '__main__':
#     main()

#################################################

# def main():
#     try:
#         with open('monsters.txt', 'r', encoding='utf-8') as f:
#             print(f.read())
#
#         with open('monsters.txt', 'r', encoding='utf-8') as f:
#             for line in f:
#                 print(line, end='')
#                 time.sleep(0.5)
#         print()     # add one more line below
#
#         with open('monsters.txt') as f:
#             lines = f.readlines()
#         print(lines)
#
#     except:
#         print('读取文件时解码错误!')
#
#
# if __name__ == '__main__':
#     main()

#################################################

# def is_prime(n):
#     assert n > 0
#     for factor in range(2, int(math.sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding='utf-8'))
#         for numbers in range(1, 10000):
#             if is_prime(numbers):
#                 if numbers < 100:
#                     fs_list[0].write(str(numbers) + '\n')
#                 elif numbers < 1000:
#                     fs_list[1].write(str(numbers) + '\n')
#                 else:
#                     fs_list[2].write(str(numbers) + '\n')
#     except IOError as ex:
#         print(ex)
#
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('done!')
#
#
# if __name__ == '__main__':
#     main()
#################################################
'''
binary file read and write
'''
# def main():
#     f = []
#     try:
#         with open('a.jpg', 'rb') as fs1:
#             f.append(fs1)
#             data = fs1.read()
#             print(type(data))
#         with open('b.jpg', 'wb') as fs2:
#             f.append(fs2)
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print(e)
#     except IOError as f:
#         print(f)
#     finally:
#         for index in f:
#             index.close()
#
# if __name__ == '__main__':
#     main()

#################################################
'''
JSON file write and read
'''


def main():
    mydict = {
        'name': 'Fei Teng',
        'age':  33,
        'cars': [
            {'brand': 'Toyota', 'model': 'Camry', 'maxspeed': 180},
            {'brand': 'Mercedes', 'model': 'C300', 'maxspeed': 220}
        ]
    }

    try:
        f = []
        with open('data.json', 'w', encoding='utf-8') as fs:
            f.append(fs)
            json.dump(mydict, fs)
    except IOError as f:
        print(f)
    finally:
        f[0].close()

    print('done')


if __name__ == '__main__':
    main()

#################################################
