#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let a = 0; a < this.width; a++) {
      let prt = '';
      for (let b = 0; b < this.height; b++) {
        prt += c;
      }
      console.log(prt);
    }
  }
};
