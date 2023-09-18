// Функция для переключения видимости выпадающего списка по его ID
function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    if (dropdown) {
        dropdown.classList.toggle("show");
    }
}

// Закрыть выпадающий список, если пользователь кликнул вне его
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.querySelectorAll(".dropdown-content.show");
        dropdowns.forEach(function (dropdown) {
            dropdown.classList.remove('show');
        });
    }
}


$("#myTable").DataTable({
    // Datatables configuration
    paging: true,       // Pagination
    pageLength: 10,     // Rows per page
    lengthChange: true, // Show enties per page
    autoWidth: true,    // Control the auto width on columns
    searching: true,    // Input search
    bInfo: true,        // Info on footer
    bSorting: true,     // Filter A to Z and Z to A (and numbers)
});


// Ждем 5 секунд и скрываем сообщение
setTimeout(function () {
    var alertMessage = document.getElementById('alertMessage');
    if (alertMessage) {
        alertMessage.style.display = 'none';
    }
}, 5000); // 5000 миллисекунд = 5 секунд