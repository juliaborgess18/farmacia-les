from datetime import date
from typing import List
from dto.convenio.cadastrar_convenio_dto import CadastrarConvenioDTO
from dto.convenio.editar_convenio_dto import EditarConvenioDTO
from dto.produto.cadastrar_produto_dto import CadastrarProdutoDTO
from dto.produto.editar_produto_dto import EditarProdutoDTO
from infrastructure.models.cliente import Cliente as ClienteModel
from schemas.cliente import Cliente as ClienteSchema
from infrastructure.models.convenio import Convenio as Convenio
from schemas.convenio import Convenio as ConvenioSchema
from infrastructure.models.devolucao import Devolucao as DevolucaoModel
from schemas.devolucao import Devolucao as DevolucaoSchema
from infrastructure.models.fornecedor import Fornecedor as FornecedorModel
from schemas.fornecedor import Fornecedor as FornecedorSchema
from infrastructure.models.funcionario import Funcionario as FuncionarioModel
from schemas.funcionario import Funcionario as FuncionarioSchema
from infrastructure.models.produto import Produto
from schemas.produto import Produto as ProdutoSchema
from infrastructure.models.usuario import Usuario as UsuarioModel
from schemas.usuario import Usuario as UsuarioSchema
from infrastructure.models.venda import Venda as VendaModel
from schemas.venda import Venda as VendaSchema
from infrastructure.models.endereco import Endereco as EnderecoModel
from schemas.endereco import Endereco as EnderecoSchema
from infrastructure.models.itemDevolucao import ItemDevolucao as ItemDevolucaoModel
from schemas.itemDevolucao import ItemDevolucao as ItemDevolucaoSchema

from infrastructure.models.itemVenda import ItemVenda as ItemVendaModel
from schemas.itemVenda import ItemVenda as ItemVendaSchema

