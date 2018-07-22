import { Component, OnInit , EventEmitter , Output} from '@angular/core';

import {Globals} from '../globals'
import { Clue } from '../clue';

import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-nav-wordboard',
  templateUrl: './nav-wordboard.component.html',
  styleUrls: ['./nav-wordboard.component.css']
})
export class NavWordboardComponent implements OnInit {

  @Output() guidesTurn = new EventEmitter<any>();

  newClue : Clue;

  constructor(private globals: Globals, private http: HttpClient) { }

  ngOnInit() {
  }

  toGuidesTurnClick(){
    this.guidesTurn.emit();
  }

  onGiveClueClick(clue : string, related : number){
    if(clue){
      this.globals.currentClue = clue;
      this.globals.numberOfRelatedWords = related;
      this.globals.canNotPass = true;

      this.globals.clueIndex++;
      if (this.globals.isBluesTurn){
        var playerName = this.globals.gameSettings.bluePlayer;
        var guideName = this.globals.gameSettings.blueGuide; 
      }
      else{
        var playerName = this.globals.gameSettings.redPlayer;
        var guideName = this.globals.gameSettings.redGuide; 
      }

      this.globals.clueList.push(new Clue(this.globals.gameid,clue,this.globals.teamsTurn[0],related,0,playerName,guideName))

      
      this.sendClue(this.globals.clueList[this.globals.clueIndex]).subscribe( data => { 
        this.globals.clueList[this.globals.clueIndex].clueID = data
        
        this.globals.isPlayersTurn = true;
        this.globals.currentGuessesLeft = related;

        this.guidesTurn.emit();
        }
      );

    }
  }

  onPass(){
    this.globals.isPlayersTurn = false;
    this.globals.canNotPass = true;
    if(this.globals.isBluesTurn && !this.globals.singleMode){
      this.globals.isBluesTurn = false;
      this.globals.teamsTurn = "Red's Turn";
    }
    else {
      this.globals.isBluesTurn = true;
      this.globals.teamsTurn = "Blue's Turn";
    }
    this.globals.clueList[this.globals.clueIndex].badness = 2;
    this.updateCurrentClue();
    this.guidesTurn.emit("pass");
  }

  sendClue(clue){
    return this.http.post<number>(this.globals.APIurl+"addClue", clue , this.globals.httpOptions);
  }

  updateCurrentClue(){
    return this.http.post<number>(this.globals.APIurl+"updateClue", this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe();
  }

}
