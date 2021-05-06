import * as axios from "axios";

const instance = axios.create({
  baseURL: "http://localhost:8000/api/v1/",
});

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
