#!/usr/bin/node

const argv = require('process');

let num = process.argv[2];
let count = process.argv[2];

if (isNaN(num))
{
	console.log('Missing size');
}
else
{
	while (count > 0)
	{
		console.log('X'.repeat(num));
		count--;
	}
}


