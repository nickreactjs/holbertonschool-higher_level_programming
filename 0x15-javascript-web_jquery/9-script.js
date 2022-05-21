#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const hello = document.querySelector('div, #hello');
  axios.get('https://fourtonfish.com/hellosalut/?lang=fr')
    .then(function (response) {
      const text = response.data.hello;
      hello.textContent = text;
    })
    .catch(function (error) {
      console.log(error);
    });
});
