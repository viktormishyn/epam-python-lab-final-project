import React from "react";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";

export default function SearchRadiobuttonPanel(props) {
  const value = null;

  const handleChange = (event) => {
    props.onGenreChange(event.target.value);
  };

  return (
    <FormControl component="fieldset">
      <FormLabel component="legend"></FormLabel>
      <RadioGroup
        aria-label="genre"
        name="genre"
        value={value}
        onChange={handleChange}
      >
        <FormControlLabel
          value="Strategy"
          control={<Radio />}
          label="Strategy"
        />
        <FormControlLabel value="RPG" control={<Radio />} label="RPG" />
        <FormControlLabel value="Action" control={<Radio />} label="Action" />
        <FormControlLabel value="" control={<Radio />} label="All" />
      </RadioGroup>
    </FormControl>
  );
}
