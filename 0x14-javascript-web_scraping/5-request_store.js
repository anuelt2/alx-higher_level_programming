#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.errror(error);
  }

  fs.writeFile(filePath, body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
