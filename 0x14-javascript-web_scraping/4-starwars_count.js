#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
const characterId = 18;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    const theMovies = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    const numberOfMovies = theMovies.length;
    console.log(numberOfMovies);
  }
});
