#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let [i, nb] = [0, 0];
  while (i < list.length) {
    if (list[i] === searchElement) {
      nb += 1;
    }
    i += 1;
  }
  return nb;
};
