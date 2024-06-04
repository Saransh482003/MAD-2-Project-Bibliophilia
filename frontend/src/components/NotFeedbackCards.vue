<template>
  <div class="feedbackContainer">
    <div class="fbookImgCont">
      <img
        :src="bookDetails.img"
        :alt="bookDetails.book_name"
        class="fbookImg"
      />
    </div>
    <div class="fbookDetails">
      <p class="fbookName">{{ bookDetails.book_name }}</p>
      <div
        class="fbookRatingCont"
        ref="ratingContainer"
        @mouseleave="hoverOff()"
      >
        <img
          v-for="i in dumStarRating"
          :key="`star${i}`"
          :id="`star${i}`"
          src="@/assets/images/star.png"
          alt=""
          class="fbookRating"
          @mouseenter="hoverOn(`star${i}`)"
          @click="rateStar(`star${i}`)"
        />
        <img
          v-for="i in 5 - dumStarRating"
          :key="`hollow_star${i}`"
          :id="`hollow_star${i}`"
          src="@/assets/images/hollow star.png"
          alt=""
          class="fbookRating"
          @mouseenter="hoverOn(`hollow_star${i}`)"
          @click="rateStar(`hollow_star${i}`)"
        />
        <div class="ratingCount">{{ dumStarRating }}</div>
      </div>
      <textarea
        name=""
        class="feedbackArea"
        cols="30"
        rows="10"
        placeholder="Enter Your Feedback Here"
        v-model="feedbackText"
      ></textarea>
      <div class="fsubmit" @click="submitRating()">
        <img
          src="@/assets/images/tick-icon.png"
          alt="Submit"
          class="fsubmitIcon"
        />
        SUBMIT
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios";
export default {
  name: "NotFeedbackCards",
  props: {
    bookDetails: {
      type: Object,
      required: true,
    },
    user_id: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      starRating: 0,
      dumStarRating: 0,
      feedbackText: "",
    };
  },
  methods: {
    hoverOn(starID) {
      const childElements =
        this.$refs.ratingContainer.querySelectorAll(".fbookRating");
      for (let i = 0; i < 5; i++) {
        if (childElements[i].id == starID) {
          this.dumStarRating = i + 1;
        }
      }
    },
    hoverOff() {
      this.dumStarRating = this.starRating.valueOf();
    },
    rateStar(starID) {
      const childElements =
        this.$refs.ratingContainer.querySelectorAll(".fbookRating");
      for (let i = 0; i < 5; i++) {
        if (childElements[i].id == starID) {
          this.starRating = i + 1;
        }
      }
      this.dumStarRating = this.starRating.valueOf();
    },
    async submitRating() {
      if (this.dumStarRating != 0 && this.feedbackText != "") {
        try {
          const response = await axios.post("/push-content/ratings", {
            book_id: this.bookDetails.book_id,
            user_id: this.user_id,
            rating: this.dumStarRating,
            feedback: this.feedbackText,
          });
          console.log("Success:", response.data);
          window.location.reload();
        } catch (error) {
          alert(
            "Unable to submit the feedback. Kindly try again or contact the librarian."
          );
        }
      } else {
        alert("Kindly enter a suitable feedback and rating.");
      }
    },
  },
};
</script>

<style scoped>
.feedbackContainer {
  display: flex;
  flex-direction: row;
  width: 47%;
  height: 17.5rem;
  margin: 1rem;
  border-radius: 1rem;
  background-color: white;
  box-shadow: 0 0.25rem 1rem #00000026;
}
.fbookImgCont {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30%;
  height: 100%;
  margin: 0rem 1rem;
  overflow: hidden;
}
.fbookImg {
  height: 100%;
  width: auto;
}
.fbookDetails {
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
  width: 70%;
  padding: 0.8rem 0rem;
  padding-right: 0.8rem;
}
.fbookName {
  font-size: 1.5rem;
  font-weight: 700;
  padding: 0.1rem 0rem;
  max-height: 75px;
}
.fbookRatingCont {
  display: flex;
  height: 1.5rem;
  width: 100%;
  /* margin: 0.5rem 0rem; */
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.1rem 0rem;
  color: rgb(61, 61, 61);
}
.fbookRating {
  height: 100%;
  width: auto;
  padding-right: 0.3rem;
  cursor: pointer;
}
.feedbackArea {
  margin: 1rem 0rem;
  margin-top: 0.8rem;
  height: 5rem;
  width: 100%;
  resize: none;
  padding: 0.5rem;
  border-radius: 0.2rem;
  outline: none;
  border-color: #25352b;
}
.fsubmit {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 8rem;
  height: 2.5rem;
  background-color: #25352b;
  color: #e6ac45;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: all 0.2s ease;
}
.fsubmit:hover {
  background-color: #111914;
}
.fsubmitIcon {
  height: 1rem;
  width: auto;
  margin-right: 0.3rem;
}
.feedbackHead {
  width: 100%;
  margin-left: 0rem;
  margin-left: 1rem;
}
.ratingCount {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-size: 0.8rem;
  font-weight: 600;
  height: 100%;
  width: max-content;
  padding: 0rem 0.5rem;
  margin-left: 0.2rem;
  border-left: 2px solid black;
}
</style>
