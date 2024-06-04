import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:5000",
});

instance.interceptors.request.use(
  (config) => {
    const librarianRequest = config.headers["x-librarian-request"];
    if (librarianRequest) {
      const librarianToken = localStorage.getItem("librarian_token");
      if (librarianToken) {
        config.headers["x-access-token"] = librarianToken;
      }
      delete config.headers["x-librarian-request"];
    } else {
      const token = localStorage.getItem("token");
      if (token) {
        config.headers["x-access-token"] = token;
      }
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default instance;
