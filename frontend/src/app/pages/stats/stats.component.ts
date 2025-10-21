import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../core/services/api.service'; 

@Component({
  selector: 'app-stats',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './stats.html'
})
export class StatsComponent implements OnInit {
  overview: any = null;
  loading = false;

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.load();
  }

  load() {
    this.loading = true;
    this.api.statsOverview().subscribe({
      next: (res) => { 
        console.log(res)
        this.overview = res; 
        this.loading = false; 
      },
      error: () => { alert('Error'); this.loading = false; }
    });
  }
}
