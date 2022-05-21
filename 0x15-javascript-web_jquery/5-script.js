#!/usr/bin/node

const btn = document.querySelector('#add_item');
const li = document.querySelector('ul, .my_list');
let node;
let textnode;

btn.addEventListener('click', function (onclick) {
  node = document.createElement('li');
  textnode = document.createTextNode('Item');
  node.appendChild(textnode);
  li.appendChild(node);
});
