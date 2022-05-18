#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
const filename = process.argv[3];

axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(filename, response.data, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  });
