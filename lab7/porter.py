consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"


def isConsonantWithException(word, i):
    letter = word[i]
    if letter in consonants:
        if letter == 'y' and word[i-1] in consonants:
            return False
        else:
            return True
    else:
        return False

def getForm(word: str):
    form = []
    formStr = ''
    for i in range(len(word)):
        if isConsonantWithException(word, i):
            if i != 0:
                prev = form[-1]
                if prev != 'C':
                    form.append('C')
            else:
                form.append('C')
        else:
            if i != 0:
                prev = form[-1]
                if prev != 'V':
                    form.append('V')
            else:
                form.append('V')
    for j in form:
        formStr += j
    return formStr


def getM(word):
    form = getForm(word)
    count = form.count('VC')
    return count


def endsWithTwoConsonant(stem):
    if len(stem) >= 2:
        if isConsonantWithException(stem, -1) and isConsonantWithException(stem, -2):
            return True
        else:
            return False
    else:
        return False

def containsVowel(stem):
    for i in stem:
        if i in vowels:
            return True
    return False


def containsConsonant(stem):
    for i in stem:
        if i in consonants:
            return True
    return False


def cvc(word: str):
    if len(word) >= 3:
        form = getForm(word)
        if form[-3:] == "CVC":
            if word[-3] not in "wxy":
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def replace(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    replaced = base + rep
    return replaced


def replaceM0(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if getM(base) > 0:
        replaced = base + rep
        return replaced
    else:
        return orig


def replaceM1(orig, rem, rep):
    result = orig.rfind(rem)
    base = orig[:result]
    if getM(base) > 1:
        replaced = base + rep
        return replaced
    else:
        return orig


def first(word: str):
    if word.endswith('sses'):
        word = word.replace('sses', 'ss')
    elif word.endswith('ies'):
        word = word.replace('ies', 'i')
    elif word.endswith('ss'):
        word = word.replace('ss', 'ss')
    elif word.endswith('s'):
        word = word.replace('s', '')
    return word


def second(word: str):
    flag = False
    if word.endswith('eed'):
        result = word.rfind('eed')
        base = word[:result]
        if getM(base) > 0:
            word = base
            word += 'ee'
    elif word.endswith('yee'):
        result = word.rfind('eed')
        word = word[:result]
    elif word.endswith('ed'):
        result = word.rfind('ed')
        base = word[:result]
        if containsVowel(base):
            word = base
            flag = True
    elif word.endswith('ing'):
        result = word.rfind('ing')
        base = word[:result]
        if containsVowel(base):
            word = base
            flag = True
    if flag:
        if word.endswith('at') or word.endswith('bl') or word.endswith('iz'):
            word += 'e'
        elif endsWithTwoConsonant(word) and not word.endswith('l') and not word.endswith('s') and not word.endswith('z'):
            word = word[:-1]

        elif getM(word) == 1 and cvc(word):
            word += 'e'
    return word


def third(word):
    # idk
    # if word.endswith('y'):
    #     result = word.rfind('y')
    #     base = word[:result]
    #     if containsVowel(base):
    #         word = base
    #         word += 'i'
    return word


def fourth(word):
    if word.endswith('ational'):
        word = replaceM0(word, 'ational', 'ate')
    elif word.endswith('tional'):
        word = replaceM0(word, 'tional', 'tion')
    elif word.endswith('enci'):
        word = replaceM0(word, 'enci', 'ence')
    elif word.endswith('anci'):
        word = replaceM0(word, 'anci', 'ance')
    elif word.endswith('izer'):
        word = replaceM0(word, 'izer', 'ize')
    elif word.endswith('abli'):
        word = replaceM0(word, 'abli', 'able')
    elif word.endswith('alli'):
        word = replaceM0(word, 'alli', 'al')
    elif word.endswith('entli'):
        word = replaceM0(word, 'entli', 'ent')
    elif word.endswith('eli'):
        word = replaceM0(word, 'eli', 'e')
    elif word.endswith('ousli'):
        word = replaceM0(word, 'ousli', 'ous')
    elif word.endswith('ization'):
        word = replaceM0(word, 'ization', 'ize')
    elif word.endswith('ation'):
        word = replaceM0(word, 'ation', 'ate')
    elif word.endswith('ator'):
        word = replaceM0(word, 'ator', 'ate')
    elif word.endswith('alism'):
        word = replaceM0(word, 'alism', 'al')
    elif word.endswith('iveness'):
        word = replaceM0(word, 'iveness', 'ive')
    elif word.endswith('fulness'):
        word = replaceM0(word, 'fulness', 'ful')
    elif word.endswith('ousness'):
        word = replaceM0(word, 'ousness', 'ous')
    elif word.endswith('aliti'):
        word = replaceM0(word, 'aliti', 'al')
    elif word.endswith('iviti'):
        word = replaceM0(word, 'iviti', 'ive')
    elif word.endswith('biliti'):
        word = replaceM0(word, 'biliti', 'ble')
    return word


def fifth(word):
    if word.endswith('icate'):
        word = replaceM0(word, 'icate', 'ic')
    elif word.endswith('ative'):
        word = replaceM0(word, 'ative', '')
    elif word.endswith('alize'):
        word = replaceM0(word, 'alize', 'al')
    elif word.endswith('iciti'):
        word = replaceM0(word, 'iciti', 'ic')
    elif word.endswith('ful'):
        word = replaceM0(word, 'ful', '')
    elif word.endswith('ness'):
        word = replaceM0(word, 'ness', '')
    return word


def sixth(word):
    if word.endswith('al'):
        word = replaceM1(word, 'al', '')
    elif word.endswith('ance'):
        word = replaceM1(word, 'ance', '')
    elif word.endswith('ence'):
        word = replaceM1(word, 'ence', '')
    elif word.endswith('er'):
        word = replaceM1(word, 'er', '')
    elif word.endswith('ic'):
        word = replaceM1(word, 'ic', '')
    elif word.endswith('able'):
        word = replaceM1(word, 'able', '')
    elif word.endswith('ible'):
        word = replaceM1(word, 'ible', '')
    elif word.endswith('ant'):
        word = replaceM1(word, 'ant', '')
    elif word.endswith('ement'):
        word = replaceM1(word, 'ement', '')
    elif word.endswith('ment'):
        word = replaceM1(word, 'ment', '')
    elif word.endswith('ent'):
        word = replaceM1(word, 'ent', '')
    elif word.endswith('ou'):
        word = replaceM1(word, 'ou', '')
    elif word.endswith('ism'):
        word = replaceM1(word, 'ism', '')
    elif word.endswith('ate'):
        word = replaceM1(word, 'ate', '')
    elif word.endswith('iti'):
        word = replaceM1(word, 'iti', '')
    elif word.endswith('ous'):
        word = replaceM1(word, 'ous', '')
    elif word.endswith('ive'):
        word = replaceM1(word, 'ive', '')
    elif word.endswith('ize'):
        word = replaceM1(word, 'ize', '')
    elif word.endswith('ion'):
        result = word.rfind('ion')
        base = word[:result]
        if getM(base) > 1 and (base.endswith('s') or base.endswith('t')):
            word = base
    word = replaceM1(word, '', '')
    return word


def seventh(word):
    if word.endswith('e'):
        base = word[:-1]
        if getM(base) > 1:
            word = base
        elif getM(base) == 1 and not cvc(base):
            word = base
    return word


def eigth(word):
    if getM(word) > 1 and endsWithTwoConsonant(word) and word.endswith('l'):
        word = word[:-1]
    return word


def main(word):
    word = first(word)
    word = second(word)
    word = third(word)
    word = fourth(word)
    word = fifth(word)
    word = sixth(word)
    word = seventh(word)
    word = eigth(word)
    return word

while True:
    word = input("Toss a word for your stemmer! : ")
    print(f"Here is your stem: {main(word)}")
