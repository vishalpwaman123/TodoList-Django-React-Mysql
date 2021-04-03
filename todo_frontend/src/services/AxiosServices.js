const axios = require("axios").default;

export class AxiosServices {
  post(url, data, isRequiredHeader = false, header) {
    console.log("Data User: ", data);
    console.log("Url User: ", url);
    return axios.post(url, data, isRequiredHeader && header);
  }

  get(url, isRequiredHeader = false, header) {
    // console.log("Data User: ", data);
    console.log("Url User: ", url);
    return axios.get(url, isRequiredHeader && header);
  }

  patch(url, data, isRequiredHeader = false, header) {
    console.log("Data User: ", data);
    console.log("Url User: ", url);
    return axios.patch(url, data, isRequiredHeader && header);
  }

  delete(url, isRequiredHeader = false, header) {
    // console.log("Data User: ", data);
    console.log("Url User: ", url);
    return axios.delete(url, isRequiredHeader && header);
  }

  put(url, data, isRequiredHeader = false, header) {
    console.log("Data User: ", data);
    console.log("Url User: ", url);
    return axios.put(url, data, isRequiredHeader && header);
  }
}

export default AxiosServices;
