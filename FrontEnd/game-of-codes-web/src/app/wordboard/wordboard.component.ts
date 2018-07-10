import { Component, OnInit, EventEmitter , Output } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material';

import { Word } from '../word';
import { Board } from '../board';
import { WordService } from '../word.service';

import { Globals } from '../globals'
import { GameDialogComponent } from '../game-dialog/game-dialog.component';

@Component({
  selector: 'app-wordboard',
  templateUrl: './wordboard.component.html',
  styleUrls: ['./wordboard.component.css']
})
export class WordboardComponent implements OnInit {

  @Output() changeTurn = new EventEmitter();

  wordlist : Word[];
  isWordboardVisible = false;
  currentClue: string;
  gameStateMessage: string;
  gameStateTitle: string;
  teamPlayingMessage: string;
  board : Board;


  constructor(private wordService : WordService, private globals: Globals, private dialog: MatDialog) { 
    
  }

  ngOnInit() {
    this.getBoardWords();
  }

  selectedWord: Word;

  onSelect(word: Word): void{
    this.selectedWord = word;
  }

  getWords(): void {
    this.wordService.getWordList().subscribe( wordlist => this.wordlist = wordlist )
  }

  getBoardWords(): void {
    this.wordService.getBoard(this.globals.game).subscribe((data: Board) => this.board = {
      GameID: data['GameID'],
      Board:  data['Board']
    });
  }

  toGuidesTurn($event): void {
    if(!this.globals.isPlayersTurn){
      if(this.isWordboardVisible){
        this.isWordboardVisible=false;
      }
      else{
        this.isWordboardVisible=true;
      }
    }
    else{
      this.isWordboardVisible=false;
    }
    
  }

  openDialog(title: string, message: string) {
    const dialogConfig = new MatDialogConfig();

        dialogConfig.disableClose = false;
        dialogConfig.autoFocus = true;

        dialogConfig.data = {
          title: title,
          description: message
        };

        this.dialog.open(GameDialogComponent, dialogConfig);
  }

  clickWord( wordClicked : number){
    if(this.globals.isPlayersTurn){
      if(this.globals.activeWords[wordClicked]){
        
        this.globals.activeWords[wordClicked] = false;
        this.globals.canNotPass = false;
        if(this.wordlist[wordClicked].colour=="BLUE"){
          this.globals.blueWordsCount--;
        }
        else if(this.wordlist[wordClicked].colour=="RED"){
          this.globals.redWordsCount--;
        }

        if(this.globals.redWordsCount==0){
          this.gameStateTitle = "Red Team Won!!";
          this.gameStateMessage = "Congratulations Red Team!!! ";
          this.globals.isGameOver = true;
          this.globals.isPlayersTurn = false;
          this.globals.teamsTurn = "Red Team Won!";
          this.globals.isBluesTurn = false;
          this.openDialog(this.gameStateTitle, this.gameStateMessage); 
        }
        else if(this.globals.blueWordsCount==0){
          this.gameStateTitle = "Blue Team Won!!";
          this.gameStateMessage = "Congratulations Blue Team!!! ";
          this.globals.isGameOver = true;
          this.globals.isPlayersTurn = false;
          this.globals.teamsTurn = "Blue Team Won!";
          this.globals.isBluesTurn = true;
          this.openDialog(this.gameStateTitle, this.gameStateMessage); 
        }
        else if(this.wordlist[wordClicked].colour=="PURPLE"){
          this.gameStateMessage = "You chose the Purple Word!! ";
          this.globals.isGameOver = true;
          this.globals.isPlayersTurn = false;
          if(this.globals.isBluesTurn){
            this.gameStateTitle = "Blue Team Defeat!!";
            this.globals.teamsTurn = "Red Team Won!";
            this.globals.isBluesTurn = false;
          }
          else {
            this.gameStateTitle = "Red Team Defeat!!";
            this.globals.teamsTurn = "Blue Team Won!";
            this.globals.isBluesTurn = true;
          }

          this.openDialog(this.gameStateTitle, this.gameStateMessage); 
        }
        else if((this.globals.isBluesTurn && this.wordlist[wordClicked].colour!="BLUE") 
        || (!this.globals.isBluesTurn && this.wordlist[wordClicked].colour!="RED")) {
          this.globals.isPlayersTurn = false;
          this.gameStateTitle = " Guessed Incorrectly!";
          this.gameStateMessage = "This ends your turn ";
          if(this.globals.isBluesTurn){
            this.gameStateTitle = "Blue Team"+this.gameStateTitle;
            this.globals.isBluesTurn = false;
            this.globals.teamsTurn = "Red's Turn";
          }
          else{
            this.gameStateTitle = "Red Team"+this.gameStateTitle;
            this.globals.isBluesTurn = true;
            this.globals.teamsTurn = "Blue's Turn";
          }
          this.openDialog(this.gameStateTitle, this.gameStateMessage); 
        }
        else if(this.globals.numberOfRelatedWords != 0){
          this.globals.currentGuessesLeft--;       
          if(this.globals.currentGuessesLeft<=0){
            this.globals.isPlayersTurn = false;        
            this.gameStateMessage = "This ends your turn ";
            if(this.globals.isBluesTurn){
              this.gameStateTitle = "Blue Team is out of guesses!!";
              this.globals.isBluesTurn = false;
              this.globals.teamsTurn = "Red's Turn";
            }
            else{
              this.gameStateTitle = "Red Team is out of guesses!!";
              this.globals.isBluesTurn = true;
              this.globals.teamsTurn = "Blue's Turn";
            }
            this.openDialog(this.gameStateTitle, this.gameStateMessage); 
          }
        }

      } 
    }
    
  }

}
