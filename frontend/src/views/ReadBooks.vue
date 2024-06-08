<template>
  <div class="middle">
    <SideNav page="read-book" @changeMyBookView="changeMiddleView" />
    <div class="mainPanel">
      <div class="bookContent">
        <p class="bookTitle">{{ bookdetails.book_name }}</p>
        <p>
          Author: <span>{{ bookdetails.author_name }}</span>
        </p>
        <p>
          Issue Date: <span>{{ bookdetails.doi }}</span>
        </p>
        <p>
          Return Date:
          <span
            >{{ bookdetails.dor }} ({{ bookdetails.days_left }} days left)</span
          >
        </p>
      </div>
      <div class="bookPages">
        <div class="bookPage">
          <img
            src="https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/299267325/original/a3c7649b344bb7608cc0099cc58b4f711e5a9acd/format-your-manuscript-for-your-novel.png"
            alt=""
            class="page"
          />
        </div>
        <div class="bookPage">
          <img
            src="https://bookcover.biz/wp-content/uploads/BCB-Print-SS-04.png"
            alt=""
            class="page"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios";
import SideNav from "@/components/SideNav.vue";
export default {
  components: {
    SideNav,
  },
  name: "ReadBooks",
  data() {
    return {
      bookdetails: {},
    };
  },
  created() {
    this.user_id = localStorage.getItem("user_id");
    this.book_id = localStorage.getItem("current-read-bookid");
  },
  mounted() {
    this.fetchBook();
  },
  methods: {
    fetchBook() {
      axios
        .get(`/get-read-books?user_id=${this.user_id}&book_id=${this.book_id}`)
        .then((response) => {
          this.bookdetails = response.data;
          console.log(this.bookdetails);
        })
        .catch(() => {
          this.$router.push("/my-books");
          alert(
            "There was a problem in loading your book. Kindly report this to the librarian."
          );
        });
    },
  },
};
</script>

<style scoped>
.middle {
  display: flex;
  flex-direction: row;
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
.bookContent {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 10rem;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 1rem 3rem;
}
.bookContent p span {
  color: rgb(85, 85, 85);
  margin-left: 0.2rem;
}
.bookContent p {
  letter-spacing: 0.5px;
  padding: 0.1rem;
}
.bookTitle {
  font-size: 1.5rem;
  letter-spacing: 0.5px;
}
.bookPages {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80rem;
  height: max-content;
}
.bookPage {
  display: flex;
  width: 40rem;
  height: 60rem;
  background-color: aqua;
  border-radius: 0.5rem;
}
.bookPage:first-child {
  clip-path: polygon(0% 0%, 100% 2%, 100% 98%, 0% 100%);
  border-right: 1px solid rgb(66, 66, 66);
}
.bookPage:last-child {
  clip-path: polygon(0% 2%, 100% 0%, 100% 100%, 0% 98%);
  border-left: 1px solid rgb(66, 66, 66);
}
.page {
  height: 100%;
  width: 100%;
}
.bookPage:first-child .page {
  clip-path: polygon(0% 0%, 100% 2%, 100% 98%, 0% 100%);
}
.bookPage:last-child .page {
  clip-path: polygon(0% 2%, 100% 0%, 100% 100%, 0% 98%);
}
</style>
