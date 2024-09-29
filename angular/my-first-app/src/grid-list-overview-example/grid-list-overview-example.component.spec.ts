import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GridListOverviewExampleComponent } from './grid-list-overview-example.component';

describe('GridListOverviewExampleComponent', () => {
  let component: GridListOverviewExampleComponent;
  let fixture: ComponentFixture<GridListOverviewExampleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GridListOverviewExampleComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GridListOverviewExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
