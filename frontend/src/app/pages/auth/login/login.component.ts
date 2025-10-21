import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../../core/services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})

export class LoginComponent {
  formLogin = new FormGroup({
    email: new FormControl('', { nonNullable: true }),
    password: new FormControl('', { nonNullable: true })
  });

  constructor(private api: ApiService, private router: Router) {}

  onSubmit() {
    if (!this.formLogin.valid) return alert("Campos invalidos!");
    this.api.login({...this.formLogin.value}).subscribe({
      next: (res: any) => {
        alert("Log-in succesfull!")
        localStorage.setItem('access_token', res.access_token);
        this.router.navigate(['/products']);
      },
      error: (err:any) => {
        if(err.error?.detail) { 
          alert("Credenciales incorrectos!")
        }else { 
          console.log(err.error || err.message)
        }
      }
    });
  }
}
