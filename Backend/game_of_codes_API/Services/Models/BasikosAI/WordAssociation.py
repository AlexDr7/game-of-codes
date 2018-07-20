from pathlib import Path
import wikipedia
import re

class WordAssociation:

    def __init__(self, board):
        self.meaninglessWords = set()
        self.wordsOnBoard = board.wordsOnBoard

        self.allWords = dict()
        self.commonWords = dict()

        self.initializeMeaninglessWords()

    def initializeMeaninglessWords(self):
        p = Path(__file__).parents[0]

        filepath = p / '100mostcommon.txt'
        try:
            with open(filepath) as fp:
                line = fp.readline()
                while line:
                    target_word = line.strip().upper()
                    if target_word not in self.meaninglessWords:
                        self.meaninglessWords.add(target_word)

                    line = fp.readline()
        except IOError:
            print("File Not Found" + filepath)

        return 0

    def calculateSimpleRelevantWords(self, targetWords, searchWidth):

        for targetWord in targetWords:

            searchOutcome = wikipedia.search(targetWord, searchWidth)

            for outcome in searchOutcome:
                self.searchWikipediaBasedOnWord(outcome, targetWord)


    def searchWikipediaBasedOnWord(self, outcome, targetWord):
        try:
            if outcome is not None:
                page = wikipedia.page(outcome)
                if page.content is not None:
                    content = self.sanitizeString(page.content)
                    contentList = content.split(" ")
                    self.addCommonWordsIgnoreMeaningless(contentList, targetWord)
        except wikipedia.exceptions.DisambiguationError as e:
            for title in e.options:
                content = self.sanitizeString(title)
                contentList = content.split(" ")
                self.addCommonWordsIgnoreMeaningless(contentList, targetWord)

        except wikipedia.exceptions.PageError:
            print(" Wikipedia Page not found: " + outcome)


    def addCommonWordsIgnoreMeaningless(self, contentWords, targetWord):

        for contentWord in contentWords:
            contentWordChecked = contentWord.strip().upper()

            if contentWordChecked not in self.meaninglessWords and contentWordChecked not in self.wordsOnBoard\
                    and not self.isRelatedEtymologicallyToBoardWords(contentWordChecked):
                if contentWordChecked in self.allWords:
                    editedList = self.allWords[contentWordChecked]
                    editedList[0] += 1
                    if editedList[len(editedList)-1] != targetWord:
                        editedList.append(targetWord)
                        self.commonWords[contentWordChecked] = editedList

                    self.allWords[contentWordChecked] = editedList
                else:
                    newWordList = [1, targetWord]
                    self.allWords[contentWordChecked] = newWordList

    def deleteEveryWordAssociatedWith(self, badWords, searchWidth):
        for badWord in badWords:
            searchOutcome = wikipedia.search(badWord, searchWidth)
            for outcome in searchOutcome:
                self.searchWikipediaBasedOnWordAndDeleteFromCommon(outcome)

    def searchWikipediaBasedOnWordAndDeleteFromCommon(self, outcome):
        try:
            if outcome is not None:
                page = wikipedia.page(outcome)
                if page.content is not None:
                    content = self.sanitizeString(page.content)
                    contentList = content.split(" ")

                    for contentWord in contentList:
                        contentWordChecked = contentWord.strip().upper()
                        if contentWordChecked in self.commonWords:
                            del self.commonWords[contentWordChecked]

        except wikipedia.exceptions.DisambiguationError as e:
            for title in e.options:
                content = self.sanitizeString(title)
                contentList = content.split(" ")
                for contentWord in contentList:
                    contentWordChecked = contentWord.strip().upper()
                    if contentWordChecked in self.commonWords:
                        del self.commonWords[contentWordChecked]

        except wikipedia.exceptions.PageError:
            print(" Wikipedia Page not found: " + outcome)

    def deleteWordsThatAppearInEveryWord(self):

        for key in list(self.commonWords.keys()):
            if len(self.commonWords[key]) > 5:
                del self.commonWords[key]

    def isRelatedEtymologicallyToBoardWords(self, wordToCheck):
        for boardWord in self.wordsOnBoard:

            if boardWord in wordToCheck or wordToCheck in boardWord:
                return True

        return False


    def sanitizeString(self, stringToBeSanitised):

        #Delete newline characters and u characters
        cleanString = re.sub('\r?\n', " ", stringToBeSanitised)

        #Replace everything that is not a character with space
        cleanString = re.sub('[^A-Za-z ]+', " ", cleanString)

        #Delete every word that is less than 2 characters
        cleanString = re.sub(r'\b[a-zA-Z]{1,2}\b', " ", cleanString)

        #Each word should only be apart by one space character maximum
        cleanString = re.sub('[  ]+', " ", cleanString)

        return cleanString

    def getSortedListOfCommonWords(self):
        return sorted(self.commonWords.items(), key=lambda e: e[1][0], reverse=True)

    def getBestClue(self):
        return self.getSortedListOfCommonWords()[0]

    def printCommonWords(self):
        print(self.commonWords)

    def commonWordsLength(self):
        return len(self.commonWords)