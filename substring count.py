def count_substring(string, sub_string):
    i = 0
    flag = 0
    for n in range(0, len(string)-len(sub_string)+1):
        if string[n] == sub_string[0]:
            flag = 1
            for m in range(0, len(sub_string)):
                if string[n+m]!= sub_string[m]:
                    flag =0
                    break
            if flag ==1:
                i = i+1
    return i


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)