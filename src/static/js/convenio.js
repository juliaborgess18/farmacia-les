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

// function submeterFormularioCadastro() {
//     var formData = {
//         'especialidade': document.getElementById('especialidade_convenio').value,
//         'cnpj': document.getElementById('cnpj_convenio').value,
//         'id_cliente': parseInt(document.getElementById('input_id_cliente').value)
//     };

//     console.log("Data: ", JSON.stringify(formData))
    
//     fetch('/cadastrar_convenio', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(formData),
//     }).then(response => {
//         if (response.ok) {
//             alert("Convênio cadastrado com sucesso.")
//         } else {
//             alert("Erro ao cadastrar o convênio.")
//         }
//     })
// }

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