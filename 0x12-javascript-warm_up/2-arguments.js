#!/usr/bin/node

if (process.argv.lenght > 3) {
  console.log('Arguments found');
} else if (process.argv.lenght === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
