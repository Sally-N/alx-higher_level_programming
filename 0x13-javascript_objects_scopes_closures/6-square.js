#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    let row;
    for (let i = 0; i < this.width; i++) {
      if (!c) {
        row += 'X';
      } else {
        row += c;
      }
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}
module.exports = Square;
