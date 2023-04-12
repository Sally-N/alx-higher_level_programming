#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments */

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt[i]);
  }
  const arrdesc = arr.sort().reverse();
  console.log(arrdesc[1]);
}
