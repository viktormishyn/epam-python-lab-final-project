import React, { useEffect, useState } from "react";
import { useParams } from "react-router";
import { gameAPI } from "../../api/api";
import s from "./Game.module.css";

function Game() {
  let { id } = useParams();

  const [game, setGame] = useState([]);
  useEffect(() => {
    gameAPI
      .getGame(id)
      .then((res) => {
        setGame(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  });

  return (
    <div className={s.game}>
      {/* image */}
      <div>
        <img src={game.image} alt={game.name} />
      </div>

      {/* name */}
      <div>
        <h1>{game.name}</h1>
      </div>

      {/* price + button */}
      <div className={s.game__buy}>
        <span className={s.game__buy__price}>${game.price}</span>
        <button className={s.game__buy__button}>BUY</button>
      </div>
      <br />
      <hr />
      <br />

      {/* genres */}
      <div>
        <span className={s.game__genre}>{game.genre}</span>
      </div>

      {/* description */}
      <p>{game.description}</p>

      {/* comments */}
    </div>
  );
}

export default Game;
