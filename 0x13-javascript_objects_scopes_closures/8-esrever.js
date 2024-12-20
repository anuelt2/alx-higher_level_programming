#!/usr/bin/node
exports.esrever = function (list) {
  const newEsrever = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newEsrever.push(list[i]);
  }
  return newEsrever;
};
