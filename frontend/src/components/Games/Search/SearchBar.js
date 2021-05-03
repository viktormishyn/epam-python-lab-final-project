import React from "react";
import s from "./SearchBar.module.css";

function SearchBar() {
  return (
    <div className={s.searchbar}>
      {/* genre checkbox */}
      <span>+ add genre</span>

      {/* genres panel  */}
      <span>Strategy</span>

      {/* search box */}
      <span>
        <input type="text" />
      </span>
    </div>
  );
}

export default SearchBar;
