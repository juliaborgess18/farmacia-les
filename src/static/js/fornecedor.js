async function cadastrarFornecedor(event) {
    // Coletando dados do formulário
    event.preventDefault(); // Evita o comportamento padrão de submissão do formulário
    
    // Obtém os elementos do formulário
    const form = event.target;
    const nome = document.getElementById("nome_fornecedor").value;
    const cnpj = document.getElementById("cnpj_fornecedor").value;
    const email = document.getElementById("email_fornecedor").value;
    const telefone = document.getElementById("telefone_fornecedor").value;

    const rua = document.getElementById("rua_endereco_fornecedor").value;
    const numero = document.getElementById("numero_endereco_fornecedor").value;
    const bairro = document.getElementById("bairro_endereco_fornecedor").value;
    const cidade = document.getElementById("cidade_endereco_fornecedor").value;
    const uf = document.getElementById("uf_endereco_fornecedor").value;

    // Cria o objeto de dados
    const data = {
        nome: nome,
        cnpj: cnpj,
        email: email,
        telefone: telefone,
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
            alert('Fornecedor cadastrado com sucesso.');
            form.reset(); // Opcional: Resetar o formulário após o sucesso
        } else {
            alert('Erro ao cadastrar fornecedor.');
        }
    } catch (error) {
        console.error("Erro ao submeter o formulário", error);
        alert('Erro ao cadastrar fornecedor.');
    }
}
