#!/usr/bin/node
const reverselist = [];
exports.esrever = function (list) {
  for (let a = list.length; a > 0; a++) {
    let b = 0;
    while(b < list.length) {
        reverselist[b] = list[a];
        b++;
    }
  }
  return reverselist;
};
