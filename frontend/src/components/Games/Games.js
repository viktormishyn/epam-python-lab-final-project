import s from "./Games.module.css";
import { useState, useEffect } from "react";
import axios from "axios";

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
      <ul>
        {games.map((game) => (
          <li key={game.id} style={{ float: "left", margin: "10px" }}>
            <img src={game.image} alt={game.name} width="400px" />
            <h2>{game.name}</h2>
            <p>Genre: {game.genre}</p>
            <p>Description: {game.description}</p>
            <p>${game.price}</p>
            <hr />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Games;
