#!/usr/bin/node
// prints the number of movies where the
// character “Wedge Antilles” is present
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Parse the response body as JSON
    const data = JSON.parse(body);
    const films = data.results;
    let wedgeCount = 0;

    // Iterate over the films to count how many include Wedge Antilles (character ID 18)
    films.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        wedgeCount++;
      }
    });

    // Print the count of movies with Wedge Antilles
    console.log(wedgeCount);
  } else {
    console.log(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
