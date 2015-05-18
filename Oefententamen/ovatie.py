k = int(input())

txt = input()

levels = []
for i in range(k+1):
    levels.append(int(txt[i]))


added = 0
have = 0
for s,n in enumerate(levels):
    #if n > 0:
    #    added = added + (s - have)
    #have = have + added + n
    if n != 0:
        if have < s:
            added += s - have
            have += s - have
        have += n
print(added)

