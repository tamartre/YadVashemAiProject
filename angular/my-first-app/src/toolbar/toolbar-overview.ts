import {Component} from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';

/**
 * @title Toolbar overview
 */
@Component({
  selector: 'toolbar-overview',
  templateUrl: 'toolbar-overview.html',
  styleUrl: 'toolbar-overview.css',
  standalone: true,
  imports: [MatToolbarModule, MatButtonModule, MatIconModule],
})
export class ToolbarOverviewExample {
    constructor() {}

    showAlert(): void {
      alert("Search button clicked!");
    }

}
