<template>
  <div class="middle">
    <SideNav @changeLibrarianView="changeMiddleView" page="librarian" />

    <div class="mainPanel" v-if="changeView == 1">Dashboard</div>
    <div class="mainPanel" v-if="changeView == 2">Search</div>
    <div class="mainPanel" v-if="changeView == 3">Issue Requests</div>
    <div class="mainPanel" v-if="changeView == 4">Issue Logs</div>
    <div class="mainPanel withPreview" v-if="changeView == 5">
      <div v-for="(book, index) in books" :key="index" class="card myCard">
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
        <div class="actions">
          <div class="actionBtns" @click="readBook(book.book_id)">
            <img
              src="@/assets/images/delete-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Delete
          </div>
          <div
            class="actionBtns sideBtn"
            @click="changePreviewBook(book.book_id)"
          >
            <img
              src="@/assets/images/edit-icon.png"
              alt=""
              class="actionBtnImg"
            />
            Edit
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 5">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer">
          <img :src="previewBook.book.img" alt="" class="imgContainer" />
        </div>
        <p class="previewTitle">{{ previewBook.book.book_name }}</p>

        <div class="majorDetails">
          <p>
            AUTHOR: <span>{{ previewBook.book.author_name }}</span>
          </p>
          <p>
            GENRE: <span>{{ previewBook.book.genre }}</span>
          </p>
          <p>
            DESCRIPTION:<br />
            <span
              >Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate repellendus quae similique natus in blanditiis
              doloribus facer?</span
            >
          </p>
        </div>
        <div class="bookStats"></div>
      </div>
    </div>
    <div class="mainPanel" v-if="changeView == 6">Section Management</div>
    <div class="mainPanel" v-if="changeView == 7">User Management</div>
  </div>
</template>

<script>
import axios from "axios";
import SideNav from "@/components/SideNav.vue";
export default {
  components: { SideNav },
  name: "LibrarianView",
  data() {
    return {
      searchBooks: [],
      books: [],
      sections: [],
      authors: [],
      genres: [],
      previewBook: {},
      changeView: 1,
    };
  },
  created() {
    this.changeView = 1;
  },
  methods: {
    changeMiddleView(view) {
      this.changeView = view;
      if (view == 5) {
        this.fetchMyBooks();
      }
    },
    fetchMyBooks() {
      axios
        .get("http://127.0.0.1:5000/get-content/books")
        .then((response) => {
          this.books = response.data;
          this.changePreviewBook(this.books[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    changePreviewBook(book_id) {
      axios
        .get(
          `http://127.0.0.1:5000/get-librarian/previewBook?book_id=${book_id}`
        )
        .then((response) => {
          this.previewBook = response.data;
          this.previewBook.avg_rating = this.previewBook.avg_rating.toFixed(1);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    shortenText(text) {
      if (text.length > 35) {
        return `${text.substring(0, 35)}...`;
      } else {
        return text;
      }
    },
    formatDateToDDMMYYYY(timestamp) {
      const date = new Date(timestamp);
      const day = String(date.getDate()).padStart(2, "0");
      const monthNames = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      const month = monthNames[date.getMonth()];
      const year = date.getFullYear();
      return `${day} ${month} ${year}`;
    },
  },
};
</script>

<style scoped>
.middle {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  width: 100%;
  height: 40.1rem;
  background: url("@/assets/images/biblio_bg.jpg");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
}
.mainPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 95%;
  height: 100%;
  padding-bottom: 1.4rem;
  padding-top: 0.7rem;
  overflow: hidden;
  overflow-y: scroll;
}
.withPreview {
  width: 75%;
}
.previewPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 20%;
  height: 100%;
  background: url("https://thumbs.dreamstime.com/b/paper-texture-1847313.jpg");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
}
.previewDetailsContainer {
  display: block;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  width: 100%;
  height: 91%;
  padding: 1rem 1.5rem;
  overflow: hidden;
  overflow-y: scroll;
}
.card {
  display: flex;
  flex-direction: column;
  height: 20rem;
  width: 15rem;
  cursor: pointer;
  margin: 0.7rem 1.4rem;
  border-radius: 0.3rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  transition: all 0.2s ease;
  background-color: white;
}
.card:hover {
  height: 21rem;
  width: 16rem;
  margin: 0.2rem 0.9rem;
}
.myCard {
  height: 23rem;
  z-index: 1;
}
.myCard:hover {
  height: 24rem;
}
.bookImgContainer {
  display: flex;
  justify-content: center;
  height: 70%;
  width: 100%;
  overflow: hidden;
}
.bookTitle {
  transition: all 0.2s ease;
  line-height: 20px;
  margin-bottom: 0.5rem;
}
.bookImg {
  height: 100%;
  width: auto;
}
.bookContent {
  height: 30%;
  padding: 0.5rem 1rem;
  transition: all 0.2s ease;
}
.bookDetails {
  display: flex;
  transition: all 0.2s ease;
}
.bookAuthor {
  width: 100%;
  font-size: 0.7rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  transition: all 0.2s ease;
}
.bookAuthor span {
  font-weight: 500;
  transition: all 0.2s ease;
}
.actions {
  display: flex;
  width: 100%;
  height: 3rem;
  background-color: #25352b;
  z-index: 3;
}
.actionBtns {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #e6ac45;
  width: 50%;
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}
.actionBtnImg {
  height: 1.3rem;
  width: auto;
  margin-right: 0.2rem;
  transition: all 0.2s ease;
}
.sideBtn {
  background-color: white;
}
.previewImgContainer {
  display: flex;
  justify-content: center;
  height: 20rem;
  width: 100%;
  position: relative;
}
.downloadPDFContainer {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: end;
  z-index: 1;
}
.downloadPDF {
  display: flex;
  height: 2rem;
  width: 2rem;
  padding: 0.4rem;
  border-radius: 30rem;
  margin-bottom: 0.8rem;
  background-color: white;
  position: relative;
  cursor: pointer;
  box-shadow: 0 0.25rem 1rem #00000026;
  z-index: 2;
  transition: all 0.2s ease;
}
.downloadPDF:hover {
  background-color: #25352b;
}
.downloadPDF:hover .pdfIcon {
  filter: none;
}
.pdfIcon {
  width: 100%;
  height: 100%;
  filter: grayscale(100%) brightness(0);
}
.imgContainer {
  height: 100%;
  width: auto;
}
.previewTitle {
  margin-top: 1rem;
  line-height: 20px;
}
.majorDetails {
  height: max-content;
  width: 100%;
  margin: 1rem 0rem;
}
.majorDetails p {
  font-size: 0.7rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  letter-spacing: 1px;
}
.majorDetails span {
  font-weight: 500;
  letter-spacing: 0rem;
}
.bookStats {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 3rem;
  background-color: aqua;
}
</style>
