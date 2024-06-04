<template>
  <div class="baseRoot">
    <div class="navbar">
      <div class="logoContainer">
        <img
          src="@/assets/images/Oak Png.png"
          alt="The Oak Tree"
          class="logoImg"
        />
      </div>
      <p class="logoText">Bibliophilia</p>
    </div>
    <div class="signinMainFrame">
      <div class="signinBox">
        <div class="info">
          <p class="welcome">Welcome to</p>
          <p class="title">Bibliophilia</p>
          <p class="description">
            Explore countless books, enjoy personalized picks, and join a
            vibrant community. Dive into your next great read today!
          </p>
          <div class="stats">
            <div class="statCard">
              <div class="upperCont">
                <div class="imgCont">
                  <img
                    src="@/assets/images/books_icon.png"
                    alt=""
                    class="img"
                  />
                </div>
              </div>
              <div class="statInfo">2L + <br />Books</div>
            </div>
            <div class="statCard">
              <div class="upperCont">
                <div class="imgCont">
                  <img
                    src="@/assets/images/author_icon.png"
                    alt=""
                    class="img"
                  />
                </div>
              </div>
              <div class="statInfo">80K + <br />Authors</div>
            </div>
            <div class="statCard">
              <div class="upperCont">
                <div class="imgCont">
                  <img src="@/assets/images/user_icon.png" alt="" class="img" />
                </div>
              </div>
              <div class="statInfo">500 + <br />Active Users</div>
            </div>
          </div>
          <p class="join">JOIN US NOW !!</p>
        </div>
        <div class="desk" v-if="signinView">
          <p class="signHead">Sign In</p>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img
                src="@/assets/images/user_icon.png"
                alt=""
                class="inputImg"
              />
            </div>
            <input v-model="username" placeholder="Enter Your Username" />
          </div>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img
                src="@/assets/images/password_icon.png"
                alt=""
                class="inputImg"
              />
            </div>
            <input
              v-model="password"
              placeholder="Enter Your Password"
              :type="passwordView ? 'text' : 'password'"
              style="width: 14rem"
            />
            <div class="inputImgCont" @click="passwordViewer()">
              <img
                src="@/assets/images/password_view.png"
                alt=""
                class="inputImg"
                ref="viewer"
              />
            </div>
          </div>
          <p class="changeSign" @click="changeView()">
            Don't have an account? Sign Up Now !!
          </p>
          <div class="continue" @click="submit()">Continue →</div>
          <p class="message" v-if="message != ''">{{ message }}</p>
        </div>

        <div class="desk" v-else>
          <p class="signHead">Sign Up</p>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img
                src="@/assets/images/user_icon.png"
                alt=""
                class="inputImg"
              />
            </div>
            <input v-model="username" placeholder="Enter Your Username" />
          </div>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img src="@/assets/images/email.png" alt="" class="inputImg" />
            </div>
            <input
              v-model="email"
              type="email"
              placeholder="Enter Your Email"
            />
          </div>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img src="@/assets/images/phone.png" alt="" class="inputImg" />
            </div>
            <input
              v-model="phone"
              type="tel"
              placeholder="Enter Your Phone Number"
            />
          </div>
          <div class="inputDiv transparentBG">
            <div class="innerDiv">
              <div class="inputImgCont">
                <img src="@/assets/images/dob.png" alt="" class="inputImg" />
              </div>
              <input
                v-model="dob"
                type="date"
                placeholder="Enter Your Date of Birth"
              />
            </div>
            <div class="innerDiv">
              <div class="inputImgCont">
                <img src="@/assets/images/gender.png" alt="" class="inputImg" />
              </div>
              <select v-model="gender" class="genderDrop">
                <option value="Male" selected>Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
          </div>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img
                src="@/assets/images/password_icon.png"
                alt=""
                class="inputImg"
              />
            </div>
            <input
              v-model="password"
              placeholder="Enter Your Password"
              :type="passwordView ? 'text' : 'password'"
              style="width: 14rem"
            />
            <div class="inputImgCont" @click="passwordViewer()">
              <img
                src="@/assets/images/password_view.png"
                alt=""
                class="inputImg"
                ref="viewer"
              />
            </div>
          </div>
          <p class="changeSign" @click="changeView()">
            Have an account already? Sign In Now?
          </p>
          <div class="continue" @click="submit()">Continue →</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UserSignin",
  data() {
    return {
      username: "",
      password: "",
      email: "",
      dob: "",
      phone: "",
      gender: "",
      passwordView: false,
      signinView: true,
      message: "",
    };
  },
  methods: {
    setUserID(user_id) {
      this.$store.dispatch("updateUserID", user_id);
    },
    passwordViewer() {
      this.passwordView = !this.passwordView;
      if (this.passwordView) {
        this.$refs.viewer.style.filter = "grayscale(100%) brightness(0.5)";
      } else {
        this.$refs.viewer.style.filter = "none";
      }
    },
    changeView() {
      this.username = "";
      this.password = "";
      this.email = "";
      this.dob = "";
      this.phone = "";
      this.gender = "";
      this.signinView = !this.signinView;
    },
    async submit() {
      if (this.signinView) {
        if (this.username != "" && this.password != "") {
          const response = await axios.post("http://192.168.1.3:5000/signin", {
            user_name: this.username,
            password: this.password,
          });
          if (response.data.code != 801) {
            this.message = response.data.message;
          } else {
            localStorage.setItem("token", response.data.token);
            axios
              .get(
                `http://192.168.1.3:5000/get-content/users?user_name=${this.username}&password=${this.password}`,
                {
                  headers: {
                    "x-access-token": response.data.token,
                  },
                }
              )
              .then((responsible) => {
                // const queryParams = new URLSearchParams({
                //   userId: responsible.data[0].user_id,
                // });
                window.location.href = `/home`;
                localStorage.setItem("user_id", responsible.data[0].user_id);
                localStorage.setItem("user_gender", responsible.data[0].gender);
              })
              .catch(() => {
                alert("There was an unexpected error.");
              });
          }
        } else {
          alert(
            "Please fill in both the Username and Password fields to proceed."
          );
        }
      } else {
        if (
          this.username != "" &&
          this.password != "" &&
          this.email != "" &&
          this.dob != "" &&
          this.phone != "" &&
          this.gender != "" &&
          this.email.includes("@")
        ) {
          const response = await axios.post("http://192.168.1.3:5000/signup", {
            user_name: this.username,
            password: this.password,
            phone: this.phone,
            email: this.email,
            dob: this.dob,
            gender: this.gender,
          });
          if (response.data.code == 805) {
            this.signinView = !this.signinView;
            this.message = response.data.message;
          } else if (response.data.code == 801) {
            axios
              .get(
                `http://192.168.1.3:5000/get-content/users?user_name=${this.username}&password=${this.password}`,
                {
                  headers: {
                    "x-access-token": localStorage.getItem("token"),
                  },
                }
              )
              .then((responsible) => {
                localStorage.setItem("user_id", responsible.data[0].user_id);
                localStorage.setItem("user_gender", responsible.data[0].gender);
                window.location.href = "/home";
              })
              .catch(() => {
                alert("There was an unexpected error.");
              });
          }
        } else {
          if (!this.email.includes("@")) {
            alert("Please enter a valid email id.");
          }
          alert("Please fill in all the fields to proceed.");
        }
      }
    },
    formatDate(dateString) {
      const [day, month, year] = dateString.split("-");
      return `${year}-${month.padStart(2, "0")}-${day.padStart(2, "0")}`;
    },
  },
};
</script>

