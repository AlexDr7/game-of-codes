import { Component, OnInit } from '@angular/core';
import { Word } from '../word';
import { WordService } from '../word.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {

  wordlist: Word[] = [];

  constructor(private wordService: WordService) { }

  ngOnInit() {
    this.getWordList();
  }

  getWordList(): void{
    this.wordService.getWordList().subscribe(wordlist => this.wordlist = wordlist)
  }

}