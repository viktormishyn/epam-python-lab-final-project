import React from "react";
import { useLocation } from "react-router";

export function Whoops404() {
  let location = useLocation();
  console.log(location);
  return (
    <div>
      <h1>Whoops... Nothing found at '{location.pathname}'</h1>
    </div>
  );
}
