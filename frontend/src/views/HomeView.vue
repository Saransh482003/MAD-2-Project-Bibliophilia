<template>
  <div class="middle">
    <SideNav @changeView="changeMiddleView" />

    <div class="mainPanel" v-if="changeView == 2">
      <div class="searchCont">
        <div class="searchbox">
          <input
            type="text"
            class="search"
            @change="bookSearcher()"
            id="searchbox"
            placeholder="Enter your search keyword"
          />
        </div>
      </div>
      <div
        v-for="(book, index) in searchBooks"
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
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="mainPanel" v-if="changeView == 3">
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
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="mainPanel" v-if="changeView == 4">
      <div v-for="(section, index) in sections" :key="index" class="authorCard">
        <div class="authorImgContainer">
          <img :src="section.img" alt="" class="authorImg" />
        </div>
        <div class="authorContent">
          <p class="authorName">{{ section.section_name }}</p>
        </div>
      </div>
    </div>

    <div class="mainPanel" v-if="changeView == 5">
      <div
        v-for="(book, index) in latestBooks"
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
            AUTHOR: <span>{{ book.author_name }}</span>
          </p>
          <p class="bookAuthor">
            GENRE: <span>{{ book.genre }}</span>
          </p>
        </div>
      </div>
    </div>

    <div class="mainPanel" v-if="changeView == 6">
      <div v-for="(author, index) in authors" :key="index" class="authorCard">
        <div class="authorImgContainer">
          <img :src="author.img" alt="" class="authorImg" />
        </div>
        <div class="authorContent">
          <p class="authorName">{{ author.author_name }}</p>
        </div>
      </div>
    </div>

    <div class="mainPanel" v-if="changeView == 7">
      <div
        v-for="(genre, index) in genres"
        :key="index"
        class="authorCard genreCard"
      >
        <div
          :class="`authorImgContainer genreContainer ${
            index % 2 == 0 ? 'evenGenreCard' : ''
          }`"
        >
          <p
            :class="`authorName ${index % 2 == 0 ? 'evenGenreContainer' : ''}`"
          >
            {{ genre }}
          </p>
          <!-- <img :src="genre.img" alt="" class="authorImg" /> -->
        </div>
      </div>
    </div>

    <div class="previewPanel">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer">
          <img :src="previewBook.img" alt="" class="imgContainer" />
          <div class="downloadPDFContainer">
            <a class="downloadPDF" :href="previewBook.book_id" target="_blank">
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
              >Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate repellendus quae similique natus in blanditiis
              doloribus facere et a? Alias excepturi quasi sapiente, aut ea fuga
              enim iusto doloribus, recusandae, soluta neque dolores reiciendis?
              Ex repellat eius deleniti molestiae? Enim pariatur illo impedit
              totam corrupti repudiandae, aliquid assumenda obcaecati
              veniam.</span
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
            rating of {{ previewBook.author_avg_rating }}, reflecting their
            talent and dedication to literature.
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
                    <img
                      src="@/assets/images/star.png"
                      alt="Star"
                      class="star"
                    />
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
      </div>
      <div class="actions">
        <div
          :class="`actionBtns ${
            allowedRequest.status == 602 ? 'disableBtn' : ''
          }`"
          @click="request_book($event, previewBook.book_id)"
          :title="allowedRequest.message"
        >
          <img
            src="@/assets/images/request_book.png"
            alt=""
            :class="`actionBtnImg ${
              allowedRequest.status == 602 ? 'disableBtnImg' : ''
            }`"
          />
          Request
        </div>
        <div class="actionBtns sideBtn" @click="save_book(previewBook.book_id)">
          <img src="@/assets/images/save.png" alt="" class="actionBtnImg" />
          Save
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SideNav from "@/components/SideNav.vue";
export default {
  components: { SideNav },
  name: "HomeView",
  data() {
    return {
      searchBooks: [],
      books: [],
      sections: [],
      authors: [],
      genres: [],
      latestBooks: [],
      previewBook: {},
      allowedRequest: {
        status: 601,
        message: "Click to Request Book",
        limit: 0,
      },
      user_id: "REPA0302",
      changeView: 1,
    };
  },
  created() {
    this.fetchBooks();
    this.changeView = 1;
  },
  methods: {
    changeMiddleView(view) {
      this.changeView = view;
      if (view == 4) {
        this.fetchSections();
      } else if (view == 6) {
        this.fetchAuthors();
      } else if (view == 5) {
        this.fetchLatest();
      } else if (view == 7) {
        this.fetchGenres();
      }
      this.searchBooks = [];
    },
    bookSearcher() {
      let keyword = document.getElementById("searchbox").value;
      axios
        .get(`http://127.0.0.1:5000/search-content?keyword=${keyword}`, {
          params: {
            keyword: keyword,
          },
        })
        .then((response) => {
          this.searchBooks = [];
          this.searchBooks = response.data;
        });
    },
    changePreviewBook(book_id) {
      axios
        .get(`http://127.0.0.1:5000/get-content/recent-book?book_id=${book_id}`)
        .then((response) => {
          this.previewBook = response.data;
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
      this.requestAllowance("UNIH4233", this.user_id);
    },
    requestAllowance(book_id, user_id) {
      axios
        .get(
          `http://127.0.0.1:5000/get-content/requests?book_id=${book_id}&user_id=${user_id}`
        )
        .then(() => {
          this.allowedRequest.status = 602;
          this.allowedRequest.message = "Book already issued";
        })
        .catch(() => {
          axios
            .get(`http://127.0.0.1:5000/get-content/requests?user_id=REPA0251`)
            .then((response) => {
              if (response.data.length >= 5) {
                this.allowedRequest.status = 603;
                this.allowedRequest.message = "Request Limit Exhausted";
              } else {
                this.allowedRequest.limit = 5 - response.data.length;
              }
            });
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
    fetchSections() {
      axios
        .get("http://127.0.0.1:5000/get-content/sections")
        .then((response) => {
          this.sections = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchLatest() {
      axios
        .get("http://127.0.0.1:5000/get-content/latestBooks")
        .then((response) => {
          this.latestBooks = response.data;
          this.changePreviewBook(this.latestBooks[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchAuthors() {
      axios
        .get("http://127.0.0.1:5000/get-content/authors")
        .then((response) => {
          this.authors = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchGenres() {
      axios
        .get("http://127.0.0.1:5000/get-content/genres")
        .then((response) => {
          this.genres = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    request_book(event, book_id) {
      event.preventDefault();
      event.stopPropagation();
      if (this.allowedRequest.status == 601) {
        const today = new Date();
        const day = today.getDate().toString().padStart(2, "0");
        const month = (today.getMonth() + 1).toString().padStart(2, "0");
        const year = today.getFullYear();
        axios
          .get(
            `http://127.0.0.1:5000/push-content/requests?book_id=${book_id}&user_id=${this.user_id}&request_date=${year}-${month}-${day}`
          )
          .then(() => {
            console.log(
              `Request successfully made for Book ID ${book_id} User ID ${this.user_id}`
            );
          })
          .catch((error) => {
            console.error("There was an error making the POST request!", error);
          });
      }
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
  background-color: beige;
}
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
  z-index: 3;
  /* background: url("https://img.freepik.com/free-vector/hand-drawn-painted-whitewash-background_23-2151214448.jpg");
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat; */
}
.previewPanel {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  width: 20%;
  height: 100%;
  /* background-color: #fff6e6; */
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
  background-color: #25352b;
  /* padding: 0.35rem; */
}
.downloadPDF:hover .pdfIcon {
  filter: none;
}
.pdfIcon {
  width: 100%;
  height: 100%;
  filter: grayscale(100%) brightness(0);
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
  display: flex;
  justify-content: center;
  align-items: center;
  width: 7rem;
  height: 4.6rem;
  margin-right: 0.5rem;
  overflow: hidden;
  background-color: aqua;
  border-radius: 30rem;
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
  height: 9%;
  background-color: #25352b;
  /* border-top: 3px solid #25352b; */
}
.actionBtns {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #e6ac45;
  width: 50%;
  cursor: pointer;
  transition: all 0.2s ease;
}
.actionBtnImg {
  height: 1.5rem;
  width: auto;
  margin-right: 0.3rem;
  transition: all 0.2s ease;
  /* filter: grayscale(100%) brightness(1000); */
}
.sideBtn {
  background-color: white;
}
.actionBtns:hover {
  font-size: 1.1rem;
}
.actionBtns:hover .actionBtnImg {
  height: 1.6rem;
}
.disableBtn {
  background-color: rgb(124, 124, 124);
  color: white;
}
.disableBtnImg {
  filter: grayscale(100%) brightness(1000);
}
.authorCard {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 13rem;
  width: 10rem;
  margin: 0.7rem 1.4rem;
}
.authorImgContainer {
  display: flex;
  height: 10rem;
  width: 10rem;
  border-radius: 10rem;
  box-shadow: 0 0.25rem 1rem #00000026;
}
.authorImg {
  height: 100%;
  width: auto;
  object-fit: cover;
}
.authorContent {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 3rem;
}
.authorName {
  text-align: center;
  margin-top: 0.5rem;
  font-size: 0.9rem;
  font-weight: 700;
}
.authorRating {
  font-size: 0.7rem;
}
.genreContainer {
  justify-content: center;
  flex-wrap: wrap;
  padding: 1rem;
  align-items: center;
  text-align: center;
  background-color: #e6ac45;
}
.genreCard {
  margin: 0.5rem 1.2rem;
  height: max-content;
  color: #25352b;
}
.evenGenreCard {
  background-color: #25352b;
}
.evenGenreContainer {
  color: #e6ac45;
}
.searchCont {
  display: flex;
  margin-top: 0.3rem;
  margin-bottom: 1rem;
  width: 100%;
  height: 4rem;
}
.searchbox {
  display: flex;
  align-items: center;
  width: 40%;
  background-color: #111914;
  border-top-right-radius: 10rem;
  border-bottom-right-radius: 10rem;
}
.search {
  margin: 1rem 1rem;
  margin-right: 2rem;
  caret-shape: bar;
  caret-color: #e6ac45;
  padding: 0.3rem 0.3rem;
  color: #e6ac45;
  font-weight: 700;
  letter-spacing: 1px;
  width: 100%;
  outline: none;
  border: 0rem;
  background-color: #111914;
  border-bottom: 3px solid #e6ac45;
}
</style>
