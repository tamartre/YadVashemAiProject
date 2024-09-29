import '@angular/localize/init';

import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { provideAnimations } from '@angular/platform-browser/animations';
import { VERSION as CDK_VERSION } from '@angular/cdk';
import { VERSION as MAT_VERSION, MatNativeDateModule } from '@angular/material/core';
import { ToolbarOverviewExample } from './toolbar/toolbar-overview';
import { AppComponent } from './app/app.component';
import { TreeFolderComponent } from './tree-folder/tree-folder.component';
import { GridListOverviewExampleComponent } from './grid-list-overview-example/grid-list-overview-example.component';
import { MyTestComponent } from './my-test/my-test.component';

console.info('Angular CDK version', CDK_VERSION.full);
console.info('Angular Material version', MAT_VERSION.full);


bootstrapApplication(ToolbarOverviewExample, {
  providers: [
    provideAnimations(),
    provideHttpClient()
  ]
}).catch(err => console.error(err));

bootstrapApplication(AppComponent, {
  providers: [
    provideAnimations(),
    provideHttpClient(),
    MatNativeDateModule
  ]
}).catch(err => console.error(err));

bootstrapApplication(MyTestComponent, {
  providers: [
    provideAnimations(),
  ]
}).catch(err => console.error(err));

