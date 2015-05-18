def nwords(str):
    i = 1
    for x in str:
        if x == ' ':
            i += 1
    return i


n = int(input())

for i in range(n):
    str = input()

    if nwords(str) > 4:
        print("Crackers!")
    else:
        print(str + " krAh!")
