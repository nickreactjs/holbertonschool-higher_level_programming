#!/usr/bin/node
const header = document.querySelector('header');
const btn = document.querySelector('div, #red-header');

btn.addEventListener('click', function (onclick) {
  header.classList.add('red');
});
