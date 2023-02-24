#!/usr/bin/node
// script that imports an array and computes a new array.

const orginallist = require('100-data.js').list;
console.log(orginalList);
const mappedList = orginalList.map (function (e, index) {
    return (e * index);
});
console.log(mappedList);
