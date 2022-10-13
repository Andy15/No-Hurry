const width_threshold = 480;

function drawLineChart() {
    if ($("#lineChart").length) {
        ctxLine = document.getElementById("lineChart").getContext("2d");
        optionsLine = {
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "Hits"
                    }
                }]
            }
        };

        // Set aspect ratio based on window width
        optionsLine.maintainAspectRatio =
            $(window).width() < width_threshold ? false : true;

        configLine = {
            type: "line",
            data: {
                labels: [
                    "星期一",
                    "星期二",
                    "星期三",
                    "星期四",
                    "星期五",
                    "星期六",
                    "星期七"
                ],
                datasets: [{
                        label: "计算机与大数据学院",
                        data: [88, 68, 79, 57, 50, 55, 70],
                        fill: false,
                        borderColor: "rgb(75, 192, 192)",
                        cubicInterpolationMode: "monotone",
                        pointRadius: 0
                    },
                    {
                        label: "数学与统计学院",
                        data: [33, 45, 37, 21, 55, 74, 69],
                        fill: false,
                        borderColor: "rgba(255,99,132,1)",
                        cubicInterpolationMode: "monotone",
                        pointRadius: 0
                    },
                    {
                        label: "外国语学院",
                        data: [44, 19, 38, 46, 85, 66, 79],
                        fill: false,
                        borderColor: "rgba(153, 102, 255, 1)",
                        cubicInterpolationMode: "monotone",
                        pointRadius: 0
                    }
                ]
            },
            options: optionsLine
        };

        lineChart = new Chart(ctxLine, configLine);
    }
}

function drawBarChart() {
    if ($("#barChart").length) {
        ctxBar = document.getElementById("barChart").getContext("2d");

        optionsBar = {
            responsive: true,
            scales: {
                yAxes: [{
                    barPercentage: 0.2,
                    ticks: {
                        beginAtZero: true
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "星期"
                    }
                }]
            }
        };

        optionsBar.maintainAspectRatio =
            $(window).width() < width_threshold ? false : true;

        /**
         * COLOR CODES
         * Red: #F7604D
         * Aqua: #4ED6B8
         * Green: #A8D582
         * Yellow: #D7D768
         * Purple: #9D66CC
         * Orange: #DB9C3F
         * Blue: #3889FC
         */

        configBar = {
            type: "horizontalBar",
            data: {
                labels: ["星期一",
                    "星期二",
                    "星期三",
                    "星期四",
                    "星期五",
                    "星期六",
                    "星期七"
                ],
                datasets: [{
                    label: "# of Days",
                    data: [70, 66, 68, 49, 77, 72, 74],
                    backgroundColor: [
                        "#F7604D",
                        "#4ED6B8",
                        "#A8D582",
                        "#D7D768",
                        "#9D66CC",
                        "#DB9C3F",
                        "#3889FC"
                    ],
                    borderWidth: 0
                }]
            },
            options: optionsBar
        };

        barChart = new Chart(ctxBar, configBar);
    }
}

function drawPieChart() {
    if ($("#pieChart").length) {
        var chartHeight = 300;

        $("#pieChartContainer").css("height", chartHeight + "px");

        ctxPie = document.getElementById("pieChart").getContext("2d");

        optionsPie = {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 10,
                    right: 10,
                    top: 10,
                    bottom: 10
                }
            },
            legend: {
                position: "top"
            }
        };

        configPie = {
            type: "pie",
            data: {
                datasets: [{
                    data: [20, 54, 50],
                    backgroundColor: ["#F7604D", "#4ED6B8", "#A8D582"],
                    label: "Storage"
                }],
                labels: [
                    "计算机与大数据学院 (20人次)",
                    "数学与统计学院 (54人次)",
                    "外国语学院 (50人次)"
                ]
            },
            options: optionsPie
        };

        pieChart = new Chart(ctxPie, configPie);
    }
}

function updateLineChart() {
    if (lineChart) {
        lineChart.options = optionsLine;
        lineChart.update();
    }
}

function updateBarChart() {
    if (barChart) {
        barChart.options = optionsBar;
        barChart.update();
    }
}