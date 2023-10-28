import Chart from "chart.js/auto";

(async function () {
  const barChartData = [
    { day: "Monday", count: 10 },
    { day: "Tuesday", count: 20 },
    { day: "Wednesday", count: 15 },
    { day: "Thursday", count: 25 },
    { day: "Friday", count: 22 },
    { day: "Saturday", count: 30 },
    { day: "Sunday", count: 28 },
  ];
  const barColors = [
    "rgba(255, 0, 0, 0.5)", // Red with 0.5 transparency
    "rgba(0, 0, 255, 0.5)", // Blue with 0.5 transparency
    "rgba(0, 255, 0, 0.5)", // Green with 0.5 transparency
    "rgba(255, 165, 0, 0.5)", // Orange with 0.5 transparency
    "rgba(128, 0, 128, 0.5)", // Purple with 0.5 transparency
    "rgba(255, 192, 203, 0.5)", // Pink with 0.5 transparency
    "rgba(0, 128, 128, 0.5)", // Teal with 0.5 transparency
  ];

  new Chart(
    document.getElementById("myChart"),
    {
      type: "bar",
      data: {
        labels: barChartData.map((row) => row.day),
        datasets: [
          {
            pointStyle: "line",
            data: barChartData.map((row) => row.count),
            backgroundColor: barColors,
          },
        ],
      },
      options: {
        animations: {
          tension: {
            duration: 1000,
            easing: "linear",
            from: 0.5,
            to: 0,
            loop: true,
          },
        },
        scales: {
          y: {
            grid: {
              display: false,
            },
            title: {
              display: true,
              text: "steps",
              font: {
                size: 15,
                weight: "bold",
              },
            },
            ticks: {
              font: {
                size: 13,
                weight: "bold",
              },
            },
          },
          x: {
            grid: {
              display: false,
            },
            ticks: {
              font: {
                size: 13,
                weight: "bold",
              },
            },
          },
        },
        plugins: {
          legend: {
            display: false,
            labels: {
              font: {
                size: 25,
              },
            },
          },
        },
        elements: {
          line: {
            borderWidth: 5,
          },
        },
      },
    },
  );

  const compliancePercentage = 75; // Example compliance percentage

  const doughnutData = {
    datasets: [
      {
        data: [compliancePercentage, 100 - compliancePercentage],
        backgroundColor: ["#2ecc71", "#DDDDDD"], // You can change colors as needed
      },
    ],
    labels: ["Streak"],
  };

  new Chart(
    document.getElementById("pieChart"),
    {
      type: "doughnut",
      data: doughnutData,
      options: {
        plugins: {
          legend: {
            display: true,
            position: "bottom", // You can change the legend position
          },
        },
      },
    },
  );
})();
