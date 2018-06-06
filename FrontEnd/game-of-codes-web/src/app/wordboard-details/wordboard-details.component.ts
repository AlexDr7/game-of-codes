import { Component, OnInit, Input } from '@angular/core';
import { Word } from '../word';

@Component({
  selector: 'app-wordboard-details',
  templateUrl: './wordboard-details.component.html',
  styleUrls: ['./wordboard-details.component.css']
})
export class WordboardDetailsComponent implements OnInit {

  @Input() word: Word;

  constructor() { }

  ngOnInit() {
  }

}
