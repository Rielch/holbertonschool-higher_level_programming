#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, data, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(body);
  let i = 0;
  const users = {};
  for (i = 0; i < tasks.length; i++) {
    if (tasks[i].completed) {
      if (!users[tasks[i].userId]) {
        users[tasks[i].userId] = 0;
      }
      users[tasks[i].userId] += 1;
    }
  }
  console.log(users);
});
