import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { ConsoleLogger } from '@angular/compiler-cli/private/localize';
@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  constructor(private _http: HttpClient) { }
  get_data() {
    console.log("start2");
    
    return this._http.get('http://127.0.0.1:5000/api/data');
  }

  get_tree() {
    console.log("start2");
    
    return this._http.get('http://127.0.0.1:5000/api/tree');
  }
}
