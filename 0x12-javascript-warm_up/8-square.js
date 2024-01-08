#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let i;
  for (i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
