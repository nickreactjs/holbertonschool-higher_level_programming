#!/usr/bin/node

const btn = document.querySelector('div, #update_header');
const header = document.querySelector('header');

btn.addEventListener('click', function (onclick) {
  header.textContent = 'New Header!!!';
});
