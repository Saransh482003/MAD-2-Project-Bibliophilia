<template>
  <div class="middle">
    <div class="sideNav"></div>
    <div class="mainPanel">
      <div
        v-for="(book, index) in books"
        :key="index"
        class="card"
        @click="changePreviewBook(book.book_id)"
      >
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
    <div class="previewPanel">
      <div class="previewImgContainer">
        <img :src="previewBook.img" alt="" class="imgContainer" />
        <div class="downloadPDFContainer">
          <a class="downloadPDF" :href="previewBook.book_id">
            <img
              src="@/assets/images/download icon.png"
              :alt="previewBook.book_name"
              class="pdfIcon"
            />
          </a>
        </div>
      </div>
      <div class="titleAndRating">
        <p class="previewTitle">{{ previewBook.book_name }}</p>
        <div class="ratingStar">
          <img
            src="@/assets/images/star.png"
            alt="Star"
            class="star"
            v-for="(star, index) in previewBook.book_avg_rating"
            :key="index"
          />
          <img
            src="@/assets/images/hollow star.png"
            alt="Star"
            class="star"
            v-for="(star, index) in 5 - previewBook.book_avg_rating"
            :key="index"
          />
        </div>
      </div>
      <div class="majorDetails">
        <p>
          AUTHOR: <span>{{ previewBook.author_name }}</span>
        </p>
        <p>
          GENRE: <span>{{ previewBook.genre }}</span>
        </p>
        <p>
          DESCRIPTION:<br />
          <span
            >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eius,
            non? Quo ex, non doloremque molestias adipisci eius vel ab
            praesentium, omnis sapiente quos aspernatur! Modi nemo officiis
            omnis ea distinctio non nisi?Lorem ipsum dolor sit, amet consectetur
            adipisicing elit. Cum placeat excepturi itaque voluptas, illum, nam
            pariatur aliquam vitae, obcaecati quod hic nostrum? Asperiores
            necessitatibus natus magnam aut quae, distinctio nulla
            exercitationem iste eligendi, aliquam libero! Facere quidem labore
            esse possimus iste facilis ducimus, reprehenderit magnam numquam
            tempora tenetur eveniet adipisci deserunt, veniam itaque recusandae
            totam consequuntur dolor assumenda fuga at officiis culpa enim?
            Totam debitis, qui dolore illo perspiciatis vel quia nulla, rerum
            tempora incidunt, officia dolores aliquid tenetur eum!</span
          >
        </p>
      </div>
      <div class="aboutAuthor">
        <div class="authorProfile">
          <img :src="previewBook.author_img" alt="" class="profilePic" />
          <div class="profileDetails">
            <p class="profileDetailsName">{{ previewBook.author_name }}</p>
            <p class="profileDetailsName">
              {{ previewBook.dob }} - {{ previewBook.dod }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      books: [],
      previewBook: {},
    };
  },
  created() {
    this.fetchBooks();
  },
  methods: {
    changePreviewBook(book_id) {
      axios
        .get(`http://127.0.0.1:5000/get-content/recent-book?book_id=${book_id}`)
        .then((response) => {
          this.previewBook = response.data;
          if (Math.floor(this.previewBook.book_avg_rating) == 0) {
            this.previewBook.book_avg_rating =
              Math.floor(Math.random() * 5) + 1;
          }
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchBooks() {
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
    shortenText(text) {
      if (text.length > 35) {
        return `${text.substring(0, 35)}...`;
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
  padding-bottom: 1.4rem;
  padding-top: 0.7rem;
  overflow: hidden;
  overflow-y: scroll;
}
.previewPanel {
  display: flex;
  flex-direction: column;
  width: 20%;
  flex-wrap: wrap;
  overflow-y: scroll;
  padding: 1rem 1.5rem;
  background-color: #fff6e6;
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
}
.card:hover {
  height: 21rem;
  width: 16rem;
  margin: 0.2rem 0.9rem;
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

.previewImgContainer {
  display: flex;
  justify-content: center;
  height: 20rem;
  width: 100%;
  position: relative;
  /* background-color: aqua; */
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
  padding: 0.2rem;
  border-radius: 30rem;
  margin-bottom: 0.8rem;
  background-color: white;
  position: relative;
  cursor: pointer;
  box-shadow: 0 0.25rem 1rem #00000026;
  z-index: 2;
}
.pdfIcon {
  width: 100%;
  height: 100%;
}
.imgContainer {
  height: 100%;
  width: auto;
}
.previewTitle {
  margin-top: 1rem;
  line-height: 20px;
}
.ratingStar {
  display: flex;
  height: 1.3rem;
  width: 100%;
  margin: 0.5rem 0rem;
  /* justify-content: center; */
}
.star {
  margin-right: 0.4rem;
}
.majorDetails {
  height: max-content;
  width: 100%;
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
.titleAndRating {
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>
