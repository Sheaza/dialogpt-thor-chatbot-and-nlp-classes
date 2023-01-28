import string


def get_bigram(subwords, bigrams, text):
    for a in [i+j for i in subwords.keys() for j in subwords]:
        if a in text:
            if a not in bigrams.keys():
                bigrams[a] = text.count(a)
    return bigrams


def bpe(text, size):
    bigrams = {}
    text = text.translate(str.maketrans('', '', string.punctuation)).replace(" ", "*").lower()
    text = "*" + text + "*"
    letters = [a for a in set(text)]
    subwords = dict(zip(letters, [text.count(a) for a in letters]))
    sum = len(subwords)
    while sum < size:
        bigrams = get_bigram(subwords, bigrams, text)
        for bigram in sorted(bigrams, key=bigrams.get, reverse=True):
            if bigram not in subwords.keys():
                subwords[bigram] = bigrams[bigram]
                sum += 1
                break
    return subwords


print(bpe("hurry on, harry, hurry on!", 10))