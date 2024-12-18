#!/usr/bin/node
const str = 'C is fun';
const arg2 = process.argv[2];
if (parseInt(arg2)) {
  for (let i = 0; i < arg2; i++) {
    console.log(str);
  }
} else {
  console.log('Missing number of occurrences');
}
