// Copyright 2023 David Cordero Rosales
// 
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
// 
//     http://www.apache.org/licenses/LICENSE-2.0
// 
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

var tblSale;

function format(d) {
    console.log(d);
    var html = '<table class="table">';
    html += '<thead class="thead-dark">';
    html += '<tr><th scope="col">Producto</th>';
    html += '<th scope="col">Categoría</th>';
    html += '<th scope="col">PVP</th>';
    html += '<th scope="col">Cantidad</th>';
    html += '<th scope="col">Subtotal</th></tr>';
    html += '</thead>';
    html += '<tbody>';
    $.each(d.det, function (key, value) {
        html+='<tr>'
        html+='<td>'+value.prod.name+'</td>'
        html+='<td>'+value.prod.cat.name+'</td>'
        html+='<td>'+value.price+'</td>'
        html+='<td>'+value.cant+'</td>'
        html+='<td>'+value.subtotal+'</td>'
        html+='</tr>';
    });
    html += '</tbody>';
    return html;
}

$(function () {

    tblSale = $('#data').DataTable({
        responsive: true,
        scrollX: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {
                "className": 'details-control',
                "orderable": false,
                "data": null,
                "defaultContent": ''
            },
            {"data": "cli.names"},
            {"data": "date_joined"},
            {"data": "fpago"},
            {"data": "subtotal"},
            {"data": "desc"},
            {"data": "total"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-2, -3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return '$' + parseFloat(data).toFixed(2);
                }
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/sale/delete/' + row.id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
                    buttons += '<a href="/sale/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
                    buttons += '<a href="/sale/invoice/pdf/'+row.id+'/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    $('#data tbody')
        .on('click', 'a[rel="details"]', function () {
            var tr = tblSale.cell($(this).closest('td, li')).index();
            var data = tblSale.row(tr.row).data();
            console.log(data);

            $('#tblDet').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                //data: data.det,
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        'action': 'search_details_prod',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": "prod.name"},
                    {"data": "prod.cat.name"},
                    {"data": "price"},
                    {"data": "cant"},
                    {"data": "subtotal"},
                ],
                columnDefs: [
                    {
                        targets: [-1, -3],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return '$' + parseFloat(data).toFixed(2);
                        }
                    },
                    {
                        targets: [-2],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    },
                ],
                initComplete: function (settings, json) {

                }
            });

            $('#myModelDet').modal('show');
        })
        .on('click', 'td.details-control', function () {
            var tr = $(this).closest('tr');
            var row = tblSale.row(tr);
            if (row.child.isShown()) {
                row.child.hide();
                tr.removeClass('shown');
            } else {
                row.child(format(row.data())).show();
                tr.addClass('shown');
            }
        });

});