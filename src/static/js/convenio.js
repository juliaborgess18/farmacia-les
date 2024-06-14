function btnClickIdCliente(id) {
    const inputIdCliente = document.getElementById("input_id_cliente")
    const rows = document.querySelectorAll("tr")
    inputIdCliente.value = id;
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

async function submitFormCadastro(event){
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    console.log(JSON.stringify(data));

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
        alert('Convênio cadastrado com sucesso.');
    } else {
        alert('Erro ao cadastrar o convênio.');
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
        alert('Convênio alterado com sucesso!');
    } else {
        alert('Erro ao alterar o convênio!');
    }
}

async function submitFormRemover(event) {
    console.log("entrou no submitFormRemover")
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    const id_convenio = formData.get('id_convenio');

    const response = await fetch(`${form.action}?id_convenio=${id_convenio}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Convênio removido com sucesso!');
    } else {
        alert('Erro ao remover o convênio!');
    }
}