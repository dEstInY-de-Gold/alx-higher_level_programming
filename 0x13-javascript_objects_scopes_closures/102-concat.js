#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);

const sourceFile1 = args[0];
const sourceFile2 = args[1];
const destinationFile = args[2];

const content1 = fs.readFileSync(sourceFile1, 'utf8');
const content2 = fs.readFileSync(sourceFile2, 'utf8');
const concatenatedContent = content1 + content2;

fs.writeFileSync(destinationFile, concatenatedContent);
