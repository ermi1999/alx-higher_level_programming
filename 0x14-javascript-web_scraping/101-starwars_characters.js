#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characterUrls = film.characters;

    function getCharacterName (characterUrl) {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (error) {
            reject(error);
          }
          const character = JSON.parse(body);
          resolve(character.name);
        });
      });
    }

    const promises = characterUrls.map(characterUrl => getCharacterName(characterUrl));

    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  }
});
