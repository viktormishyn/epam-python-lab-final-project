import * as axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/",
});

export const gameAPI = {
  getGames() {
    return instance.get(`games/`);
  },
  getGame(id) {
    return instance.get(`games/${id}/`);
  },
};
