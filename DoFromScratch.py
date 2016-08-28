wordDictionary = {}

text = "this is a collection of words of nice words this is a fun thing it is"

wordList = text.split()


for words in wordList:

    if words in wordDictionary:
        wordDictionary[words] += 1
    else:
        wordDictionary[words] = 1

for key, value in sorted(wordDictionary.items()):

    print("{:{}} : {}".format(key, 1, value))
