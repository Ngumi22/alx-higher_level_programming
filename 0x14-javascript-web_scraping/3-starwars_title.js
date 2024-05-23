#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number
// matches a given integer
//
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
