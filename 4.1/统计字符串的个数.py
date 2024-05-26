def zifu(s,char):
    count = 0
    for c in s:
        if c == char:
            count+=1
    return count
s='hello world'
char_count='l'
print(zifu(s,char_count))

