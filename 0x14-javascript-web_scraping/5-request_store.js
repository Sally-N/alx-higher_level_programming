#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, functioni (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(path, body, { encoding: 'utf8' }, function (error) {
      if (error) {
	console.log(error);
      }
    });
  }
});
