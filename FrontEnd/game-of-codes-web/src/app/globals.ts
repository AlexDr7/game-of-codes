import { Injectable } from '@angular/core';
import { Game } from './game';
import { GameSettings } from './gamesettings';

@Injectable()
export class Globals {
  gameid: number = 0 ;
  game: Game;

  isBluesTurn: boolean = true;
  teamsTurn: string ;

  isPlayersTurn: boolean = false;
  canNotPass: boolean = true;
  isGameOver: boolean = true;
  
  singleMode: boolean = false;
  gameSettings: GameSettings;

  currentClue : string;
  currentGuessesLeft: number = 0;
  numberOfRelatedWords: number = 0;

  blueWordsCount: number = 0;
  redWordsCount: number = 0;
  activeWords : boolean[] = new Array(25);

}