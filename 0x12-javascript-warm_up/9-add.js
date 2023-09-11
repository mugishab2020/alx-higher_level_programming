#!/usr/bin/node
const a1 = parseInt(process.argv[2]);
const a2 = parseInt(process.argv[3]);
function add (a, b) {
  const results = a + b;
  return results;
}

console.log(add(a1, a2));
