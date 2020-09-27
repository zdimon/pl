import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-user-panel',
  templateUrl: './user-panel.component.html',
  styleUrls: ['./user-panel.component.scss']
})
export class UserPanelComponent implements OnInit {

  @Input() user: any;
  constructor() { }

  ngOnInit() {
  }

}
