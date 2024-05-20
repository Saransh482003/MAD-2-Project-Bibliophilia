<template>
  <div class="footer">
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
    <div class="footerContent">Copyright © 2024 bibliophilia.com</div>
  </div>
</template>

<script>
export default {
  name: "AppFooter",
};
</script>

<style scoped>
.footer {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 5.5rem;
}
.logo {
  display: flex;
  align-items: center;
  width: 23%;
}
.logoContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 4rem;
  width: 4rem;
  margin: 0rem 1rem;
  background-color: #25352b;
  border-radius: 40rem;
}
.logoImg {
  height: 65%;
  width: 65%;
}
.logoText {
  margin-top: 0.5rem;
  font-size: 1.8rem;
  letter-spacing: 8px;
  font-family: "Insomnia";
  font-weight: 900;
  color: #25352b;
}
.footerContent {
  display: flex;
  justify-content: start;
  align-items: center;
  width: 80%;
  height: 65%;
  padding-left: 2rem;
  border-left: 2px rgb(112, 112, 112) solid;
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
  box-shadow: 0 0.25rem 1rem #00000026;
}
.profilePic {
  height: 65%;
  width: 65%;
}
</style>
