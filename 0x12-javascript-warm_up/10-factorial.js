#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (!isNaN(number)) {
  console.log(factorial(number));
} else {
  console.log('1');
}
