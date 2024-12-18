#!/usr/bin/node
const size = process.argv[2];
if (parseInt(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(parseInt(size)));
  }
} else {
  console.log('Missing size');
}
