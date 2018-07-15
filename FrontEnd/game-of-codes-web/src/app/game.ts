
import { Word } from './word';

export interface Game {
    GameID: number;
    isBlueFirst: boolean;
    blueWordsCount: number;
    redWordsCount: number;
    Board: Word[];
}
