var path = window.location.pathname;

switch(path)
{
    case "/cliente":
        var item = document.getElementById("sidebar-cliente");
        item.classList.add('active');
        break;
    case "/fornecedor":
        var item = document.getElementById("sidebar-fornecedor");
        item.classList.add('active');
        break;
    case "/produto":
        var item = document.getElementById("sidebar-produto");
        item.classList.add('active');
        break;
    case "/venda":
        var item = document.getElementById("sidebar-venda");
        item.classList.add('active');
        break;
}

const inputIdFornecedor = document.getElementById("id_fornecedor_produto")
const rows = document.querySelectorAll("tr")

function btnClickIdFornecedor(id) {
    inputIdFornecedor.value = id;
    TableRowLimparClassesDeEstilo();
    TableRowAdicionarClasseSucesso(id);
}

function TableRowLimparClassesDeEstilo(){
    rows.forEach(function(row) {
        row.classList.remove("table-success")
    });
}

function TableRowAdicionarClasseSucesso(id){
    rows.forEach(function(row) {
        if (row.id == id){
            row.classList.add("table-success");
        } 
    });
}

function submitForm() {
    var formData = {
        'nome': document.getElementById('nome_produto').value,
        'valor': parseFloat(document.getElementById('valor_produto').value),
        'data_validade': document.getElementById('validade_produto').value,
        'id_fornecedor': parseInt(document.getElementById('id_fornecedor_produto').value)
    };
    
    fetch('/cadastrar_produto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
}
