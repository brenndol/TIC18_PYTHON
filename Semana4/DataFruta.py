
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        quantidade = int(input("Quantos nomes na lista? "))
        for _ in range(quantidade):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista, key=lambda x: x.lower())
        size = len(sorted_list)
        if size % 2 == 0:
            median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
        else:
            median = sorted_list[size // 2]
        print("Mediana:", median)   

    def mostraMenor(self):
        menor_nome = min(self.__lista, key=lambda x: x.lower())
        print("Menor nome:", menor_nome)

    def mostraMaior(self):
        maior_nome = max(self.__lista, key=lambda x: x.lower())
        print("Maior nome:", maior_nome)

    def __str__(self):
        return str(self.__lista)

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista, key=lambda x: x.lower())
        print("Lista de nomes em ordem:", sorted_list)

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        dat = int(input("Quantas datas na lista? "))
        for _ in range(dat):
            dia = int(input("Dia: "))
            mes = int(input("Mês:"))
            ano = int(input("Ano: (entre 2000 e 2100): "))
            nova_data = Data(dia, mes, ano)
            self.__lista.append(nova_data)

    def mostraMediana(self):
        sorted_list = sorted(self.__lista, key=lambda data:(data.dia, data.mes, data.ano))
        size = len(sorted_list)
        if size % 2 == 0:
            med1 = sorted_list[size // 2 - 1]
            med2 = sorted_list[size // 2]
            mediana = f"{med1} e {med2}"
        else:
            median = sorted_list[size // 2]
        print("Mediana: ", mediana)
     
    def mostraMenor(self):
        menor_med = min(self.__lista, key=lambda data: (data.dia, data.mes, data.ano))
        print("Menor", menor_med)

    def mostraMaior(self):
        maior_med = max(self.__lista, key=lambda data: (data.dia, data.mes, data.ano))
        print("Maior Data", maior_med)
    
    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista, key=lambda data: (data.dia, data.mes, data.ano))
        print("Lista de datas em ordem:", sorted_list)
    
    def __str__(self):
        return str(self.__lista)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        sal = int(input("Quantos salários na lista? "))
        for _ in range(sal):
            salario = float(input("Salário: "))
            self.__lista.append(salario)


    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        size = len(sorted_list)
        if size % 2 == 0:
            mediana = (float(sorted_list[size // 2 - 1]) + float(sorted_list[size // 2])) / 2
        else:
            mediana = float(sorted_list[size // 2])
        print("Mediana", mediana)  

    def mostraMenor(self):
        menor_sal = min(self.__lista)
        print("Menor salário", menor_sal)

    def mostraMaior(self):
        maior_sal = max(self.__lista)
        print("Maior salário", maior_sal)

    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista de salários em ordem:", sorted_list)
    
    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        ida = int(input("Quantas idades na lista?"))
        for _ in range(ida):
            idade = int(input("Idade: "))
            self.__lista.append(idade)

    
    def mostraMediana(self):
        sorted_list = sorted(map(int,self.__lista))
        size = len(sorted_list)
        if size % 2 == 0:
            median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
        else: 
            median = sorted_list[size // 2]
        print("Mediana ", median)
    
    def mostraMenor(self):
        menor_idade = min(self.__lista)
        print("Menor idade: ", menor_idade)
    
    def mostraMaior(self):
        maior_idade = max(self.__lista)
        print("Maior idade: ", maior_idade)
    
    def listarEmOrdem(self):
        sorted_list = sorted(self.__lista)
        print("Lista de idades em ordem:", sorted_list)

    def __str__(self):
        return str(self.__lista)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        lista.listarEmOrdem()
        print("___________________")
    # Iterador zip
    nomes = ["Alice", "Bia", "Charlie"]
    salarios = [50000, 60000, 75000]

    for nome, salario in zip(nomes, salarios):
        print(f"{nome}: Salário - {salario}")

    #Iterador map
    salarios = [50000, 60000, 75000]

    novos_salarios = list(map(lambda x: x + 1.1, salarios))
    print("Salários em reajuste:", novos_salarios)

    #iterador filter
    datas = [Data()]
    datas_modificadas = list(map(lambda x: x if x.ano >= 2023 else Data(1, x.mes, x.ano), datas))
    print("Datas modificadas:", datas_modificadas)



    print("Fim do teste!!!")

if __name__ == "__main__":
    main()