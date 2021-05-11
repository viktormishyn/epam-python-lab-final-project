import React, { useState, useEffect } from "react";
import { genreAPI } from "../../../api/api";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";

export default function SearchRadiobuttonPanel(props) {
  const [genres, setGenres] = useState([]);
  const [value, setValue] = React.useState("");

  useEffect(() => {
    genreAPI
      .getGenres()
      .then((res) => setGenres(res.data))
      .catch((err) => console.log(err));
  }, [genres]);

  const handleChange = (event) => {
    props.onGenreChange(event.target.value);
    setValue(event.target.value);
  };

  return (
    <FormControl component="fieldset">
      <RadioGroup
        aria-label="genre"
        name="genre"
        value={value}
        onChange={handleChange}
      >
        {genres.map((genre) => (
          <FormControlLabel
            value={genre.name}
            control={<Radio color="default" />}
            label={genre.name}
            key={genre.id}
          />
        ))}
        <FormControlLabel
          value=""
          control={<Radio color="default" />}
          label="All"
        />
      </RadioGroup>
    </FormControl>
  );
}
