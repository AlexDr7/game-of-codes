import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material';

@Component({
  selector: 'app-game-dialog',
  templateUrl: './game-dialog.component.html',
  styleUrls: ['./game-dialog.component.css']
})
export class GameDialogComponent implements OnInit {

  title: string;
  message :string;

  constructor(private dialogRef: MatDialogRef<GameDialogComponent>,
    @Inject(MAT_DIALOG_DATA) data) {

    this.title = data.title;
    this.message = data.description;
}

  ngOnInit() {
  }

  close() {
    this.dialogRef.close();
}

}
