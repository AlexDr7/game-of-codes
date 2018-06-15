import { Component, OnInit , EventEmitter , Output} from '@angular/core';

import {Globals} from '../globals'

@Component({
  selector: 'app-nav-wordboard',
  templateUrl: './nav-wordboard.component.html',
  styleUrls: ['./nav-wordboard.component.css']
})
export class NavWordboardComponent implements OnInit {

  @Output() guidesTurn = new EventEmitter<boolean>();

  currentClue;

  isPlayersTurn=true;
  isBluesTurn=true;

  constructor(private globals: Globals) {
      this.isPlayersTurn = globals.isPlayersTurn;
      this.isBluesTurn = globals.isBluesTurn;
   }

  ngOnInit() {
  }

  toGuidesTurnClick(){
    this.guidesTurn.emit(this.isPlayersTurn);
  }

  onGiveClueClick(clue : string){

    this.currentClue = clue;
    
    this.isPlayersTurn = true;
    this.globals.isPlayersTurn = true;

    this.guidesTurn.emit(this.isPlayersTurn);
  }

}
