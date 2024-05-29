<template>
  <div class="middle">
    <SideNav @changeLibrarianView="changeMiddleView" page="librarian" />

    <div class="mainPanel" v-if="changeView == 1">Dashboard</div>
    <div class="mainPanel" v-if="changeView == 2">Search</div>
    <div class="mainPanel" v-if="changeView == 3">Issue Requests</div>
    <div class="mainPanel" v-if="changeView == 4">Issue Logs</div>
    <div class="mainPanel withPreview" v-if="changeView == 5">
      <div class="headBookTitleContainer">
        <div class="headBookTitle">Book Management</div>
        <div class="addNewBook" @click="createBook()">Add Book</div>
      </div>
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
          <div
            class="actionBtns"
            @click="confirmDelete(book.book_id, book.book_name)"
          >
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
    <div class="previewPanel" v-if="changeView == 5 && !addBookPallet">
      <div class="previewDetailsContainer">
        <div class="previewImgContainer">
          <img :src="previewBook.book.img" alt="" class="imgContainer" />
        </div>
        <div class="titleDiv" v-if="!isTitleEdit">
          <p class="previewTitle">
            {{ previewBook.book.book_name }}
          </p>
          <img
            src="@/assets/images/edit-icon.png"
            alt=""
            class="editActions"
            @click="editTitle()"
          />
        </div>

        <div class="previewTitleEdit" v-else>
          <input
            v-model="titleNew"
            @keyup.enter="isTitleEdit = false"
            @blur="handleTitleBlur"
            ref="titleInput"
          />
          <img
            src="@/assets/images/tick-icon.png"
            alt="Edit Title"
            title="Edit Title"
            class="editActions"
            @mousedown.prevent="saveTitle"
          />
        </div>

        <div class="majorDetails">
          <p v-if="!isAuthorEdit">
            AUTHOR: <span>{{ previewBook.book.author_name }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @click="editAuthor()"
            />
          </p>
          <div class="editable" v-else>
            AUTHOR:
            <input
              v-model="authorNew"
              @keyup.enter="isAuthorEdit = false"
              @blur="handleAuthorBlur"
              ref="authorInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Author"
              title="Edit Author"
              class="editActions"
              @mousedown.prevent="saveAuthor"
            />
          </div>
          <p v-if="!isGenreEdit">
            GENRE: <span>{{ previewBook.book.genre }}</span>
            <img
              src="@/assets/images/edit-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @click="editGenre()"
            />
          </p>
          <div class="editable" v-else>
            GENRE:
            <input
              v-model="genreNew"
              @keyup.enter="isGenreEdit = false"
              @blur="handleGenreBlur"
              ref="genreInput"
            />
            <img
              src="@/assets/images/tick-icon.png"
              alt="Edit Genre"
              title="Edit Genre"
              class="editActions"
              @mousedown.prevent="saveGenre"
            />
          </div>

          <p>DESCRIPTION:</p>
          <p>
            <span style="margin-left: 0rem"
              >Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Cupiditate repellendus quae similique natus in blanditiis
              doloribus facer?</span
            >
          </p>
        </div>
        <div class="bookStats">
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.issues }}</div>
            <p class="bookStatTitle"># Issues</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.requests }}</div>
            <p class="bookStatTitle"># Requests</p>
          </div>
          <div class="bookStatOption">
            <div class="bookStatData">{{ previewBook.avg_rating }}</div>
            <p class="bookStatTitle">Avg. Rating</p>
          </div>
        </div>
      </div>
    </div>
    <div class="previewPanel" v-if="changeView == 5 && addBookPallet">
      <p class="previewTitle">Add New Book</p>
      <div class="previewDetailsContainer">
        <div class="createNewEntry">
          BOOK COVER URL:
          <input v-model="createBookImg" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          TITLE:
          <input v-model="createBookName" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          AUTHOR NAME:
          <input v-model="createBookAuthor" class="createNewEntryInput" />
        </div>
        <div class="createNewEntry">
          SECTION NAME:
          <select
            name="cars"
            ref="sectionDrop"
            class="createNewEntryDropDown"
            v-model="selectedSection"
            @change="getGenres()"
          >
            <option
              v-for="(dropOption, dropIndex) in sections"
              :key="dropIndex"
              :value="dropOption.section_id"
            >
              {{ dropOption.section_name }}
            </option>
          </select>
        </div>
        <div class="createNewEntry">
          GENRE:
          <select name="cars" ref="genreDrop" class="createNewEntryDropDown">
            <option
              v-for="(dropOption, dropIndex) in dropGenre"
              :key="dropIndex"
              :value="dropOption"
            >
              {{ dropOption }}
            </option>
          </select>
        </div>
        <div class="submitNew">SUBMIT</div>
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
      selectedSection: null,
      dropGenre: [],
      previewBook: {},
      changeView: 1,
      isTitleEdit: false,
      isAuthorEdit: false,
      isGenreEdit: false,
      titleNew: "",
      genreNew: "",
      authorNew: "",
      addBookPallet: true,
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
    createBook() {
      this.addBookPallet = true;
      axios
        .get("http://127.0.0.1:5000/get-content/sections")
        .then((response) => {
          this.sections = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    getGenres() {
      console.log(this.selectedSection);
      axios
        .get(
          `http://127.0.0.1:5000/get-content/books?section_id=${this.selectedSection}`
        )
        .then((response) => {
          let genres = response.data.forEach((element) => {
            element.genre;
          });
          console.log(genres);
          this.dropGenre = [...new Set(genres)];
          console.log(this.dropGenre);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    editTitle() {
      this.titleNew = this.previewBook.book.book_name;
      this.isTitleEdit = true;
    },
    handleTitleBlur(event) {
      if (this.$refs.titleInput.contains(event.relatedTarget)) {
        return;
      }
      this.isTitleEdit = false;
    },
    async saveTitle(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://127.0.0.1:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            book_name: this.titleNew,
          }
        );
        this.previewBook.book.book_name = this.titleNew;
        this.isTitleEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Title. Kindly try again.");
      }
    },
    editGenre() {
      this.genreNew = this.previewBook.book.genre;
      this.isGenreEdit = true;
    },
    handleGenreBlur(event) {
      if (this.$refs.genreInput.contains(event.relatedTarget)) {
        return;
      }
      this.isGenreEdit = false;
    },
    async saveGenre(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://127.0.0.1:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            genre: this.genreNew,
          }
        );
        this.previewBook.book.genre = this.genreNew;
        this.isGenreEdit = false;
        console.log("Success:", response.data);
      } catch (error) {
        alert("Unable to edit the Genre. Kindly try again.");
      }
    },
    editAuthor() {
      this.authorNew = this.previewBook.book.author_name;
      this.isAuthorEdit = true;
    },
    handleAuthorBlur(event) {
      if (this.$refs.authorInput.contains(event.relatedTarget)) {
        return;
      }
      this.isAuthorEdit = false;
    },
    async saveAuthor(event) {
      event.stopPropagation();
      try {
        const response = await axios.put(
          "http://127.0.0.1:5000/put-content/books",
          {
            book_id: this.previewBook.book.book_id,
            author_name: this.authorNew,
          }
        );
        const responseAuthor = await axios.put(
          "http://127.0.0.1:5000/put-content/authors",
          {
            author_id: this.previewBook.book.author_id,
            author_name: this.authorNew,
          }
        );
        this.previewBook.book.author_name = this.authorNew;
        this.isAuthorEdit = false;
        console.log("Success:", response.data, responseAuthor.data);
      } catch (error) {
        alert("Unable to edit the Author Name. Kindly try again.");
      }
    },
    async deleteBook(book_id) {
      try {
        const response = await axios.delete(
          `http://127.0.0.1:5000/delete-content/books?book_id=${book_id}`
        );
        console.log("Success:", response.data);
        window.location.reload();
      } catch (error) {
        alert("Unable to Delete the book. Kindly try again.");
      }
    },
    confirmDelete(book_id, book_name) {
      if (
        confirm(`Are you sure you want to delete this book : ${book_name}?`)
      ) {
        this.deleteBook(book_id, book_name);
      }
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
  height: 100%;
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
.editable {
  display: flex;
}
.imgContainer {
  height: 100%;
  width: auto;
}
.previewTitle {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  line-height: 20px;
  font-weight: 600;
  font-size: 1.1rem;
  padding: 0.2rem 0rem;
}
.previewTitle img {
  height: 1.2rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails {
  height: max-content;
  width: 100%;
  margin: 1rem 0rem;
}
.majorDetails p {
  display: flex;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  letter-spacing: 1px;
}
.majorDetails div {
  display: flex;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  color: rgb(61, 61, 61);
  letter-spacing: 1px;
}
.majorDetails p > img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails div > img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.majorDetails span {
  font-weight: 500;
  letter-spacing: 0rem;
  margin-left: 0.3rem;
}
.majorDetails input {
  font-weight: 500;
  margin-left: 0.3rem;
  padding: 0rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 0.7rem;
  font-weight: 500;
  color: rgb(61, 61, 61);
}
.bookStats {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin: 1rem 0rem;
  height: max-content;
}
.previewTitleEdit {
  display: flex;
  align-items: center;
  margin-top: 1rem;
  line-height: 20px;
  font-weight: 600;
  font-size: 1.1rem;
  padding: 0.2rem 0rem;
}
.previewTitleEdit input {
  font-weight: 600;
  padding: 0rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 1rem;
  color: rgb(61, 61, 61);
}
.previewTitleEdit img {
  height: 1rem;
  width: auto;
  margin-left: 0.3rem;
  cursor: pointer;
  filter: grayscale(100%) brightness(0.2);
}
.bookStatOption {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 5rem;
  width: 30%;
  margin: 0rem 0.5rem;
}
.bookStatData {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 3rem;
  width: 3rem;
  margin: 0.5rem;
  background-color: white;
  border-radius: 10rem;
  font-size: 1rem;
  font-weight: 600;
  box-shadow: 0 0.25rem 1rem #00000026;
  transition: all 0.2s ease;
  cursor: pointer;
  color: #e6ac45;
  background-color: #25352b;
}
.bookStatTitle {
  height: 1rem;
  width: 100%;
  font-size: 0.7rem;
  text-align: center;
}
.titleDiv {
  display: flex;
  align-items: center;
}
.titleDiv p {
  max-width: 90%;
  width: max-content;
}
.titleDiv img {
  height: 1rem;
  width: auto;
  margin-top: 1rem;
  margin-left: 0.3rem;
  filter: grayscale(100%) brightness(0);
}
.headBookTitleContainer {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 5rem;
  margin-left: 1.4rem;
}
.headBookTitle {
  display: flex;
  width: 80%;
  font-weight: 600;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
}
.addNewBook {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20%;
  height: 2.5rem;
  margin: 0rem 1.4rem;
  font-weight: 600;
  background-color: white;
  color: #e6ac45;
  border-radius: 0.5rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  cursor: pointer;
  letter-spacing: 1px;
  transition: all 0.2s ease;
}
.addNewBook:hover {
  background-color: #25352b;
  color: #e6ac45;
}
.createNewEntry {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.5rem;
  width: 100%;
  font-weight: 600;
  font-size: 0.8rem;
}
.createNewEntryInput {
  font-weight: 500;
  padding: 0.2rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
  border: 1px solid rgb(61, 61, 61);
  font-size: 0.8rem;
  font-weight: 500;
  color: rgb(61, 61, 61);
}
.submitNew {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  background-color: #25352b;
  color: #e6ac45;
  padding: 0.5rem;
  margin-top: 1rem;
  border-radius: 0.25rem;
  font-weight: 600;
  letter-spacing: 1px;
  cursor: pointer;
  transition: all 0.2s ease;
}
.submitNew:hover {
  background-color: #111914;
}
.createNewEntryDropDown {
  padding: 0.2rem 0.2rem;
  border-radius: 0.2rem;
  outline: none;
}
</style>
