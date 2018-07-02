import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs';
import { User } from "../models/user";
import { map } from "rxjs/operators";
import { catchError } from "rxjs/operators";



@Injectable()
export class UserService {
   constructor(private http: Http) {
   }
 
   getUsers(): Observable<User[]> {
      return this.http.get("https://jsonplaceholder.typicode.com/users")
        .pipe(map((res: Response) => res.json()),
         catchError((error: any) => Observable.throw(error.json().error || 'Server error')));
   }
}