#!/usr/bin/node

const arg = process.argv.slice(2);
const num = parseInt(arg[0]);

if (!isNaN(num)) {
  let nm = num;
  while (nm > 0) {
    nm--;
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
