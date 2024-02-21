#!/usr/bin/node

const ps = require('fs');
const args = process.argv.slice(2);

ps.writeFile(args[0], args[1], 'utf8', (err) => {
  if (err) {
    console.error();
  }
});
