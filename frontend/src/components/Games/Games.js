import s from "./Games.module.css";
import { useState, useEffect } from "react";
import SearchBar from "./Search/SearchBar";
import GameItem from "./GameItem/GameItem";
import { gameAPI } from "../../api/api";

function Games() {
  const [games, setGames] = useState([]);
  const [genre, setGenre] = useState("");
  const [search, setSearch] = useState("");

  useEffect(() => {
    gameAPI
      .getGames(genre, search)
      .then((res) => {
        setGames(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [genre, search]);

  return (
    <div className={s.games}>
      {/* search bar: genre checkbox + search box */}
      <div className={s.games__searchbar}>
        <SearchBar
          onGenreChange={(value) => setGenre(value)}
          genre={genre}
          onSearch={(value) => setSearch(value)}
          search={search}
        />
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