<style scoped>
.baseRoot {
  height: 45.6rem;
  width: 100%;
  background: url("@/assets/images/signin_bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}
.navbar {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 5.5rem;
}
.signinMainFrame {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40.1rem;
  width: 100%;
}
.logoContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
  width: 4rem;
  margin: 0rem 1rem;
  background-color: #25352b;
  /* background: linear-gradient(90deg, #d8ba86, #c2913b); */
  border-radius: 40rem;
}
.logoImg {
  height: 65%;
  width: 65%;
  /* filter: brightness(100); */
}
.logoText {
  margin-top: 0.5rem;
  font-size: 1.8rem;
  letter-spacing: 8px;
  font-family: "Insomnia";
  font-weight: 900;
  color: #25352b;
}
.signinBox {
  display: flex;
  height: 35rem;
  width: 60rem;
  border-radius: 0.25rem;
}
.info {
  display: flex;
  flex-direction: column;
  padding: 1rem;
  width: 50%;
  height: 100%;
  background-color: white;
}
.desk {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1rem;
  width: 50%;
  height: 100%;
  backdrop-filter: blur(30px);
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-left: 0rem;
}
.welcome {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: rgb(72, 72, 72);
  text-align: center;
}
.title {
  font-family: "Insomnia";
  font-size: 3rem;
  letter-spacing: 15px;
  font-weight: 900;
  color: #25352b;
  margin: 1.3rem 0rem;
  text-align: center;
}
.description {
  text-align: center;
  font-size: 0.8rem;
  margin-top: 3rem;
}
.stats {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 8rem;
  width: 100%;
  margin: 2rem 0rem;
}
.statCard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 30%;
  height: 7rem;
}
.upperCont {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
.imgCont {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.7rem;
  background-color: #25352b;
  border-radius: 10rem;
  height: 4rem;
  width: 4rem;
  margin: 0rem 1rem;
}
.img {
  height: 80%;
  width: auto;
}
.statInfo {
  text-align: center;
  line-height: 1rem;
  margin: 0.5rem;
  height: 3rem;
  font-size: 0.8rem;
}
.join {
  text-align: center;
  margin: 1rem 0rem;
  font-size: 2rem;
  font-weight: 700;
  letter-spacing: 8px;
}
.signHead {
  text-align: center;
  color: #25352b;
  margin: 0.5rem 0rem;
  font-size: 2rem;
  font-weight: 600;
  margin-bottom: 2rem;
}
.inputDiv {
  display: flex;
  flex-direction: row;
  width: 20rem;
  height: 3rem;
  background-color: white;
  border-radius: 0.25rem;
  margin-bottom: 1rem;
}
.inputImgCont {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 3rem;
  height: 3rem;
  background-color: white;
  cursor: pointer;
}
.inputImg {
  height: 50%;
  width: auto;
}
.inputDiv input {
  width: 17rem;
  height: 3rem;
  outline: none;
  border: 0rem;
  padding: 0rem 0.5rem;
}
.changeSign {
  font-size: 0.75rem;
  font-weight: 500;
  color: #e6ac45;
  cursor: pointer;
  border-bottom: 0rem;
}
.changeSign:hover {
  border-bottom: 2px solid #e6ac45;
}
.continue {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem;
  margin: 1.5rem;
  width: 10rem;
  height: 3rem;
  font-weight: 600;
  letter-spacing: 1px;
  color: #e6ac45;
  background-color: white;
  border-radius: 0.25rem;
  cursor: pointer;
}
.message {
  color: white;
  text-align: center;
}
.innerDiv {
  display: flex;
  height: 100%;
  border-radius: 0.25rem;
}
.innerDiv:first-child {
  width: 14rem;
  margin-right: 1rem;
}
.innerDiv:last-child {
  width: 8.15rem;
}
.innerDiv input {
  width: 12.35rem;
  font-size: 0.8rem;
}
.innerDiv select {
  width: 5.15rem;
}
.transparentBG {
  background-color: transparent;
}
.genderDrop {
  outline: none;
  border: none;
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}
</style>
