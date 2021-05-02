import s from "./Games.module.css";
import { useState, useEffect } from "react";
import axios from "axios";

function Games() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/games")
      .then((res) => {
        setGames(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  });

  return (
    <div className={s.games}>
      <h1>Games</h1>
      <ul>
        {games.map((game) => (
          <li key={game.id} style={{ float: "left", margin: "10px" }}>
            <p>{game.name}</p>
            <p>{game.genre}</p>
            <p>{game.description}</p>
            <p>{game.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Games;
