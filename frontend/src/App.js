import React from "react";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import { Whoops404 } from "./components/Whoops404";
import Games from "./components/Games/Games";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";

function App() {
  return (
    <div className="app-wraper">
      <Header />
      <Routes>
        <Route path="/" element={<Games />} />
        <Route path="/games" element={<Games />} />
        <Route path="*" element={<Whoops404 />} />
      </Routes>
      <Footer />
    </div>
  );
}

export default App;
