var path = window.location.pathname;

if (path.includes("cliente")){
    var item = document.getElementById("sidebar-cliente");
    item.classList.add('active');
} 
if (path.includes("fornecedor")){
    var item = document.getElementById("sidebar-fornecedor");
    item.classList.add('active');
} 
if (path.includes("produto")){
    var item = document.getElementById("sidebar-produto");
    item.classList.add('active');
} 
if (path.includes("venda")){
    var item = document.getElementById("sidebar-venda");
    item.classList.add('active');
}

function btnClickIdFornecedor(id) {
    const inputIdFornecedor = document.getElementById("id_fornecedor_produto")
    const rows = document.querySelectorAll("tr")
    inputIdFornecedor.value = id;
    TableRowLimparClassesDeEstilo(rows);
    TableRowAdicionarClasseSucesso(id, rows);
}

function TableRowLimparClassesDeEstilo(rows){
    rows.forEach(function(row) {
        row.classList.remove("table-success")
    });
}

function TableRowAdicionarClasseSucesso(id, rows){
    rows.forEach(function(row) {
        if (row.id == id){
            row.classList.add("table-success");
        } 
    });
}

function submeterFormularioCadastroDeProduto() {
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
    }).then(response => {
        if (response.ok) {
            alert("Produto cadastrado com sucesso.")
        } else {
            alert("Erro ao cadastrar o produto.")
        }
    })
}
