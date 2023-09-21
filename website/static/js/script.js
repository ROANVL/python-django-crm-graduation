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


$(document).ready(function () {
    $("#myTable1").DataTable({
        // Datatables configuration
        order: [0, 'desc'], // 'asc'
        colReorder: {
            realtime: false
        },
        paging: true,
        pageLength: 10,
        lengthChange: true,
        autoWidth: true, // Adjust to fit the content within the page width
        searching: true,
        bInfo: true,
        bSorting: true,
        "columnDefs": [{
            "targets": [-1],
            "orderable": false,
            targets: ['_all'],
            className: "dt-head-center",
        }],
        dom: 'lBfrtip',
        buttons: [
            {   // COPY
                extend: 'copy',
                text: '<i class="fas fa-clone"></i>',
                className: 'btn btn-primary',
                titleAttr: 'Copy',
                exportOptions: {
                    columns: ':not(.exclude-column)'
                },
            },
            {   // Excel
                extend: 'excel',
                text: '<i class="fas fa-file-excel"></i>',
                className: 'btn btn-primary',
                titleAttr: 'Excel',
                exportOptions: {
                    columns: ':not(.exclude-column)'
                },
            },
            {   // Print
                extend: 'print',
                text: '<i class="fas fa-print"></i>',
                className: 'btn btn-primary',
                titleAttr: 'Print',
                exportOptions: {
                    columns: ':not(.exclude-column)'
                },
                customize: function (win) {
                    // Устанавливаем стили для печати
                    $(win.document.body).css('font-size', '10pt');

                    // Добавляем стили для таблицы
                    $(win.document.body).find('table')
                        .addClass('table table-bordered table-striped')
                        .css({
                            'font-size': 'inherit',
                            'page-break-inside': 'auto',
                            'width': '95%',
                            'margin': '20px' // Устанавливаем отступы от краев в портретной ориентации
                        });

                    // Добавляем стили для ландшафтной (альбомной) ориентации
                    // Обратите внимание, что здесь мы используем @media (orientation: landscape) для настройки ландшафтной ориентации.
                    $(win.document.head).append('<style>@media print { @page { size: landscape; } }</style>');
                }
            },
            {   // PDF
                extend: 'pdfHtml5',
                text: '<i class="fas fa-file-pdf"></i>',
                className: 'btn btn-primary',
                titleAttr: 'PDF',
                exportOptions: {
                    columns: ':not(.exclude-column)'
                },
                orientation: 'landscape',
                pageSize: 'A4',
                tableHeader: {
                    alignment: 'center'
                },
                customize: function (doc) {
                    doc.pageMargins = [20, 20, 20, 20]; // Adjust page margins as needed
                    doc.defaultStyle.fontSize = 7;
                    doc.styles.tableHeader.fontSize = 7;
                    // Header and footer customization
                    doc['header'] = (function () {
                        // Your header content here
                    });
                    doc['footer'] = (function (page, pages) {
                        // Your footer content here
                    });


                    // Table layout customization
                    var objLayout = {};
                    objLayout['hLineWidth'] = function (i) {
                        return 0.5;
                    };
                    objLayout['vLineWidth'] = function (i) {
                        return 0.5;
                    };
                    objLayout['hLineColor'] = function (i) {
                        return '#aaa';
                    };
                    objLayout['vLineColor'] = function (i) {
                        return '#aaa';
                    };
                    objLayout['paddingLeft'] = function (i) {
                        return 4;
                    };
                    objLayout['paddingRight'] = function (i) {
                        return 4;
                    };
                    doc.content[0].layout = objLayout;
                }
            }
        ]
    });
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