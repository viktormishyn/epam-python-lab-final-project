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
import Register from "./components/Header/Register";
import { createMuiTheme, ThemeProvider } from "@material-ui/core";
import Login from "./components/Header/Login";
import Logout from "./components/Header/Logout";
import { useNavigate } from "react-router-dom";

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
  const navigate = useNavigate();

  return (
    <div className="app-wraper">
      <ThemeProvider theme={theme}>
        <Header />

        {/* body */}
        <div className="main">
          <Routes>
            <Route path="/register" element={<Register />} />
            <Route path="/games/:id" element={<Game />} />
            <Route path="/" element={<Games />} />
            <Route path="/games" element={<Games />} />
            <Route path="/community" element={<Community />} />
            <Route path="/about" element={<About />} />
            <Route path="/support" element={<Support />} />
            <Route path="*" element={<Whoops404 />} />
            <Route
              path="/login"
              element={
                <Login
                  open={true}
                  handleClose={() => {
                    navigate("/");
                  }}
                />
              }
            />
            <Route path="/logout" element={<Logout />} />
          </Routes>
        </div>

        <Footer />
      </ThemeProvider>
    </div>
  );
}

export default App;
