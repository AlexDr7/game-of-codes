import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { WordboardComponent } from './wordboard/wordboard.component';
import { MenuComponent } from './menu/menu.component';
import { RulesComponent } from './rules/rules.component';

const routes: Routes = [
  { path: 'wordboard', component: WordboardComponent },
  { path: 'menu' , component: MenuComponent},
  { path: '', redirectTo: '/menu', pathMatch: 'full' },
  { path: 'rules', component: RulesComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class AppRoutingModule {}