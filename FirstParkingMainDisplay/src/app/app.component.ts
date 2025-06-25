import { Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule, isPlatformBrowser } from '@angular/common';

interface ParkingSpot {
  parkingSpotId: number;
  parkingSpotName: string;
  isReserved: boolean;
  label?: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  availableCount: number = 0;

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {}

  ngOnInit() {
    this.getAvailableCount();

    if (isPlatformBrowser(this.platformId)) {
      setInterval(() => this.getAvailableCount(), 5000);
    }
  }

  getAvailableCount() {
    this.http.get<ParkingSpot[]>('/api/parkingSpot').subscribe({
      next: (spots) => {
        this.availableCount = spots.filter(spot => !spot.isReserved).length;
      },
      error: (err) => {
        console.error('Error fetching available count:', err);
      }
    });
  }
}
