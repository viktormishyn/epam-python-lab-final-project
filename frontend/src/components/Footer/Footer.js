import s from "./Footer.module.css";
import logo from "../../static/logo.svg";

function Footer() {
  return (
    <footer className={s.footer}>
      <span className={s.footer_logo}>
        <img src={logo} alt="logo" />
      </span>
      <div className={s.footer_left}>
        <span>GameStore</span>
      </div>
      <div className={s.footer_right}>
        <span>Copyrights - 2021</span>
      </div>
    </footer>
  );
}

export default Footer;
