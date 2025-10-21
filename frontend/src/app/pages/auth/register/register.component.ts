import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../../core/services/api.service'; 
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: "./register.html",
  styleUrls: ['./register.css']
})

export class RegisterComponent {
  form = new FormGroup({
    username: new FormControl('', { nonNullable: true }),
    email: new FormControl('', { nonNullable: true }),
    password: new FormControl('', { nonNullable: true })
  });

  constructor(private api: ApiService, private router: Router) {}

  onSubmit() {
    if (!this.form.valid) return alert('Invalid values!');
    this.api.register( {...this.form.value} ).subscribe({
      next: () => {
        alert('registration successful!')
        this.router.navigate(['/auth/login'])
      }, 
      error: (err) => {
        if(err.error?.detail) { 
          console.log("Campos invalidos!")
        }else { 
          console.log(err.error || err.message)
        }
      }
    });
  }
}
