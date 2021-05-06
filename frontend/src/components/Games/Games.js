import s from "./Games.module.css";
import { useState, useEffect } from "react";
import SearchBar from "./Search/SearchBar";
import GameItem from "./GameItem/GameItem";
import { gameAPI } from "../../api/api";

function Games() {
  const [games, setGames] = useState([]);
  const [genre, setGenre] = useState(null);

  useEffect(() => {
    gameAPI
      .getGames(genre)
      .then((res) => {
        setGames(res.data);
      })
      .then(console.log("rendering"))
      .catch((err) => {
        console.log(err);
      });
  }, [genre]);

  return (
    <div className={s.games}>
      {/* search bar: genre checkbox + search box */}
      <div className={s.games__searchbar}>
        <SearchBar onChange={(value) => setGenre(value)} genre={genre} />
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
