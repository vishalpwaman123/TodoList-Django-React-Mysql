import React, { Component } from "react";
import "./../SignUp/SignUp.scss";

import Snackbar from "@material-ui/core/Snackbar";
import Slide from "@material-ui/core/Slide";

function TransitionUp(props) {
  return <Slide {...props} direction="up" />;
}

export class SignIn extends Component {
  constructor(props) {
    super(props);

    this.state = {
      open: false,
      transition: "",
    };
  }

  handleClick = (Transition) => () => {
    this.setState({ transition: Transition });
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
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
                Name:
              </label>
              <input
                type="text"
                class="form-control form-control-sm"
                id="usr"
                name="username"
                placeholder="Username or Email Id"
              />
            </div>
            <div class="form-group">
              <label for="pwd" className="label">
                Password:
              </label>
              <input
                type="password"
                class="form-control form-control-sm"
                id="pwd"
                name="password"
                placeholder="Password"
              />
            </div>

            <div className="button">
              <button
                onClick={this.handleClick(TransitionUp)}
                type="button"
                class="btn btn-info"
              >
                Sign In
              </button>
            </div>
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
