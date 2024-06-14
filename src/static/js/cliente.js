async function submeterFormulario(event) {
    // Coletando dados do formulário
    event.preventDefault(); // Evita o comportamento padrão de submissão do formulário
    const nome = document.getElementById('nome_cliente').value;
    const sobrenome = document.getElementById('sobrenome_cliente').value;
    const dataNascimento = document.getElementById('data_nascimento_cliente').value;
    const cpf = document.getElementById('cpf_cliente').value;
    const celular = document.getElementById('celular_cliente').value;
    const endereco = document.getElementById('endereco_cliente').value;
    const numero = parseInt(document.getElementById('numero_endereco_cliente').value);
    const bairro = document.getElementById('bairro_endereco_cliente').value;
    const cidade = document.getElementById('cidade_endereco_cliente').value;
    const uf = document.getElementById('uf_endereco_cliente').value;

    const clienteData = {
        nome: nome,
        sobrenome: sobrenome,
        data_nascimento: dataNascimento,
        tel_contato: celular,
        cpf: cpf,
        endereco: {
            rua: endereco,
            numero: numero,
            bairro: bairro,
            cidade: cidade,
            uf: uf
        }
    };

    // Enviando dados para o servidor
    fetch('/cadastrar_cliente', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clienteData)
    }).then(response => {
        if (response.ok) {
            alert("Cliente cadastrado com sucesso.");
        } else {
            alert("Erro ao cadastrar o cliente.");
        }
    }).catch(error => {
        console.error("Erro na requisição:", error);
        alert("Erro ao cadastrar o cliente. Por favor, tente novamente mais tarde.");
    });
}

async function removerCliente(event) {
    event.preventDefault();
    
    const form = event.target;
    const formData = new FormData(form);
    const id_cliente = formData.get('id_cliente');

    const response = await fetch(`${form.action}?id_cliente=${id_cliente}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    const result = await response.json();
    console.log(result);

    if (response.ok) {
        alert('Cliente removido com sucesso!');
    } else {
        alert('Erro ao remover o Cliente!');
    }
}

async function editarCliente(event) {
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
        alert('Cliente alterado com sucesso!');
    } else {
        alert('Erro ao alterar o cliente!');
    }
}

