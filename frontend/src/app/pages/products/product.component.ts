import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../core/services/api.service'; 
import { Router, RouterLink } from '@angular/router';
import { Product } from '../../core/models/product.model'; 

@Component({
  selector: 'products-list',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './product.html',
  styleUrls: ["./products.styles.css"]
})

export class ProductsListComponent implements OnInit {
  products: Product[] = [];
  loading = false;

  constructor(private api: ApiService, private router: Router) {}

  ngOnInit() {
    this.load();
  }

  load() {
    this.loading = true;
    this.api.listProducts().subscribe({
      next: (res: any) => { this.products = res; this.loading = false; },
      error: () => { this.loading = false; alert('Error cargando productos'); }
    });
  }

  edit(id?: number) {
    this.router.navigate(['/products/edit', id]);
  }

  remove(id?: number) {
    if (!id) return;
    if (!confirm('Delete product?')) return;
    this.api.deleteProduct(id).subscribe({
      next: () => this.load(),
      error: () => alert('Error deleting!')
    });
  }

}
