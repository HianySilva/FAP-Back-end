from datetime import datetime, timedelta
from collections import deque

class Usuario:
    def __init__(self, nome):
        self.nome = nome

class Administrador(Usuario):
    def permitir_entrada_gratuita(self, placa, estacionamento):
        estacionamento.veiculos_gratis.add(placa)
        print(f"\n[Administração] Entrada gratuita autorizada para o veículo de placa {placa}.\n")

class Cliente:
    def __init__(self):
        self.nome = input("Digite o nome do cliente: ")
        self.documento = input("Digite o número do documento do cliente: ")
        self.telefone = input("Digite o telefone do cliente: ")

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Documento: {self.documento}")
        print(f"Telefone: {self.telefone}\n")

class Veiculo:
    def __init__(self, placa, cor, modelo, ano, marca, cliente=None):
        self.placa = placa
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.hora_entrada = None
        self.cliente = cliente

    def mostrar_informacoes(self):
        cliente_info = f"Cliente: {self.cliente.nome}" if self.cliente else "Cliente: Não informado"
        return (f"Placa: {self.placa}, Tipo: {self.tipo}, Marca: {self.marca}, Cor: {self.cor}, "
                f"Modelo: {self.modelo}, Ano: {self.ano}, Entrada: {self.hora_entrada.strftime('%d/%m/%Y %H:%M:%S')}, {cliente_info}")

class Carro(Veiculo):
    def __init__(self, placa, cor, modelo, ano, marca, num_portas, cliente=None):
        super().__init__(placa, cor, modelo, ano, marca, cliente)
        self.tipo = 'Carro'
        self.num_portas = num_portas

class Moto(Veiculo):
    def __init__(self, placa, cor, modelo, ano, marca, cilindrada, cliente=None):
        super().__init__(placa, cor, modelo, ano, marca, cliente)
        self.tipo = 'Moto'
        self.cilindrada = cilindrada

class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.veiculos_gratis = set()
        self.historico = deque(maxlen=5)

    def registrar_entrada(self, veiculo):
        veiculo.hora_entrada = datetime.now()
        self.veiculos[veiculo.placa] = veiculo
        print(f"\n[Entrada] {veiculo.tipo} de placa {veiculo.placa} ({veiculo.marca} {veiculo.modelo}) entrou no estacionamento às {veiculo.hora_entrada.strftime('%H:%M:%S')}.\n")

    def registrar_saida(self, placa, metodo_pagamento):
        if placa in self.veiculos:
            veiculo = self.veiculos.pop(placa)
            tempo_permanencia = datetime.now() - veiculo.hora_entrada
            print(f"\n[Saída] {veiculo.tipo} de placa {veiculo.placa} ({veiculo.marca} {veiculo.modelo}) está saindo do estacionamento às {datetime.now().strftime('%H:%M:%S')}.\n")
            if tempo_permanencia > timedelta(minutes=20) and placa not in self.veiculos_gratis:
                self.processar_pagamento(metodo_pagamento, tempo_permanencia, veiculo.cliente)
            else:
                print(f"[Saída] Saída gratuita permitida para o veículo de placa {veiculo.placa} ({veiculo.marca} {veiculo.modelo}), pois permaneceu dentro dos 20 minutos.\n")
            self.historico.append((veiculo, datetime.now()))

    def processar_pagamento(self, metodo_pagamento, tempo_permanencia, cliente):
        print(f"[Pagamento] O pagamento foi processado com sucesso.\nMétodo de pagamento: {metodo_pagamento}\nTempo de permanência: {tempo_permanencia}.")
        print(f"Cliente responsável: {cliente.nome}\n")

    def mostrar_historico(self):
        print("\n[Histórico de Veículos no Estacionamento]")
        if not self.historico:
            print("Não há registros no histórico.\n")
        for veiculo, saida in self.historico:
            print(f"{veiculo.mostrar_informacoes()}, Saída: {saida.strftime('%d/%m/%Y %H:%M:%S')}")
        print("")

nome_usuario = input("Por favor, digite seu nome: ")
admin = Administrador(nome_usuario)
estacionamento = Estacionamento()

print("\nCadastro do cliente do carro:")
cliente_carro = Cliente()

print("\nCadastro do cliente da moto:")
cliente_moto = Cliente()

carro = Carro("ABC1234", "Azul", "Sedan", 2022, "Toyota", 4, cliente_carro)
moto = Moto("XYZ5678", "Preta", "Sport", 2021, "Yamaha", 600, cliente_moto)

estacionamento.registrar_entrada(carro)
estacionamento.registrar_entrada(moto)

admin.permitir_entrada_gratuita("ABC1234", estacionamento)

# Simulação de pagamento
metodo_pagamento_carro = input("Digite o método de pagamento para o carro (pix, débito, crédito, dinheiro): ")
metodo_pagamento_moto = input("Digite o método de pagamento para a moto (pix, débito, crédito, dinheiro): ")

estacionamento.registrar_saida("ABC1234", metodo_pagamento_carro)
estacionamento.registrar_saida("XYZ5678", metodo_pagamento_moto)

print("\nInformações dos Clientes:")
cliente_carro.mostrar_informacoes()
cliente_moto.mostrar_informacoes()

estacionamento.mostrar_historico()
