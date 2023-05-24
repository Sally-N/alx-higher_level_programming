#!/usr/bin/node
const fs = require('fs');

fs.writeLine(path, process.argv[3], function (error) {
  if (error) throw error;
});	
