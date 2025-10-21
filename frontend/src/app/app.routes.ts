import { Routes } from '@angular/router';

import { LoginComponent } from './pages/auth/login/login.component'; 
import { RegisterComponent } from './pages/auth/register/register.component';
import { ProductsListComponent } from './pages/products/product.component';
import { ProductFormComponent } from './pages/products/form/product.form.component'; 
import { StatsComponent } from './pages/stats/stats.component';
import { AuthGuardClass } from './core/guards/auth.guard'; 
import { NoAuthGuard } from './core/guards/no-auth.guard'; 

export const routes: Routes = [
  { path: 'auth/login', component: LoginComponent, canActivate: [NoAuthGuard] },
  { path: 'auth/register', component: RegisterComponent, canActivate: [NoAuthGuard] },
  { path: 'products', component: ProductsListComponent, canActivate: [AuthGuardClass] },
  { path: 'products/new', component: ProductFormComponent, canActivate: [AuthGuardClass] },
  { path: 'products/edit/:id', component: ProductFormComponent, canActivate: [AuthGuardClass] },
  { path: 'stats/overview', component: StatsComponent, canActivate: [AuthGuardClass]},
  { path: '**', redirectTo: '/products' }
];
