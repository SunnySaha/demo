n = int(input())
dic = {}
for i in range(n):
    raw = input().split()
    name = raw[0]
    marks = raw[1:]
    marks = map(float, marks)
    dic[name] = marks
find_name = str(input())
specific_marks = dic[find_name]
print("{0:.2f}".format(sum(specific_marks)/(len(raw[1:]))))


