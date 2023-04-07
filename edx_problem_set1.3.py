a = list(input().lower())
collections = list()
temp = list()
# enumerate() help to get the idx of the current item
for idx, item in enumerate(a):
    if idx + 1 < len(a) - 1 and ord(item) <= ord(a[idx + 1]):
        temp.append(item)
    else:
        temp.append(item)
        collections.append(temp)
        temp = list()

# find the longest length
longest = ''
for substr in collections:
    if len(substr) > len(longest):
        longest = ''.join(substr)

print(f'Longest substring in alphabetical order is: {longest}')
