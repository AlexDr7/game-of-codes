import { Component, OnInit, EventEmitter , Output } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material';

import { Word } from '../word';
import { Clue } from '../clue';
import { Game } from '../game';

import { WordService } from '../word.service';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';

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

  AIPlayermsg: string;

  redWordActiveArray: Word[];
  blueWordActiveArray: Word[];
  purpleWord: Word;
  previousAITurnTime: number;

  GuessClueinterval ;

  singleModeMessages: String[] = ["Well, a win is a win, right?","Okay. But you can do better.", "There is a connection in your team.",
    "Really good work!", "You are amazing!!", "Woooooooooow!!!", "How did you manage to do so well!!?!", "This is ...difficult to believe."]


  constructor(private wordService : WordService, private globals: Globals, private dialog: MatDialog, private router: Router, private http: HttpClient) { 
    this.AIPlayermsg = " Words Guessed by AI: ";
  }

  ngOnInit() {
    
    if (this.globals.isGameOver){
      this.router.navigateByUrl('/menu');
    }
    else {
      this.getWords();
      this.checkAITurn();      
    }
    
  }

  selectedWord: Word;

  onSelect(word: Word): void{
    this.selectedWord = word;
  }

  getVasikiaClue(){
    this.globals.isAITurn = true;
    this.globals.game.teamTurn = this.globals.teamsTurn[0];

    this.http.post(this.globals.APIurl+"guideVasikiaAskClue", this.globals.game , this.globals.httpOptions).subscribe((data: Clue) => {
      this.globals.clueList.push(data)
      this.globals.clueIndex++;
      this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed = 0;
      this.globals.clueList[this.globals.clueIndex].wordsGuessed = []
      this.globals.isAITurn = false;
      this.globals.canNotPass = true;

      this.globals.isPlayersTurn = true;
      this.globals.isVasikiaActive = false;
      this.globals.currentGuessesLeft = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;
      this.globals.numberOfRelatedWords = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;

      this.globals.currentClue = this.globals.clueList[this.globals.clueIndex].clueText;

      this.checkAITurn();
    },
    error => {
      this.openDialog(" Error while getting data from the server while asking for clue", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  getSlowVasikiaClue(){
    this.globals.isAITurn = true;
    this.globals.game.teamTurn = this.globals.teamsTurn[0];

    this.http.post(this.globals.APIurl+"guideSlowVasikiaAskClue", this.globals.game , this.globals.httpOptions).subscribe((data: Clue) => {
      this.globals.clueList.push(data)
      this.globals.clueIndex++;
      this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed = 0;
      this.globals.clueList[this.globals.clueIndex].wordsGuessed = []
      this.globals.isAITurn = false;
      this.globals.canNotPass = true;

      this.globals.isPlayersTurn = true;
      this.globals.isVasikiaActive = false;
      this.globals.currentGuessesLeft = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;
      this.globals.numberOfRelatedWords = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;

      this.globals.currentClue = this.globals.clueList[this.globals.clueIndex].clueText;

      this.checkAITurn();
    },
    error => {
      this.openDialog(" Error while getting data from the server while asking for clue", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  getErmisClue(){
    this.globals.isAITurn = true;
    this.globals.game.teamTurn = this.globals.teamsTurn[0];

    this.http.post(this.globals.APIurl+"guideErmisAskClue", this.globals.game , this.globals.httpOptions).subscribe((data: Clue) => {
      this.globals.clueList.push(data)
      this.globals.clueIndex++;
      this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed = 0;
      this.globals.clueList[this.globals.clueIndex].wordsGuessed = []
      this.globals.isAITurn = false;
      this.globals.canNotPass = true;

      this.globals.isErmisActive = false;

      this.globals.isPlayersTurn = true;
      this.globals.currentGuessesLeft = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;
      this.globals.numberOfRelatedWords = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;

      this.globals.currentClue = this.globals.clueList[this.globals.clueIndex].clueText;

      this.checkAITurn();
    },
    error => {
      this.openDialog(" Error while getting data from the server while asking for clue", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  getTantalusClue(){
    this.globals.isAITurn = true;
    this.globals.game.teamTurn = this.globals.teamsTurn[0];

    this.http.post(this.globals.APIurl+"guideTantalusAskClue", this.globals.game , this.globals.httpOptions).subscribe((data: Clue) => {
      this.globals.clueList.push(data)
      this.globals.clueIndex++;
      this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed = 0;
      this.globals.clueList[this.globals.clueIndex].wordsGuessed = []
      this.globals.isAITurn = false;
      this.globals.canNotPass = true;
      
      this.globals.isTantalusActive = false;

      this.globals.isPlayersTurn = true;
      this.globals.currentGuessesLeft = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;
      this.globals.numberOfRelatedWords = this.globals.clueList[this.globals.clueIndex].numOfHintedWords;

      this.globals.currentClue = this.globals.clueList[this.globals.clueIndex].clueText;

      this.checkAITurn();
    },
    error => {
      this.openDialog(" Error while getting data from the server while asking for clue", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  giveClueToVasikia(){
    this.globals.isAITurn = true;
    this.globals.isPlayersTurn = true;
    this.globals.clueList[this.globals.clueIndex].teamTurn = this.globals.teamsTurn[0]
    this.http.post(this.globals.APIurl+"playerVasikiaGiveClue",  this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe(data => {

      this.globals.clueList[this.globals.clueIndex].clueID = data["clueID"];
      var wordsToBeGuessed = data["wordsToBeGuessed"];

      var i=0;

      this.GuessClueinterval = setInterval(()=>{          
        if(i <= this.globals.clueList[this.globals.clueIndex].numOfHintedWords && this.globals.isPlayersTurn && !this.globals.isGameOver){
          this.clickWord(wordsToBeGuessed[i] - this.globals.game.Board[0].id);
          i++;
        }
        else{
          clearInterval(this.GuessClueinterval);
          this.globals.isAITurn = false;
          this.globals.isPlayersTurn = false;
          this.globals.isVasikiaActive = false;
          this.checkAITurn(); 
        }
      }, 3000); 

    },
    error => {
      this.openDialog(" Error while getting data from the server while guessing words", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  giveClueToSlowVasikia(){
    this.globals.isAITurn = true;
    this.globals.isPlayersTurn = true;
    this.globals.clueList[this.globals.clueIndex].teamTurn = this.globals.teamsTurn[0]
    this.http.post(this.globals.APIurl+"playerSlowVasikiaGiveClue",  this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe(data => {

      this.globals.clueList[this.globals.clueIndex].clueID = data["clueID"];
      var wordsToBeGuessed = data["wordsToBeGuessed"];

      var i=0;

      this.GuessClueinterval = setInterval(()=>{          
        if(i <= this.globals.clueList[this.globals.clueIndex].numOfHintedWords && this.globals.isPlayersTurn && !this.globals.isGameOver){
          this.clickWord(wordsToBeGuessed[i] - this.globals.game.Board[0].id);
          i++;
        }
        else{
          clearInterval(this.GuessClueinterval);
          this.globals.isAITurn = false;
          this.globals.isPlayersTurn = false;
          this.globals.isVasikiaActive = false;
          this.checkAITurn(); 
        }
      }, 3000); 

    },
    error => {
      this.openDialog(" Error while getting data from the server while guessing words", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  giveClueToErmis(){
    this.globals.isAITurn = true;
    this.globals.isPlayersTurn = true;
    this.globals.clueList[this.globals.clueIndex].teamTurn = this.globals.teamsTurn[0]
    this.http.post(this.globals.APIurl+"playerErmisGiveClue",  this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe(data => {

      this.globals.clueList[this.globals.clueIndex].clueID = data["clueID"];
      var wordsToBeGuessed = data["wordsToBeGuessed"];

      var i=0;

      this.GuessClueinterval = setInterval(()=>{          
        if(i <= this.globals.clueList[this.globals.clueIndex].numOfHintedWords && this.globals.isPlayersTurn && !this.globals.isGameOver){
          this.clickWord(wordsToBeGuessed[i] - this.globals.game.Board[0].id);
          i++;
        }
        else{
          clearInterval(this.GuessClueinterval);
          this.globals.isAITurn = false;
          this.globals.isPlayersTurn = false;
          this.globals.isErmisActive = false;
          this.checkAITurn(); 
        }
      }, 3000); 

    },
    error => {
      this.openDialog(" Error while getting data from the server while guessing words", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  giveClueToTantalus(){
    this.globals.isAITurn = true;
    this.globals.isPlayersTurn = true;
    this.globals.clueList[this.globals.clueIndex].teamTurn = this.globals.teamsTurn[0]
    this.http.post(this.globals.APIurl+"playerTantalusGiveClue",  this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe(data => {

      this.globals.clueList[this.globals.clueIndex].clueID = data["clueID"];
      var wordsToBeGuessed = data["wordsToBeGuessed"];

      var i=0;

      this.GuessClueinterval = setInterval(()=>{          
        if(i <= this.globals.clueList[this.globals.clueIndex].numOfHintedWords && this.globals.isPlayersTurn && !this.globals.isGameOver){
          this.AIPlayermsg = this.AIPlayermsg + " "
          this.clickWord(wordsToBeGuessed[i] - this.globals.game.Board[0].id);
          i++;
        }
        else{
          clearInterval(this.GuessClueinterval);
          this.globals.isAITurn = false;
          this.globals.isPlayersTurn = false;
          this.globals.isTantalusActive = false;
          this.checkAITurn(); 
        }
      }, 3000); 

    },
    error => {
      this.openDialog(" Error while getting data from the server while guessing words", "Wait for a few minutes and then try to go back to the menu and start a new game");
    } );
  }

  checkAITurn(){
    if (!this.globals.isGameOver){
      this.AIPlayermsg = "";
      if(this.globals.isBluesTurn){
        if(!this.globals.isPlayersTurn && this.globals.gameSettings.blueGuide != "HumanG" && !this.globals.isAITurn){
          if (this.globals.gameSettings.blueGuide == "VasikiaG"){
            this.globals.isVasikiaActive = true;
            this.getVasikiaClue();
          }
          else if (this.globals.gameSettings.blueGuide == "ErmisG"){
            this.globals.isErmisActive = true;
            this.getErmisClue();
          }
          else if (this.globals.gameSettings.blueGuide == "TantalusG"){
            this.globals.isTantalusActive = true;
            this.getTantalusClue();
          }
          else if (this.globals.gameSettings.blueGuide == "SlowVasikiaG"){
            this.globals.isVasikiaActive = true;
            this.getSlowVasikiaClue();
          }
        }
        else if(this.globals.isPlayersTurn && this.globals.gameSettings.bluePlayer != "HumanP" && !this.globals.isAITurn){  
          this.AIPlayermsg = " Words Guessed by AI: "; 
          if (this.globals.gameSettings.bluePlayer == "VasikiaP"){
            this.globals.isVasikiaActive = true;
            this.giveClueToVasikia();
          }
          else if (this.globals.gameSettings.bluePlayer == "ErmisP"){
            this.globals.isErmisActive = true;
            this.giveClueToErmis();
          }
          else if (this.globals.gameSettings.bluePlayer == "TantalusP"){
            this.globals.isTantalusActive = true;
            this.giveClueToTantalus();
          }
          else if (this.globals.gameSettings.bluePlayer == "SlowVasikiaP"){
            this.globals.isVasikiaActive = true;
            this.giveClueToSlowVasikia();
          }
          else{
            this.AIPlayermsg = "";
          }
        }

      }
      else{
        if(!this.globals.isPlayersTurn && this.globals.gameSettings.redGuide != "HumanG"){
          if (this.globals.gameSettings.redGuide == "VasikiaG"){
            this.globals.isVasikiaActive = true;
            this.getVasikiaClue();
          }
          else if (this.globals.gameSettings.redGuide == "ErmisG"){
            this.globals.isErmisActive = true;
            this.getErmisClue();
          }
          else if (this.globals.gameSettings.redGuide == "TantalusG"){
            this.globals.isTantalusActive = true;
            this.getTantalusClue();
          }
          else if (this.globals.gameSettings.redGuide == "SlowVasikiaG"){
            this.globals.isVasikiaActive = true;
            this.getSlowVasikiaClue();
          }
        }
        else if(this.globals.isPlayersTurn && this.globals.gameSettings.redPlayer != "HumanP"){
          this.AIPlayermsg = " Words Guessed by AI: ";
          if (this.globals.gameSettings.redPlayer == "VasikiaP"){
            this.globals.isVasikiaActive = true;
            this.giveClueToVasikia();
          }
          else if (this.globals.gameSettings.redPlayer == "ErmisP"){
            this.globals.isErmisActive = true;
            this.giveClueToErmis();
          }
          else if (this.globals.gameSettings.redPlayer == "TantalusP"){
            this.globals.isTantalusActive = true;
            this.giveClueToTantalus();
          }
          else if (this.globals.gameSettings.redPlayer == "SlowVasikiaP"){
            this.globals.isVasikiaActive = true;
            this.giveClueToSlowVasikia();
          }
          else{
            this.AIPlayermsg = "";
          }
        }
      }
    }
  }

  getWords(): void {
    if(this.globals.game){
      this.wordlist = this.globals.game.Board;
    }
    else {
      this.wordService.getWordList().subscribe( wordlist => this.wordlist = wordlist );
    }
  }

  toGuidesTurn(evt): void {

    if (evt === "pass"){
      this.checkAITurn();
      this.isWordboardVisible=false;
      if (this.globals.singleMode){
        this.revealRandomRedWord();
      }
      
    }
    else if(!this.globals.isPlayersTurn){
      if(this.isWordboardVisible){
        this.isWordboardVisible=false;
      }
      else{
        this.isWordboardVisible=true;
      }
    }
    else{
      this.isWordboardVisible=false;
      this.checkAITurn();
    }
    
  }

  openDialog(title: string, message: string) {
    const dialogConfig = new MatDialogConfig();

    dialogConfig.disableClose = false;
    dialogConfig.autoFocus = true;

    if (this.globals.isAITurn) {
      message = message;
    }

    dialogConfig.data = {
      title: title,
      description: message,
      AImsg: this.AIPlayermsg
    };
    
    this.AIPlayermsg = "";
    this.updateCurrentClue();
    this.dialog.open(GameDialogComponent, dialogConfig);
  }

  clickWord( wordClicked : number){
    if(this.globals.isPlayersTurn){
      if(this.globals.activeWords[wordClicked]){

        if (this.globals.isAITurn){
          this.AIPlayermsg = this.AIPlayermsg + " | " + this.wordlist[wordClicked].value + " ( colour: " + this.wordlist[wordClicked].colour + " )";
        }

        this.globals.activeWords[wordClicked] = false;
        this.globals.canNotPass = false;

        this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed++;
        this.globals.clueList[this.globals.clueIndex].wordsGuessed.push(this.wordlist[wordClicked]);
        
        if(this.wordlist[wordClicked].colour=="B"){
          this.globals.blueWordsCount--;
          if(this.globals.isBluesTurn){
            this.globals.game.blueCorrectGuesses++;
          }
          else{
            this.globals.game.redWrongGuesses++;
            this.globals.clueList[this.globals.clueIndex].badness = 3;
          }
        }
        else if(this.wordlist[wordClicked].colour=="R"){
          this.globals.redWordsCount--;
          if(this.globals.isBluesTurn){
            this.globals.clueList[this.globals.clueIndex].badness = 3;
            this.globals.game.blueWrongGuesses++;
          }
          else{
            this.globals.game.redCorrectGuesses++;
          }
        }
        else{
          if(this.globals.isBluesTurn){
            this.globals.game.blueWrongGuesses++;
          }
          else{
            this.globals.game.redWrongGuesses++;
          }
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
        if(this.wordlist[wordClicked].colour=="G"){
          this.globals.clueList[this.globals.clueIndex].badness = 1;
        }
        else{
          this.globals.clueList[this.globals.clueIndex].badness = 3;
        }

        this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed--;
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

          this.globals.clueList[this.globals.clueIndex].badness = 0;
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
        
        this.globals.clueList[this.globals.clueIndex].numOfCorrectlyGuessed--;

        if(this.wordlist[wordClicked].colour=="G"){
          this.globals.clueList[this.globals.clueIndex].badness = 1;
        }
        else{
          this.globals.clueList[this.globals.clueIndex].badness = 3;
        }
        this.openDialog(this.gameStateTitle, this.gameStateMessage); 
        this.revealRandomRedWord();
      }
      else if(this.globals.numberOfRelatedWords != 0){
        this.globals.currentGuessesLeft--;       
        if(this.globals.currentGuessesLeft<=0){
          this.globals.isPlayersTurn = false;        
          this.gameStateMessage = "This ends your turn and one Red Word is revealed";  
          this.gameStateTitle = "You are out of guesses!!";

          this.globals.clueList[this.globals.clueIndex].badness = 0;
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
    this.globals.activeWords[this.redWordActiveArray[randomIndex].index] = false;
    this.globals.redWordsCount--;

    this.checkGameEnd(this.redWordActiveArray[randomIndex].index);
        
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
        this.globals.game.winner = "R";
      }
      this.globals.isBluesTurn = false;
      this.updateGameFinished();
      this.openDialog(this.gameStateTitle, this.gameStateMessage); 
    }
    else if(this.globals.blueWordsCount==0){
      if (!this.checkSingleModeGameOver(true)){
        this.gameStateTitle = "Blue Team Won!!";
        this.gameStateMessage = "Congratulations Blue Team!!! ";
        this.globals.teamsTurn = "Blue Team Won!";
        this.globals.game.winner = "B";
      }
      this.globals.isBluesTurn = true;

      this.updateGameFinished();
      this.openDialog(this.gameStateTitle, this.gameStateMessage); 
    }
    else if(this.wordlist[wordClicked].colour=="P"){
      this.gameStateMessage = "You chose the Purple Word!! ";


      if(this.globals.isBluesTurn){
        this.gameStateTitle = "Blue Team Defeat!!";
        this.globals.teamsTurn = "Red Team Won!";
        this.globals.isBluesTurn = false;
        this.globals.game.winner = "R";
      }
      else {
        this.gameStateTitle = "Red Team Defeat!!";
        this.globals.teamsTurn = "Blue Team Won!";
        this.globals.isBluesTurn = true;
        this.globals.game.winner = "B";
      }

      this.globals.clueList[this.globals.clueIndex].badness = 4;
      this.checkSingleModeGameOver(false);
      this.updateGameFinished();
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
        this.globals.game.winner = "B";
      }
      else{
        this.gameStateTitle = "You lost!!"
        this.gameStateMessage = " Better luck next time!"
        this.globals.game.winner = "R";
      }
      return true;
    }
    return false;
  }

  updateCurrentClue(){
    return this.http.post<number>(this.globals.APIurl+"updateClue", this.globals.clueList[this.globals.clueIndex] , this.globals.httpOptions).subscribe( data => { 
      if (!this.globals.isGameOver){
        if (this.globals.isAITurn){
          clearInterval(this.GuessClueinterval);
          this.globals.isAITurn = false;
          this.globals.isPlayersTurn = false;
          this.globals.isVasikiaActive = false;
          this.globals.isErmisActive = false;
          this.globals.isTantalusActive = false;
        }
        this.checkAITurn();
      }}
    );
  }

  updateGameFinished(){
    return this.http.post(this.globals.APIurl+"updateGame", this.globals.game , this.globals.httpOptions).subscribe();
  }

}


