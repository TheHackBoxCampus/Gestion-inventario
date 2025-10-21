import { Injectable } from '@angular/core';
import { ApiService } from './api.service';
import { tap } from 'rxjs/operators';
import { Router } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private api: ApiService, private router: Router) {}

  login(correo: string, password: string) {
    return this.api.login({ correo, password }).pipe(
      tap((res: any) => {
        if (res?.access_token) {
          localStorage.setItem('access_token', res.access_token);
        }
      })
    );
  }

  register(payload: any) {
    return this.api.register(payload);
  }

  logout() {
    localStorage.removeItem('access_token');
    this.router.navigate(['/auth/login']);
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('access_token');
  }
}
