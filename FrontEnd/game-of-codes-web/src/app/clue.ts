import { Word } from './word';

export class Clue {
    GameID: number;
    clueID: number;
    colour: string;
    wordsGuessed: Word[];
    badness: number;
    numOfHintedWords: number;
    numOfCorrectlyGuessed: number;
    clueText: string;
    playerName: string;
    guideName: string;
    teamTurn: string;

    constructor(gameId: number,clueTxt: string, colour: string, numOfWordsHinted:number, numOfCorrectlyGuessed:number, playerName: string, guideName: string){
        this.GameID = gameId;
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