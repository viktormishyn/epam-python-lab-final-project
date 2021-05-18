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

      <div className={s.gameItem__description}>
        {/* price and button */}
        <div className={s.gameItem__price_buy}>
          <span className={s.gameItem__price}>${game.price}</span>
          <button className={s.gameItem__buy_button}>BUY</button>
        </div>

        {/* genre and name */}
        <div className={s.gameItem__genre_name}>
          <br />
          {game.genre}
          <br />
          <strong>{game.name}</strong>
        </div>
      </div>
    </div>
  );
}

export default GameItem;
