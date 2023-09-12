#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let row = '';
      for (let b = 0; b < this.width; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
