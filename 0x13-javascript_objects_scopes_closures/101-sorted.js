#!/usr/bin/node
const dict = require('./101-data.js').dict;

const newDict = {};
for (const id in dict) {
  const occurrence = dict[id];
  if (!Array.isArray(newDict[occurrence])) {
    newDict[occurrence] = [];
  }
  newDict[occurrence].push(id);
}

console.log(newDict);
