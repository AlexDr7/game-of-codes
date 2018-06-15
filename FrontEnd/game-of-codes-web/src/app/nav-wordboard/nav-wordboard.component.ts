import { Component, OnInit , EventEmitter , Output} from '@angular/core';

import {Globals} from '../globals'

@Component({
  selector: 'app-nav-wordboard',
  templateUrl: './nav-wordboard.component.html',
  styleUrls: ['./nav-wordboard.component.css']
})
export class NavWordboardComponent implements OnInit {

  @Output() guidesTurn = new EventEmitter<any>();

  currentClue;
  relatedWords;

  constructor(private globals: Globals) { }

  ngOnInit() {
  }

  toGuidesTurnClick(){
    this.guidesTurn.emit();
  }

  onGiveClueClick(clue : string, related : number){
    if(clue){
      this.currentClue = clue;
      this.relatedWords = related;
      
      this.globals.isPlayersTurn = true;
      this.globals.currentGuessesLeft = related;

      this.guidesTurn.emit(clue);
    }
  }

}
