#!/usr/bin/node

const size = process.argv.length;
if (size < 3) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
