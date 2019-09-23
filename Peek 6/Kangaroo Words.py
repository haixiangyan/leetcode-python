def findKangarooScore(words, wordsToSynonyms, wordsToAntonyms):
    wts = {}
    for item in wordsToSynonyms:
        token = item.split(':')[0].lower()
        synonyms = item.split(':')[1].split(',')
        wts[token] = synonyms
    wta = {}
    for item in wordsToAntonyms:
        token = item.split(':')[0].lower()
        antonyms = item.split(':')[1].split(',')
        wta[token] = antonyms

    score = 0
    visitedSynonyms, visitedAntonyms = set(), set()
    for word in words:
        word = word.lower()
        if word in wts:
            for synonyms in wts[word]:
                synonyms = synonyms.lower()
                if isInside(word, synonyms) and synonyms not in visitedSynonyms:
                    visitedSynonyms.add(synonyms)
                    score += 1
        if word in wta:
            for antonyms in wta[word]:
                antonyms = antonyms.lower()
                if isInside(word, antonyms) and antonyms not in visitedAntonyms:
                    score -= 1
                    visitedAntonyms.add(antonyms)

    return score


def isInside(word, wordlike):
    index1, index2 = 0, 0
    while index1 < len(word) and index2 < len(wordlike):
        if word[index1] == wordlike[index2]:
            index2 += 1
        index1 += 1

    return index2 == len(wordlike)


words = ['Devilish', 'Devilishly', 'phone']
wordsToSynonyms = ['Devilish:evil', 'phone:cell,telephone', 'decoy:facade,fake', 'Devilishly:evil']
wordsToAntonyms = ['decoy:truth,real']

print(findKangarooScore(words, wordsToSynonyms, wordsToAntonyms))
