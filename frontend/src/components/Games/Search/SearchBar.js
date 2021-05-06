import React from "react";
import s from "./SearchBar.module.css";
import SearchIcon from "@material-ui/icons/Search";
import SearchPopover from "./SearchPopover";

function SearchBar(props) {
  return (
    <div className={s.searchbar}>
      {/* genre checkbox */}
      <div className={s.searchbar__popover}>
        <SearchPopover onGenreChange={props.onGenreChange} />
      </div>

      {/* genres panel  */}
      <div>
        <span className={s.searchbar__genre}>
          {props.genre ? props.genre : "All genres"}
        </span>
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
