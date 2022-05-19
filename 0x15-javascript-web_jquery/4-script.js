#!/usr/bin/node
const header = document.querySelector('header');
const btn = document.querySelector('div, #toggle_header');

btn.addEventListener('click', function (onclick) {
  header.classList.toggle('green');
  header.classList.toggle('red');
});
