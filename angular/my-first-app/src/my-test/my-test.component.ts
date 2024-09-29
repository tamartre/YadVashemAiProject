import { Component, EventEmitter, Input ,OnInit,Output} from '@angular/core';
import { AppComponent } from '../app/app.component';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-my-test',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './my-test.component.html',
  styleUrl: './my-test.component.css'
})
export class MyTestComponent {

  @Input() newdata: any;


  ngOnInit(){
      console.log("from test",this.newdata);
  }

  @Output() 
  myEvent = new EventEmitter<string>();

  emitEvent() {
    this.myEvent.emit("Hello World!");
  }

}
