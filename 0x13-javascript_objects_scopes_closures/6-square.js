#!/usr/bin/node
const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    let row = '';
    if (c === undefined) {
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        row += 'c';
      }
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
