#!/usr/bin/node

const character = document.querySelector('div, #character');

axios.get('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    character.textContent = response.data.name;
  })
  .catch(function (error) {
    console.log(error);
  });
