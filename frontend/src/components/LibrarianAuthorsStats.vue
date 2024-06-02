<template>
  <div class="coreStatistics">
    <div class="dashRow">
      <div class="dataCards">
        <div class="dataCardTitle">Most Issued</div>
        <div class="cardImgContaiener">
          <img
            :src="authorsStatsData.dataValues.most_issued[0]"
            alt=""
            class="cardImg"
          />
        </div>
        <div class="dataCardTitle authName">
          {{ authorsStatsData.dataValues.most_issued[1] }}
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Most Popular</div>
        <div class="cardImgContaiener">
          <img
            :src="authorsStatsData.dataValues.most_popular[0]"
            alt=""
            class="cardImg"
          />
        </div>
        <div class="dataCardTitle authName">
          {{ authorsStatsData.dataValues.most_popular[1] }}
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Least Popular</div>
        <div class="cardImgContaiener">
          <img
            :src="authorsStatsData.dataValues.least_popular[0]"
            alt=""
            class="cardImg"
          />
        </div>
        <div class="dataCardTitle authName">
          {{ authorsStatsData.dataValues.least_popular[1] }}
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Highest Book Rating</div>
        <div class="cardImgContaiener">
          <img
            :src="authorsStatsData.dataValues.highest_book_rating[0]"
            alt=""
            class="cardImg"
          />
        </div>
        <div class="dataCardTitle authName">
          {{ authorsStatsData.dataValues.highest_book_rating[1] }}
        </div>
      </div>
      <div class="dataCards">
        <div class="dataCardTitle">Lowest Book Rating</div>
        <div class="cardImgContaiener">
          <img
            :src="authorsStatsData.dataValues.lowest_book_rating[0]"
            alt=""
            class="cardImg"
          />
        </div>
        <div class="dataCardTitle authName">
          {{ authorsStatsData.dataValues.lowest_book_rating[1] }}
        </div>
      </div>
    </div>
    <div class="dashRow">
      <div class="authorBars" id="avg_country">
        <!-- <p class="chartTitle">Highest Issue Counts</p> -->
        <BarChartView
          :barData="authorsStatsData.avg_country"
          class="chartView"
          beginAtZero="false"
        />
      </div>
      <div class="authorPies" id="count_country">
        <!-- <p class="chartTitle">Highest Issues for Males</p> -->
        <PieChartView
          :pieData="authorsStatsData.count_country"
          class="chartView"
        />
      </div>
    </div>
    <div class="dashRow">
      <div class="authorBars" id="avg_age">
        <!-- <p class="chartTitle">Highest Issues for Ages 15-30</p> -->
        <BarChartView
          :barData="authorsStatsData.avg_age"
          class="chartView"
          beginAtZero="false"
        />
      </div>
      <div class="authorPies" id="count_age">
        <!-- <p class="chartTitle">Highest Issues for Ages 30-60</p> -->
        <PieChartView :pieData="authorsStatsData.count_age" class="chartView" />
      </div>
    </div>
  </div>
</template>

<script>
import PieChartView from "@/components/PieChartView.vue";
import BarChartView from "@/components/BarChartView.vue";

export default {
  components: { PieChartView, BarChartView },
  name: "LibrarianAuthorsStats",
  props: {
    authorsStatsData: {
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
.authorBars {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 60%;
  height: 24rem;
  padding: 1rem 0rem;
  padding-right: 2rem;
  position: relative;
  z-index: 3;
}
.authorPies {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40%;
  height: 24rem;
  padding: 1rem 0rem;
  padding-right: 5rem;
  position: relative;
  z-index: 3;
}
#avg_country::before {
  content: "Avg. Author Rating by Country of Birth (Top 10)";
  width: 30%;
  font-weight: 600;
  font-size: 1rem;
  color: rgb(61, 61, 61);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: start;
  padding-top: 1.8rem;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
#avg_age::before {
  content: "Avg. Author Rating by Age";
  width: 30%;
  font-weight: 600;
  font-size: 1rem;
  color: rgb(61, 61, 61);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: start;
  padding-top: 1.8rem;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
#count_country::before {
  content: "Count by Country";
  width: 30%;
  font-weight: 600;
  font-size: 0.8rem;
  color: rgb(61, 61, 61);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  top: 0;
  left: auto;
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 4;
}
#count_age::before {
  content: "Count by Age";
  width: 30%;
  font-weight: 600;
  font-size: 0.8rem;
  color: rgb(61, 61, 61);
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
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
  height: 13rem;
  width: 13rem;
  border-radius: 10rem;
  margin: 1rem 0rem;
  margin-bottom: 0.2rem;
  overflow: hidden;
}
.cardImg {
  height: 100%;
  width: auto;
  object-fit: cover;
}
.chartView {
  margin: 0rem;
}
.authName {
  font-size: 0.9rem;
  color: rgb(80, 80, 80);
}
</style>
