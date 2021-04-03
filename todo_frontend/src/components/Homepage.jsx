import React, { Component } from "react";
import "./Homepage.scss";

import userService from "../services/UserServices";
const userServices = new userService();

export class Homepage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      todoList: [],
      activeItem: {
        id: null,
        Name: "",
        category: "",
        price: "",
        description: "",
        star: "",
      },
      editing: false,
    };
    this.handleChange = this.handleChange.bind(this);
    this.fetchingAllData = this.fetchingAllData.bind(this);
    this.editdetail = this.editdetail.bind(this);
  }

  componentWillMount() {
    console.log("component will unmount");
    this.fetchingAllData();
  }

  fetchingAllData() {
    userServices
      .AllList()
      .then((data) => {
        console.log(data.data);
        this.setState({ todoList: data.data });
        console.log(this.state.todoList);
      })
      .catch((error) => {
        console.log(error);
      });
  }

  editdetail(task) {
    // console.log(task);
    this.setState({
      activeItem: {
        id: task.id,
        Name: task.name,
        category: task.category,
        price: task.price,
        description: task.description,
        star: task.stars,
      },
      editing: true,
    });
    // console.log(this.state);
  }

  deleteDetail(task) {
    const user = {
      id: task.id,
    };
    userServices
      .DeleteList(user)
      .then((data) => {
        console.log(data);
        this.setState({
          activeItem: {
            id: "",
            Name: "",
            category: "",
            price: "",
            description: "",
            star: "",
          },
          editing: false,
        });
        this.fetchingAllData();
      })
      .catch((error) => {
        console.log(error);
      });
  }

  handleChange(event) {
    event.preventDefault();
    const { name, value } = event.target;
    // var names = event.target.name;
    // var value = event.target.value;
    console.log("Name :", name);
    console.log("Value :", value);
    switch (name) {
      case "name":
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            Name: value,
          },
        });
        console.log("Name 1", value);
        break;
      case "category":
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            category: value,
          },
        });
        console.log("Category 1", this.state.activeItem.category);
        break;
      case "description":
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            description: value,
          },
        });
        console.log("Description 1");
        break;
      case "price":
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            price: value,
          },
        });
        console.log("Price 1");
        break;
      case "star":
        this.setState({
          activeItem: {
            ...this.state.activeItem,
            star: value,
          },
        });
        console.log("Star 1");
        break;
      default:
        break;
    }

    console.log(this.state.activeItem);
  }

  handleSubmit = (event) => {
    event.preventDefault();
    var activeItems = this.state.activeItem;
    if (
      activeItems.Name === null ||
      activeItems.category === null ||
      activeItems.description === null ||
      activeItems.price === null ||
      activeItems.star === null
    ) {
      console.log("Invalid Submition");
    } else {
      if (this.state.editing === true) {
        const user = {
          id: activeItems.id,
          name: activeItems.Name,
          category: activeItems.category,
          description: activeItems.description,
          price: activeItems.price,
          stars: activeItems.star,
        };
        userServices
          .UpdateList(user)
          .then((data) => {
            console.log(data);
            this.fetchingAllData();
            this.setState({ editing: false });
          })
          .catch((error) => {
            console.log(error);
          });
      } else {
        const user = {
          name: activeItems.Name,
          category: activeItems.category,
          description: activeItems.description,
          price: activeItems.price,
          stars: activeItems.star,
        };
        userServices
          .AddList(user)
          .then((data) => {
            console.log(data);
            this.fetchingAllData();
            this.setState({
              activeItems: {
                Name: null,
                category: null,
                price: null,
                description: null,
                star: null,
              },
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    }
  };

  render() {
    var todoList = this.state.todoList;
    var activeItem = this.state.activeItem;
    var self = this;
    console.log(this.state);
    return (
      <div className="container">
        <div className="sub-Container">
          <div id="task-container">
            <div id="form-wrapper">
              <form id="form" onSubmit={this.handleSubmit}>
                <div className="flex-wrapper">
                  <div style={{ flex: 2 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="name"
                      placeholder="Add name"
                      value={activeItem.Name}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div style={{ flex: 4 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="category"
                      placeholder="Add category"
                      value={activeItem.category}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div style={{ flex: 6 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="description"
                      placeholder="Add description"
                      value={activeItem.description}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div style={{ flex: 2 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="price"
                      placeholder="Add price"
                      value={activeItem.price}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div style={{ flex: 1 }}>
                    <input
                      className="form-control"
                      id="title"
                      type="text"
                      name="star"
                      placeholder="Add Rating ( 1 to 5 )"
                      value={activeItem.star}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div style={{ flex: 1 }}>
                    <input
                      id="submit"
                      className="btn btn-warning"
                      type="submit"
                      name="Add"
                    />
                  </div>
                </div>
              </form>
            </div>
            <div id="list-wrapper">
              {todoList.map(function (task, index) {
                return (
                  <div key={index} className="task-wrapper flex-wrapper">
                    <div style={{ flex: 5 }}>
                      <span>{task.name}</span>
                    </div>
                    <div style={{ flex: 7 }}>
                      <span>{task.category}</span>
                    </div>
                    <div style={{ flex: 5 }}>
                      <span>{task.price}</span>
                    </div>
                    <div style={{ flex: 8 }}>
                      <span>{task.description}</span>
                    </div>
                    <div style={{ flex: 2 }}>
                      <span>{task.stars}</span>
                    </div>
                    <div style={{ flex: 1, margin: "0 1px" }}>
                      <button
                        className="btn btn-sm btn-outline-info"
                        onClick={() => {
                          self.editdetail(task);
                        }}
                      >
                        Edit
                      </button>
                    </div>
                    <div style={{ flex: 1, margin: "0 1px" }}>
                      <button
                        className="btn btn-sm btn-outline-dark delete"
                        onClick={() => {
                          self.deleteDetail(task);
                        }}
                      >
                        -
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Homepage;
