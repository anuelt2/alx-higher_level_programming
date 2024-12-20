#!/usr/bin/node
const list = require('./100-data.js').list;

const indexMultiply = list.map((listItem, index) => listItem * index);
console.log(list);
console.log(indexMultiply);
