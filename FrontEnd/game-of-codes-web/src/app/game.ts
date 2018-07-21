
import { Word } from './word';

export interface Game {
    GameID: number;
    isBlueFirst: boolean;
    blueWordsCount: number;
    redWordsCount: number;
    Board: Word[];

    teamTurn: string;

    blueCorrectGuesses: number;
    blueWrongGuesses: number;
    redCorrectGuesses: number;
    redWrongGuesses: number;
}
