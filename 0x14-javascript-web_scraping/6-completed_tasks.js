#!/usr/bin/node
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const tasksCompletedByUserId = {};

    todos.forEach(function (task) {
    if (task.completed) {
      tasksCompletedByUserId[task.userId] = (completedTasksByUserId[task.userId] || 0) + 1;
    }
    });

    for (const userId in tasksCompletedByUserId) {
      console.log(tasksCompletedById[userId]);
    } else {
      console.log(error);
    }
  }
});
