#!/usr/bin/node

// importng the module
const request = require('request');

// the URL to request (GET)
const url = process.argv[2];

// Making an HTTP GET request to the specified URL
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    // If there are no errors, print the HTTP status code
    console.log('code:', response.statusCode);
  }
});
