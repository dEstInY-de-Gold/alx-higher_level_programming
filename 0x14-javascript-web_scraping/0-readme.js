#!/usr/bin/node

const ps = require('fs');
const filepath = process.argv.slice(2);

ps.readFile(filepath[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
