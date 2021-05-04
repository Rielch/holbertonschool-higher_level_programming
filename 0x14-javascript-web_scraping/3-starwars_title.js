#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, data, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
