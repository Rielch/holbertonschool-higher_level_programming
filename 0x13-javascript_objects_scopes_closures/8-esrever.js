#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length - 1;
  for (let i = 0; i < (size / 2); i++) {
    const temp = list[i];
    list[i] = list[size - i];
    list[size - i] = temp;
  }
  return list;
};
