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
      <p class="logoText">Bibliophilia<span>LIBRARIAN</span></p>
    </div>
    <div class="signinMainFrame">
      <div class="signinBox">
        <div class="info">
          <p class="welcome">Welcome back to</p>
          <p class="title">Bibliophilia</p>
          <p class="description">
            Librarians are like search engines, but they smile and talk to you,
            and they don't track your searches.
            <span>~ Sun Tzu (probably)</span>
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
              <div class="statInfo">50K + <br />Books</div>
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
              <div class="statInfo">25K + <br />Authors</div>
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
          <p class="join">GET READY !!</p>
        </div>
        <div class="desk">
          <p class="signHead">Sign In</p>
          <div class="inputDiv">
            <div class="inputImgCont">
              <img
                src="@/assets/images/user_icon.png"
                alt=""
                class="inputImg"
              />
            </div>
            <input v-model="username" placeholder="Enter Your Librarian Key" />
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
          <div class="continue" @click="submit()">Continue →</div>
          <p class="message" v-if="message != ''">{{ message }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios";
export default {
  name: "LibrarianSignin",
  data() {
    return {
      username: "",
      password: "",
      passwordView: false,
      message: "",
    };
  },
  mounted() {
    localStorage.clear();
  },
  methods: {
    passwordViewer() {
      this.passwordView = !this.passwordView;
      if (this.passwordView) {
        this.$refs.viewer.style.filter = "grayscale(100%) brightness(0.5)";
      } else {
        this.$refs.viewer.style.filter = "none";
      }
    },
    async submit() {
      if (this.username != "" && this.password != "") {
        const response = await axios.post("/librarian-signin", {
          user_name: this.username,
          password: this.password,
        });
        if (response.data.code != 801) {
          this.message = response.data.message;
        } else {
          localStorage.setItem("librarian-token", response.data.token);
          localStorage.setItem("token", response.data.token);
          window.location.href = "/librarian";
        }
      } else {
        alert(
          "Please fill in both the Username and Password fields to proceed."
        );
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
  background: url("https://wallpapercrafter.com/desktop/66717-firewatch-games-artist-digital-art.jpg");
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
.logoText span {
  font-size: 0.8rem;
  letter-spacing: 1px;
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
.description span {
  font-style: italic;
  color: rgb(72, 72, 72);
  font-size: 0.7rem;
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
