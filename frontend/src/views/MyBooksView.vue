<template>
  <div class="middle">
    <SideNav page="my-books" @changeMyBookView="changeMiddleView" />

    <div class="mainPanel" v-if="changeMyBookView == 1">
      <div class="myBooks">
        <p class="myBooksHead">MY BOOKS</p>
        <div class="myBooksTrack" v-if="myBooks.length > 0">
          <div
            v-for="(book, index) in myBooks"
            :key="index"
            class="card myCard"
          >
            <div class="bookImgContainer">
              <img :src="book.img" alt="" class="bookImg" />
            </div>
            <div class="bookContent">
              <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
              <p class="bookAuthor">
                ISSUE: <span>{{ book.doi }}</span>
              </p>
              <p class="bookAuthor">
                RETURN: <span>{{ book.dor }}</span>
              </p>
            </div>
            <div class="actions">
              <div class="actionBtns" @click="readBook(book.book_id)">
                <img
                  src="@/assets/images/read_icon.png"
                  alt=""
                  class="actionBtnImg"
                />
                Read
              </div>
              <div class="actionBtns sideBtn" @click="returnBook(book.book_id)">
                <img
                  src="@/assets/images/return_icon.png"
                  alt=""
                  class="actionBtnImg"
                />
                Return
              </div>
            </div>
          </div>
        </div>
        <div class="myBooksTrack" v-else>
          <p class="myBooksHead">No issued books found.</p>
        </div>
      </div>
      <div class="myBooks">
        <p class="myBooksHead">MY HISTORY</p>
        <div class="myBooksTrack" v-if="myHistory.length > 0">
          <div v-for="(book, index) in myHistory" :key="index" class="card">
            <div class="bookImgContainer">
              <img :src="book.img" alt="" class="bookImg" />
            </div>
            <div class="bookContent">
              <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
              <p class="bookAuthor">
                ISSUE: <span>{{ book.doi }}</span>
              </p>
              <p class="bookAuthor">
                RETURN: <span>{{ book.dor }}</span>
              </p>
            </div>
          </div>
        </div>
        <div class="myBooksTrack" v-else>
          <p class="myBooksHead">No issued books found.</p>
        </div>
      </div>
    </div>
    <div class="mainPanel" v-if="changeMyBookView == 2">
      <div class="searchCont">
        <div class="searchbox">
          <input
            type="text"
            class="search"
            @change="bookSearcher()"
            id="searchbox"
            placeholder="Search your history"
          />
        </div>
      </div>
      <div v-for="(book, index) in searchBooks" :key="index" class="card">
        <div class="bookImgContainer">
          <img :src="book.img" alt="" class="bookImg" />
        </div>
        <div class="bookContent">
          <p class="bookTitle">{{ shortenText(book.book_name) }}</p>
          <p class="bookAuthor">
            ISSUE: <span>{{ book.doi }}</span>
          </p>
          <p class="bookAuthor">
            RETURN: <span>{{ book.dor }}</span>
          </p>
        </div>
      </div>
    </div>
    <div class="mainPanel" v-if="changeMyBookView == 3">
      <div class="statistics">
        <p class="myBooksHead">DASHBOARD</p>
        <div class="coreStatistics">
          <div class="d1profileContainer">
            <div class="d1profile">
              <div class="d1profilePicContainer">
                <img
                  v-if="statsData.user_info.gender == 'male'"
                  src="@/assets/images/male profile.png"
                  alt="username"
                  class="d1profilePic"
                />
                <img
                  v-else
                  src="@/assets/images/female profile.png"
                  alt="username"
                  class="d1profilePic"
                />
              </div>
              <div class="d1profileContent">
                <p class="d1profileHead">{{ statsData.user_info.user_name }}</p>
                <p class="d1profileEmail">
                  Email: <span>{{ statsData.user_info.email }}</span>
                </p>
                <p class="d1profileEmail">
                  Date Joined: <span>{{ statsData.user_info.doj }}</span>
                </p>
                <p class="d1profileEmail">
                  Last Loged: <span>{{ statsData.user_info.last_loged }}</span>
                </p>
              </div>
            </div>
            <div class="d1ranking">
              <p class="d1CardHeader">{{ statsData.rank }} League</p>
              <div class="leagueContainer">
                <img
                  v-if="statsData.rank == 'Sage'"
                  src="@/assets/images/Sage_logo.png"
                  :alt="`${statsData.rank} League`"
                  class="leagueLogo"
                />
                <img
                  v-if="statsData.rank == 'Scholar'"
                  src="@/assets/images/Scholar_logo.png"
                  :alt="`${statsData.rank} League`"
                  class="leagueLogo"
                />
                <img
                  v-if="statsData.rank == 'Literati'"
                  src="@/assets/images/Literati_logo.png"
                  :alt="`${statsData.rank} League`"
                  class="leagueLogo"
                />
                <img
                  v-if="statsData.rank == 'Reader'"
                  src="@/assets/images/Reader_logo.png"
                  :alt="`${statsData.rank} League`"
                  class="leagueLogo"
                />
              </div>
            </div>
            <div class="d1rankingSubTop">
              <div
                class="d1rankingSubs"
                v-if="statsData.rank != 'Sage'"
                style="margin-bottom: 1rem"
              >
                <p class="d1CardHeader">Next Objective</p>
                <div class="objectives">
                  <div
                    class="objectiveNote"
                    v-for="(note, index) in statsData.next_criteria"
                    :key="index"
                  >
                    <div class="bulletContainer">
                      <img
                        src="@/assets/images/bullet.png"
                        alt="bullet"
                        class="bullet"
                      />
                    </div>
                    <div class="bulletPoint">
                      <p class="bulletText">{{ note }}</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="d1rankingSubs" v-else style="margin-bottom: 1rem">
                <p class="d1CardHeader">No New Objective</p>
                <div class="objectives">
                  <div
                    class="objectiveNote"
                    v-for="(note, index) in statsData.next_criteria"
                    :key="index"
                  >
                    <div class="bulletPoint">
                      <p class="bulletText">{{ note }}</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="d1rankingSubs">
                <p class="d1CardHeader">Score</p>
                <div class="objectives" style="flex-direction: row">
                  <p class="scoreText">{{ statsData.score }}</p>
                  <img
                    src="@/assets/images/points.png"
                    alt="points"
                    class="scorePoint"
                  />
                </div>
              </div>
            </div>
          </div>
          <div class="charts">
            <div class="barChart">
              <BarChartView :barData="statsData.barchart" class="chartView" />
            </div>
            <div class="pieChart">
              <PieChartView :pieData="statsData.piechart" class="chartView" />
            </div>
          </div>
          <div class="dataValues">
            <DataCards
              cardHead="# Books Issued"
              :cardValue="statsData.cardData.total_issued"
            />
            <DataCards
              cardHead="# Requests Pending"
              :cardValue="statsData.cardData.total_requests"
            />
            <DataCards
              cardHead="Most Active Month"
              :cardValue="statsData.cardData.most_active_month"
            />
            <DataCards
              cardHead="# Books Rated"
              :cardValue="statsData.cardData.total_ratings"
            />
            <DataCards
              cardHead="# Days since Last Loged"
              :cardValue="statsData.cardData.days_last_loged"
            />
          </div>
        </div>
      </div>
    </div>
    <div class="mainPanel" v-if="changeMyBookView == 4">Feedbacks</div>
  </div>
