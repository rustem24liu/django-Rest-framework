x = input().split(',')
y = int(input())

# print(x, type(x))
# print(y, type(y))
# print(len[x])

for i in range(0, len(x)):
    x[i] = int(x[i])
result = []

for j in range(0,len(x)-1): 
    for i in range(0, len(x)-1):
        if x[j] != x[i+1] or j!=i+1:
            if x[j]+x[i+1] == y:
                result.append(j)
                result.append(i+1)
                # print(j, i+1)
                # res = x.index(x[j])
                # res2 = x.index(x[i+1])
                # print(res, res2)

print(result)           
            


