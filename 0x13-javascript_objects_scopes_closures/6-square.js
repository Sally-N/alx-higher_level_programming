#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      if (!c) {
        row += 'X';
      } else {
        row += 'C';
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
