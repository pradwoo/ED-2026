from caixa import Caixa
from cliente import Cliente

class SimuladorDeFila():
    ''' Modela um simulador de uma fila de caixa '''

    def __init__(self, tempoDeSimulacao, tempoGastoPorCliente,
                 probDeNovosClientes):
        ''' Inicializa o simulador '''
        self.probDeNovosClientes = probDeNovosClientes
        self.tempoDeSimulacao = tempoDeSimulacao
        self.tempoGastoPorCliente = tempoGastoPorCliente
        self.caixa = Caixa()
   
    def executaSimulador(self):
        ''' Executa o simulador pelo tempoDeSimulacao '''
        for tempoAtual in range(self.tempoDeSimulacao):
            # Tente gerar um novo cliente
            cliente = Cliente.geraCliente(
                self.probDeNovosClientes,
                tempoAtual,
                self.tempoGastoPorCliente)

            # Se o cliente foi gerado, inclua-o na fila do caixa
            if cliente != None:
                self.caixa.adicionaCliente(cliente)

            # Faça o caixa atender um cliente
            self.caixa.atendeClientes(tempoAtual)

    def imprimeResultado(self):
        ''' Retorna os resultados da simulação '''
        print(str(self.caixa))


def main() -> None:
    '''Lê os dados de entrada'''
    totalClientesFila = int(input("Informe o total de clientes na fila: "))
    TamMax = int(input("Informe o tamanho máximo que a fila pode atingir: "))
    tempoDeSimulacao = int(input("Informe o tempo total de simulação que será utilizado: "))

    '''Cria o simulador'''
    Simulador = SimuladorDeFila(totalClientesFila, TamMax, tempoDeSimulacao)

    '''Executar a simulação'''
    Simulador.executaSimulador(tempoDeSimulacao)
    
    '''Imprimir o resultado'''
    print("SIMULADOR DE FILA")
    print("Clientes atendidos: ")
    print("Tempo gasto com cada cliente: ")
    print("Clientes restantes na fila: ")


if __name__ == "__main__":
    main()