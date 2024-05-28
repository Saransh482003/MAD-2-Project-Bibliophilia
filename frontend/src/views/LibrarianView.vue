<template>
  <div class="middle">
    <SideNav @changeLibrarianView="changeMiddleView" page="librarian" />

    <div class="mainPanel" v-if="changeView == 1">Dashboard</div>
    <div class="mainPanel" v-if="changeView == 2">Search</div>
    <div class="mainPanel" v-if="changeView == 3">Issue Requests</div>
    <div class="mainPanel" v-if="changeView == 4">Issue Logs</div>
    <div class="mainPanel" v-if="changeView == 5">Book Management</div>
    <div class="mainPanel" v-if="changeView == 6">Section Management</div>
    <div class="mainPanel" v-if="changeView == 7">User Management</div>
  </div>
</template>

<script>
// import axios from "axios";
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
.ratingStar {
  display: flex;
  height: 1.3rem;
  width: 100%;
  margin: 0.8rem 0rem;
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
  border-radius: 10rem;
  color: #25352b;
  box-shadow: 0 0.25rem 1rem #00000026;
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
.myBooks {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 25rem;
}
.myBooksHead {
  margin: 0.5rem 1.4rem;
  color: rgb(61, 61, 61);
  font-weight: 700;
}
.myBooksTrack {
  display: flex;
  width: max-content;
  height: 100%;
  overflow: hidden;
  overflow-x: scroll;
}
</style>
