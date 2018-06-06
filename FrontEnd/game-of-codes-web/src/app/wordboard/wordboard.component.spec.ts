import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WordboardComponent } from './wordboard.component';

describe('WordboardComponent', () => {
  let component: WordboardComponent;
  let fixture: ComponentFixture<WordboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WordboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WordboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
