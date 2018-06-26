import { Component, OnInit } from '@angular/core';

import { Globals } from '../globals'

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit {

  constructor(private globals: Globals) { }

  ngOnInit() {
  }

}
