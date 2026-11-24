#!/usr/bin/node

const request = require('request');

const endpoint = 'https://swapi-api.hbtn.io/api/films'.concat('/', process.argv[2].toString()).concat('/','');
request(endpoint, (error, response, body) => {
    if (!error & response.statusCode === 200) {
        const character_endpoints = JSON.parse(body)['characters'];
        for (const endpoint in character_endpoints) {
            request(endpoint, (error, response, body) => {
                if (!error & response.statusCode === 200) {
                    console.log(JSON.parse(body)['name'])
                }
            })
        }
    }
});
