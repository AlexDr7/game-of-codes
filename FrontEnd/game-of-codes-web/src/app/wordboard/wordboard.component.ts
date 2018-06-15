import { Component, OnInit, EventEmitter , Output } from '@angular/core';
import { Word } from '../word';
import { WordService } from '../word.service';

import {Globals} from '../globals'

@Component({
  selector: 'app-wordboard',
  templateUrl: './wordboard.component.html',
  styleUrls: ['./wordboard.component.css']
})
export class WordboardComponent implements OnInit {

  @Output() changeTurn = new EventEmitter();

  word: Word = {
    id: 0,
    value: "Knife",
    colour: "Blue"
  };

  wordlist : Word[];
  isWordboardVisible = false;
  isPlayersTurn = false;

  constructor(private wordService : WordService, private globals: Globals) { 
    this.isPlayersTurn = globals.isPlayersTurn;
  }

  ngOnInit() {
    this.getWords();
  }

  selectedWord: Word;

  onSelect(word: Word): void{
    this.selectedWord = word;
  }

  getWords(): void {
      this.wordService.getWordList().subscribe( wordlist => this.wordlist = wordlist )
  }

  toGuidesTurn(isPlayersTime : boolean): void {
    if(!isPlayersTime){
      if(this.isWordboardVisible){
        this.isWordboardVisible=false;
      }
      else{
        this.isWordboardVisible=true;
      }
      console.log("Button Click"+isPlayersTime);
    }
    else{
      this.isWordboardVisible=false;
      this.changeTurns(isPlayersTime);
    }
    
  }

  changeTurns(isPlayersTime: boolean): void {
    console.log("Button Click2"+isPlayersTime);
    this.isPlayersTurn = isPlayersTime;
    this.globals.isPlayersTurn=this.isPlayersTurn;
  }

}
