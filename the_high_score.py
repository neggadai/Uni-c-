def high(sentense):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    number = [i for i in range(1,len(alphabet)+1)]
    LetterScoreDict = dict(zip(alphabet,number))

    def WordScore(word):
        score = 0
        for letter in word:
            score += LetterScoreDict[letter]
        return score

    def FindMax(sentense):
        ListOfWords = sentense.split()
        HighestScore = 0
        HighWord = None
        for word in ListOfWords:
            score = WordScore(word)
            if score > HighestScore:
                HighestScore = score
                HighWord = word
        return HighWord
    return FindMax(sentense)
