#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  console.log('code:', response.statusCode);
});
