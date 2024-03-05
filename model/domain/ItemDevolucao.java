package model.domain;

public class ItemDevolucao {
    private int idProdutoDevolucao;

    public ItemDevolucao(int idProdutoDevolucao) {
        this.idProdutoDevolucao = idProdutoDevolucao;
    }

    public int getIdProdutoDevolucao() {
        return idProdutoDevolucao;
    }

    public void setIdProdutoDevolucao(int idProdutoDevolucao) {
        this.idProdutoDevolucao = idProdutoDevolucao;
    }

    @Override
    public String toString() {
        return "ItemDevolucao [idProdutoDevolucao=" + idProdutoDevolucao + "]";
    }

    
}
