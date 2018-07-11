import { Component, OnInit } from '@angular/core';
import { Word } from '../word';
import { Game } from '../game';
import { WordService } from '../word.service';

import { Globals } from '../globals'

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  wordlist: Word[] = [];

  constructor(private wordService: WordService, private globals: Globals) { }

  ngOnInit() {
    
  }

  getWordList(): void{
    this.wordService.getWordList().subscribe(wordlist => this.wordlist = wordlist)
  }

  getBoardWords(): void {
    this.wordService.getBoard(this.globals.gameid).subscribe((data: Game) => {
      console.log(data)
      this.globals.game = data;
      this.wordlist = this.globals.game.Board;
      console.log(this.globals.game.Board);
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

    this.getBoardWords();
  }

}