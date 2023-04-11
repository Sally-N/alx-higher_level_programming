#!/usr/bin/node

/* script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer */

if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + parseInt(process.argv[2]));
}
