let lista_items_devolucao = []

function btnClickIdVenda(idProduto, qtde) {
    const rows = document.querySelectorAll("tr")

    var item = {
        qtde: qtde,
        id_produto: idProduto
    }
    
    ControladorListaItens(idProduto, item, rows)
    }
    
function ControladorListaItens(idProduto, novoItem, rows){
    let existe = lista_items_devolucao.some(function(item) {
        return item.id_produto === novoItem.id_produto;
    });

    if (!existe) {
        lista_items_devolucao.push(novoItem);
        TableRowAdicionarClasseSucesso(idProduto, rows);
    } else{
        lista_items_devolucao = removerItem(lista_items_devolucao, idProduto)
        TableRowRemoverClasseSucesso(idProduto, rows);
    }

}

function ControladorTableRow(idProduto, row){
    lista_items_devolucao.forEach(function(item, index) {
        if(idProduto == item.id_produto){
            TableRowRemoverClasseSucesso(idProduto, row)
        } else{
            TableRowAdicionarClasseSucesso(idProduto, row)
        }
    });
}

function TableRowAdicionarClasseSucesso(idProduto, rows){
    rows.forEach(function(row) {
        if (row.id == idProduto){
            row.classList.add("table-success");
        } 
    });
}

function TableRowRemoverClasseSucesso(idProduto, rows){
    rows.forEach(function(row) {
        if (row.id == idProduto){
            row.classList.remove("table-success");
        } 
    });
}

function removerItem(lista, id_produto) {
    return lista.filter(function(item) {
        return  item.id_produto !== id_produto;
    });
}


function calcValorTotal(rows){
    var valor_total = 0
    rows.forEach(function(row) {
        
        lista_items_devolucao.forEach(function(item, index){
            if(item.id_produto === row.id){
                var tableData = document.getElementById("valor-"+item.id_produto)
                valor_total+=parseInt(tableData.textContent);
            }
        });
    })
    return valor_total
}

async function submitFormCadastro(event){
    event.preventDefault();

    const rows = document.querySelectorAll("tr")
    var valor_total = calcValorTotal(rows).toString()
    var formData = {
        'id_venda': document.getElementById("th_id_venda").textContent,
        'valor_devolucao': valor_total,
        'itens_devolucao': lista_items_devolucao,
    };
    
    console.log(JSON.stringify(formData))
    fetch('/api/cadastrar_devolucao', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    }).then(response => {
        if (response.ok) {
            alert("Devolução cadastrada com sucesso.")
        } else {
            alert("Erro ao cadastrar a devolução.")
        }
    })
}

async function submitFormRemover(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const id_devolucao = formData.get('id_devolucao');

    const response = await fetch(`${form.action}?id_devolucao=${id_devolucao}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Devolução removida com sucesso!');
    } else {
        alert('Erro ao remover a devolução!');
    }
}

function btnClickEditarDevolucao(qtde, id){
    const inputQtde = document.getElementById("input_qtde")
    inputQtde.value=qtde
    const rows = document.querySelectorAll("tr")
    TableRowLimparClassesDeEstilo(rows);
    TableRowAdicionarClasseSucesso(id, rows)
}

function TableRowLimparClassesDeEstilo(rows){
    rows.forEach(function(row) {
        row.classList.remove("table-success")
    });
}

async function submitFormEditar(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const data = Object.fromEntries(formData.entries());
    console.log(JSON.stringify(data))
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