class Mapper():

    class MapperProduto():

        @classmethod
        def mapear_cadastrar_produto_dto(cls, dto: CadastrarProdutoDTO) -> Produto:
            return Produto(
                nome=dto.nome,
                valor=dto.valor,
                data_validade=dto.data_validade,
                id_fornecedor=dto.id_fornecedor,
                data_delete=None,
                foi_deletado=False
            )
        
        @classmethod
        def mapear_editar_produto_dto(cls, dto: EditarProdutoDTO) -> Produto:
            return Produto(
                id_produto= dto.id_produto,
                nome=dto.nome,
                valor=dto.valor,
                data_validade=dto.data_validade
            )
    
    class MapperConvenio():
        
        @classmethod
        def mapear_cadastrar_convenio_dto(cls, dto: CadastrarConvenioDTO) -> Convenio: 
            return Convenio(
                especialidade=dto.especialidade,
                data_inicio_convenio=date.today(),
                cnpj=dto.cnpj,
                data_delete=None,
                foi_deletado=False,
                id_cliente = dto.id_cliente)
        
        @classmethod
        def mapear_editar_convenio_dto(cls, dto: EditarConvenioDTO) -> Convenio: 
            return Convenio(
                id_convenio=dto.id_convenio,
                especialidade=dto.especialidade,
                cnpj=dto.cnpj)
             

    @classmethod
    def mapear_endereco(cls, endereco: EnderecoSchema) -> EnderecoModel:
        endereco_mapeado = EnderecoModel(
            id_endereco=endereco.id_endereco,
            rua=endereco.rua,
            numero=endereco.numero,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
            uf=endereco.uf
        )
        return endereco_mapeado


    @classmethod
    def mapear_cliente(cls, cliente: ClienteSchema) -> ClienteModel:
        endereco_mapeado = None
        if cliente.endereco is not None:
            endereco_mapeado = cls.mapear_endereco(cliente.endereco)

        cliente_mapeado = ClienteModel(
            nome=cliente.nome,
            sobrenome=cliente.sobrenome,
            data_nascimento=cliente.data_nascimento,
            tel_contato=cliente.tel_contato,
            data_cadastro=date.today(),
            data_delete=None,
            foi_deletado=False,
            cpf=cliente.cpf,
            id_endereco=cliente.id_endereco,
            endereco=endereco_mapeado)
        return cliente_mapeado  

    @classmethod
    def mapear_itens_devolucao(cls, itens_devolucao: List[ItemDevolucaoSchema]) -> ItemDevolucaoModel:
        itens_mapeados=[]
        for item in itens_devolucao:
            item_mapeado = ItemDevolucaoModel(
                qtde=item.qtde,
                id_produto=item.id_produto,
                id_devolucao=item.id_devolucao
            )
            itens_mapeados.append(item_mapeado)
        return itens_mapeados

    @classmethod
    def mapear_devolucao(cls, devolucao: DevolucaoSchema) -> DevolucaoModel:
        devolucao_mapeado = DevolucaoModel(
            id_venda=devolucao.id_venda,
            valor_devolucao=devolucao.valor_devolucao,
            data_delete=None,
            foi_deletado=False,
            itens_devolucao=cls.mapear_itens_devolucao(devolucao.itens_devolucao)
            )
        return devolucao_mapeado
    
    @classmethod
    def mapear_fornecedor(cls, fornecedor: FornecedorSchema) -> FornecedorModel:
        endereco_mapeado = None
        if fornecedor.endereco is not None:
            endereco_mapeado = cls.mapear_endereco(fornecedor.endereco)

        fornecedor_mapeado = FornecedorModel(
            nome=fornecedor.nome,
            cnpj=fornecedor.cnpj,
            email=fornecedor.email,
            telefone=fornecedor.telefone,
            data_delete=None,
            foi_deletado=False,
            id_endereco=fornecedor.id_endereco,
            endereco=endereco_mapeado)
        return fornecedor_mapeado
    
    @classmethod
    def mapear_funcionario(cls, funcionario: FuncionarioSchema) -> FuncionarioModel:
        endereco_mapeado = None
        if funcionario.endereco is not None:
            endereco_mapeado = cls.mapear_endereco(funcionario.endereco)

        funcionario_mapeado = FuncionarioModel(
            nome=funcionario.nome,
            sobrenome=funcionario.sobrenome,
            data_nascimento=funcionario.data_nascimento,
            tel_contato=funcionario.tel_contato,
            data_admissao=funcionario.data_admissao,
            cargo=funcionario.cargo,
            esta_ativo=funcionario.esta_ativo,
            salario=funcionario.salario,
            cpf=funcionario.cpf,
            data_delete=None,
            foi_deletado=False,
            id_endereco=funcionario.id_endereco,
            endereco=endereco_mapeado)
        return funcionario_mapeado
    
    @classmethod
    def mapear_usuario(cls, usuario: UsuarioSchema) -> UsuarioModel:
        usuario_mapeado = UsuarioModel(
            nome_usuario=usuario.nome_usuario,
            senha_usuario=usuario.senha_usuario)
        return usuario_mapeado


    @classmethod
    def mapear_itens_venda(cls, itens_venda: List[ItemVendaSchema]) -> ItemVendaModel:
        itens_mapeados=[]
        for item in itens_venda:
            item_mapeado = ItemVendaModel(
                qtde=item.qtde,
                id_produto=item.id_produto,
                id_venda=item.id_venda
            )
            itens_mapeados.append(item_mapeado)
        return itens_mapeados


    @classmethod
    def mapear_venda(cls, venda: VendaSchema) -> VendaModel:
        venda_mapeado = VendaModel(
            data_venda=venda.data_venda,
            valor_total=venda.valor_total,
            status=venda.status,
            data_delete=None,
            foi_deletado=False,
            id_funcionario=venda.id_funcionario,
            id_cliente=venda.id_cliente,
            id_formapagamento=venda.id_formapagamento,
            itens_venda=cls.mapear_itens_venda(venda.itens_venda)
        )
        return venda_mapeado