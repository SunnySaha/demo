def minion_game(string):
    n = str(string.upper())
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(n)):
        if n[i] in vowels:
            kevin += (len(n)-i)
        else:
            stuart += (len(n)-i)
    if kevin > stuart:
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)