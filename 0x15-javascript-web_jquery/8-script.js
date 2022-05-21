const list = document.querySelector('ul, #list_movies');

axios.get('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    for (const film of response.data.results) {
      const node = document.createElement('li');
      const textnode = document.createTextNode(film.title);
      node.appendChild(textnode);
      list.appendChild(node);
    }
  })
  .catch(function (error) {
    console.log(error);
  });
