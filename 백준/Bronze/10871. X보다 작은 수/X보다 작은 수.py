option = input().split(' ')
str_list = input().split(' ')

for i in str_list:
    if int(i) < int(option[1]):
        print(i, end=' ')
