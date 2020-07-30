name = []
marks = []

for _ in range(int(input())):
    n = input()
    m = float(input())
    name += [[n, m]]
    marks += [m]

marks = list(dict.fromkeys(marks))
sort = sorted(marks)[1] #it takes second number in the sorted list

for val, val2 in sorted(name):
    #print(val) it will print first item names of the list
    #print(val2) it will print second item value of the list
    #if value is  equal with sort list cause sort also contains value
    #then print names of that value

    if val2 == sort:
        print(val)