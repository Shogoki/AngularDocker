import { Component } from '@angular/core';
import { ServerService } from "./services/server.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  servers;
 
   constructor(private serverService: ServerService) {
      this.servers = serverService.getServers();
   }
}
