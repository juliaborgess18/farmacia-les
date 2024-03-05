package model;

import java.util.ArrayList;
import java.util.List;

public class Devolucao {
    private int idVenda;
    private double valorDevolucao;
    private int idDevolucao;   
    private List<ItemDevolucao> itensDevolucao = new ArrayList<>();
    
    public Devolucao(int idVenda, double valorDevolucao, int idDevolucao, List<ItemDevolucao> itensDevolucao) {
        this.idVenda = idVenda;
        this.valorDevolucao = valorDevolucao;
        this.idDevolucao = idDevolucao;
        this.itensDevolucao = itensDevolucao;
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
    public List<ItemDevolucao> getItensDevolucao() {
        return itensDevolucao;
    }
    public void setItensDevolucao(List<ItemDevolucao> itensDevolucao) {
        this.itensDevolucao = itensDevolucao;
    }

    
}
