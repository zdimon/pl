

import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router} from "@angular/router";
import {Observable} from "rxjs";
import { Injectable } from '@angular/core';
import { SessionService } from './../../../../core/src/lib/services/session.service';

@Injectable()
export class AuthGuard implements CanActivate{

    constructor(
      private session: SessionService,
      private router: Router
    ){}
 
    canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) : Observable<boolean> | boolean {
        if (this.session.getIsAuth()) {
          return true;
        } else {
          this.router.navigate(['/tabs/registration']);
        }
         
        
    }
}