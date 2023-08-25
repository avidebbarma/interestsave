function calculateEMI() {
  var principal = parseFloat(document.getElementById('principal').value);
  var interestRate = parseFloat(document.getElementById('interest').value);
  var tenure = parseFloat(document.getElementById('tenure').value);

  var monthlyInterest = interestRate / 12 / 100;
  var months = tenure;
  var emi = (principal * monthlyInterest * Math.pow(1 + monthlyInterest, months)) / (Math.pow(1 + monthlyInterest, months) - 1);
  var totalAmount = emi * months;
  var totalInterest = totalAmount - principal;

  document.getElementById('totalAmount').textContent = "Rs. " + totalAmount.toFixed(2);
  document.getElementById('totalInterest').textContent = "Rs. " + totalInterest.toFixed(2);
  document.getElementById('emi').textContent = "Rs. " + emi.toFixed(2);

  document.getElementById('results').classList.remove('d-none');
  document.getElementById('default-chart').style.display = 'none';
  document.getElementById('pieChart').style.display = 'block';

  // Create Pie Chart
  var ctx = document.getElementById('pieChart').getContext('2d');
  var myPieChart = new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Total Interest Amount', 'Total Payable Amount'],
      datasets: [{
        data: [totalInterest, totalAmount],
        backgroundColor: ['#FF6384', '#36A2EB'],
      }]
    },
    options: {
      responsive: true,
      legend: {
        position: 'bottom',
      },
      tooltips: {
        callbacks: {
          label: function (tooltipItem, data) {
            var dataset = data.datasets[tooltipItem.datasetIndex];
            var currentValue = dataset.data[tooltipItem.index];
            return data.labels[tooltipItem.index] + ': Rs. ' + currentValue.toFixed(2);
          }
        }
      }
    }
  });
}

