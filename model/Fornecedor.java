package model;

public class Fornecedor {
    private String cnpj;
    private String email;
    private String telefone;
    private String nome;
    
    public Fornecedor(String cnpj, String email, String telefone, String nome) {
        this.cnpj = cnpj;
        this.email = email;
        this.telefone = telefone;
        this.nome = nome;
    }
    
    public String getCnpj() {
        return cnpj;
    }
    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getTelefone() {
        return telefone;
    }
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    @Override
    public String toString() {
        return "Fornecedor [cnpj=" + cnpj + ", email=" + email + ", telefone=" + telefone + ", nome=" + nome + "]";
    }
    
}
