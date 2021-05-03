import s from "./Footer.module.css";
import logo from "../../static/logo.svg";

function Footer() {
  return (
    <footer className={s.footer}>
      <span>
        <img src={logo} alt="logo" />
      </span>
      <div>
        <span>GameStore</span>
      </div>
      <div>
        <span>Copyrights - 2021</span>
      </div>
    </footer>
  );
}

export default Footer;
