import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { WordboardComponent } from './wordboard/wordboard.component';
import { MenuComponent } from './menu/menu.component';


const routes: Routes = [
  { path: 'wordboard', component: WordboardComponent },
  { path: 'menu' , component: MenuComponent},
  { path: '', redirectTo: '/menu', pathMatch: 'full' },
  { path: 'detail/:id', component: WordboardComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {}