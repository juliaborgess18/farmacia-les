package model;

import java.time.LocalDate;

public class Funcionario extends Pessoa{
    private LocalDate dataAdmissao;
    private String funcao;
    private boolean estaAtivo;
    private double salario;
    private String cpf;
    
    public Funcionario(Endereco endereco, LocalDate dataNascimento, String telContato, String nome, String sobrenome,
            int id) {
        super(endereco, dataNascimento, telContato, nome, sobrenome, id);
        //TODO Auto-generated constructor stub
    }
    
    public LocalDate getDataAdmissao() {
        return dataAdmissao;
    }
    public void setDataAdmissao(LocalDate dataAdmissao) {
        this.dataAdmissao = dataAdmissao;
    }
    public String getFuncao() {
        return funcao;
    }
    public void setFuncao(String funcao) {
        this.funcao = funcao;
    }
    public boolean isEstaAtivo() {
        return estaAtivo;
    }
    public void setEstaAtivo(boolean estaAtivo) {
        this.estaAtivo = estaAtivo;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }
    public String getCpf() {
        return cpf;
    }
    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    
}
