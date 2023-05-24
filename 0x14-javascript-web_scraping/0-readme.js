#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], function (error, content) {
  console.log(error || content.toString('utf8'));
});	
