#!/usr/bin/node
const str = process.argv[2];
if (parseInt(str)) {
  console.log('My number: ' + parseInt(str));
} else {
  console.log('Not a number');
}
