package model;

public class ItemVenda {
    private int idVenda;
    private int idProduto;
    private int qtd;  

    public ItemVenda(int idVenda, int idProduto, int qtd) {
        this.idVenda = idVenda;
        this.idProduto = idProduto;
        this.qtd = qtd;
    }
    public int getIdVenda() {
        return idVenda;
    }
    public void setIdVenda(int idVenda) {
        this.idVenda = idVenda;
    }
    public int getIdProduto() {
        return idProduto;
    }
    public void setIdProduto(int idProduto) {
        this.idProduto = idProduto;
    }
    public int getQtd() {
        return qtd;
    }
    public void setQtd(int qtd) {
        this.qtd = qtd;
    }
    @Override
    public String toString() {
        return "ItemVenda [idVenda=" + idVenda + ", idProduto=" + idProduto + ", qtd=" + qtd + "]";
    }
    
}
