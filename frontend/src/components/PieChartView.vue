<template>
  <div class="canvas">
    <Pie class="pieChart" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script>
import { Pie } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  DoughnutController,
} from "chart.js";
import ChartDataLabels from "chartjs-plugin-datalabels";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement,
  DoughnutController,
  ChartDataLabels
);

export default {
  name: "PieChartView",
  props: {
    pieData: {
      type: Array,
      required: true,
      default: () => [
        ["A", 0],
        ["A", 0],
        ["A", 0],
        ["A", 0],
        ["A", 0],
      ],
    },
  },
  components: {
    Pie,
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: "50%",
        layout: {
          padding: {
            top: 30,
            bottom: 20,
          },
        },
        plugins: {
          legend: {
            display: false,
          },
          datalabels: {
            anchor: "end",
            align: "end",
            // offset: 5,
            color: "#4a4a4a",
            borderWidth: 1,
            font: {
              family: "Poppins",
              size: 10,
              weight: "bold",
            },
            formatter: (value, context) => {
              return `${
                context.chart.data.labels[context.dataIndex]
              }: ${value}`;
            },
          },
        },
      },
    };
  },
  computed: {
    chartData() {
      const labels = this.pieData.map((item) => item[0]);
      const data = this.pieData.map((item) => item[1]);
      return {
        labels: labels,
        datasets: [
          {
            backgroundColor: [
              "#b6f492",
              "#92d792",
              "#74bf93",
              "#4fa193",
              "#338a92",
            ],
            data: data,
          },
        ],
      };
    },
  },
};
</script>

<style scoped>
.canvas {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  margin: 0rem 1rem;
  margin-right: 2rem;
  border-radius: 1rem;
  box-shadow: 0 0.25rem 1rem #00000026;
  backdrop-filter: blur(30px);
  -webkit-backdrop-filter: blur(30px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
.pieChart {
  height: 100%;
  width: 100%;
  /* margin: 1rem; */
}
</style>
