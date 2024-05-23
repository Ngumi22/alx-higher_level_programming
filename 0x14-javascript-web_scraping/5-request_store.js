#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Write the response body to the file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  } else {
    console.log(`Failed to retrieve data. Status code: ${response.statusCode}`);
  }
});
