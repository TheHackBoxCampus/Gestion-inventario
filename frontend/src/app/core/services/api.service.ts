import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../enviroments/enviroments';
import { Product } from '../models/product.model';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private API = environment.apiUrl;

  constructor(private http: HttpClient) {}

  // Auth
  register(payload: any) {
    console.log(payload)
    return this.http.post(`${this.API}/users/register`, payload );
  }

  login(payload: any) {
    console.log(payload)
    return this.http.post(
      `${this.API}/users/login`,
      payload
    );
  }

  // Products
  listProducts() {
    return this.http.get<Product[]>(`${this.API}/products`);
  }

  getProduct(id: number) {
    return this.http.get<Product>(`${this.API}/products/${id}`);
  }

  createProduct(payload: Product) {
    return this.http.post<Product>(`${this.API}/products`, payload);
  }

  updateProduct(id: number, payload: Product) {
    return this.http.put<Product>(`${this.API}/products/${id}`, payload);
  }

  deleteProduct(id: number) {
    return this.http.delete(`${this.API}/products/${id}`);
  }

  // stats 
  statsOverview() {
    return this.http.get(`${this.API}/stats/overview`);
  }
}
