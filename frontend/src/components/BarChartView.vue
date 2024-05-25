<template>
  <Bar class="barChart" :data="chartData" :options="chartOptions" />
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";
import ChartDataLabels from "chartjs-plugin-datalabels";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  ChartDataLabels
);

export default {
  name: "BarChartView",
  props: {
    barData: {
      type: Array,
      required: true,
      default: () => [
        ["Jan'24", 0],
        ["Feb'24", 0],
        ["Mar'24", 0],
        ["Apr'24", 0],
        ["May'24", 0],
        ["Jun'24", 2],
        ["Jul'24", 0],
        ["Aug'24", 0],
        ["Sep'24", 0],
        ["Oct'24", 0],
        ["Nov'24", 0],
        ["Dec'24", 0],
      ],
    },
  },
  components: {
    Bar,
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        // layout: {
        //   padding: {
        //     top: 50,
        //   },
        // },
        title: {
          display: true,
          text: "Past 12 months Activity Tracker",
          font: {
            size: 18,
            weight: "bold",
          },
        },
        scales: {
          x: {
            ticks: {
              color: "#4a4a4a",
              font: {
                family: "Poppins",
                size: 10,
                weight: "bold",
              },
              padding: 10,
            },
            grid: {
              color: "rgba(200, 200, 200, 0.3)",
              lineWidth: 1,
              drawOnChartArea: true,
              drawTicks: false,
            },
          },
          y: {
            ticks: {
              color: "#4a4a4a",
              font: {
                family: "Poppins",
                size: 10,
                weight: "bold",
              },
              padding: 10,
            },
            grid: {
              color: "rgba(200, 200, 200, 0.3)",
              lineWidth: 1,
              drawOnChartArea: true,
              drawTicks: false,
            },
          },
        },
        plugins: {
          legend: {
            display: false,
          },
          datalabels: {
            color: "white",
            font: {
              size: 12,
              weight: "bold",
              family: "Poppins",
            },
          },
        },
      },
    };
  },
  computed: {
    chartData() {
      const labels = this.barData.map((item) => item[0]);
      const data = this.barData.map((item) => item[1]);
      return {
        labels: labels,
        datasets: [
          {
            label: "Activity",
            backgroundColor: this.createGradient,
            borderColor: "#ffffff",
            borderRadius: 5,
            borderWidth: 2,
            data: data,
          },
        ],
      };
    },
  },
  methods: {
    createGradient(context) {
      const chart = context.chart;
      const { ctx, chartArea } = chart;

      if (!chartArea) {
        return null;
      }

      const gradient = ctx.createLinearGradient(
        0,
        chartArea.top,
        0,
        chartArea.bottom
      );
      gradient.addColorStop(0, "rgba(121, 241, 164, 1)"); // Start color
      gradient.addColorStop(1, "rgba(71, 171, 168, 1)"); // End color

      return gradient;
    },
  },
};
</script>

<style scoped>
.barChart {
  height: 100%;
  width: 100%;
}
</style>
