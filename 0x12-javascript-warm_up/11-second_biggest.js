#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
  process.exit();
}

const array = process.argv.slice(2).map(element => parseInt(element));

function secondBiggestInt (array) {
  let biggest = -Infinity;
  let secondBiggest = -Infinity;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > biggest) {
      secondBiggest = biggest;
      biggest = array[i];
    } else if (array[i] > secondBiggest && array[i] < biggest) {
      secondBiggest = array[i];
    }
  }
  return (secondBiggest);
}

console.log(secondBiggestInt(array));
