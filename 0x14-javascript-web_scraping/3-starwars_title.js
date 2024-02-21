#!/usr/bin/node

const episodeNum = process.argv[2];
const request = require('request');
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';

request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJson = JSON.parse(body);
    console.log(responseJson.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
