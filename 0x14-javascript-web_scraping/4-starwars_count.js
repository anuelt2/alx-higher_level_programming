#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  let antillesMovieCount = 0;
  let characters = [];

  body.results.forEach(movie => {
    characters = characters.concat(movie.characters);
  });
  antillesMovieCount = characters.filter(characterURL => characterURL.includes('18')).length;
  console.log(antillesMovieCount);
});
