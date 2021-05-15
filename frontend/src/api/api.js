import * as axios from "axios";

export const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
  timeout: 5000,
  headers: {
    Authorization: localStorage.getItem("access_token")
      ? "JWT " + localStorage.getItem("access_token")
      : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});
// we add to our requests 2 headers: 'Content-Type': 'application/json' and 'Authorization': <'JWT '+token>

export const gameAPI = {
  getGames(genre = null, search = null) {
    return instance.get(`games/`, {
      params: {
        genre: genre,
        search: search,
      },
    });
  },
  getGame(id) {
    return instance.get(`games/${id}/`);
  },
};

export const genreAPI = {
  getGenres() {
    return instance.get(`genres/`);
  },
};

export const registerAPI = {
  postNewUser(email, username, password) {
    return instance.post(`users/register/`, {
      email: email,
      username: username,
      password: password,
    });
  },
};

export const loginAPI = {
  login(email, password) {
    return instance.post(`token/`, {
      email: email,
      password: password,
    });
  },
};
