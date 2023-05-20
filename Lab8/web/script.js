// Listen for path form submission and fetch logs
const pathForm = document.getElementById('path-form');
pathForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const path = new FormData(pathForm).get('path');

  eel.read_logs(path)(({status, logs}) => {
    if (status === 'success') {
      // Display all fetched logs
      displayLogs(logs);

      // Set start date to the first date in the logs
      eel.get_js_date(logs[0])((date) => {
        document.getElementById('start-date').valueAsDate = new Date(date);
      });

      // Set end date to the last date in the logs
      eel.get_js_date(logs.at(-1))((date) => {
        document.getElementById('end-date').valueAsDate = new Date(date);
      });

      // Listen for changes in log selection and display log details
      const logsForm = document.getElementById('logs');
      logsForm.addEventListener('change', (e) => {
        e.preventDefault();
        const log = new FormData(logsForm).get('log');
        showLogDetails(log);
      });

      // Listen for changes in date range and filter logs accordingly
      const dateRangeForm = document.getElementById('date-range-form');
      dateRangeForm.addEventListener('change', (e) => {
        e.preventDefault();
        const startDate = new FormData(dateRangeForm).get('start-date');
        const endDate = new FormData(dateRangeForm).get('end-date');

        eel.filter_logs_by_date(logs, startDate, endDate)(displayLogs);
        resetLogDetails();
      });
    } else {
      document.getElementById('logs').innerHTML = `<p id="not-found-err">File not found</p>`;
      resetLogDetails();
    }
  });
});

document.getElementById('next-btn').addEventListener('click', (e) => {
  e.preventDefault();
  selectNextLog();
});

document.getElementById('prev-btn').addEventListener('click', (e) => {
  e.preventDefault();
  selectPreviousLog();
});

const displayLogs = (logs) => {
  document.getElementById('logs').innerHTML = logs.map((log, index) =>
    `<input id="log-${index}" type="radio" name="log" value='${log}' style="display: none"><label for="log-${index}">${log.slice(0, 50)}...</label>`
  ).join('');
}

const showLogDetails = (log) => {
  eel.get_log_details(log)((details) => {
    document.getElementById('host').innerText = details['host'];
    document.getElementById('date').innerText = details['date'];
    document.getElementById('time').innerText = details['time'];
    document.getElementById('timezone').innerText = details['timezone'];
    document.getElementById('status-code').innerText = details['status_code'];
    document.getElementById('method').innerText = details['method'];
    document.getElementById('resource').innerText = details['resource'];
    document.getElementById('size').innerText = details['size'];
  });
}

const resetLogDetails = () => {
  document.getElementById('host').innerText = '';
  document.getElementById('date').innerText = '';
  document.getElementById('time').innerText = '';
  document.getElementById('timezone').innerText = '';
  document.getElementById('status-code').innerText = '';
  document.getElementById('method').innerText = '';
  document.getElementById('resource').innerText = '';
  document.getElementById('size').innerText = '';
}

const selectNextLog = () => {
  const selectedLog = document.querySelector('input[name="log"]:checked');
  if (selectedLog) {
    // Next sibling twice because of the label
    const nextLog = selectedLog.nextElementSibling.nextElementSibling;

    if (nextLog && nextLog.type === 'radio') {
      nextLog.checked = true;
      showLogDetails(nextLog.value);
    }
  }
}

const selectPreviousLog = () => {
  const selectedLog = document.querySelector('input[name="log"]:checked');
  if (selectedLog) {
    // Previous sibling twice because of the label
    const previousLog = selectedLog.previousElementSibling.previousElementSibling;

    if (previousLog && previousLog.type === 'radio') {
      previousLog.checked = true;
      showLogDetails(previousLog.value);
    }
  }
}
