import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NavWordboardComponent } from './nav-wordboard.component';

describe('NavWordboardComponent', () => {
  let component: NavWordboardComponent;
  let fixture: ComponentFixture<NavWordboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavWordboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavWordboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
