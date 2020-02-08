def delAccent(word):
    accents = ['á', 'à', 'ã', 'â', 'ä', 'é', 'è', 'ê', 'í', 'ì', 'î', 'ó', 'ò', 'õ', 'ô', 'ö', 'ú', 'ù', 'û', 'ü', 'ç']
    for c0 in range(len(word)):
        change = ''
        for c1 in range(0, len(accents)):
            if c1 <= 4:
                change = 'a'
            elif 4 < c1 <= 7:
                change = 'e'
            elif 7 < c1 <= 10:
                change = 'i'
            elif 10 < c1 <= 15:
                change = 'o'
            elif 15 < c1 <= 19:
                change = 'u'
            elif c1 > 19:
                change = 'c'

            if word[c0].lower() == accents[c1]:
                if word[c0].isupper() == 1:
                    word = word.replace(word[c0], change.upper())
                else:
                    word = word.replace(word[c0], change.lower())
                break

    return word