</template>

<script>
import axios from "axios";
import BarChartView from "@/components/BarChartView.vue";
import PieChartView from "@/components/PieChartView.vue";
import DataCards from "@/components/DataCards.vue";
import SideNav from "@/components/SideNav.vue";

export default {
  components: { SideNav, BarChartView, PieChartView, DataCards },
  name: "MyBooksView",
  data() {
    return {
      changeMyBookView: 1,
      gender: "male",
      myBooks: [],
      myHistory: [],
      searchBooks: [],
      statsData: [],
      user_id: "REPA0354",
    };
  },
  created() {
    this.changeMyBookView = 1;
    this.fetchMyBooks();
    this.fetchMyHistory();
  },
  methods: {
    changeMiddleView(view) {
      this.changeMyBookView = view;
      if (view == 1) {
        this.fetchMyBooks();
        this.fetchMyHistory();
      } else if (view == 2) {
        this.searchBooks = [];
      } else if (view == 3) {
        this.fetchStatistics();
      }
    },
    fetchMyBooks() {
      axios
        .get(
          `http://127.0.0.1:5000/get-content/myBooks?user_id=${this.user_id}`
        )
        .then((response) => {
          this.myBooks = response.data;

          // this.changePreviewBook(this.myBooks[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchMyHistory() {
      axios
        .get(
          `http://127.0.0.1:5000/get-content/myBooks?user_id=${this.user_id}&all=true`
        )
        .then((response) => {
          this.myHistory = response.data;
          // this.changePreviewBook(this.myBooks[0].book_id);
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    fetchStatistics() {
      axios
        .get(`http://127.0.0.1:5000/get-statistics?user_id=${this.user_id}`)
        .then((response) => {
          this.statsData = response.data;
        })
        .catch(() => {
          this.$router.push("/error");
        });
    },
    bookSearcher() {
      let keyword = document.getElementById("searchbox").value;
      axios
        .get(`http://127.0.0.1:5000/search-content/my-books`, {
          params: {
            user_id: this.user_id,
            keyword: keyword,
          },
        })
        .then((response) => {
          this.searchBooks = [];
          this.searchBooks = response.data;
        })
        .catch(() => {});
    },
    shortenText(text) {
      if (text.length > 35) {
        return `${text.substring(0, 35)}...`;
      } else {
        return text;
      }
    },
    readBook(book_id) {
      console.log(`Reading ${book_id}`);
    },
    returnBook(book_id) {
      console.log(`Returning ${book_id}`);
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
.myBooks {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: max-content;
}
.myBooksHead {
  margin: 0.5rem 2.4rem;
  color: rgb(61, 61, 61);
  font-weight: 700;
}
.myBooksTrack {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 100%;
  overflow: hidden;
  overflow-x: scroll;
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
.statistics {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: max-content;
}
.coreStatistics {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: 0rem 1.4rem;
}
.charts {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 24rem;
}
.barChart {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 100%;
  padding: 1rem 0rem;
  position: relative;
  z-index: 3;
  /* background-color: white;
  padding: 1rem 2rem; */
  /* background-color: #e6ac45; */
}
.barChart::before {
  content: "Past 12 Months Activity";
  padding-right: 1rem;
  font-weight: 600;
  font-size: 1rem;
  margin-top: 1.5rem;
  color: rgb(61, 61, 61);
  display: flex;
  justify-content: center;
  align-items: start;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
.pieChart {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 40%;
  height: 100%;
  padding: 1rem 0rem;
  /* padding: ; */
  /* background-color: #e6ac45; */
  position: relative;
  z-index: 3;
}
.pieChart::before {
  content: "Genres";
  padding-right: 1rem;
  font-weight: 600;
  font-size: 1rem;
  color: rgb(61, 61, 61);
  display: flex;
  justify-content: center;
  align-items: center;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
.dataValues {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 11rem;
  margin-right: 1rem;
}
.d1profileContainer {
  display: flex;
  flex-direction: row;
  /* justify-content: center; */
  align-items: center;
  width: 100%;
  height: 20rem;
}
.d1profile {
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 50%;
  height: 80%;
  margin: 1rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.d1ranking {
  display: flex;
  flex-direction: row;
  width: 20%;
  height: 80%;
  margin: 1rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.d1rankingSubTop {
  display: flex;
  flex-direction: column;
  width: 20%;
  height: 80%;
  margin: 0rem 1rem;
}
.d1rankingSubs {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: center; */
  height: 48%;
  width: 100%;
  /* margin: 1rem; */
  border-radius: 1rem;
  /* box-shadow: 0 0.25rem 1rem #00000026; */
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.d1profilePicContainer {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10rem;
  height: 10rem;
  padding: 1rem;
  margin: 1rem 2rem;
  border-radius: 10rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  background-color: #ffffff;
}
.d1profilePic {
  height: 80%;
}
.d1profileHead {
  font-size: 2.8rem;
  font-weight: 700;
}
.d1profileEmail {
  font-size: 1rem;
}
.d1profileEmail span {
  color: rgb(79, 79, 79);
  margin-left: 0.3rem;
}
.d1ranking {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  padding: 1rem;
}
.leagueContainer {
  display: flex;
  height: 10rem;
  width: 10rem;
  padding: 1.2rem;
  margin-top: 1.5rem;
  border-radius: 10rem;
  background-color: #111914;
}
.leagueLogo {
  height: 100%;
  width: 100%;
}
.d1CardHeader {
  font-size: 1rem;
  font-weight: 600;
  font-style: italic;
  color: rgb(79, 79, 79);
  padding: 0rem 1rem;
}
.objectives {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  align-items: center;
  height: max-content;
  width: 100%;
  margin-top: 1rem;
}
.objectiveNote {
  display: flex;
  flex-direction: row;
  padding: 0rem 1rem;
  /* justify-content: center; */
  align-items: center;
  width: 100%;
  height: max-content;
}
.bulletContainer {
  display: flex;
  width: 10%;
  height: max-content;
  margin-right: 0.5rem;
}
.bullet {
  height: 1rem;
  width: auto;
}
.bulletPoint {
  display: flex;
  flex-wrap: wrap;
}
.scoreText {
  font-size: 2rem;
  font-weight: 700;
  padding: 0rem 1rem;
  padding-right: 0.5rem;
  color: #e6ac45;
}
.scorePoint {
  height: 1.8rem;
  width: auto;
  margin-left: 0.1rem;
}
</style>
