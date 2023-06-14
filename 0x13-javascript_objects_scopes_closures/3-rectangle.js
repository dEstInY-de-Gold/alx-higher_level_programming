#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((parseInt(w) > 0) && (parseInt(h) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if ((this.width) && (this.height)) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
};
