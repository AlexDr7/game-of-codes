import { Component, OnInit } from '@angular/core';
import { Word } from '../word';
import { Game } from '../game';
import { GameSettings } from '../gamesettings';

import { WordService } from '../word.service';

import {Router} from '@angular/router';

import { Globals } from '../globals'

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  wordlist: Word[] = [];
  bluePlayer: string = "HumanP";
  blueGuide: string = "HumanG";
  redPlayer: string = "HumanP";
  redGuide: string = "HumanG";
  loading: boolean = false;

  constructor(private wordService: WordService, private globals: Globals, private router: Router) { }

  ngOnInit() {
    
  }

  getWordList(): void{
    this.wordService.getWordList().subscribe(wordlist => this.wordlist = wordlist)
  }

  getBoardWords(): void {
    this.loading = true;
    this.wordService.getBoard(this.globals.gameSettings).subscribe((data: Game) => {
      this.loading = false;
      this.globals.game = data;
      this.globals.isBluesTurn = this.globals.game.isBlueFirst;
      this.globals.blueWordsCount = this.globals.game.blueWordsCount;
      this.globals.redWordsCount = this.globals.game.redWordsCount;
      this.globals.gameid = this.globals.game.GameID;

      this.globals.game.blueCorrectGuesses = 0;
      this.globals.game.blueWrongGuesses = 0;
      this.globals.game.redCorrectGuesses = 0;
      this.globals.game.redWrongGuesses = 0;

      this.globals.game.winner = 'Null';

      if (!this.globals.isBluesTurn){
        this.globals.teamsTurn = "Red's Turn";
      }
      this.wordlist = this.globals.game.Board;
      this.router.navigateByUrl('/wordboard');
    });
    this.globals.clueList= [];
  }

  onClickStartNewGame(){
    
    for(var i = 0;i<25;i++) { 
      this.globals.activeWords[i] = true; 
    }
    this.globals.isGameOver = false;
    
    this.globals.isPlayersTurn = false;
    this.globals.isAITurn = false;
    this.globals.teamsTurn = "Blue's Turn";
    this.globals.canNotPass = true;

    this.globals.clueIndex=-1;
    this.globals.clueList=[];

    this.globals.gameSettings  = {
      singleMode : this.globals.singleMode,
      bluePlayer : this.bluePlayer,
      blueGuide : this.blueGuide,
      redPlayer : this.redPlayer,
      redGuide : this.redGuide
    }
    this.getBoardWords();
  }

}