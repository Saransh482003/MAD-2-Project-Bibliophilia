<template>
  <div class="middle">
    <div class="sideNav"></div>
    <div class="mainPanel">
      <div v-for="(book, index) in books" :key="index" class="card">
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            AUTHOR: <span>{{ book.author_id }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
      </div>
    </div>
    <div class="previewPanel">code</div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      books: [],
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      axios
        .get("http://127.0.0.1:5000/get-content/books")
        .then((response) => {
          this.books = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    shortenText(text) {
      if (text.length > 40) {
        return `${text.substring(0, 40)}...`;
      } else {
        return text;
      }
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
  /* background-color: aqua; */
}
.sideNav {
  display: flex;
  flex-direction: column;
  width: 5%;
  height: 100%;
  background-color: black;
}
.mainPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 75%;
  height: 100%;
  padding-bottom: 1.5rem;
  overflow: hidden;
  overflow-y: scroll;
}
.previewPanel {
  display: flex;
  flex-direction: column;
  width: 20%;
  background-color: beige;
}
.card {
  display: flex;
  flex-direction: column;
  height: 20rem;
  width: 15rem;
  /* background-color: aquamarine; */
  margin: 1.3rem;
  margin-bottom: 0rem;
  border-radius: 0.3rem;
  box-shadow: 0 0.25rem 1rem #00000026;
}
.bookImgContainer {
  display: flex;
  justify-content: center;
  overflow: hidden;
  height: 70%;
  width: 100%;
}
.bookImg {
  height: 100%;
  width: auto;
}
.bookContent {
  height: 30%;
  padding: 0.5rem 1rem;
}
.bookDetails {
  display: flex;
}
.bookAuthor {
  width: 100%;
  font-size: 0.7rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
}
.bookAuthor span {
  font-weight: 500;
}
</style>
