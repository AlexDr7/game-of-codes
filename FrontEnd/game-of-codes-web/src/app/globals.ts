import { Injectable } from '@angular/core';
import { Game } from './game';
import { GameSettings } from './gamesettings';
import { Clue } from './clue';

import { HttpHeaders } from '@angular/common/http';

@Injectable()
export class Globals {
  APIurl: string = "http://0.0.0.0:8000/";
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json'
    })
  }

  gameid: number = 0 ;
  game: Game;

  isBluesTurn: boolean = true;
  teamsTurn: string ;
  isAITurn: boolean = false;

  isPlayersTurn: boolean = false;
  canNotPass: boolean = true;
  isGameOver: boolean = true;
  
  singleMode: boolean = false;
  gameSettings: GameSettings;

  
  currentGuessesLeft: number = 0;
  numberOfRelatedWords: number = 0;

  clueList: Clue[];
  clueIndex: number = -1;
  currentClue : string;

  blueWordsCount: number = 0;
  redWordsCount: number = 0;
  activeWords : boolean[] = new Array(25);

  
}