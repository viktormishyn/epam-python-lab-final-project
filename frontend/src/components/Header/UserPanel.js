import { Button, Dialog } from "@material-ui/core";
import { NavLink } from "react-router-dom";
import Login from "./Login";
import s from "./Header.module.css";

export default function UserPanel({ open, handleOpen, handleClose }) {
  return (
    <div className={s.header__userbar}>
      {/* Login button*/}
      <span>
        <Button onClick={handleOpen} color="secondary" size="medium">
          Sign in
        </Button>
        <Dialog open={open} onClose={handleClose}>
          <Login open={open} handleClose={handleClose} />
        </Dialog>
      </span>

      {/* Logout button*/}
      <span>
        <Button color="secondary" component={NavLink} to="/logout">
          Logout
        </Button>
      </span>
    </div>
  );
}
