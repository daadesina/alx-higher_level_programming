#!/usr/bin/node

const argv = require('process');
let num;

function myFactorial(num)
{
	if (num > 0)
	{
		return (num * myFactorial(num - 1));
	}
	else
	{
		return 1;
	}
}

console.log(myFactorial(process.argv[2]));
