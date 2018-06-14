import { Component, OnInit , EventEmitter , Output} from '@angular/core';

@Component({
  selector: 'app-nav-wordboard',
  templateUrl: './nav-wordboard.component.html',
  styleUrls: ['./nav-wordboard.component.css']
})
export class NavWordboardComponent implements OnInit {

  @Output() guidesTurn = new EventEmitter<boolean>();

  constructor() { }

  ngOnInit() {
  }

  toGuidesTurn(){
    this.guidesTurn.emit();
  }

}
