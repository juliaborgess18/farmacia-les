package model;

public class Devolucao {
    private int idVenda;
    private double valorDevolucao;
    private int idDevolucao;   

    public Devolucao(int idVenda, double valorDevolucao, int idDevolucao) {
        this.idVenda = idVenda;
        this.valorDevolucao = valorDevolucao;
        this.idDevolucao = idDevolucao;
    }
    public int getIdVenda() {
        return idVenda;
    }
    public void setIdVenda(int idVenda) {
        this.idVenda = idVenda;
    }
    public double getValorDevolucao() {
        return valorDevolucao;
    }
    public void setValorDevolucao(double valorDevolucao) {
        this.valorDevolucao = valorDevolucao;
    }
    public int getIdDevolucao() {
        return idDevolucao;
    }
    public void setIdDevolucao(int idDevolucao) {
        this.idDevolucao = idDevolucao;
    }
    @Override
    public String toString() {
        return "Devolucao [idVenda=" + idVenda + ", valorDevolucao=" + valorDevolucao + ", idDevolucao=" + idDevolucao
                + "]";
    }

    
}
