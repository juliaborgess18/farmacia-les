package model.domain;

import java.time.LocalDate;

public class Produto {
    private int idProduto;
    private String nome;
    private double valor;
    private LocalDate dataValidade;

    public Produto(int idProduto, String nome, double valor, LocalDate dataValidade) {
        this.idProduto = idProduto;
        this.nome = nome;
        this.valor = valor;
        this.dataValidade = dataValidade;
    }
    public int getIdProduto() {
        return idProduto;
    }
    public void setIdProduto(int idProduto) {
        this.idProduto = idProduto;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getValor() {
        return valor;
    }
    public void setValor(double valor) {
        this.valor = valor;
    }
    public LocalDate getDataValidade() {
        return dataValidade;
    }
    public void setDataValidade(LocalDate dataValidade) {
        this.dataValidade = dataValidade;
    }
    @Override
    public String toString() {
        return "Produto [idProduto=" + idProduto + ", nome=" + nome + ", valor=" + valor + ", dataValidade="
                + dataValidade + "]";
    }
    
}
