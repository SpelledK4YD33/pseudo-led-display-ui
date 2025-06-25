import { Component, Inject, OnInit, PLATFORM_ID } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule, isPlatformBrowser } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  directions: string[] = ['front', 'right', 'left', 'down'];
  displayNames: Record<string, string> = {
    front: '⬆️',
    right: '➡️',
    left: '⬅️',
    down: 'B2:⬇️',
  };

  counts: Record<string, number> = {
    front: 0,
    right: 0,
    left: 0,
    down: 0,
  };

  zone: string = 'Zone B1';

  constructor(
    private http: HttpClient,
    @Inject(PLATFORM_ID) private platformId: Object
  ) {}

  ngOnInit() {
    this.fetchData();

    // Prevent polling during SSR to avoid NG0205 injector errors
    if (isPlatformBrowser(this.platformId)) {
      setInterval(() => this.fetchData(), 5000); // every 10 seconds
    }
  }

  fetchData(): void {
    const url = `/api/parkingSpot/directional-screen-status?zone=${encodeURIComponent(this.zone)}`;
    this.http.get<any>(url).subscribe({
      next: (data) => {
        this.zone = data.zone;
        for (const dir of this.directions) {
          this.counts[dir] = data[dir] ?? 0;
        }
      },
      error: (err) => console.error(`[${this.zone}] Fetch error:`, err),
    });
  }
}
