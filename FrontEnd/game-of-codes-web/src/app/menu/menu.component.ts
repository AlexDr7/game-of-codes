import { Component, OnInit } from '@angular/core';
import { Word } from '../word';
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
    this.getWordList();
  }

  getWordList(): void{
    this.wordService.getWordList().subscribe(wordlist => this.wordlist = wordlist)
  }

  onClickStartNewGame(){
    
    for(var i = 0;i<25;i++) { 
      this.globals.activeWords[i] = true; 
    }
    this.globals.isGameOver = false;
    this.globals.blueWordsCount = 8;
    this.globals.redWordsCount = 8;
    this.globals.teamsTurn = "Blue";
    console.log("constructor");
  }

}