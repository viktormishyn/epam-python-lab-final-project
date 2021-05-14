import React from "react";
import "./App.css";
import { Routes, Route } from "react-router-dom";
import { Whoops404 } from "./components/Whoops404";
import Games from "./components/Games/Games";
import Header from "./components/Header/Header";
import Footer from "./components/Footer/Footer";
import Community from "./components/Community";
import About from "./components/About";
import Support from "./components/Support";
import Game from "./components/Game/Game";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#4caf50",
    },
    secondary: {
      main: "#fefefe",
    },
    action: {
      hover: "#000000",
      focusOpacity: 1,
    },
  },
  typography: {
    button: {
      textTransform: "none",
    },
  },
});

function App() {
  return (
    <div className="app-wraper">
      <ThemeProvider theme={theme}>
        <Header />

        {/* body */}
        <div className="main">
          <Routes>
            <Route path="/games/:id" element={<Game />} />
            <Route path="/" element={<Games />} />
            <Route path="/games" element={<Games />} />
            <Route path="/community" element={<Community />} />
            <Route path="/about" element={<About />} />
            <Route path="/support" element={<Support />} />
            <Route path="*" element={<Whoops404 />} />
          </Routes>
        </div>

        <Footer />
      </ThemeProvider>
    </div>
  );
}

export default App;
