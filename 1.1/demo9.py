print(1, 2, 3)
fp = open('text.txt', 'w')
print(1, 2, 3, sep="---", end='<+++>', file=fp)
fp.close()