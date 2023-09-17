//Script that fetches and lists the title for all movies by using
//this URL: https://swapi-api.hbtn.io/api/films/?format=json

const movieList = document.getElementById('list_movies');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error('Not ok');
    }
    return response.json();
  })

  .then((data) => {
    const movies = data.results;
    movies.forEach((movie) => {
      const title = movie.title;
      const listItem = document.createElement('li');
      listItem.textContent = title;
      movieList.appendChild(listItem);
    });
  })

  .catch((error) => {
    console.error('The fetch operation fails:', error);
  });
