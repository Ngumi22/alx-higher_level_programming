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

    // Function to fetch and print each character's name
    const fetchCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            console.log(`Failed. Status code: ${response.statusCode}`);
          }
        });
      });
    };

    // Fetch all character names in the correct order
    const fetchAllCharacters = async () => {
      for (const characterUrl of characters) {
        try {
          const name = await fetchCharacterName(characterUrl);
          console.log(name);
        } catch (error) {
          console.error('Error:', error);
        }
      }
    };

    // Call the function to fetch and print all character names
    fetchAllCharacters();
  } else {
    console.log(`Failed. Status code: ${response.statusCode}`);
  }
});
