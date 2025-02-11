#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const characters = body.characters;

  function getCharacterName (index) {
    if (index >= characters.length) {
      return;
    }
    request(characters[index], { json: true }, (err, res, characterBody) => {
      if (err) {
        console.error(err);
      }
      console.log(characterBody.name);
      getCharacterName(index + 1);
    });
  }
  getCharacterName(0);
});
