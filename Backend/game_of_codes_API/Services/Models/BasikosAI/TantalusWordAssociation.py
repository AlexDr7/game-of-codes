import wikipedia
import re

from Services.Models.BasikosAI.WordAssociation import WordAssociation

#This agent is similar to normal WordAssociation but works with summary of wikipedia pages

class TantalusWordAssociation(WordAssociation):

    def __init__(self, board):
        super().__init__(board)


    def TantalusRelateClueToWordsOnBoardforPlayer(self, clueWord, wordsActiveOnBoard, clueSearchWidth, wordsOnBoardSearchWidth,
                                          wordsOnBoardMaxWordSearch):

        #Initialize AllWords with all the words that appear in articles related to the clue
        searchOutcome = wikipedia.search(clueWord, clueSearchWidth)

        for outcome in searchOutcome:
            try:
                if outcome is not None:
                    page = wikipedia.page(outcome)
                    if page.content is not None:
                        content = self.sanitizeString(page.content)
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
            searchOutcome = wikipedia.search(word, wordsOnBoardSearchWidth)

            if word in self.allWords:
                self.commonWords[word][0] += float(self.allWords[word][0])*250

            self.countWords = 0

            for outcome in searchOutcome:
                try:
                    if outcome is not None:
                        if self.countWords > wordsOnBoardMaxWordSearch:
                            break;
                        page = wikipedia.page(outcome)
                        if page.content is not None:
                            content = self.sanitizeString(page.content)
                            contentList = content.split(" ")
                            self.addCommonWordsforPlayer(contentList, word, wordsOnBoardMaxWordSearch, clueWord)

                except wikipedia.exceptions.DisambiguationError as e:
                    for title in e.options:
                        content = self.sanitizeString(title)
                        contentList = content.split(" ")
                        self.addCommonWordsforPlayer(contentList, word, wordsOnBoardMaxWordSearch, clueWord)
                    if self.countWords > wordsOnBoardMaxWordSearch:
                        break;

                except wikipedia.exceptions.PageError:
                    print(" Wikipedia Page not found: " + outcome)

    def addAllWordsIgnoreMeaninglessforPlayer(self, contentWords, targetWord):
        for contentWord in contentWords:
            contentWordChecked = contentWord.strip().upper()

            if contentWordChecked not in self.meaninglessWords and contentWordChecked not in self.wordsOnBoard\
                    and not self.isRelatedEtymologicallyToBoardWords(contentWordChecked):
                if contentWordChecked in self.allWords:
                    editedList = self.allWords[contentWordChecked]
                    editedList[0] += 1
                    self.allWords[contentWordChecked] = editedList
                else:
                    newWordList = [1, targetWord]
                    self.allWords[contentWordChecked] = newWordList

    def addCommonWordsforPlayer(self, contentWords, targetWord, wordsOnBoardMaxWordSearch, clueWord):
        for contentWord in contentWords:
            contentWordChecked = contentWord.strip().upper()
            self.countWords += 1;
            if contentWordChecked in self.allWords:
                self.commonWords[targetWord][0] += float(self.allWords[contentWordChecked][0])/2.0
            if contentWordChecked == clueWord :
                self.commonWords[targetWord][0] += 300
            if self.countWords > wordsOnBoardMaxWordSearch:
                break;
