import React, { Component } from "react";
import "./SignUp.scss";
import Modal from "./Modal.jsx";

import { Visibility, VisibilityOff } from "@material-ui/icons";
import CancelRoundedIcon from "@material-ui/icons/CancelRounded";
import CheckCircleOutlineRoundedIcon from "@material-ui/icons/CheckCircleOutlineRounded";

import {
  Snackbar,
  Slide,
  Input,
  Button,
  InputAdornment,
  IconButton,
} from "@material-ui/core";

const EmailRegrex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
const PasswordRegrex = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;

function TransitionUp(props) {
  return <Slide {...props} direction="up" />;
}

export class SignUp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      open: false,
      transition: "",
      disabledBtn: false,
      UserName: "",
      Email: "",
      Password: "",
      ConfirmPassword: "",
      showPassword: false,
      PasswordMatch: false,
      AccountType: "Student",
      GenderType: "Male",
      selectedDate: "",
    };

    this.error = {
      UserNameError: "",
      EmailError: "",
      PasswordError: "",
      ConfirmPasswordError: "",
    };
  }

  handleClick = (Transition) => () => {
    this.setState({ transition: Transition });
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  handleClickShowPassword = () => {
    this.setState({ ...this.state, showPassword: !this.state.showPassword });
  };

  handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  handledetailButtonVisibility(PasswordMatch, value) {
    console.log("Value :", value);
    if (PasswordMatch === true) {
      if (
        this.error.UserNameError !== "" ||
        this.error.EmailError !== "" ||
        value === ""
      ) {
        console.log(
          "line 1 ",
          this.error.UserNameError,
          " ",
          this.error.EmailError,
          " ",
          value
        );
        this.setState({ disabledBtn: false });
      } else {
        console.log(
          "line 2 ",
          this.error.UserNameError,
          " ",
          this.error.EmailError,
          " ",
          value
        );
        this.setState({ disabledBtn: true });
      }
    } else {
      console.log("Password Match False");
      this.setState({ disabledBtn: false });
    }
  }

  handleChange = (event) => {
    const { value, name } = event.target;
    var errors = this.error;
    var state = this.state;
    var flag = this.state.PasswordMatch;
    switch (name) {
      case "UserName":
        errors.UserNameError = value.length > 3 ? "" : "UserName Not Valid";
        break;
      case "Email":
        errors.EmailError = EmailRegrex.test(value) ? "" : "Email Id Not Valid";
        break;
      case "Password":
        errors.PasswordError = PasswordRegrex.test(value)
          ? ""
          : "Invalid Password eg.use atleast one Upper,Lower, Number case";
        break;
      case "ConfirmPassword":
        if (state.Password !== "") {
          console.log("Password Not Null", state.Password, " ", value);
          if (state.Password === value) {
            console.log("Password Match");
            this.setState({ PasswordMatch: true });
            flag = true;
            errors.ConfirmPasswordError = "Password Match";
            // flag = 1;
          } else {
            console.log("Password Not Match");
            this.setState({ PasswordMatch: false });
            flag = false;
            errors.ConfirmPasswordError = "Password Not Match";
          }
        } else {
          return;
        }
        break;
      default:
        break;
    }
    console.log(name, " ", value, " flag", flag);
    this.setState({ errors, [name]: value });
    this.handledetailButtonVisibility(flag, value);
  };

  render() {
    console.log(this.state);
    return (
      <div id="container">
        <div id="sub_Container2">
          <div id="Header">
            <div id="main-Header">ToDo List</div>
            <div id="sub-Header">Sign Up</div>
          </div>

          <form className="forms">
            <div className="form-group">
              <label for="usr" className="label">
                Name:
              </label>
              <div className="sub-Part">
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="usr"
                  name="UserName"
                  placeholder="Eg. vishalpwaman"
                  autoComplete="off"
                  value={this.state.UserName}
                  onChange={this.handleChange}
                />
                <div className="error">
                  {this.error.UserNameError && (
                    <div>{this.error.UserNameError}</div>
                  )}
                </div>
              </div>
            </div>
            <div className="form-group">
              <label for="email" className="label">
                Email:
              </label>
              <div className="sub-Part">
                <input
                  type="email"
                  class="form-control form-control-sm"
                  id="pwd"
                  name="Email"
                  placeholder="Ed. vishalpwaman123@gmail.com"
                  autoComplete="off"
                  value={this.state.Email}
                  onChange={this.handleChange}
                />
                <div className="error">
                  {this.error.EmailError && <div>{this.error.EmailError}</div>}
                </div>
              </div>
            </div>
            <div className="form-group">
              <label for="pwd" className="label">
                Password:
              </label>
              <div className="sub-Part">
                <Input
                  type={this.state.showPassword ? "text" : "password"}
                  // class="form-control form-control-sm"
                  style={{
                    background: "#fff",
                    width: "100%",
                    borderRadius: "3px",
                    fontSize: "15px",
                    padding: "5px",
                  }}
                  id="pwd"
                  name="Password"
                  placeholder="Password"
                  autoComplete="off"
                  endAdornment={
                    <InputAdornment position="end">
                      <IconButton
                        aria-label="toggle password visibility"
                        onClick={this.handleClickShowPassword}
                        onMouseDown={this.handleMouseDownPassword}
                      >
                        {this.state.showPassword ? (
                          <Visibility />
                        ) : (
                          <VisibilityOff />
                        )}
                      </IconButton>
                    </InputAdornment>
                    // State.showPassword ? <Visibility /> : <VisibilityOff />
                  }
                  value={this.state.Password}
                  onChange={this.handleChange}
                />
                <div className="error">
                  {this.error.PasswordError && (
                    <div>{this.error.PasswordError}</div>
                  )}
                </div>
              </div>
            </div>
            <div className="form-group">
              <label for="pwd" className="label">
                Confirm Password:
              </label>
              <div className="sub-Part">
                <Input
                  type={this.state.showPassword ? "text" : "password"}
                  // class="form-control form-control-sm"
                  style={{
                    background: "#fff",
                    width: "100%",
                    borderRadius: "3px",
                    fontSize: "15px",
                    padding: "5px",
                  }}
                  // InputLabelProps={{ style: { fontSize: 10 } }}
                  variant="outlined"
                  id="pwd"
                  name="ConfirmPassword"
                  placeholder="Confirm Password"
                  autoComplete="off"
                  value={this.state.ConfirmPassword}
                  onChange={this.handleChange}
                  endAdornment={
                    <InputAdornment position="end">
                      {this.state.ConfirmPassword === "" ? (
                        ""
                      ) : !this.state.PasswordMatch ? (
                        <CancelRoundedIcon style={{ color: "red" }} />
                      ) : (
                        <CheckCircleOutlineRoundedIcon
                          style={{ color: "green" }}
                        />
                      )}
                      <IconButton
                        aria-label="toggle password visibility"
                        onClick={this.handleClickShowPassword}
                        onMouseDown={this.handleMouseDownPassword}
                      >
                        {this.state.showPassword ? (
                          <Visibility />
                        ) : (
                          <VisibilityOff />
                        )}
                      </IconButton>
                    </InputAdornment>
                    // State.showPassword ? <Visibility /> : <VisibilityOff />
                  }
                />
                <div className="error">
                  {this.error.ConfirmPasswordError && (
                    <div>{this.error.ConfirmPasswordError}</div>
                  )}
                </div>
              </div>
            </div>
            <div className="button">
              {!this.state.disabledBtn ? (
                <div></div>
              ) : (
                // <button
                //   // onClick={this.handleClick(TransitionUp)}
                //   type="button"
                //   class="btn btn-primary"
                //   data-toggle="modal"
                //   data-target="#myModal"
                // >
                //     Add Detail
                //   </button>
                <Button
                  variant="contained"
                    color="primary"
                    
                  data-toggle="modal"
                  data-target="#myModal"
                >
                  Add Detail
                </Button>
              )}
              <button
                onClick={this.handleClick(TransitionUp)}
                type="button"
                class="btn btn-info"
              >
                Register
              </button>
            </div>
          </form>
        </div>

        <div className="modal fade" id="myModal">
          <div className="modal-dialog modal-xl" id="modal-Dialog">
            <div className="modal-content" id="modal-Content">
              <Modal state={this.state} />
            </div>
          </div>
        </div>

        <Snackbar
          open={this.state.open}
          onClose={this.handleClose}
          TransitionComponent={this.state.transition}
          message="Registration Successful"
        />
      </div>
    );
  }
}

export default SignUp;
