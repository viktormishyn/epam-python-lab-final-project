import React from "react";
import { Link } from "react-router-dom";
import s from "./GameItem.module.css";

function GameItem({ game }) {
  let link = "/games/" + game.id;
  return (
    <div className={s.gameItem}>
      <Link to={link}>
        <img src={game.image} alt={game.name} />
      </Link>

      <h2>{game.name}</h2>
      <p>Genre: {game.genre}</p>
      <p>${game.price}</p>
    </div>
  );
}

export default GameItem;
