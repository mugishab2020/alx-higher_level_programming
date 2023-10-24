#!/usr/bin/node

//modules requesting
const fs = require('fs');

const file = process.argv[2];


fs.readFile(file, 'utf-8', (err, data) => {
	if (err) {
		console.error('Error reading file:', err);
		return;
	} 
	console.log(data);
	});