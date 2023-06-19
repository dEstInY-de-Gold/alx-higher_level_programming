#!/usr/bin/node

exports.logMe = function (item) {
  if (!(this.cnt)) {
    this.cnt = 0;
  }
  console.log(`${this.cnt}: ${item}`);
  this.cnt += 1;
};
