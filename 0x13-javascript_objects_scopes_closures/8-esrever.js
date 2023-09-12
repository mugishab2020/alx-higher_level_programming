#!/usr/bin/node
exports.esrever = function (list) {
  for (let a = 0; a < list.length; a++) {
    list[a] = list[list.length - a - 1];
  }
  return list;
};
