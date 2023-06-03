// Listen for path form submission and fetch logs
const dbForm = document.getElementById('db-form');
dbForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const dbName = new FormData(dbForm).get('db');

  eel.get_all_stations(dbName)(({status, stations}) => {
    if (status === 'success') {
      // Display all fetched logs
      displayStations(stations);

      // Listen for changes in station selection and display station details
      const stationsForm = document.getElementById('stations');
      stationsForm.addEventListener('change', (e) => {
        e.preventDefault();
        const stationId = new FormData(stationsForm).get('station');
        showStationStats(dbName, stationId);
      });
    } else {
      document.getElementById('stations').innerHTML = `<p id="not-found-err">File not found</p>`;
      resetStationStats();
    }
  });
});

const displayStations = (stations) => {
  document.getElementById('stations').innerHTML = stations.map((station, index) =>
    `<input id="station-${index}" type="radio" name="station" value='${station.station_id}' style="display: none"><label for="station-${index}">${station.station_name}</label>`
  ).join('');
}

const showStationStats = (dbName, stationId) => {
  eel.calculate_statistics(dbName, stationId)((details) => {
    document.getElementById('time-from').innerText = details['mean_time_from'];
    document.getElementById('time-to').innerText = details['mean_time_to'];
    document.getElementById('diff-bikes').innerText = details['different_bikes'];
  });
}

const resetStationStats = () => {
  document.getElementById('time-from').innerText = '';
  document.getElementById('time-to').innerText = '';
  document.getElementById('diff-bikes').innerText = '';
}
