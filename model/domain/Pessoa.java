package model.domain;

import java.time.LocalDate;

public abstract class Pessoa {
    private Endereco endereco;
    private LocalDate dataNascimento;
    private String telContato;
    private String nome;
    private String sobrenome;
    private int id;

    public Pessoa() {
    }

    public Pessoa(Endereco endereco, LocalDate dataNascimento, String telContato, String nome, String sobrenome,
            int id) {
        this.endereco = endereco;
        this.dataNascimento = dataNascimento;
        this.telContato = telContato;
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.id = id;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    public LocalDate getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(LocalDate dataNascimento) {
        this.dataNascimento = dataNascimento;
    }

    public String getTelContato() {
        return telContato;
    }

    public void setTelContato(String telContato) {
        this.telContato = telContato;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Pessoa [endereco=" + endereco + ", dataNascimento=" + dataNascimento + ", telContato=" + telContato
                + ", nome=" + nome + ", sobrenome=" + sobrenome + ", id=" + id + "]";
    }

}
