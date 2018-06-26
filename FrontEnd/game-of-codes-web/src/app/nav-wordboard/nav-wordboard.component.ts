import { Component, OnInit , EventEmitter , Output} from '@angular/core';

import {Globals} from '../globals'

@Component({
  selector: 'app-nav-wordboard',
  templateUrl: './nav-wordboard.component.html',
  styleUrls: ['./nav-wordboard.component.css']
})
export class NavWordboardComponent implements OnInit {

  @Output() guidesTurn = new EventEmitter<any>();

  constructor(private globals: Globals) { }

  ngOnInit() {
  }

  toGuidesTurnClick(){
    this.guidesTurn.emit();
  }

  onGiveClueClick(clue : string, related : number){
    if(clue){
      this.globals.currentClue = clue;
      this.globals.numberOfRelatedWords = related;
      
      this.globals.isPlayersTurn = true;
      this.globals.currentGuessesLeft = related;

      this.guidesTurn.emit(clue);
    }
  }

}
