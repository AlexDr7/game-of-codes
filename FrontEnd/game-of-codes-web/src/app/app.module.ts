import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from "@angular/material";


import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { WordboardComponent } from './wordboard/wordboard.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './/app-routing.module';
import { MenuComponent } from './menu/menu.component';
import { NavComponent } from './nav/nav.component';
import { NavWordboardComponent } from './nav-wordboard/nav-wordboard.component';
import { Globals } from './globals';
import { GameDialogComponent } from './game-dialog/game-dialog.component';
import { RulesComponent } from './rules/rules.component';
import { AboutComponent } from './about/about.component';

@NgModule({
  declarations: [
    AppComponent,
    WordboardComponent,
    MessagesComponent,
    MenuComponent,
    NavComponent,
    NavWordboardComponent,
    GameDialogComponent,
    RulesComponent,
    AboutComponent
  ],
  entryComponents: [
    GameDialogComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    MatDialogModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [Globals],
  bootstrap: [AppComponent]
})
export class AppModule { }
