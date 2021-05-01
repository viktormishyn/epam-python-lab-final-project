import React from "react";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import { Whoops404 } from "./components/Whoops404";
import { Games } from "./components/Games/Games";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Games />} />
        <Route path="/games" element={<Games />} />
        <Route path="*" element={<Whoops404 />} />
      </Routes>
    </div>
  );
}

export default App;
