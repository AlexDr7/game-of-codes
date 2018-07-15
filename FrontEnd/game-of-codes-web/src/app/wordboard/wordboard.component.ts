import { Component, OnInit, EventEmitter , Output } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material';

import { Word } from '../word';
import { Game } from '../game';

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
  board : Game;


  redWordActiveArray: Word[];
  blueWordActiveArray: Word[];
  purpleWord: Word;

  singleModeMessages: String[] = ["Well, a win is a win, right?","Okay. But you can do better.", "There is a connection in your team.",
    "Really good work!", "You are amazing!!", "Woooooooooow!!!", "How did you manage to do so well!!?!", "This is ...difficult to believe."]


  constructor(private wordService : WordService, private globals: Globals, private dialog: MatDialog) { 
    
  }

  ngOnInit() {
    this.getWords();
  }

  selectedWord: Word;

  onSelect(word: Word): void{
    this.selectedWord = word;
  }

  getWords(): void {
    if(this.globals.game){
      this.wordlist = this.globals.game.Board;
      console.log(this.wordlist);
    }
    else {
      this.wordService.getWordList().subscribe( wordlist => this.wordlist = wordlist );
      console.log("else");
    }
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
        if(this.wordlist[wordClicked].colour=="B"){
          this.globals.blueWordsCount--;
        }
        else if(this.wordlist[wordClicked].colour=="R"){
          this.globals.redWordsCount--;
        }

        if (!this.checkGameEnd(wordClicked)){
          this.endTurn(wordClicked);
        }
      } 
    }
    
  }


  endTurn(wordClicked){
    if (!this.checkSingleModeEndTurn(wordClicked)){
      if((this.globals.isBluesTurn && this.wordlist[wordClicked].colour!="B") 
          || (!this.globals.isBluesTurn && this.wordlist[wordClicked].colour!="R")) {
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

  checkSingleModeEndTurn(wordClicked){
    if(this.globals.singleMode){
      if((this.globals.isBluesTurn && this.wordlist[wordClicked].colour!="B")) {
        this.globals.isPlayersTurn = false;
        this.gameStateTitle = "You Guessed Incorrectly!";
        this.gameStateMessage = "This ends your turn and one Red Word is revealed";
                
        this.openDialog(this.gameStateTitle, this.gameStateMessage); 

        this.revealRandomRedWord();
      }
      else if(this.globals.numberOfRelatedWords != 0){
        this.globals.currentGuessesLeft--;       
        if(this.globals.currentGuessesLeft<=0){
          this.globals.isPlayersTurn = false;        
          this.gameStateMessage = "This ends your turn and one Red Word is revealed";  
          this.gameStateTitle = "You are out of guesses!!";
            
          this.openDialog(this.gameStateTitle, this.gameStateMessage); 
          this.revealRandomRedWord();
        }
      }
      return true;
    }
    return false;
  }

  revealRandomRedWord(){
    this.populateRedWordActiveArray();
    var randomIndex = Math.floor(Math.random() * this.redWordActiveArray.length);
    console.log(randomIndex);
    console.log(this.redWordActiveArray[randomIndex].index);
    this.globals.activeWords[this.redWordActiveArray[randomIndex].index] = false;
    this.globals.redWordsCount--;
    
    return this.redWordActiveArray[randomIndex];
  }

  populateRedWordActiveArray(){
    this.redWordActiveArray = [];
    for (var i = 0; i < this.wordlist.length; i++){
      if (this.wordlist[i].colour == "R" && this.globals.activeWords[i]){
        this.redWordActiveArray.push(this.wordlist[i]);
      }
    }
  }

  checkGameEnd(wordClicked){

    if(this.globals.redWordsCount==0){
      if (!this.checkSingleModeGameOver(false)){
        this.gameStateTitle = "Red Team Won!!";
        this.gameStateMessage = "Congratulations Red Team!!! ";
        this.globals.teamsTurn = "Red Team Won!";
      }
      this.globals.isBluesTurn = false;
      this.openDialog(this.gameStateTitle, this.gameStateMessage); 
    }
    else if(this.globals.blueWordsCount==0){
      if (!this.checkSingleModeGameOver(true)){
        this.gameStateTitle = "Blue Team Won!!";
        this.gameStateMessage = "Congratulations Blue Team!!! ";
        this.globals.teamsTurn = "Blue Team Won!";
      }
      this.globals.isBluesTurn = true;
      this.openDialog(this.gameStateTitle, this.gameStateMessage); 
    }
    else if(this.wordlist[wordClicked].colour=="P"){
      this.gameStateMessage = "You chose the Purple Word!! ";


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

      this.checkSingleModeGameOver(false);
      this.openDialog(this.gameStateTitle, this.gameStateMessage); 
    }
    else {
      return false;
    }

    this.globals.isGameOver = true;
    this.globals.isPlayersTurn = false;
    return true;

  }

  checkSingleModeGameOver( blueFoundAllWords ){
    if (this.globals.singleMode){
      if(blueFoundAllWords){
        this.gameStateTitle = "Congratulations !! You found all the words!!"
        this.gameStateMessage = " Your score is "+this.globals.redWordsCount+", \""+ this.singleModeMessages[this.globals.redWordsCount]+ "\"";
      }
      else{
        this.gameStateTitle = "You lost!!"
        this.gameStateMessage = " Better luck next time!"
      }
      return true;
    }
    return false;
  }

}
