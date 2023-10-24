#!/usr/bin/node

// importing the mode
const fs = require('fs');

// this is the file path
const file = process.argv[2];

// The second argument is the string to write
const content = process.argv[3];

// writing to file
fs.writeFile(file, content, 'utf-8', error => {
  if (error) {
    console.log(error);
  }
});
