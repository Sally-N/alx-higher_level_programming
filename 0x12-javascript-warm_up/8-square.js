#!/usr/bin/node

/* script that prints a square */

let string = '';
if (parseInt(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      string += 'X';
    }
    string += '\n';
  }
  console.log(string);
} else {
  console.log('Missing size');
}
