import { NgModule, Type } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
// import { TreeComponent } from '../tree/tree';
import { MatTreeModule } from '@angular/material/tree';
import { ngExpressEngine } from '@nguniversal/express-engine';
import { ApplicationRef } from '@angular/core';
import { mergeApplicationConfig, ApplicationConfig } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app.config';
import { MyTestComponent } from '../my-test/my-test.component';

 @NgModule({
 declarations: [
  
  
//AppComponent,
//TreeComponent
   ],
  imports: [
    BrowserModule,
    MatTreeModule,
    
  ],
  //bootstrap: [AppComponent]
})
export class AppModule { }

const bootstrap = (rootComponent: Type<unknown>) => bootstrapApplication(rootComponent);

const serverConfig: ApplicationConfig = {

providers: [
    { provide: ngExpressEngine, useFactory: bootstrap }
  ]
};
export const config = mergeApplicationConfig(appConfig, serverConfig);