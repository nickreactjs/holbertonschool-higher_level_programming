#!/usr/bin/node
const axios = require('axios');
let nb = 0;
const char = 'people/18';

axios.get(process.argv[2])
  .then(function (response) {
    for (const film of response.data.results) {
      for (const character of film.characters) {
        if (character.includes(char)) {
          nb += 1;
        }
      }
    }
    console.log(nb);
  })
  .catch(function (error) {
    console.log(`code: ${error}`);
  });
