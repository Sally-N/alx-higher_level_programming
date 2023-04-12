#!/usr/bin/node

/* script that searches the second biggest integer in the list of arguments */

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt[i]);
  }
  arr.sort((a, b)=>b-a);
  console.log(arr[1]);
}
