if __name__ == '__main__':
    s = str(input())

print (any(a.isalnum() for a in s))
print(any(a.isalpha() for a in s))
print(any(a.isdigit() for a in s))
print(any(a.isupper() for a in s))
print(any(a.islower() for a in s))
