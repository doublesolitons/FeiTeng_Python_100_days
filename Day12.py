import re

# def main():
#     username = input('input a user name\n')
#     qq = input('input your qq number\n')
#
#     m1 = re.match(r'^[0-9a-zA-Z_]{6, 20}$', username)
#     m2 = re.match(r'^[1-9]\d{4, 11}$', qq)
#
#     if not m1:
#         print('pls input a valid username')
#     if not m2:
#         print('pls input a valid number')
#     if m1 and m2:
#         print('valid')
#
# if __name__ == '__main__':
#     main()

#######################################################################

# def main():
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#
#     print(str.center('华丽分割线', 30, '-'))
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print(str.center('华丽分割线', 30, '-'))
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
#
#
# if __name__ == '__main__':
#     main()

#######################################################################


def main():
    poem = '窗前 明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:          # in case there are multiple punctuations between two neighboring strings
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main()

