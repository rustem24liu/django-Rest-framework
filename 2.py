s = input().split(',')

# print(s, type(s))

result = []
res = []
for i in range(len(s)):
    # print(s[i], type(s[i]))
    for j in range(len(s[i])):
        k = str(j)
        # print(s[i][j]+k)
        result.extend([s[i][j]+k])
# print(result)
res1 = {}
for i in range(len(result)):
    x = result.count(result[i])
    res1[result[i]] = x
# print(res1)

res2 = ''
for i, j in res1.items():
    if j == len(s):
        res2 += i
if len(res2)>=2:
    if res2[1] == '0':
        for i in range(len(res2)):
            if i % 2 == 0:
                print(res2[i], end = '')

