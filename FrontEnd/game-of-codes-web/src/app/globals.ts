import { Injectable } from '@angular/core';

@Injectable()
export class Globals {
  isBluesTurn: boolean = true;
  isPlayersTurn: boolean = false;
  currentGuessesLeft: number = 0;
}