import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../../core/services/api.service';
import { Router, ActivatedRoute, RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { Product } from '../../../core/models/product.model';

@Component({
  selector: 'app-producto-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterLink, RouterLinkActive ],
  templateUrl: './product.form.html',
  styleUrls: ['./product.form.css']
})

export class ProductFormComponent implements OnInit {
  form = new FormGroup({
    name: new FormControl('', { nonNullable: true }),
    description: new FormControl('', { nonNullable: true }),
    stock: new FormControl(0),
    price: new FormControl(0)
  });

  id?: number;
  loading = false;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute) {}

  ngOnInit() {
    const idParam = this.route.snapshot.paramMap.get('id');
    if (idParam) {
      this.id = Number(idParam);
      this.load();
    }
  }

  load() {
    if (!this.id) return;
    this.api.getProduct(this.id).subscribe({
      next: (p: any) => this.form.patchValue(p),
      error: () => {
        this.router.navigate(['/products'])
        alert('Error cargando producto')
      }
    });
  }

  save() {
    if (!this.form.valid) return;
    
    let price = Number(this.form.value.price);
    let stock = Number(this.form.value.stock); 

    if(price < 0 || stock < 0) { 
      return alert('Valores negativos!')
    }

    const payload:Product = { ...this.form.value };
    this.loading = true;
   
    if (this.id) {
      this.api.updateProduct(this.id, payload).subscribe({
        next: () => { this.loading = false; this.router.navigate(['/products']); },
        error: () => { this.loading = false; alert('Error actualizando'); }
      });

    } else {
      this.api.createProduct(payload).subscribe({
        next: () => { this.loading = false; this.router.navigate(['/products']); },
        error: () => { this.loading = false; alert('Error creando'); }
      });
    }
  }
}
