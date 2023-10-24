#!/usr/bin/node

// importing request module
const request = require('request');
const fs = require('fs');

// The URL to request
const apiUrl = process.argv[2];

// The file path to store the body response
const file = process.argv[3];

// Making HTTP GET request to the specified URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // write response to file
    fs.writeFile(file, body, 'utf-8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
