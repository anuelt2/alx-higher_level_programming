#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter(listItem => listItem === searchElement).length;
};
