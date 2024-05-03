#!/usr/bin/node
const arg = process.argv[2];
const intArg = parseInt(arg);

if (isNaN(intArg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${intArg}`);
}
