package model;

public class Endereco {
    private String cidade;
    private String estado;
    private String uf;
    private String bairro;
    private String rua;
    private int num;
    
    public Endereco(String cidade, String estado, String uf, String bairro, String rua, int num) {
        this.cidade = cidade;
        this.estado = estado;
        this.uf = uf;
        this.bairro = bairro;
        this.rua = rua;
        this.num = num;
    }

    public String getCidade() {
        return cidade;
    }
    public void setCidade(String cidade) {
        this.cidade = cidade;
    }
    public String getEstado() {
        return estado;
    }
    public void setEstado(String estado) {
        this.estado = estado;
    }
    public String getUf() {
        return uf;
    }
    public void setUf(String uf) {
        this.uf = uf;
    }
    public String getBairro() {
        return bairro;
    }
    public void setBairro(String bairro) {
        this.bairro = bairro;
    }
    public String getRua() {
        return rua;
    }
    public void setRua(String rua) {
        this.rua = rua;
    }
    public int getNum() {
        return num;
    }
    public void setNum(int num) {
        this.num = num;
    }
    @Override
    public String toString() {
        return "Endereco [cidade=" + cidade + ", estado=" + estado + ", uf=" + uf + ", bairro=" + bairro + ", rua="
                + rua + ", num=" + num + "]";
    }

    
}
