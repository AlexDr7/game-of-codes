import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from "@angular/material";

import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { WordboardComponent } from './wordboard/wordboard.component';
import { WordboardDetailsComponent } from './wordboard-details/wordboard-details.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './/app-routing.module';
import { MenuComponent } from './menu/menu.component';
import { NavComponent } from './nav/nav.component';
import { NavWordboardComponent } from './nav-wordboard/nav-wordboard.component';
import { Globals } from './globals';
import { GameDialogComponent } from './game-dialog/game-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    WordboardComponent,
    WordboardDetailsComponent,
    MessagesComponent,
    MenuComponent,
    NavComponent,
    NavWordboardComponent,
    GameDialogComponent
  ],
  entryComponents: [
    GameDialogComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    MatDialogModule,
    BrowserAnimationsModule
  ],
  providers: [Globals],
  bootstrap: [AppComponent]
})
export class AppModule { }
