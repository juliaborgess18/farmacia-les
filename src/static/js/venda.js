    let produtos = [];

    function adicionarProduto() {
        const idProduto = document.getElementById('id_produto').value;
        const nomeProduto = document.getElementById('id_produto').value; // Não temos o nome do produto aqui, você pode adicioná-lo de outra forma
        const quantidadeProduto = document.getElementById('quantidade_produto').value;

        if (idProduto && quantidadeProduto) {
            produtos.push({ id: idProduto, nome: nomeProduto, quantidade: quantidadeProduto });
            atualizarListaProdutos();
            document.getElementById('id_produto').value = '';
            document.getElementById('quantidade_produto').value = '';
        } else {
            alert('Por favor, preencha todos os campos do produto.');
        }
    }

    function removerProduto(index) {
        produtos.splice(index, 1);
        atualizarListaProdutos();
    }

    function atualizarListaProdutos() {
        const tbody = document.getElementById('lista_produtos').getElementsByTagName('tbody')[0];
        tbody.innerHTML = '';

        produtos.forEach((produto, index) => {
            const row = tbody.insertRow();
            const cellNomeProduto = row.insertCell(0);
            const cellQuantidade = row.insertCell(1);
            const cellAcoes = row.insertCell(2);

            cellNomeProduto.textContent = produto.nome;
            cellQuantidade.textContent = produto.quantidade;
            cellAcoes.innerHTML = `<button class="btn btn-danger" type="button" onclick="removerProduto(${index})">Remover</button>`;
        });
    }

    document.getElementById('form_venda').addEventListener('submit', function (event) {
        event.preventDefault();

        const idFuncionario = document.getElementById('id_funcionario').value;
        const idCliente = document.getElementById('id_cliente').value;
        const idFormaPagamento = document.getElementById('id_forma_pagamento').value;

        if (!idFuncionario || !idCliente || !idFormaPagamento || produtos.length === 0) {
            alert('Por favor, preencha todos os campos e adicione pelo menos um produto.');
            return;
        }

        // Obter a data atual
        const dataAtual = new Date();
        const dataVenda = `${dataAtual.getFullYear()}-${(dataAtual.getMonth() + 1).toString().padStart(2, '0')}-${dataAtual.getDate().toString().padStart(2, '0')}`;

        const dadosVenda = {
            id_funcionario: idFuncionario,
            id_cliente: idCliente,
            id_forma_pagamento: idFormaPagamento,
            data_venda: dataVenda, // Inclua a data da venda nos dados enviados
            produtos: produtos
        };

        console.log('Dados da Venda:', dadosVenda);

        fetch('/api/cadastrar_venda', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dadosVenda),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Successo:', data);
            document.getElementById('form_venda').reset();
            produtos = [];
            atualizarListaProdutos();
            alert('Venda cadastrada com sucesso!');
        })
        .catch((error) => {
            console.error('Erro:', error);
            alert('Erro ao cadastrar a venda.');
        });
    });
