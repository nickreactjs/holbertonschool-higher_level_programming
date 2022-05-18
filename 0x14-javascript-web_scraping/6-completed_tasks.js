#!/usr/bin/node
const axios = require('axios');
const dict = { 1: 0 };

axios.get(process.argv[2])
  .then(function (response) {
    for (const task of response.data) {
      if (task.completed) {
        if (dict[task.userId]) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  })
  .catch(function (error) {
    console.log(error);
  });
