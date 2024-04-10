#!/usr/bin/node

const argv = require('process');

let myList = [];

let num = (process.argv.length - 1);

let count = 0;

while (num > 1)
{
	myList[count] = Number(process.argv[num]);
	count++;
	num--;
}

let biggest = Math.max.apply(null, myList);
let index = myList.length;
while (index >= 0)
{
	if (myList[index] == biggest)
	{
		break;
	}
	index--;
}

let newList = myList.slice(0, index).concat(myList.slice(index + 1));

console.log(Math.max.apply(null, newList));
