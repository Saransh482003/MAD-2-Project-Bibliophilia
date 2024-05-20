<template>
  <div id="app">
    <AppNavbar gender="male" />
    <router-view />
    <!-- <AppFooter /> -->
  </div>
</template>

<style>
* {
  padding: 0rem;
  margin: 0rem;
  box-sizing: border-box;
  text-decoration: none;
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}
@font-face {
  font-family: "Insomnia";
  src: url("@/assets/fonts/Fantastica.ttf") format("truetype");
}
@font-face {
  font-family: "Poppins";
  src: url("@/assets/fonts/Poppins.ttf") format("truetype");
}
::-webkit-scrollbar {
  width: 10px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 2rem;
}
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>

<script>
import AppNavbar from "./components/AppNavbar.vue";
// import AppFooter from "./components/AppFooter.vue";
export default {
  name: "App",
  components: {
    AppNavbar,
    // AppFooter,
  },
};
</script>
