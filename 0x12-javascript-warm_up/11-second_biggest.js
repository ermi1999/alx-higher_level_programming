#!/usr/bin/node
const arr = process.argv.splice(2);

let largest = 0;
let secondLargest = 0;

if (arr.length === 1) {
  console.log(0);
} else {
  let i;
  for (i = 0; i < arr.length; i++) {
    if (parseInt(arr[i]) > largest) {
      largest = parseInt(arr[i]);
    }
  }
  for (i = 0; i < arr.length; i++) {
    if (parseInt(arr[i]) > secondLargest && parseInt(arr[i]) !== largest) {
      secondLargest = parseInt(arr[i]);
    }
  }
  console.log(secondLargest);
}
