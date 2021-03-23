#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (element of list) {
    if (element === searchElement) {
      i++;
    }
  }
  return i;
}
