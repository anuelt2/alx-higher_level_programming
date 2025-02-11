#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const antillesId = 18;
const antillesURL = `https://swapi-api.alx-tools.com/api/people/${antillesId}/`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  let antillesMovieCount = 0;

  body.results.forEach(movie => {
    if (movie.characters.includes(antillesURL)) {
      antillesMovieCount++;
    }
  });
  console.log(antillesMovieCount);
});
