import model.domain.Cliente;
import model.domain.Pessoa;

public class main {
    
    public static void main(String[] args) {
        Cliente clientePessoa = new Cliente();
        clientePessoa.setCpf("123456789");
        clientePessoa.setNome("Ayrton");
        System.out.println(clientePessoa.getNome());
    }

}
