import Vue from "vue";
import VueRouter from "vue-router";
import ErrorPage from "../views/ErrorPage.vue";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import MyBooksView from "../views/MyBooksView.vue";
import LibrarianView from "../views/LibrarianView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/error",
    name: "error",
    component: ErrorPage,
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
  },
  {
    path: "/my-books",
    name: "my-books",
    component: MyBooksView,
  },
  {
    path: "/librarian",
    name: "librarian",
    component: LibrarianView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
