/* eslint-disable no-undef */

const API_URL = "http://localhost:8000"; // in the normal docker network mode set this to the name of the fastapi container.

// when the network mode is host, set this to the host machine's IP address, or localhost if you are running the front-end on the same machine as the fastapi server.

function listUsers(cb) {
  return fetch(`${API_URL}/api/users`, {
    accept: "application/json",
  })
    .then(checkStatus)
    .then(parseJSON)
    .then(cb);
}

function checkStatus(response) {
  if (response.status >= 200 && response.status < 300) {
    return response;
  }
  const error = new Error(`HTTP Error ${response.statusText}`);
  error.status = response.statusText;
  error.response = response;
  console.log(error); // eslint-disable-line no-console
  throw error;
}

function parseJSON(response) {
  return response.json();
}

const Client = { listUsers };
export default Client;
