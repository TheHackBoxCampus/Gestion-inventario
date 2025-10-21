// alternative (if you want class-based)
import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthGuardClass implements CanActivate {
  constructor(private router: Router) {}

  canActivate() {
    const token = localStorage.getItem('access_token');
    if (token) return true; 
    this.router.navigate(['/auth/login']);
    return false;
  }
}
