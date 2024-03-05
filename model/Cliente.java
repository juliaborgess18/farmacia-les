package model;

import java.time.LocalDate;

public class Cliente extends Pessoa {
    private LocalDate dataCadastro;
    private String cpf;

    public Cliente(Endereco endereco, LocalDate dataNascimento, String telContato, String nome, String sobrenome,int id, LocalDate dataCadastro, String cpf) {
        super(endereco, dataNascimento, telContato, nome, sobrenome, id);
        this.dataCadastro = dataCadastro;
        this.cpf = cpf;
    }

    public LocalDate getDataCadastro() {
        return dataCadastro;
    }

    public void setDataCadastro(LocalDate dataCadastro) {
        this.dataCadastro = dataCadastro;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

}
