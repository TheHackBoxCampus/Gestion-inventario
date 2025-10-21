import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive, CommonModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})

export class AppComponent {
  title = 'Inventory';
  get isLogged() {
    return !!localStorage.getItem('access_token');
  }
  
  logout() {
    localStorage.removeItem('access_token');
    location.href = '/auth/login';
  }
}
