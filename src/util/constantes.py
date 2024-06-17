RELATORIO_QTDE_PRODUTOS_VENDIDOS = '''
SELECT 
    iv.idproduto AS id_produto, 
    p.nome, 
    SUM(iv.qtde) AS qtde, 
	p.valor AS valor_unitario,
    SUM(iv.qtde * p.valor) AS valor_total
FROM 
    venda v
INNER JOIN 
    itemvenda iv ON v.idvenda = iv.idvenda
INNER JOIN 
    produto p ON iv.idproduto = p.idproduto
WHERE v.datavenda BETWEEN :data_inicio AND :data_final	
GROUP BY 
    iv.idproduto, p.nome, p.valor
ORDER BY 
    qtde DESC;
'''