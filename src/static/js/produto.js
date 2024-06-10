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

// function submeterFormularioCadastro() {
//     var formData = {
//         'nome': document.getElementById('nome_produto').value,
//         'valor': parseFloat(document.getElementById('valor_produto').value),
//         'data_validade': document.getElementById('validade_produto').value,
//         'id_fornecedor': parseInt(document.getElementById('id_fornecedor_produto').value)
//     };
    
//     fetch('/api/cadastrar_produto', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(formData),
//     }).then(response => {
//         if (response.ok) {
//             alert("Produto cadastrado com sucesso.")
//         } else {
//             alert("Erro ao cadastrar o produto.")
//         }
//     })
// }

async function submitFormCadastro(event){
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    const response = await fetch(form.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Produto cadastrado com sucesso.');
    } else {
        alert('Erro ao cadastrar o produto.');
    }
}

async function submitFormEditar(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const data = Object.fromEntries(formData.entries());

    const response = await fetch(form.action, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Produto alterado com sucesso!');
    } else {
        alert('Erro ao alterar o produto!');
    }
}

async function submitFormRemover(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const id_produto = formData.get('id_produto');

    const response = await fetch(`${form.action}?id_produto=${id_produto}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Produto removido com sucesso!');
    } else {
        alert('Erro ao remover o produto!');
    }
}