#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (n) {
  if (Number.isNaN(n) || n <= 1) {
    return (1);
  }
  const result = n * factorial(n - 1);
  return (result);
}

console.log(factorial(num));
