import { useState } from "react";
import { loginAPI } from "../../api/api";
import axiosInstance from "../../api/api";
// Material-UI
import {
  makeStyles,
  Button,
  Checkbox,
  FormControlLabel,
  Grid,
  Link,
  TextField,
  Dialog,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: "#f0f2f5",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    padding: theme.spacing(3, 7, 3, 7),
    "& .MuiTextField-root": {
      margin: theme.spacing(1),
      width: "350px",
    },
    "& .MuiButtonBase-root": {
      margin: theme.spacing(0),
    },
  },
  title: {
    fontSize: "1.6em",
  },
  field: {
    backgroundColor: "#ffffff",
  },
  checkbox: {
    alignSelf: "left",
    margin: theme.spacing(0, 0, 1),
  },
  submit: {
    color: "#ffffff",
    borderRadius: "6px",
    width: "100px",
  },
  grid: {
    margin: theme.spacing(5, 0, 0),
  },
}));

export default function Login({ open, handleClose }) {
  const initialFormData = Object.freeze({
    email: "",
    password: "",
  });
  const [formData, updateFormData] = useState(initialFormData);

  const handleChange = (e) => {
    updateFormData({
      ...formData,
      // Trimming any whitespace
      [e.target.name]: e.target.value.trim(),
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // console.log(formData);

    loginAPI.login(formData.email, formData.password).then((res) => {
      localStorage.setItem("access_token", res.data.access);
      localStorage.setItem("refresh_token", res.data.refresh);
      axiosInstance.defaults.headers["Authorization"] =
        "JWT " + localStorage.getItem("access_token");
      handleClose();
      // console.log(res);
      // console.log(res.data);
    });
  };

  const classes = useStyles();

  return (
    <Dialog open={open} onClose={handleClose}>
      <form className={classes.root}>
        <div className={classes.title}>
          Please login
          <br />
          <br />
        </div>
        <TextField
          label="Email"
          type="email"
          name="email"
          id="email"
          className={classes.field}
          variant="outlined"
          onChange={handleChange}
        />
        <TextField
          label="Password"
          type="password"
          name="password"
          id="password"
          className={classes.field}
          variant="outlined"
          onChange={handleChange}
        />
        <Grid container justify="flex-start">
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
            className={classes.checkbox}
          />
        </Grid>

        <Button
          type="submit"
          variant="contained"
          className={classes.submit}
          color="primary"
          onClick={handleSubmit}
        >
          Sign in
        </Button>
        <Grid container className={classes.grid}>
          <Grid item xs>
            <Link href="#" variant="body2"></Link>
          </Grid>
          <Grid item>
            <Link href="/register" variant="body2">
              {"Don't have an account? Sign Up"}
            </Link>
          </Grid>
        </Grid>
      </form>
    </Dialog>
  );
}
