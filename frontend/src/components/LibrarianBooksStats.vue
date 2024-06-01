<template>
  <div class="coreStatistics">
    <div class="dashRow">
      <div class="bookPies">
        <PieChartView
          :pieData="bookStatsData.general_genres"
          class="chartView"
        />
      </div>
      <div class="bookPies">
        <PieChartView :pieData="bookStatsData.male_genres" class="chartView" />
      </div>
      <div class="bookPies">
        <PieChartView
          :pieData="bookStatsData.female_genres"
          class="chartView"
        />
      </div>
    </div>
    <div class="dashRow">
      <div class="bookPies">
        <PieChartView :pieData="bookStatsData.age_young" class="chartView" />
      </div>
      <div class="bookPies">
        <PieChartView :pieData="bookStatsData.age_middle" class="chartView" />
      </div>
      <div class="bookPies">
        <PieChartView :pieData="bookStatsData.age_old" class="chartView" />
      </div>
    </div>
    <div class="dashRow"></div>
  </div>
</template>

<script>
import PieChartView from "@/components/PieChartView.vue";
// import DataCards from "@/components/DataCards.vue";

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
  justify-content: center;
  align-items: center;
  width: 33%;
  height: 20rem;
  padding: 1rem 0rem;
  padding-right: 2rem;
  position: relative;
  z-index: 3;
}
.bookPies::before {
  content: "Genders";
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
</style>
