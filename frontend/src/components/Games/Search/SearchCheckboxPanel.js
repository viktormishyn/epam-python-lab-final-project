import React from "react";
import Checkbox from "@material-ui/core/Checkbox";
import FormGroup from "@material-ui/core/FormGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";

export default function SearchCheckboxPanel() {
  return (
    <FormControl component="fieldset">
      <FormLabel component="legend"></FormLabel>
      <FormGroup aria-label="position" row>
        <div></div>
        <FormControlLabel
          value="Strategy"
          control={<Checkbox color="primary" />}
          label="Strategy"
          labelPlacement="end"
        />
        <FormControlLabel
          value="RPG"
          control={<Checkbox color="primary" />}
          label="RPG"
          labelPlacement="end"
        />{" "}
        <FormControlLabel
          value="Action"
          control={<Checkbox color="primary" />}
          label="Action"
          labelPlacement="end"
        />
      </FormGroup>
    </FormControl>
  );
}
