import s from "./Games.module.css";
import { useState, useEffect } from "react";
import axios from "axios";
import SearchBar from "./Search/SearchBar";
import GameItem from "./GameItem/GameItem";

function Games() {
  const [games, setGames] = useState([]);
  const BASE_URL = "http://localhost:8000/";

  useEffect(() => {
    axios
      .get(BASE_URL + "api/games/")
      .then((res) => {
        setGames(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  });

  return (
    <div className={s.games}>
      {/* search bar: genre checkbox + search box */}
      <div className={s.games__searchbar}>
        <SearchBar />
      </div>

      {/* games */}
      <div className={s.games__items}>
        {games.map((game) => (
          <div className={s.games__item}>
            <GameItem game={game} key={game.id} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Games;
