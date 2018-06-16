import { Injectable } from '@angular/core';

@Injectable()
export class Globals {
  isBluesTurn: boolean = true;
  teamsTurn: string ;

  isPlayersTurn: boolean = false;
  isGameOver: boolean = false;
  currentGuessesLeft: number = 0;
  numberOfRelatedWords: number = 0;
  blueWordsCount: number = 0;
  redWordsCount: number = 0;
}