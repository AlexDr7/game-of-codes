import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appBoardViewChange]'
})
export class BoardViewChangeDirective {

  @Input('appBoardViewChange') wordColour: string;

  constructor(private el : ElementRef) {   }

  @HostListener('mouseenter') onMouseEnter() {
    this.highlight(this.wordColour || 'red');
  }
 
  @HostListener('mouseleave') onMouseLeave() {
    this.highlight(null);
  }
 
  private highlight(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }

}
