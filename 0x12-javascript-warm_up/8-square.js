#!/usr/bin/node

/* script that prints a square */

if (parseInt(process.argv[2])) {
  let string = '';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      string += 'X';
    }
    console.log(string);
  }
} else {
  console.log('Missing size');
}
