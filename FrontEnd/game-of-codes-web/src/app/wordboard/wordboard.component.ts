import { Component, OnInit, EventEmitter , Output } from '@angular/core';
import { Word } from '../word';
import { WordService } from '../word.service';

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

  constructor(private wordService : WordService) { }

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

  toGuidesTurn(): void {
    if(this.isWordboardVisible){
      this.isWordboardVisible=false;
    }
    else{
      this.isWordboardVisible=true;
    }
    
    console.log("Button Click");
  }

}
