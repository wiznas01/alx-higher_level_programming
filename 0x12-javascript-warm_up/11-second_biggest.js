#!/usr/bin/node
function findSecondBiggest (numbers) {
  if (numbers.length < 2) {
    return 0;
  }
  let first = -Infinity;
  let second = -Infinity;
  for (const number of numbers) {
    if (number > first) {
      second = first;
      first = number;
    } else if (number > second && number !== first) {
      second = number;
    }
  }
  return second;
}

const args = process.argv.slice(2).map(Number);

const secondBiggest = findSecondBiggest(args);

console.log(secondBiggest);
