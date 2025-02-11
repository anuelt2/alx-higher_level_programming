#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const completedTaskCount = {};

  body.forEach(task => {
    if (task.completed === true) {
      if (!(task.userId in completedTaskCount)) {
        completedTaskCount[task.userId] = 0;
      }
      completedTaskCount[task.userId] += 1;
    }
  });
  console.log(completedTaskCount);
});
