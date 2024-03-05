package model;

import java.time.LocalDate;

public class Medico extends Pessoa {
    private LocalDate dataInicioConvenio;
    private String especialidade;
    private String cnpj;
    
    public Medico(Endereco endereco, LocalDate dataNascimento, String telContato, String nome, String sobrenome,
            int id) {
        super(endereco, dataNascimento, telContato, nome, sobrenome, id);
        //TODO Auto-generated constructor stub
    }
    
    public LocalDate getDataInicioConvenio() {
        return dataInicioConvenio;
    }
    public void setDataInicioConvenio(LocalDate dataInicioConvenio) {
        this.dataInicioConvenio = dataInicioConvenio;
    }
    public String getEspecialidade() {
        return especialidade;
    }
    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }
    public String getCnpj() {
        return cnpj;
    }
    public void setCnpj(String cnpj) {
        this.cnpj = cnpj;
    }
    @Override
    public String toString() {
        return "Medico [dataInicioConvenio=" + dataInicioConvenio + ", especialidade=" + especialidade + ", cnpj="
                + cnpj + "]";
    }

    
}
