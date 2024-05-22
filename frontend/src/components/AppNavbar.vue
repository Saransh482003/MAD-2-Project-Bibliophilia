<template>
  <div class="navbar">
    <router-link to="/" class="logo">
      <div class="logoContainer">
        <img
          src="@/assets/images/Oak Png.png"
          alt="The Oak Tree"
          class="logoImg"
        />
      </div>
      <p class="logoText">Bibliophilia</p>
    </router-link>
    <div class="navLinks">
      <router-link to="/home" class="link">Home</router-link>
      <router-link to="/about" class="link">About</router-link>
      <router-link to="/my-books" class="link">My Books</router-link>
      <div class="profile">
        <img
          v-if="gender == 'male'"
          src="@/assets/images/male profile.png"
          alt="username"
          class="profilePic"
        />
        <img
          v-else
          src="@/assets/images/female profile.png"
          alt="username"
          class="profilePic"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppNavbar",
  props: {
    gender: {
      type: String,
      required: false,
      default: "male",
    },
  },
};
</script>

<style scoped>
.navbar {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 5.5rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  /* background-color: aqua; */
}
.logo {
  display: flex;
  align-items: center;
  width: 25%;
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
.navLinks {
  display: flex;
  justify-content: end;
  align-items: center;
  width: 80%;
  height: 100%;
}
.profile {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
  width: 4rem;
  margin: 0rem 1rem;
  background-color: white;
  border-radius: 40rem;
  cursor: pointer;
  box-shadow: 0 0.25rem 1rem #00000026;
}
.profile:hover .profilePic {
  height: 73%;
  width: 73%;
}
.profilePic {
  height: 65%;
  width: 65%;
  transition: all 0.2s ease;
}
.link {
  font-size: 1.2rem;
  margin: 0rem 1.5rem;
  text-decoration: none;
  color: black;
  transition: all 0.1s ease;
}
.link:hover {
  padding-bottom: 5px;
  border-bottom: 3px solid #25352b;
}
</style>
