import AxiosServices from "./AxiosServices.js";
const Config = require("../configuration/Configuration.js");

const axiosServices = new AxiosServices();

export class UserServices {
  AllList() {
    let url = Config.AllList;
    return axiosServices.get(url, false);
  }

  AddList(data) {
    let url = Config.AddList;
    return axiosServices.post(url, data, false);
  }

  UpdateList(data) {
    let url = Config.UpdateList + data.id + "/";
    console.log(url);
    return axiosServices.patch(url, data, false);
  }

  DeleteList(data) {
    let url = Config.DeleteList + data.id + "/";
    console.log(url);
    return axiosServices.delete(url, false);
  }
}
export default UserServices;
