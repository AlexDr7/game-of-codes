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

  wordlist : Word[];
  isWordboardVisible = false;
  currentClue;

  activeWords : boolean[] = new Array(25);

  constructor(private wordService : WordService, private globals: Globals) { 
    
    for(var i = 0;i<25;i++) { 
      this.activeWords[i] = true; 
    }

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

  toGuidesTurn($event): void {
    if(!this.globals.isPlayersTurn){
      if(this.isWordboardVisible){
        this.isWordboardVisible=false;
      }
      else{
        this.isWordboardVisible=true;
      }
      console.log("Button Click"+this.globals.isPlayersTurn);
    }
    else{
      this.isWordboardVisible=false;
    }
    
  }

  clickWord( wordClicked : number){
    if(this.globals.isPlayersTurn){
      if(this.activeWords[wordClicked]){
        this.activeWords[wordClicked] = false;
        this.globals.currentGuessesLeft--;
        if(this.globals.currentGuessesLeft<=0){
          this.globals.isPlayersTurn = false;
        }
      } 
    }
    
  }

}
