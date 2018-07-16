import { Injectable } from '@angular/core';
import { Word } from  './word';
import { Game } from './game';
import { Globals } from './globals'

import { WORDSLIST } from './WordsList';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';


import { Observable, of } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class WordService {

  boardUrl :string;

  constructor(private messageService: MessageService,  private globals: Globals, private http: HttpClient) { 
    this.boardUrl = this.globals.APIurl +"wordService";
  }

  

  getWordList(): Observable<Word[]>{
    this.messageService.add('WordService: fetched words');
    return of (WORDSLIST);
  }

  getBoard(game): Observable<Game> {
    return this.http.post<Game>(this.boardUrl, game , this.globals.httpOptions);
  }
}
