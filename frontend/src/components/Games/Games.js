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
      .then(console.log("rendering"))
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div className={s.games}>
      {/* search bar: genre checkbox + search box */}
      <div className={s.games__searchbar}>
        <SearchBar />
      </div>

      {/* games */}
      <div className={s.games__items}>
        {games.map((game) => (
          <div className={s.games__item} key={game.id}>
            <GameItem game={game} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Games;
