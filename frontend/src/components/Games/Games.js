import s from "./Games.module.css";
import { useState, useEffect } from "react";
import SearchBar from "./Search/SearchBar";
import GameItem from "./GameItem/GameItem";
import { gameAPI } from "../../api/api";

function Games() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    gameAPI
      .getGames()
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
