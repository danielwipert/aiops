#!/usr/bin/env node
/*
 * Print an HTML file to PDF with a real per-page footer, using the locally
 * installed Chrome via puppeteer-core (no Chromium download).
 *
 *   node html_to_pdf.js <input.html> <output.pdf> "<footer text>"
 *
 * The footer text renders centered on every page. Page margins are owned here
 * (the HTML should use @page{margin:0}); background colors print full-bleed.
 */
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const [, , inHtml, outPdf, footerText = ''] = process.argv;
if (!inHtml || !outPdf) {
  console.error('usage: node html_to_pdf.js <input.html> <output.pdf> "<footer>"');
  process.exit(2);
}
const CHROME = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
].find((p) => fs.existsSync(p));
if (!CHROME) {
  console.error('Chrome/Edge not found.');
  process.exit(1);
}

const footer = `<div style="width:100%;font-family:'Archivo','Segoe UI',sans-serif;font-size:7.6px;`
  + `letter-spacing:.04em;color:#6B6152;text-align:center;padding:0 1.1in;">${footerText}</div>`;

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  const url = 'file:///' + path.resolve(inHtml).replace(/\\/g, '/');
  await page.goto(url, { waitUntil: 'networkidle0', timeout: 60000 });
  await page.pdf({
    path: outPdf,
    format: 'Letter',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: footer,
    margin: { top: '0.9in', bottom: '0.72in', left: '1.1in', right: '1.1in' },
  });
  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
