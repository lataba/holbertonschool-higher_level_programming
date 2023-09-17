//JavaScript script that fetches the character name from the 
//URL: https://swapi-api.hbtn.io/api/people/5/?format=json

const characterElement = document.getElementById('character');
const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(apiUrl)
  .then((response) => {
    if (!response.ok) {
      throw new Error('Not ok');
    }
    return response.json();
  })

  .then((data) => {
    const characterName = data.name;
    characterElement.textContent = `Character Name: ${characterName}`;
  })

  .catch((error) => {
    console.error('The fetch operation fails:', error);
  });
