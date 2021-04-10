import "./App.css";
import Header from "./components/Homepage.jsx";
import SignUp from "./components/SignUp/SignUp.jsx";
import SignIn from "./components/SignIn/SignIn.jsx";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route exact path="/" component={SignUp} />
          <Route exact path="/SignIn" component={SignIn} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
