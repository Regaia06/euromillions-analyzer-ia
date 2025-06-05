let chart, chartEtoile;

function fetchAnalyse() {
  const excludeLast = document.getElementById('exclude_last').value;
  const jour = document.getElementById('jour').value;
  const startDate = document.getElementById('start_date').value;
  const endDate = document.getElementById('end_date').value;

  const url = `/api/analyse?exclude_last=${excludeLast}&jour=${jour}&start_date=${startDate}&end_date=${endDate}`;

  fetch(url)
    .then(res => res.json())
    .then(data => {
      const div = document.getElementById('resultat');
      if (data.error) {
        div.innerHTML = '<p style="color:red;">Erreur : ' + data.error + '</p>';
        return;
      }
      div.innerHTML = `
        <h2>Numéros les plus probables</h2>
        <p><strong>Numéros :</strong> ${data.top_nums.join(', ')}</p>
        <p><strong>Étoiles :</strong> ${data.top_etoiles.join(', ')}</p>
        <h3>Scores de probabilité</h3>
        <ul>
          ${data.top_nums.map(n => `<li>${n} → ${data.score_nums[n]}</li>`).join('')}
          ${data.top_etoiles.map(e => `<li>Étoile ${e} → ${data.score_etoiles[e]}</li>`).join('')}
        </ul>
        <p><em>Basé sur ${data.filtrés} tirages après filtres.</em></p>
      `;

      const ctx = document.getElementById('graph').getContext('2d');
      const ctx2 = document.getElementById('graph2').getContext('2d');

      const labels = Object.keys(data.freq_nums).map(Number).sort((a, b) => a - b);
      const values = labels.map(l => data.freq_nums[l]);

      const stars = Object.keys(data.freq_etoiles).map(Number).sort((a, b) => a - b);
      const valuesEtoile = stars.map(s => data.freq_etoiles[s]);

      if (chart) chart.destroy();
      chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [{
            label: 'Fréquence des numéros',
            data: values,
            backgroundColor: 'rgba(54, 162, 235, 0.6)'
          }]
        },
        options: { scales: { y: { beginAtZero: true } } }
      });

      if (chartEtoile) chartEtoile.destroy();
      chartEtoile = new Chart(ctx2, {
        type: 'bar',
        data: {
          labels: stars,
          datasets: [{
            label: 'Fréquence des étoiles',
            data: valuesEtoile,
            backgroundColor: 'rgba(255, 206, 86, 0.6)'
          }]
        },
        options: { scales: { y: { beginAtZero: true } } }
      });
    });
}