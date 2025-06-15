let csvDataArray = [];
let sortDirection = {};
let currentSortCol = null;

function displayCSVAsTable(csvData) {
    const rows = csvData.trim().split('\n').map(row => row.split(','));
    csvDataArray = rows;
    renderTable(csvDataArray);
}

function renderTable(data) {
    const table = document.getElementById('csvTable');
    table.innerHTML = '';

    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');

    data[0].forEach((header, colIndex) => {
        const th = document.createElement('th');
        th.style.cursor = 'pointer';

        let arrow = ' ⬍';
        if (currentSortCol === colIndex) {
            arrow = sortDirection[colIndex] ? ' ▲' : ' ▼';
        }

        th.textContent = header.trim() + arrow;
        th.onclick = () => sortTableByColumn(colIndex);
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement('tbody');
    for (let i = 1; i < data.length; i++) {
        const row = document.createElement('tr');
        data[i].forEach(cell => {
            const td = document.createElement('td');
            td.textContent = cell.trim();
            row.appendChild(td);
        });
        tbody.appendChild(row);
    }

    table.appendChild(tbody);
}

function sortTableByColumn(columnIndex) {
    const isAscending = sortDirection[columnIndex] = !sortDirection[columnIndex];
    currentSortCol = columnIndex;

    const sorted = [...csvDataArray.slice(1)].sort((a, b) => {
        const valA = a[columnIndex].toLowerCase();
        const valB = b[columnIndex].toLowerCase();

        const numA = parseFloat(valA);
        const numB = parseFloat(valB);
        if (!isNaN(numA) && !isNaN(numB)) {
            return isAscending ? numA - numB : numB - numA;
        }

        return isAscending
            ? valA.localeCompare(valB)
            : valB.localeCompare(valA);
    });

    renderTable([csvDataArray[0], ...sorted]);
    filterTable();
}

function filterTable() {
    const input = document.getElementById('searchInput').value.toUpperCase();
    const table = document.getElementById('csvTable');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        let match = false;

        for (let j = 0; j < cells.length; j++) {
            if (cells[j].textContent.toUpperCase().indexOf(input) > -1) {
                match = true;
                break;
            }
        }

        rows[i].style.display = match ? '' : 'none';
    }
}

// Initial fetch
const csvUrl = 'https://raw.githubusercontent.com/parth-rathod/etf-screener-backend/refs/heads/dev/docs/etfs.csv';
fetch(csvUrl)
    .then(response => response.text())
    .then(csvData => displayCSVAsTable(csvData))
    .catch(error => console.error('Error fetching CSV:', error));