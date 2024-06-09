function submeterFormulario() {
    // Coletando dados do formulário
    const id_cliente = 0;
    const id_endereco = 0;
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


