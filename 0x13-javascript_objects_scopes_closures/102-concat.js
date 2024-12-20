#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, contentA) => {
  if (err) {
    console.error(err);
  }
  fs.readFile(fileB, 'utf8', (err, contentB) => {
    if (err) {
      console.error(err);
    }
    const contentC = contentA + contentB;
    fs.writeFile(fileC, contentC, (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});
