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
  blueGuide: string = "HumanP";
  redPlayer: string = "HumanP";
  redGuide: string = "HumanP";
  
  constructor(private wordService: WordService, private globals: Globals, private router: Router) { }

  ngOnInit() {
    
  }

  getWordList(): void{
    this.wordService.getWordList().subscribe(wordlist => this.wordlist = wordlist)
  }

  getBoardWords(): void {

    this.wordService.getBoard(this.globals.gameSettings).subscribe((data: Game) => {
      console.log(data)
      this.globals.game = data;
      this.wordlist = this.globals.game.Board;
      this.router.navigateByUrl('/wordboard');
    });
  
  }

  onClickStartNewGame(){
    
    for(var i = 0;i<25;i++) { 
      this.globals.activeWords[i] = true; 
    }
    this.globals.isGameOver = false;
    this.globals.blueWordsCount = 8;
    this.globals.redWordsCount = 8;
    this.globals.teamsTurn = "Blue's Turn";
    this.globals.canNotPass = true;

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