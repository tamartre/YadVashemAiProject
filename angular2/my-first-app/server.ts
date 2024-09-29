import { APP_BASE_HREF } from '@angular/common';
import { ngExpressEngine } from '@nguniversal/express-engine';
import express from 'express';
import { join } from 'path';
import { readFileSync } from 'fs';
import { enableProdMode } from '@angular/core';
import  bootstrap  from './src/app/main.server';
const cors = require('cors');

enableProdMode();

const app = express();

app.use(cors());


// app.engine('html', ngExpressEngine({
//   bootstrap: bootstrap,
// }));

app.set('view engine', 'html');
app.set('views', join(process.cwd(), 'dist/browser'));

app.get('*.*', express.static(join(process.cwd(), 'dist/browser')));
app.get('*', (req, res) => {
  res.render('index', { req, providers: [{ provide: APP_BASE_HREF, useValue: req.baseUrl }] });
});

const port = process.env['PORT'] || '4000';
app.listen(port, () => {
  console.log(`Node Express server listening on http://localhost:${port}`);
});