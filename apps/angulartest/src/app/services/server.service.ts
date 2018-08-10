import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import { Server } from "../models/server";
import { map } from "rxjs/operators";
import { catchError } from "rxjs/operators";



@Injectable()
export class ServerService {
   constructor(private http: Http) {
   }
 
   getServers(): Observable<Server[]> {
      return this.http.get("http://servername-api:8080/rest/servers")
        .pipe(map((res: Response) => res.json()),
         catchError((error: any) => Observable.throw(error.json().error || 'Server error')));
   }
}