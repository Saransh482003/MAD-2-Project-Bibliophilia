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
    meta: {
      title: "Bibliophilia - Something went wrong",
    },
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
    meta: {
      title: "Bibliophilia : A Library of Dreams",
    },
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,
    meta: {
      title: "Bibliophilia - About Us",
    },
  },
  {
    path: "/my-books",
    name: "my-books",
    component: MyBooksView,
    meta: {
      title: "Bibliophilia - Your Books",
    },
  },
  {
    path: "/librarian",
    name: "librarian",
    component: LibrarianView,
    meta: {
      title: "Bibliophilia - Librarian Control Panel",
    },
  },
  {
    path: "/",
    name: "signin",
    component: UserSignin,
    meta: {
      title: "Bibliophilia - User Signin",
    },
  },
  {
    path: "/librarian-signin",
    name: "librarian-signin",
    component: LibrarianSignin,
    meta: {
      title: "Bibliophilia - Librarian Signin",
    },
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});
router.beforeEach((to, from, next) => {
  Vue.nextTick(() => {
    document.title = to.meta.title || "Bibliophilia : A Library of Dreams";
  });
  next();
});

export default router;
