#!/usr/bin/node

const args = process.argv.slice(2);
const numb = parseInt(args[0]);

if (!isNaN(numb)) {
  for (let x = args[0]; x > 0; x--) {
    let rw = '';
    for (let y = args[0]; y > 0; y--) {
      rw += 'X';
    }
    console.log(rw);
  }
} else {
  console.log('Missing size');
}
