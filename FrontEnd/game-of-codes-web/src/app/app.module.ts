import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { WordboardComponent } from './wordboard/wordboard.component';
import { WordboardDetailsComponent } from './wordboard-details/wordboard-details.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './/app-routing.module';
import { MenuComponent } from './menu/menu.component';
import { NavComponent } from './nav/nav.component';
import { NavWordboardComponent } from './nav-wordboard/nav-wordboard.component';

@NgModule({
  declarations: [
    AppComponent,
    WordboardComponent,
    WordboardDetailsComponent,
    MessagesComponent,
    MenuComponent,
    NavComponent,
    NavWordboardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
