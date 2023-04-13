#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const words = list.filter((element) => element === searchElement);
  return (words.length);
};
