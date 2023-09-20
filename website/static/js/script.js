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
    order: [0, 'desc'], // 'asc'
    //                  // scrollY: 800 vertical scrolling
    colReorder: {       // reorder columns
        realtime: false
    },
    paging: true,       // Pagination
    pageLength: 10,     // Rows per page
    lengthChange: true, // Show entries per page
    autoWidth: true,    // Control the auto width on columns
    searching: true,    // Input search
    bInfo: true,        // Info on footer
    bSorting: true,     // Filter A to Z and Z to A (and numbers)
    // Disable columns with specific filter A to Z, Z to A
    "columnDefs": [{
        "targets": [-1],   // More than 1 [4, 5, 6]
        "orderable": false,
    }],
    // BUTTONS
    dom: 'lBfrtip',
    buttons: [
        {   // COPY
            extend: 'copy',
            text: '<i class="fas fa-clone"></i>',
            className: 'btn btn-primary',
            titleAttr: 'Copy',
            // Choose the columns you want to copy
            exportOptions: {
                columns: ':not(.exclude-column)' // [0, 1, 3, 5], "_all", ':not(:last-child)'
            },
        },
        {   // Excel
            extend: 'excel',
            text: '<i class="fas fa-file-excel"></i>',
            className: 'btn btn-primary',
            titleAttr: 'Excel',
            // Choose the columns you want to export to excel
            exportOptions: {
                columns: ':not(.exclude-column)'  // [0, 1, 3, 5], "_all", ':not(:last-child)'
            },
        },
        {   // Print
            extend: 'print',
            text: '<i class="fas fa-print"></i>',
            className: 'btn btn-primary',
            titleAttr: 'Print',
            // Choose the columns you want to print
            exportOptions: {
                columns: ':not(.exclude-column)'  // [0, 1, 3, 5], "_all", ':not(:last-child)'
            },
            // Font size (when export ti print)
            customize: function (win) {
                $(win.document.body).css('font-size', '10pt')
                $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size', 'inherit');
            }
        },

        {   // PDF
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"></i>',
            className: 'btn btn-primary',
            titleAttr: 'PDF',
            // Choose the columns you want to export to pdf
            exportOptions: {
                columns: ':not(.exclude-column)'  // [0, 1, 3, 5], "_all", ':not(:last-child)'
            },
            // Center the table
            tableHeader: {
                alignment: 'center'
            },
            // Font size and optimazation
            customize: function (doc) {
                doc.styles.tableHeader.alignment = 'center';  // Header position
                doc.styles.tableBodyOdd.alignment = 'center';  // Body position 1 (grey_)
                doc.styles.tableBodyEven.alignment = 'center';  // Body position 2 (white)
                doc.styles.tableHeader.fontSize = 7;  // Header font size            }
                doc.defaultStyle.fonySize = 6;  // Body font size            }
                // To get 100% width of the table
                doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
            },
        },

    ]
});




// Enable Searchbox Outside
var newSearch = $('#myTable').DataTable();
$('#search').keyup(function () {
    newSearch.search($(this).val()).draw();
})




// Ждем 5 секунд и скрываем сообщение
setTimeout(function () {
    var alertMessage = document.getElementById('alertMessage');
    if (alertMessage) {
        alertMessage.style.display = 'none';
    }
}, 5000); // 5000 миллисекунд = 5 секунд