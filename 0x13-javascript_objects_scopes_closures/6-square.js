#!/usr/bin/node

const square = require('./5-square.js');

module.exports = class Square extends square {
  charPrint (c) {
    if (!(c)) {
      this.print();
    } else {
      for (let s = 0; s < this.width; s++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
