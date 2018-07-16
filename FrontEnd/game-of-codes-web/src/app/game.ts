
import { Word } from './word';

export interface Game {
    GameID: number;
    isBlueFirst: boolean;
    blueWordsCount: number;
    redWordsCount: number;
    Board: Word[];

    blueCorrectGuesses: number;
    blueWrongGuesses: number;
    redCorrectGuesses: number;
    redWrongGuesses: number;
}
