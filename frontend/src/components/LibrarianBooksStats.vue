<template>
  <div class="coreStatistics">
    <div class="dashRow">
      <div class="dataCards">
        <div class="dataCardTitle">Most Issued</div>
        <div class="cardImgContaiener">
          <img
            :src="bookStatsData.dataValues.most_issued"
            alt=""
            class="cardImg"
          />
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Most Rated</div>
        <div class="cardImgContaiener">
          <img
            :src="bookStatsData.dataValues.most_rated"
            alt=""
            class="cardImg"
          />
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Highest Rated</div>
        <div class="cardImgContaiener">
          <img
            :src="bookStatsData.dataValues.highest_rated"
            alt=""
            class="cardImg"
          />
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Least Rated</div>
        <div class="cardImgContaiener">
          <img
            :src="bookStatsData.dataValues.least_rated"
            alt=""
            class="cardImg"
          />
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Latest Release</div>
        <div class="cardImgContaiener">
          <img
            :src="bookStatsData.dataValues.latest_book"
            alt=""
            class="cardImg"
          />
        </div>
      </div>
    </div>
    <div class="dashRow">
      <div class="bookPies">
        <p class="chartTitle">Highest Issue Counts</p>
        <PieChartView
          :pieData="bookStatsData.general_genres"
          class="chartView"
          id="general_genres"
        />
      </div>
      <div class="bookPies">
        <p class="chartTitle">Highest Issues for Males</p>
        <PieChartView
          :pieData="bookStatsData.male_genres"
          class="chartView"
          id="male_genres"
        />
      </div>
      <div class="bookPies">
        <p class="chartTitle">Highest Issues for Females</p>
        <PieChartView
          :pieData="bookStatsData.female_genres"
          class="chartView"
          id="female_genres"
        />
      </div>
    </div>
    <div class="dashRow">
      <div class="bookPies">
        <p class="chartTitle">Highest Issues for Ages 15-30</p>
        <PieChartView
          :pieData="bookStatsData.age_young"
          class="chartView"
          id="age_young"
        />
      </div>
      <div class="bookPies">
        <p class="chartTitle">Highest Issues for Ages 30-60</p>
        <PieChartView
          :pieData="bookStatsData.age_middle"
          class="chartView"
          id="age_middle"
        />
      </div>
      <div class="bookPies">
        <p class="chartTitle">Highest Issues for Ages above 60</p>
        <PieChartView
          :pieData="bookStatsData.age_old"
          class="chartView"
          id="age_old"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PieChartView from "@/components/PieChartView.vue";

export default {
  components: { PieChartView },
  name: "LibrarianBooksStats",
  props: {
    bookStatsData: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.coreStatistics {
  display: flex;
  flex-direction: column;
  width: 100%;
  margin: 0rem 1.4rem;
}
.dashRow {
  display: flex;
  flex-direction: row;
  align-items: center;
  height: max-content;
  width: 100%;
  margin: 0rem 1.5rem;
}
.bookPies {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 33%;
  height: 24rem;
  padding: 1rem 0rem;
  padding-right: 2rem;
  position: relative;
  z-index: 3;
}
.bookPies::before {
  content: "Genres";
  /* padding-right: 1rem; */
  width: 30%;
  font-weight: 600;
  font-size: 1rem;
  color: rgb(61, 61, 61);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  padding-top: 1rem;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
.chartTitle {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  color: rgb(52, 52, 52);
}
.dataCards {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 20rem;
  width: 18%;
  margin: 1rem;
  margin-left: 0rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.dataCardTitle {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.2rem;
  height: 10%;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  /* font-style: italic; */
}
.cardImgContaiener {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90%;
  width: 90%;
  padding-bottom: 1rem;
  overflow: hidden;
}
.cardImg {
  height: 100%;
  width: auto;
}
</style>
