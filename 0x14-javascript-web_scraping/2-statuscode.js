#!/usr/bin/node

const request = require('request')

request(process.argv[2], (error, data) => {
    if (error) {
	console.error('error:', error);
	return;
    }
    console.log(`code: ${data.statusCode}`);
});
