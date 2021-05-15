import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { loginAPI } from "../../api/api";
import axiosInstance from "../../api/api";

export default function SignUp() {
  const navigate = useNavigate();

  useEffect(() => {
    loginAPI.logout();
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    axiosInstance.defaults.headers["Authorization"] = null;
    navigate("/login");
  });
  return <div>Logout</div>;
}
