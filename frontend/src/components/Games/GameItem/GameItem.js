import React from "react";
import s from "./GameItem.module.css";

function GameItem({ game }) {
  return (
    <div className={s.gameItem}>
      <img src={game.image} alt={game.name} />
      <h2>{game.name}</h2>
      <p>Genre: {game.genre}</p>
      <p>${game.price}</p>
    </div>
  );
}

export default GameItem;
