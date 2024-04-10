#!/usr/bin/node

const argv = require('process');
let num = Number(process.argv[2]);
let count = num;
let result = Number(1);

while (count > 0)
{
	result = result * count;
	count--;
}

console.log(result);
