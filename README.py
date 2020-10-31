# Definição da Classe Mãe Pessoa


class Pessoa:
    # Construtor
    def __init__(self, nome, rg, cpf, telefone):
        # Atributos
        self.nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.telefone = telefone

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def set_rg(self, rg):
        self.__rg = rg
        return self.__rg

"""
class Especialidade:
   def _init_(self, especialidade):
        self.especialidade = especialidade
    
    def exibir_especialidade(self):
        print(especialidade)    
"""

class Medico(Pessoa):
    def __init__(self, nome, rg, cpf, 
               telefone, crm, salario, especialidade):
        super().__init__(nome, rg, cpf, telefone)
        self.crm = crm
        self.salario = salario
        self.especialidade = especialidade

    def info_medico(self):
        print("NOME:", self.nome)
        #print("RG:", self.__rg)
        #print("CPF:", self.__cpf)
        print("TELEFONE:", self.telefone)
        print("CRM:", self.crm)
        print("SALÁRIO:", self.salario)
        print("Especialidade:", self.especialidade)

    def visitar_paciente(self):
        print('O MÉDICO VISITOU O PACIENTE: ', Paciente.nome)

    def registrar_obs(self):
        print("""O MÉDICO REGISTROU AS OBSERVAÇÕES
        REALIZADAS DO PACIENTE: """, Paciente.nome)

    def historico_paciente(self):
        historico = []
        for i in historico:
            historico.append(i.registrar_obs())

    class Historico:
        def __init__(self, data, hora, observacao, nome_med):
            self.historico_pac = []
            self.data = data
            self.hora = hora
            self.observacao = observacao
            self.nome_med = nome_med

        def historico_paciente(self):
            for i in historico_pac:
                self.historico_pac.append(Historico)

        def retornar_dados(self):
            return historico_paciente()

class Paciente(Pessoa):
    def __init__(self, nome, rg, cpf,
               telefone, endereco, data_nasc):
        super().__init__(nome, rg, cpf, telefone)
        self.enderco = endereco
        self.data_nasc = data_nasc
        
    def info_paciente(self):
        print("NOME:", self.nome)
        print("TELEFONE:", self.telefone)
 
    def get__rg(self):
        return self.__rg
        
    def set__rg(self, rg):
        return self.__rg
        
    def get__cpf(self):
        return self.__cpf
        
    def set__cpf(self, cpf):
        return self.__cpf

#def ficar_internado(self):
#    print("PACIENTE DE NOME: ", self.nome)
#    Quarto.info_quarto(self)

    def medico_responsavel(self):
        Medico.info_medico(self)


class Quarto:
    def __init__(self, numero_quarto, numero_andar):
        self.numero_quarto = numero_quarto
        self.numero_andar = numero_andar

    def info_quarto(self):
        print("LOCALIZADO NO QUARTO DE NÚMERO: ", self.numero_quarto)
        print("LOCALIZADO NO ANDAR: ", self.numero_andar)


medico = Medico('João', 283122312, 12231223,
                11923423453, 13811, 10000, 'Cardiologia')
medico.info_medico()
print("RG do médico:", medico.get_rg())
print("CPF do médico:", medico.get_cpf())

medico.historico_paciente()

print('------------------------------')

paciente = Paciente('Filipe', 1231231, 220390121,
                    11957483940, 'Rua Guarani 320', '11/08/1976')

paciente.info_paciente()
print("RG do paciente:", paciente.get_rg())
print("CPF do paciente:", paciente.get_cpf())

quarto = Quarto(54, '5° andar')

quarto.info_quarto()

historico = Historico("31/10/2020", "16:58", "Marlene")
