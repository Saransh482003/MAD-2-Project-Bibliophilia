<template>
  <div id="app">
    <AppNavbar :gender="gender" v-if="!no_nav.includes($route.name)" />
    <LibrarianNavbar
      v-else-if="$route.name !== 'signin' && $route.name !== 'librarian-signin'"
    />
    <router-view />
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
// import axios from "@/axios";
import AppNavbar from "./components/AppNavbar.vue";
import LibrarianNavbar from "./components/LibrarianNavbar.vue";
export default {
  name: "App",
  components: {
    AppNavbar,
    LibrarianNavbar,
  },
  data() {
    return {
      no_nav: ["librarian", "signin", "librarian-signin"],
      gender: "Male",
    };
  },

  beforeMount() {
    this.gender = localStorage.getItem("user_gender");
  },
};
</script>
