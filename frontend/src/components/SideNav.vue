<template>
  <div class="sideNav">
    <div class="sideNavInner" v-if="page == 'home'">
      <div class="navBtns" @click="emitChangeMiddleView(2)" id="nav2">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/search_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Search</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(1)" id="nav1">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/home_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Home</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(3)" id="nav3">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/books_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">All Books</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(4)" id="nav4">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/section_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">All Sections</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(5)" id="nav5">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/latest_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Latest Books</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(6)" id="nav6">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/author_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">All Authors</p>
      </div>
      <div class="navBtns" @click="emitChangeMiddleView(7)" id="nav7">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/genre_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">All Genres</p>
      </div>
    </div>
    <div class="sideNavInner" v-else-if="page == 'my-books'">
      <div class="navBtns" @click="emitChangeMyBooksView(2)" id="nav2">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/search_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Search</p>
      </div>
      <div class="navBtns" @click="emitChangeMyBooksView(1)" id="nav1">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/my_books_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">My Books</p>
      </div>
      <div class="navBtns" @click="emitChangeMyBooksView(3)" id="nav3">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/stats_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Dashboard</p>
      </div>
      <div class="navBtns" @click="emitChangeMyBooksView(4)" id="nav4">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/feedback_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Feedbacks</p>
      </div>
    </div>
    <div class="sideNavInner" v-else-if="page == 'librarian'">
      <div class="navBtns" @click="emitChangeLibrarianView(2)" id="nav2">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/search_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Search</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(1)" id="nav1">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/stats_icon.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Dashboard</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(3)" id="nav3">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/important_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Issue Requests</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(4)" id="nav4">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/current_issue.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Issue Logs</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(5)" id="nav5">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/books_managament_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Book Management</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(6)" id="nav6">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/section_management_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Section Management</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(7)" id="nav7">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/author_management_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">Author Management</p>
      </div>
      <div class="navBtns" @click="emitChangeLibrarianView(8)" id="nav8">
        <div class="navBtnImgContainer">
          <img
            src="@/assets/images/user_management_icon.png"
            alt=""
            class="navBtnImg"
          />
        </div>
        <p class="navBtnsText">User Management</p>
      </div>
    </div>
    <div class="sideNavInner" v-else-if="page == 'read-book'">
      <div class="navBtns" @click="goBack()" id="nav2">
        <div class="navBtnImgContainer">
          <img src="@/assets/images/back.png" alt="" class="navBtnImg" />
        </div>
        <p class="navBtnsText">Go Back</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SideNav",
  props: {
    page: {
      type: String,
      required: true,
      default: "home",
    },
  },
  methods: {
    emitChangeMiddleView(view) {
      this.$emit("changeView", view);

      let navs = document.getElementsByClassName("navBtns");
      Array.from(navs).forEach((element) => {
        element.classList.remove("selected");
      });

      let nav = document.getElementById(`nav${view}`);
      nav.classList.add("selected");
    },
    emitChangeMyBooksView(view) {
      this.$emit("changeMyBookView", view);

      let navs = document.getElementsByClassName("navBtns");
      Array.from(navs).forEach((element) => {
        element.classList.remove("selected");
      });

      let nav = document.getElementById(`nav${view}`);
      nav.classList.add("selected");
    },
    emitChangeLibrarianView(view) {
      this.$emit("changeLibrarianView", view);

      let navs = document.getElementsByClassName("navBtns");
      Array.from(navs).forEach((element) => {
        element.classList.remove("selected");
      });

      let nav = document.getElementById(`nav${view}`);
      nav.classList.add("selected");
    },
    goBack() {
      window.location.href = "/my-books";
    },
  },
};
</script>

<style scoped>
.sideNav {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  width: 5%;
  height: 100%;
  padding: 1rem 0rem;
  z-index: 5;
  background: linear-gradient(180deg, #25352b, black);
}
.sideNavInner {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  width: 100%;
}
.navBtns {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 4rem;
  width: 100%;
  padding: 0.3rem 0.2rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
}
.navBtnImgContainer {
  display: flex;
  justify-content: center;
  width: 100%;
  height: max-content;
  /* padding: 0.1rem; */
  margin-bottom: 0.3rem;
}
.navBtns:hover {
  background-color: rgba(0, 0, 0, 0.5);
  border-left: 5px solid #e6ac45;
  border-right: 5px solid transparent;
}
.navBtnImg {
  height: 1.5rem;
  width: auto;
  filter: grayscale(100%) brightness(1000);
}
.navBtnsText {
  font-size: 0.5rem;
}
.navBtns:hover .navBtnImg {
  filter: none;
}
.navBtnsText {
  text-align: center;
  width: 100%;
}
.selected {
  background-color: rgba(0, 0, 0, 0.5);
  border-left: 5px solid #e6ac45;
  border-right: 5px solid transparent;
}
.selected img {
  filter: none;
}
</style>
