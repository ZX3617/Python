sentence = 'I love coding in Python'
words = sentence.split(' ')
longest_word = max(words, key=len)
mingest_word = min(words, key=min)
print("最长的是：",longest_word)
print('最短的是', mingest_word)