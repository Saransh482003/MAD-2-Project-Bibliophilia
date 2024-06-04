import Vue from "vue";
import VueRouter from "vue-router";
import ErrorPage from "../views/ErrorPage.vue";
import HomeView from "../views/HomeView.vue";
import AboutView from "../views/AboutView.vue";
import MyBooksView from "../views/MyBooksView.vue";
import LibrarianView from "../views/LibrarianView.vue";
import UserSignin from "../views/UserSignin.vue";
import LibrarianSignin from "../views/LibrarianSignin.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/error",
    name: "error",
    component: ErrorPage,
  },
  {
    path: "/home",
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
  {
    path: "/",
    name: "signin",
    component: UserSignin,
  },
  {
    path: "/librarian-signin",
    name: "librarian-signin",
    component: LibrarianSignin,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
