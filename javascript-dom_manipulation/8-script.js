//script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr 
//and displays the value of hello from that fetch in the HTML element 
//with id hello

document.addEventListener('DOMContentLoaded', () => {
    const helloElement = document.getElementById('hello');
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Not ok');
        }
        return response.json();
      })

      .then((data) => {
        const translation = data.hello;
        helloElement.textContent = translation;
      })

      .catch((error) => {
        console.error('The fetch operation fails:', error);
      });
  });
  