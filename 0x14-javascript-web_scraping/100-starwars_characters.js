#!/usr/bin/node
// prints all characters of a Star Wars movie
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the movie URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Parse the response body as JSON
    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode === 200) {
          // Parse the character data and print the name
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.log(`Failed. Status code: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Failed.Status code: ${response.statusCode}`);
  }
});
