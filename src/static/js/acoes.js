var path = window.location.pathname;

if (path === "/"){
    var item = document.getElementById("navbar-row")
    item.hidden = true;
}
if (path.includes("cliente")){
    var item = document.getElementById("sidebar-cliente");
    item.classList.add('active');
} 
if (path.includes("fornecedor")){
    var item = document.getElementById("sidebar-fornecedor");
    item.classList.add('active');
} 
if (path.includes("produto")){
    var item = document.getElementById("sidebar-produto");
    item.classList.add('active');
} 
if (path.includes("venda")){
    var item = document.getElementById("sidebar-venda");
    item.classList.add('active');
}
if (path.includes("funcionario")){
    var item = document.getElementById("sidebar-funcionario");
    item.classList.add('active');
}
if (path.includes("devolucao")){
    var item = document.getElementById("sidebar-devolucao");
    item.classList.add('active');
}
if (path.includes("convenio")){
    var item = document.getElementById("sidebar-convenio");
    item.classList.add('active');
}


// testes

// let produtos = [];

// function adicionarProduto() {
//     const idProduto = document.getElementById('id_produto').value;
//     const nomeProduto = document.getElementById('id_produto').value; // Não temos o nome do produto aqui, você pode adicioná-lo de outra forma
//     const quantidadeProduto = document.getElementById('quantidade_produto').value;

//     if (idProduto && quantidadeProduto) {
//         produtos.push({ id: idProduto, nome: nomeProduto, quantidade: quantidadeProduto });
//         atualizarListaProdutos();
//         document.getElementById('id_produto').value = '';
//         document.getElementById('quantidade_produto').value = '';
//     } else {
//         alert('Por favor, preencha todos os campos do produto.');
//     }
// }

// function removerProduto(index) {
//     produtos.splice(index, 1);
//     atualizarListaProdutos();
// }

// function atualizarListaProdutos() {
//     const tbody = document.getElementById('lista_produtos').getElementsByTagName('tbody')[0];
//     tbody.innerHTML = '';

//     produtos.forEach((produto, index) => {
//         const row = tbody.insertRow();
//         const cellNomeProduto = row.insertCell(0);
//         const cellQuantidade = row.insertCell(1);
//         const cellAcoes = row.insertCell(2);

//         cellNomeProduto.textContent = produto.nome;
//         cellQuantidade.textContent = produto.quantidade;
//         cellAcoes.innerHTML = `<button class="btn btn-danger" type="button" onclick="removerProduto(${index})">Remover</button>`;
//     });
// }

// // Carregar opções de forma de pagamento via fetch
// window.onload = function () {
//     fetch('/obter_formas_pagamento')
//         .then(response => response.json())
//         .then(data => {
//             const selectFormaPagamento = document.getElementById('id_forma_pagamento');

//             data.forEach(formaPagamento => {
//                 const option = document.createElement('option');
//                 option.value = formaPagamento.id;
//                 option.textContent = formaPagamento.nome;
//                 selectFormaPagamento.appendChild(option);
//             });
//         })
//         .catch(error => console.error('Erro ao carregar formas de pagamento:', error));
// }

// document.getElementById('form_venda').addEventListener('submit', function (event) {
//     event.preventDefault();

//     const idFuncionario = document.getElementById('id_funcionario').value;
//     const idCliente = document.getElementById('id_cliente').value;
//     const idFormaPagamento = document.getElementById('id_forma_pagamento').value;

//     if (!idFuncionario || !idCliente || !idFormaPagamento || produtos.length === 0) {
//         alert('Por favor, preencha todos os campos e adicione pelo menos um produto.');
//         return;
//     }

//     const dadosVenda = {
//         id_funcionario: idFuncionario,
//         id_cliente: idCliente,
//         id_forma_pagamento: idFormaPagamento,
//         produtos: produtos
//     };

//     console.log('Dados da Venda:', dadosVenda);
    
//     fetch('/cadastrar_venda', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(dadosVenda),
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log('Successo:', data);
//         document.getElementById('form_venda').reset();
//         produtos = [];
//         atualizarListaProdutos();
//     })
//     .catch((error) => {
//         console.error('Erro:', error);
//     });
// });
