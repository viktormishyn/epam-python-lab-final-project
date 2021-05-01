import { useState, useEffect } from "react";
import axios from "axios";

export function Games() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/games")
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  });

  return (
    <div>
      <h1>Games</h1>
      <ul>
        {games.map((game) => (
          <li key={game.id}>{game.name}</li>
        ))}
      </ul>
    </div>
  );
}
