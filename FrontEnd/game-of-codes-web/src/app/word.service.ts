import { Injectable } from '@angular/core';
import { Word } from  './word';
import { Board } from './board';

import { WORDSLIST } from './WordsList';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
}

@Injectable({
  providedIn: 'root'
})
export class WordService {

  constructor(private messageService: MessageService, private http: HttpClient) { }

  boardUrl = "http://127.0.0.1:8000/wordService"

  getWordList(): Observable<Word[]>{
    this.messageService.add('WordService: fetched words');
    return of (WORDSLIST);
  }

  getBoard(game) {
    return this.http.post<Board>(this.boardUrl, game , httpOptions);
  }
}
