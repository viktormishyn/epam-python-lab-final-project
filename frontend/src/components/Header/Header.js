import { useState } from "react";
import s from "./Header.module.css";
import logo from "../../static/logo.svg";
import { Link } from "react-router-dom";
import Login from "./Login";
// Material-UI
import { Dialog, Button } from "@material-ui/core";

function Header() {
  const [open, setOpen] = useState(false);

  const handleOpen = () => {
    setOpen(true);
  };
  const handleClose = () => {
    setOpen(false);
  };

  return (
    <header className={s.header}>
      {/* logo */}
      <span>
        <Link to="/">
          <img src={logo} alt="logo" />
        </Link>
      </span>

      {/* left subscription near logo */}
      <div>
        <Link to="/" className={s.header__subscription}>
          <span>GameStore</span>
        </Link>
      </div>

      {/* navbar */}
      <div className={s.header__nav}>
        <Link to="/" className={s.header__nav__link}>
          <span>Games</span>
        </Link>
        <Link to="/community" className={s.header__nav__link}>
          <span>Community</span>
        </Link>
        <Link to="/about" className={s.header__nav__link}>
          <span>About</span>
        </Link>
        <Link to="/support" className={s.header__nav__link}>
          <span>Support</span>
        </Link>
      </div>

      {/* user panel */}
      <div className={s.header__userbar}>
        <Button onClick={handleOpen} color="secondary" size="medium">
          Sign in
        </Button>
        <Dialog open={open} onClose={handleClose}>
          <Login open={open} handleClose={handleClose} />
        </Dialog>
      </div>
    </header>
  );
}

export default Header;
