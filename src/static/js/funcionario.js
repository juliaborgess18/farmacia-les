async function submeterFormulario(event) {
    // Coletando dados do formulário
    event.preventDefault(); // Evita o comportamento padrão de submissão do formulário
    
    // Obtém os elementos do formulário
    const form = event.target;
    const nome = document.getElementById("nome_funcionario").value;
    const sobrenome = document.getElementById("sobrenome_funcionario").value;
    const dataNascimento = document.getElementById("data_nascimento_funcionario").value;
    const cpf = document.getElementById("cpf_funcionario").value;
    const telContato = document.getElementById("celular_funcionario").value;
    const dataAdmissao = document.getElementById("data_admissao_funcionario").value;
    const cargo = document.getElementById("cargo_funcionario").value;
    const salario = document.getElementById("salario_funcionario").value;
    
    const rua = document.getElementById("rua_endereco_funcionario").value;
    const numero = document.getElementById("numero_endereco_funcionario").value;
    const bairro = document.getElementById("bairro_endereco_funcionario").value;
    const cidade = document.getElementById("cidade_endereco_funcionario").value;
    const uf = document.getElementById("uf_endereco_funcionario").value;

    // Cria o objeto de dados
    const data = {
        nome: nome,
        sobrenome: sobrenome,
        data_nascimento: dataNascimento,
        cpf: cpf,
        tel_contato: telContato,
        data_admissao: dataAdmissao,
        cargo: cargo,
        salario: salario,
        endereco: {
            rua: rua,
            numero: numero,
            bairro: bairro,
            cidade: cidade,
            uf: uf
        }
    };

    console.log("Dados do formulário:", data);

    try {
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
            alert('Funcionário cadastrado com sucesso.');
            form.reset(); // Opcional: Resetar o formulário após o sucesso
        } else {
            alert('Erro ao cadastrar funcionário.');
        }
    } catch (error) {
        console.error("Erro ao submeter o formulário", error);
        alert('Erro ao cadastrar funcionário.');
    }
}

