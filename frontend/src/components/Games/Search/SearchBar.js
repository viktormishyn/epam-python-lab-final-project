import React from "react";
import s from "./SearchBar.module.css";
import SearchIcon from "@material-ui/icons/Search";

function SearchBar() {
  return (
    <div className={s.searchbar}>
      {/* genre checkbox */}
      <span>+ add genre</span>

      {/* genres panel  */}
      <div>
        <span className={s.searchbar__genre}>Strategy</span>
        <span className={s.searchbar__genre}>RPG</span>
      </div>

      {/* search box */}
      <div className={s.searchbar__search}>
        <input type="text" className={s.searchbar__input} />
        <SearchIcon className={s.searchbar__icon} />
      </div>
    </div>
  );
}

export default SearchBar;
