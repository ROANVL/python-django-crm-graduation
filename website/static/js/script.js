// SEARCH BY

function filterTableByColumn() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue, column;
    input = document.getElementsByClassName("search_by_name")[0]; // Получаем элемент ввода
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");
    column = document.getElementsByClassName('filter_by')[0].value; // Получаем выбранный столбец из выпадающего списка

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[column];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().startsWith(filter)) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}



// PAGINATION

let currentPage = 1;
let rowsPerPage = 10; // Начальное количество строк на странице
const table = document.getElementById("myTable");
const tableRows = table.querySelectorAll("tbody tr");

function displayPage() {
    const startIndex = (currentPage - 1) * rowsPerPage;
    const endIndex = startIndex + rowsPerPage;

    tableRows.forEach((row, index) => {
        if (index >= startIndex && index < endIndex) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });

    updatePageNumbers();
}

function changePage(direction) {
    const maxPage = Math.ceil(tableRows.length / rowsPerPage);

    if (direction === "prev" && currentPage > 1) {
        currentPage--;
    } else if (direction === "next" && currentPage < maxPage) {
        currentPage++;
    } else if (typeof direction === 'number' && direction >= 1 && direction <= maxPage) {
        currentPage = direction;
    }

    displayPage();
}

function changeRowsPerPage() {
    const newRowsPerPage = parseInt(document.getElementById("rowsPerPage").value);
    rowsPerPage = newRowsPerPage;
    currentPage = 1; // При изменении количества строк сбрасываем текущую страницу на первую
    displayPage();
}

function updatePageNumbers() {
    const maxPage = Math.ceil(tableRows.length / rowsPerPage);
    const pagination = document.getElementById("pagination");

    pagination.innerHTML = `
        <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
            <a class="page-link" onclick="changePage('prev')">Previous</a>
        </li>
    `;

    for (let i = 1; i <= maxPage; i++) {
        const li = document.createElement("li");
        li.className = `page-item ${i === currentPage ? 'active' : ''}`;
        const a = document.createElement("a");
        a.className = "page-link";
        a.textContent = i;
        a.onclick = () => changePage(i);
        li.appendChild(a);
        pagination.appendChild(li);
    }

    pagination.innerHTML += `
        <li class="page-item ${currentPage === maxPage ? 'disabled' : ''}">
            <a class="page-link" onclick="changePage('next')">Next</a>
        </li>
    `;
}

displayPage(); // Инициализация при загрузке страницы
updatePageNumbers(); // Обновляем номера страниц при инициализации




/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function toggleDropdown() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}


