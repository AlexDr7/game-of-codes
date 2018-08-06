from pathlib import Path
import wikipedia
import re

from Services.Models.BasikosAI.WordAssociation import WordAssociation

#This agent is similar to normal WordAssociation but works with summary of wikipedia pages

class ErmisWordAssociation(WordAssociation):

    def __init__(self, board, upperWordLimit = 500, numOfSentences=5):
        self.upperWordLimit = upperWordLimit
        self.numberOfSentences = numOfSentences
        super().__init__(board)

    def searchWikipediaBasedOnWord(self, outcome, targetWord):
        if self.countWords > self.upperWordLimit:
            print(targetWord, " Limit of words ", self.countWords)
            return
        try:
            if outcome is not None:
                page = wikipedia.summary(outcome, self.numberOfSentences)
                if page is not None:
                    content = self.sanitizeString(page)
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
            self.countWords = self.countWords + 1
            if self.countWords > self.upperWordLimit:
                print(targetWord, " Limit of words ", self.countWords)
                break

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

    def searchWikipediaBasedOnWordAndDeleteFromCommon(self, outcome):
        if self.countWords > self.upperWordLimit:
            return

        try:
            if outcome is not None:
                page = wikipedia.summary(outcome, self.numberOfSentences)
                if page is not None:
                    content = self.sanitizeString(page)
                    contentList = content.split(" ")

                    for contentWord in contentList:
                        self.countWords = self.countWords + 1
                        if self.countWords > self.upperWordLimit:
                            break
                        contentWordChecked = contentWord.strip().upper()
                        if contentWordChecked in self.commonWords:
                            del self.commonWords[contentWordChecked]

        except wikipedia.exceptions.DisambiguationError as e:
            for title in e.options:
                content = self.sanitizeString(title)
                contentList = content.split(" ")
                for contentWord in contentList:
                    self.countWords = self.countWords + 1
                    if self.countWords > self.upperWordLimit:
                        break
                    contentWordChecked = contentWord.strip().upper()
                    if contentWordChecked in self.commonWords:
                        del self.commonWords[contentWordChecked]

        except wikipedia.exceptions.PageError:
            print(" Wikipedia Page not found: " + outcome)

    def relateClueToWordsOnBoardforErmisPlayer(self, clueWord, wordsActiveOnBoard, wikipediaClueSearchWidth, wikipediaWordsOnBoardSearchWidth):

        #Initialize AllWords with all the words that appear in articles related to the clue
        searchOutcome = wikipedia.search(clueWord, wikipediaClueSearchWidth)

        for outcome in searchOutcome:
            try:
                if outcome is not None:
                    page = wikipedia.summary(outcome, self.numberOfSentences)
                    if page is not None:
                        content = self.sanitizeString(page)
                        contentList = content.split(" ")
                        self.addAllWordsIgnoreMeaninglessforPlayer(contentList, clueWord)
            except wikipedia.exceptions.DisambiguationError as e:
                for title in e.options:
                    content = self.sanitizeString(title)
                    contentList = content.split(" ")
                    self.addAllWordsIgnoreMeaninglessforPlayer(contentList, clueWord)

            except wikipedia.exceptions.PageError:
                print(" Wikipedia Page not found: " + outcome)

        #Search articles of every word on the board and compare the articles to the articles related to the clue
        for word in wordsActiveOnBoard.keys():

            newWordList = [0, wordsActiveOnBoard[word]]
            self.commonWords[word] = newWordList
            searchOutcome = wikipedia.search(word, wikipediaWordsOnBoardSearchWidth)

            if word in self.allWords:
                self.commonWords[word][0] += float(self.allWords[word][0])*500

            self.countWords = 0

            for outcome in searchOutcome:
                print(word, "  ", self.commonWords[word][0])
                try:
                    if outcome is not None:
                        if self.countWords > self.upperWordLimit:
                            break;
                        page = wikipedia.summary(outcome, self.numberOfSentences)
                        if page is not None:
                            content = self.sanitizeString(page)
                            contentList = content.split(" ")
                            self.addCommonWordsforPlayer(contentList, word, self.upperWordLimit, clueWord)

                except wikipedia.exceptions.DisambiguationError as e:
                    for title in e.options:
                        content = self.sanitizeString(title)
                        contentList = content.split(" ")
                        self.addCommonWordsforPlayer(contentList, word, self.upperWordLimit, clueWord)
                    if self.countWords > self.upperWordLimit:
                        break;

                except wikipedia.exceptions.PageError:
                    print(" Wikipedia Page not found: " + outcome)

    def addCommonWordsforPlayer(self, contentWords, targetWord, wordsOnBoardMaxWordSearch, clueWord):
        for contentWord in contentWords:
            contentWordChecked = contentWord.strip().upper()
            self.countWords += 1;
            if contentWordChecked in self.allWords:
                self.commonWords[targetWord][0] += float(self.allWords[contentWordChecked][0])
            if contentWordChecked == clueWord:
                self.commonWords[targetWord][0] += 1200
            if self.countWords > self.upperWordLimit:
                break;
