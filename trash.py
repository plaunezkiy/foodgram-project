a = input()
b = ''
for i in range(len(a)):
    b += a[i]*(len(a)-i)
print(b)

