import React, { Component } from "react";
import "./Modal.scss";

import {
  MuiPickersUtilsProvider,
  KeyboardTimePicker,
  KeyboardDatePicker,
} from "@material-ui/pickers";

import {
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  FormLabel,
  Snackbar,
  Slide,
  Input,
  InputAdornment,
  IconButton,
  Button,
} from "@material-ui/core";

import PhotoCamera from "@material-ui/icons/PhotoCamera";

import "date-fns";
import DateFnsUtils from "@date-io/date-fns";

export class Modal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      FullName: "",
      selectedDate: "",
      AccountType: "",
      GenderType: "",
      MobileNumber: "",
    };
  }

  handleDateChange = (date) => {
    this.setState({ selectedDate: date });
  };

  handleAccountType = (event) => {
    this.setState({ AccountType: event.target.value });
  };

  handleGenderType = (event) => {
    this.setState({ GenderType: event.target.value });
  };

  render() {
    return (
      //   <div className="modal-Container">
      //     <div className="modal fade" id="myModal">
      //       <div className="modal-dialog modal-lg" id="modal-Dialog">
      <div className="modal-content" id="modal-Content">
        <div className="modal-header">
          <h4 className="modal-title">User Detail</h4>
          <button type="button" className="close" data-dismiss="modal">
            &times;
          </button>
        </div>
        <div className="modal-body">
          <div className="detailbody">
            <div className="FullName">
              <label for="usr" className="label">
                Full Name :
              </label>
              <Input
                type="text"
                // class="form-control form-control-sm"
                style={{
                  background: "#fff",
                  width: "100%",
                  borderRadius: "3px",
                  fontSize: "15px",
                  padding: "5px",
                }}
                // variant="contained"
                id="fullname"
                name="FullName"
                className="FullNames"
                placeholder="Eg. Vishal Waman"
                autoComplete="off"
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={this.handleClickShowPassword}
                      onMouseDown={this.handleMouseDownPassword}
                    ></IconButton>
                  </InputAdornment>
                  // State.showPassword ? <Visibility /> : <VisibilityOff />
                }
                value={this.state.FullName}
                onChange={this.handleChange}
              />
            </div>
            <div className="AccountType">
              <FormControl component="fieldset" className="fieldSet">
                <label component="legend" className="label">
                  Account :
                </label>
                <RadioGroup
                  aria-label="account"
                  name="Account"
                  className="Accounts"
                  value={this.state.AccountType}
                  onChange={this.handleAccountType}
                >
                  <FormControlLabel
                    value="student"
                    control={<Radio />}
                    label="Student"
                  />
                  <FormControlLabel
                    value="employee"
                    control={<Radio />}
                    label="Employee"
                  />
                  <FormControlLabel
                    value="homies"
                    control={<Radio />}
                    label="Homies"
                  />
                </RadioGroup>
              </FormControl>
            </div>
            <div className="MobileNumber">
              <label for="usr" className="label">
                Mobile Number :
              </label>
              <Input
                type="number"
                // class="form-control form-control-sm"
                style={{
                  background: "#fff",
                  width: "80%",
                  borderRadius: "3px",
                  fontSize: "15px",
                  padding: "5px",
                }}
                id="mobilenumber"
                name="MobileNumber"
                className="MobileNumbers"
                placeholder="Eg. 9881563158"
                autoComplete="off"
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={this.handleClickShowPassword}
                      onMouseDown={this.handleMouseDownPassword}
                    ></IconButton>
                  </InputAdornment>
                  // State.showPassword ? <Visibility /> : <VisibilityOff />
                }
                value={this.state.MobileNumber}
                onChange={this.handleChange}
              />
            </div>
            <div className="BOD">
              <label for="usr" className="label">
                Date Of Birth :
              </label>
              <MuiPickersUtilsProvider utils={DateFnsUtils}>
                <KeyboardDatePicker
                  margin="normal"
                  id="date-picker-dialog"
                  // label="Date picker dialog"
                  name="DateInput"
                  format="MM/dd/yyyy"
                  value={this.state.selectedDate}
                  onChange={this.handleDateChange}
                  KeyboardButtonProps={{
                    "aria-label": "change date",
                  }}
                  helperText=""
                />
              </MuiPickersUtilsProvider>
            </div>
            <div className="Gender">
              <FormControl component="fieldset" className="fieldSet">
                <label component="legend" className="label">
                  Gender :
                </label>
                <RadioGroup
                  aria-label="gender"
                  name="gender1"
                  className="genders"
                  value={this.state.GenderType}
                  onChange={this.handleGenderType}
                >
                  <FormControlLabel
                    value="female"
                    control={<Radio />}
                    label="Female"
                  />
                  <FormControlLabel
                    value="male"
                    control={<Radio />}
                    label="Male"
                  />
                  <FormControlLabel
                    value="other"
                    control={<Radio />}
                    label="Other"
                  />
                </RadioGroup>
              </FormControl>
            </div>
          </div>
          <div className="detailImage">
            <div className="DisplayImage">
              <img src="" className="Image" alt="" />
            </div>
            <div className="profileImage">
              <input
                accept="image/*"
                className="uploadImage"
                id="icon-button-file"
                type="file"
              />
              <label htmlFor="icon-button-file" style={{ margin: "0px" }}>
                <IconButton
                  color="primary"
                  aria-label="upload picture"
                  component="span"
                >
                  <PhotoCamera />
                </IconButton>
              </label>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <Button variant="contained" color="secondary">
            Submit
          </Button>
        </div>
      </div>
      //     </div>
      //   </div>
    );
  }
}

export default Modal;
