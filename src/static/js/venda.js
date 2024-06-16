    let produtos = [];

    function adicionarProduto() {
        const id = document.getElementById('id_produto').value;
        const quantidade = document.getElementById('quantidade_produto').value;

        if (id && quantidade) {
            produtos.push({ id_produto: id, qtde: quantidade });
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
            const cellIdProduto = row.insertCell(0);
            const cellQuantidade = row.insertCell(1);
            const cellAcoes = row.insertCell(2);

            cellIdProduto.textContent = produto.id_produto;
            cellQuantidade.textContent = produto.qtde;
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


        const dadosVenda = {
            id_funcionario: idFuncionario,
            id_cliente: idCliente,
            id_forma_pagamento: idFormaPagamento,
            itens_venda: produtos
        };

        console.log('Dados da Venda:', JSON.stringify(dadosVenda));

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
