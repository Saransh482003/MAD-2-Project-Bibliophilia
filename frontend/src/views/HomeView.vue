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
            >Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate
            repellendus quae similique natus in blanditiis doloribus facere et
            a? Alias excepturi quasi sapiente, aut ea fuga enim iusto doloribus,
            recusandae, soluta neque dolores reiciendis? Ex repellat eius
            deleniti molestiae? Enim pariatur illo impedit totam corrupti
            repudiandae, aliquid assumenda obcaecati veniam.</span
          >
        </p>
      </div>
      <div class="aboutAuthor">
        <p class="authorDesc boldTitle">ABOUT THE AUTHOR</p>
        <div class="authorProfile">
          <div class="profilePicContainer">
            <img :src="previewBook.author_img" alt="" class="profilePic" />
          </div>
          <div class="profileDetails">
            <p class="profileDetailsName">
              {{ previewBook.author_name }}
            </p>
            <p class="profileDetailsDate">
              {{ previewBook.dob }} - {{ previewBook.dod }}
            </p>
          </div>
        </div>
        <p class="authorDesc">
          {{ previewBook.author_name }} is an acclaimed author from
          {{ previewBook.country }}. Born on {{ previewBook.dob }}, they have
          captured the hearts of many readers with their outstanding works in
          the genre of {{ previewBook.genre }}. Their books have an average
          rating of {{ previewBook.author_avg_rating }}, reflecting their talent
          and dedication to literature.
        </p>
      </div>
      <div class="aboutAuthor">
        <p class="authorDesc boldTitle">FEEDBACKS</p>
        <div class="feedbacks">
          <div
            class="userFeedback"
            v-for="(user, index) in previewBook.ratings"
            :key="index"
          >
            <div class="userDetails">
              <div class="userPicContainer">
                <img
                  v-if="user.gender == 'Male'"
                  src="@/assets/images/male profile.png"
                  :alt="user.user_name"
                  class="userPic"
                />
                <img
                  v-else
                  src="@/assets/images/female profile.png"
                  :alt="user.user_name"
                  class="userPic"
                />
              </div>
              <div class="userProfileDetails">
                <p>
                  {{ user.user_name }}
                </p>
                <div class="userRating">
                  <p style="line-height: 10px; margin-top: 2px">
                    {{ user.book_avg_rating }}
                  </p>
                  <img src="@/assets/images/star.png" alt="Star" class="star" />
                </div>
              </div>
            </div>
            <p class="authorDesc">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Consectetur explicabo voluptatibus, exercitationem architecto
              corrupti vitae cum. Architecto neque sit voluptas?
            </p>
          </div>
        </div>
      </div>
      <div class="actions">
        <div class="actionBtns">Request</div>
        <div class="actionBtns">Save</div>
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
          console.log(this.previewBook);
          this.previewBook.dob = this.formatDateToDDMMYYYY(
            Date.parse(response.data.dob)
          );
          this.previewBook.dod = this.formatDateToDDMMYYYY(
            Date.parse(response.data.dod)
          );
          this.previewBook.author_avg_rating =
            this.previewBook.author_avg_rating.toFixed(1);
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
  /* background-color: aqua; */
}
.sideNav {
  display: flex;
  flex-direction: column;
  color: white;
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
  flex-wrap: wrap;
  justify-content: center;
  width: 20%;
  height: 100%;
  padding: 1rem 1.5rem;
  overflow: hidden;
  overflow-y: scroll;
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
  background-color: rgb(0, 129, 6);
  /* padding: 0.35rem; */
}
.downloadPDF:hover .pdfIcon {
  filter: grayscale(100%) brightness(100);
}
.pdfIcon {
  width: 100%;
  height: 100%;
  /* transition: all 0.2s ease; */
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
  margin: 0.8rem 0rem;
  /* justify-content: center; */
}
.star {
  margin-right: 0.4rem;
}
.majorDetails {
  height: max-content;
  width: 100%;
  margin-bottom: 1rem;
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
.authorProfile {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: max-content;
  width: 100%;
  margin: 0.5rem 0rem;
}
.profilePicContainer {
  display: flex; /* Use flexbox */
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  width: 7rem;
  height: 4.6rem; /* Ensure it takes up the full height of its parent */
  margin-right: 0.5rem;
  overflow: hidden;
  background-color: aqua;
  border-radius: 30rem;
  /* box-shadow: 0 0.25rem 1rem #00000026; */
}
.profileDetails {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.profilePic {
  height: 100%;
  width: auto;
  object-fit: cover;
}
.profileDetailsName {
  font-size: 0.95rem;
  font-weight: 700;
}
.profileDetailsDate {
  font-size: 0.6rem;
  font-weight: 500;
}
.authorDesc {
  font-size: 0.7rem;
  color: rgb(61, 61, 61);
}
.aboutAuthor {
  margin-bottom: 1rem;
}
.boldTitle {
  font-weight: 700;
}
.feedBacks {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: max-content;
}
.userFeedback {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: max-content;
  margin-top: 0.5rem;
}
.userDetails {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: max-content;
}
.userPicContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 3rem;
  height: 3rem;
  background-color: white;
  padding: 0.5rem;
  border-radius: 10rem;
}
.userPic {
  height: 100%;
  width: auto;
}
.userProfileDetails {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 0.5rem;
}
.userProfileDetails p {
  font-size: 0.7rem;
  font-weight: 700;
}
.userProfileDetails div {
  display: flex;
  align-items: center;
  font-size: 0.7rem;
  font-weight: 700;
}
.userProfileDetails img {
  height: 0.7rem;
  width: 0.7rem;
  margin-left: 0.3rem;
}
.userRating {
  display: flex;
  align-items: center;
}
.actions {
  display: flex;
  width: 100%;
  height: 5rem;
  background-color: green;
  border: 3px solid green;
}
.actionBtns {
  display: flex;
  justify-content: center;
  align-items: center;
  color: gold;
  width: 50%;
}
</style>
