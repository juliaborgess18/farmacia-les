package model.domain;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Venda {
    private int idVenda;
    private LocalDate dataVenda;
    private int idComprador;
    private int idVendedor;
    private double valorTotal;
    private String status;
    private List<ItemVenda> itensVenda = new ArrayList<>();
    
    public Venda(int idVenda, LocalDate dataVenda, int idComprador, int idVendedor, double valorTotal, String status,
            List<ItemVenda> itensVenda) {
        this.idVenda = idVenda;
        this.dataVenda = dataVenda;
        this.idComprador = idComprador;
        this.idVendedor = idVendedor;
        this.valorTotal = valorTotal;
        this.status = status;
        this.itensVenda = itensVenda;
    }
    public List<ItemVenda> getItensVenda() {
        return itensVenda;
    }
    public void setItensVenda(List<ItemVenda> itensVenda) {
        this.itensVenda = itensVenda;
    }
    
    public int getIdVenda() {
        return idVenda;
    }
    public void setIdVenda(int idVenda) {
        this.idVenda = idVenda;
    }
    public LocalDate getDataVenda() {
        return dataVenda;
    }
    public void setDataVenda(LocalDate dataVenda) {
        this.dataVenda = dataVenda;
    }
    public int getIdComprador() {
        return idComprador;
    }
    public void setIdComprador(int idComprador) {
        this.idComprador = idComprador;
    }
    public int getIdVendedor() {
        return idVendedor;
    }
    public void setIdVendedor(int idVendedor) {
        this.idVendedor = idVendedor;
    }
    public double getValorTotal() {
        return valorTotal;
    }
    public void setValorTotal(double valorTotal) {
        this.valorTotal = valorTotal;
    }
    public String getStatus() {
        return status;
    }
    public void setStatus(String status) {
        this.status = status;
    }
    @Override
    public String toString() {
        return "Venda [idVenda=" + idVenda + ", dataVenda=" + dataVenda + ", idComprador=" + idComprador
                + ", idVendedor=" + idVendedor + ", valorTotal=" + valorTotal + ", status=" + status + "]";
    }

    
}