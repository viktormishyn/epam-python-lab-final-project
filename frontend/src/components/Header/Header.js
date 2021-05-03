import s from "./Header.module.css";
import logo from "../../static/logo.svg";
import { Link } from "react-router-dom";

function Header() {
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
        <span>Games</span>
        <span>Community</span>
        <span>About</span>
        <span>Support</span>
      </div>

      {/* user panel */}
      <div className={s.header__userbar}>
        <span>Sing In</span>
      </div>
    </header>
  );
}

export default Header;
