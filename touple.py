n = int(input())

f = (input()).split(" ")
for i in range(n):

    f[i] = int(f[i])
t = tuple(f)
print(hash(t))