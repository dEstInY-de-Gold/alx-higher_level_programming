#!/usr/bin/node

const arg = process.argv.slice(2);
const numb = parseInt(arg[0]);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(numb));
