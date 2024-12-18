#!/usr/bin/node
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(num1, num2);
