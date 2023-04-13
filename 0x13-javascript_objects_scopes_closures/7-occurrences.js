#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const words = list.filter(function (element) {
    return element === searchElement;
  });
  console.log(words.length);
};
