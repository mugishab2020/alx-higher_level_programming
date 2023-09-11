#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < size; a++) {
    let x = '';
    for (let b = 0; b < size; b++) {
      x += 'X';
    }
    console.log(x);
  }
}
