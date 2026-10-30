/**
 * Dashboard & Progress Charts with Chart.js
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Subject-wise Performance Bar Chart
  const subjectChartCanvas = document.getElementById('subjectPerformanceChart');
  if (subjectChartCanvas && window.dashboardData && window.dashboardData.subjects) {
    const labels = window.dashboardData.subjects.map(s => s.subject_name);
    const scores = window.dashboardData.subjects.map(s => s.accuracy);

    new Chart(subjectChartCanvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Subject Accuracy (%)',
          data: scores,
          backgroundColor: scores.map(score => {
            if (score < 40) return '#ef4444'; // Weak
            if (score <= 70) return '#f59e0b'; // Average
            return '#10b981'; // Strong
          }),
          borderRadius: 6,
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            ticks: {
              callback: value => value + '%'
            },
            title: {
              display: true,
              text: 'Accuracy (%)'
            }
          },
          x: {
            ticks: {
              maxRotation: 45,
              minRotation: 20
            }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: ctx => `Score: ${ctx.raw}%`
            }
          }
        }
      }
    });
  }

  // 2. Topic-wise Performance Horizontal Bar Chart
  const topicChartCanvas = document.getElementById('topicPerformanceChart');
  if (topicChartCanvas && window.dashboardData && window.dashboardData.topics) {
    // Sort topics weakest to strongest for clear presentation
    const sortedTopics = [...window.dashboardData.topics].sort((a, b) => a.accuracy - b.accuracy);
    const topicLabels = sortedTopics.map(t => t.topic_name.length > 25 ? t.topic_name.slice(0, 25) + '...' : t.topic_name);
    const topicScores = sortedTopics.map(t => t.accuracy);

    new Chart(topicChartCanvas, {
      type: 'bar',
      data: {
        labels: topicLabels,
        datasets: [{
          axis: 'y',
          label: 'Accuracy (%)',
          data: topicScores,
          backgroundColor: topicScores.map(score => {
            if (score < 40) return 'rgba(239, 68, 68, 0.85)';
            if (score <= 70) return 'rgba(245, 158, 11, 0.85)';
            return 'rgba(16, 185, 129, 0.85)';
          }),
          borderColor: topicScores.map(score => {
            if (score < 40) return '#b91c1c';
            if (score <= 70) return '#b45309';
            return '#047857';
          }),
          borderWidth: 1,
          borderRadius: 4
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          x: {
            beginAtZero: true,
            max: 100,
            ticks: {
              callback: value => value + '%'
            }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: ctx => `Accuracy: ${ctx.raw}%`
            }
          }
        }
      }
    });
  }

  // 3. Topic Classification Distribution Doughnut Chart (Weak / Average / Strong)
  const distributionCanvas = document.getElementById('distributionDoughnutChart');
  if (distributionCanvas && window.dashboardData && window.dashboardData.counts) {
    const counts = window.dashboardData.counts;

    new Chart(distributionCanvas, {
      type: 'doughnut',
      data: {
        labels: ['Weak (<40%)', 'Average (40-70%)', 'Strong (>70%)'],
        datasets: [{
          data: [counts.weak || 0, counts.average || 0, counts.strong || 0],
          backgroundColor: ['#ef4444', '#f59e0b', '#10b981'],
          borderWidth: 2,
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              padding: 15,
              usePointStyle: true
            }
          }
        },
        cutout: '65%'
      }
    });
  }

  // 4. Progress / Historical Comparison Chart (Previous vs Current vs All Attempts)
  const progressChartCanvas = document.getElementById('progressComparisonChart');
  if (progressChartCanvas && window.progressData && window.progressData.attempts) {
    const attempts = window.progressData.attempts;
    const attemptLabels = attempts.map((a, idx) => `Attempt ${a.attempt_number} (${a.attempt_type})`);
    const scores = attempts.map(a => a.score_percentage);

    new Chart(progressChartCanvas, {
      type: 'line',
      data: {
        labels: attemptLabels,
        datasets: [{
          label: 'Overall Score (%)',
          data: scores,
          borderColor: '#2563eb',
          backgroundColor: 'rgba(37, 99, 235, 0.1)',
          pointBackgroundColor: scores.map(s => (s >= 70 ? '#10b981' : (s >= 40 ? '#f59e0b' : '#ef4444'))),
          pointRadius: 6,
          pointHoverRadius: 8,
          borderWidth: 3,
          tension: 0.25,
          fill: true
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            ticks: {
              callback: value => value + '%'
            },
            title: {
              display: true,
              text: 'Score (%)'
            }
          }
        },
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: ctx => `Score: ${ctx.raw}%`
            }
          }
        }
      }
    });
  }
});
