import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WordboardDetailsComponent } from './wordboard-details.component';

describe('WordboardDetailsComponent', () => {
  let component: WordboardDetailsComponent;
  let fixture: ComponentFixture<WordboardDetailsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WordboardDetailsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WordboardDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
