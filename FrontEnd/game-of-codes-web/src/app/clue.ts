import { Word } from './word';

export class Clue {
    gameID: number;
    clueID: number;
    colour: string;
    wordsGuessed: Word[];
    badness: number;
    numOfHintedWords: number;
    numOfCorrectlyGuessed: number;
    clueText: string;
    playerName: string;
    guideName: string;

    constructor(gameId: number,clueTxt: string, colour: string, numOfWordsHinted:number, numOfCorrectlyGuessed:number, playerName: string, guideName: string){
        this.gameID = gameId;
        this.clueText = clueTxt;
        this.colour = colour;
        this.numOfHintedWords = numOfWordsHinted;
        this.numOfCorrectlyGuessed = numOfCorrectlyGuessed;
        this.playerName = playerName;
        this.guideName = guideName;
        this.wordsGuessed = [];
        this.badness = -1;
    }
}