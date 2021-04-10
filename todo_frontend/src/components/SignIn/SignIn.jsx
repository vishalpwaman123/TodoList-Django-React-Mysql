import React, { Component } from "react";
import "./SignIn.scss";

import Snackbar from "@material-ui/core/Snackbar";
import Slide from "@material-ui/core/Slide";
import TextField from "@material-ui/core/TextField";
import { Input, InputAdornment, IconButton, Button } from "@material-ui/core";
import { Visibility, VisibilityOff } from "@material-ui/icons";

const EmailRegrex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

function TransitionUp(props) {
  return <Slide {...props} direction="up" />;
}

function TransitionLeft(props) {
  return <Slide {...props} direction="left" />;
}

function TransitionRight(props) {
  return <Slide {...props} direction="right" />;
}

export class SignIn extends Component {
  constructor(props) {
    super(props);

    this.state = {
      open: false,
      transition: "",
      showPassword: false,
      Password: "",
      forgetpasswordFlag: false,
    };

    this.errors = {
      UserNameError: "",
    };
  }

  handleClick = (Transition) => () => {
    this.setState({ transition: Transition });
    this.setState({ open: true });
  };

  handleClickShowPassword = () => {
    this.setState({ ...this.state, showPassword: !this.state.showPassword });
  };

  handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  handleForgetPassword = () => {
    this.setState({ forgetpasswordFlag: !this.state.forgetpasswordFlag });
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  handleChange = (event) => {
    const { value, name } = event.target;
    this.setState({ [name]: value });
  };
  render() {
    return (
      <div id="container">
        <div id="sub-Container1"></div>
        <div id="sub_Container2">
          <div id="Header">
            <div id="main-Header">ToDo List</div>
            <div id="sub-Header">Sign In</div>
          </div>

          <form className="forms">
            <div className="form-group">
              <label for="usr" className="label">
                Name :
              </label>
              <Input
                id="standard-basic"
                autoComplete="off"
                style={{ marginbotton: "5px" }}
                type="text"
                name="username"
                className="UserName"
                placeholder="Username or Email Id"
              />
            </div>
            <div className="form-group">
              <label for="pwd" className="label">
                Password :
              </label>
              <Input
                type={this.state.showPassword ? "text" : "password"}
                // class="form-control form-control-sm"
                style={{
                  background: "#fff",
                  width: "70%",
                  borderRadius: "3px",
                  fontSize: "15px",
                  padding: "5px",
                }}
                // InputLabelProps={{ style: { fontSize: 10 } }}
                variant="outlined"
                id="pwd"
                name="Password"
                placeholder="Password"
                autoComplete="off"
                value={this.state.Password}
                onChange={this.handleChange}
                className="Password"
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
              />
            </div>
            <div className="buttons">
              <Button color="primary" onClick={this.handleForgetPassword}>
                Forget Password
              </Button>
              <Button
                variant="contained"
                color="primary"
                className="SignInButton"
                onClick={this.handleClick(TransitionUp)}
              >
                SignIn
              </Button>
            </div>
            {this.state.forgetpasswordFlag ? (
              <div className="ForgetPassword">
                <div className="Header">Forget Password</div>
                <div className="Body">
                  <label className="Label">Email/UserName :</label>
                  <div className="InputField">
                    <TextField
                      id="standard-basic-small"
                      autoComplete="off"
                      style={{ marginbotton: "10px" }}
                      type="text"
                      name="username"
                      className="IdInput"
                      placeholder="Username or Email Id"
                      variant="filled"
                      size="small"
                    />
                  </div>
                </div>
                <div className="footer">
                  <Button
                    variant="contained"
                    color="primary"
                    className="SignInButton"
                    onClick={this.handleClick(TransitionRight)}
                  >
                    Search
                  </Button>
                </div>
              </div>
            ) : (
              <div></div>
            )}
          </form>
        </div>
        <Snackbar
          open={this.state.open}
          onClose={this.handleClose}
          TransitionComponent={this.state.transition}
          message="Sign In Successful"
        />
      </div>
    );
  }
}

export default SignIn;
