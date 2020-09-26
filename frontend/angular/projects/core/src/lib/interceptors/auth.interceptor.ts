import { Injectable } from '@angular/core';
import {
    HttpRequest,
    HttpHandler,
    HttpEvent,
    HttpInterceptor
  } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SessionService } from './../services/session.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    token: string;


    constructor(
        private sessionService: SessionService
    ) {
    }

    intercept(req: HttpRequest<any>,
              next: HttpHandler): Observable<HttpEvent<any>> {

        const idToken = this.sessionService.getToken();
        console.log(idToken);
        if (req.headers.get('Authorization') !== null) {
            
            return next.handle(req.clone());
            
        }

        if (idToken) {

            const cloned = req.clone({
                headers: req.headers.set('Authorization',
                    'Token ' + idToken)
            });
            console.log('cxcxcxcxcx');
            return next.handle(cloned);
        }

        return next.handle(req.clone());
    }
}