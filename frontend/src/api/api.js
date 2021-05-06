import * as axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
});

export const gameAPI = {
  getGames(genre = null) {
    if (genre === null) {
      return instance.get(`games/`);
    } else {
      return instance.get(`games/?genre=${genre}`);
    }
  },
  getGame(id) {
    return instance.get(`games/${id}/`);
  },
};
