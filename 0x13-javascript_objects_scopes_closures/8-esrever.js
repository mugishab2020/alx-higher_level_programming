#!/usr/bin/node
let newlist = '';
exports.esrever = function (list) {
  for (let a = 0; a < list.length / 2; a++) {
    newlist = list[a];
    list[a] = list[list.length - a - 1];
    list[list.length - a - 1] = newlist;
  }
  return list;
};
