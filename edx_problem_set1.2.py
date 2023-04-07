a = list(input())
total = 0

# enumerate() help to get the idx of the current item
for idx, item in enumerate(a):
    if idx - 1 >= 0 and idx + 1 < len(a):
        check_list = f'{a[idx - 1]}{item}{a[idx + 1]}'
        if check_list == 'bob':
            total += 1
print(f'Number of times bob occurs is: {total}')
