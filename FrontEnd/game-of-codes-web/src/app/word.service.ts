import { Injectable } from '@angular/core';
import { Word } from  './word';
import { WORDSLIST } from './WordsList';
import { MessageService } from './message.service';

import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class WordService {

  constructor(private messageService: MessageService) { }

  getWordList(): Observable<Word[]>{
    this.messageService.add('WordService: fetched words');
    return of (WORDSLIST);
  }
}
