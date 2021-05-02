import s from "./Header.module.css";
import logo from "../../static/logo.svg";

function Header() {
  return (
    <header className={s.header}>
      <span className={s.header_logo}>
        <img src={logo} alt="logo" />
      </span>
      <div className={s.header_left}>
        <span>GameStore</span>
      </div>
      <div className={s.header_nav}>
        <span>Games</span>
        <span>Community</span>
        <span>About</span>
        <span>Support</span>
      </div>
      <div className={s.header_login}>
        <span>Sing In</span>
      </div>
    </header>
  );
}

export default Header;
