#!/usr/bin/node

exports.esrever = function (list) {
  let cnt = list.length - 1;
  const tmpList = [];
  for (let i = 0; i < list.length; i++) {
    tmpList[i] = list[cnt];
    cnt -= 1;
  }
  return tmpList;
};
