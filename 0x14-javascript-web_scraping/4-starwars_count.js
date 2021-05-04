#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, data, body) => {
    if (error) {
	console.log(error);
	return;
    }
    const films = JSON.parse(body).results;
    const films_count = films.length;
    let i = 0;
    let j = 0;
    let total = 0;
    for (i = 0; i < films_count; i++) {
	for (j = 0; j < films[i].characters.length; j++) {
	    if (films[i].characters[j].includes('/18/')) {
		total += 1;
	    }
	}
    }
    console.log(total);
});
