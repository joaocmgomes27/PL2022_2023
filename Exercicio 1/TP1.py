import graphviz

class AFD:
    def __init__(self):
        self.estados = ['S0', 'S1', 'S2', 'S3', 'S4', 'F']
        self.estado_atual = 'S0'
        self.estados_finais = ['S7', 'S4', 'F']
        self.simbolos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'E', '-', '+']
        
    def transicao(self, simbolo):
        if simbolo not in self.simbolos:
            return None
        
        if self.estado_atual == 'S0':
            if simbolo == '-':
                return 'S1'
            elif simbolo == '+':
                return 'S1'
            elif simbolo.isdigit():
                return 'S2'
            elif simbolo == '.':
                return 'S3'
            
        elif self.estado_atual == 'S1':
            if simbolo.isdigit():
                return 'S2'
            elif simbolo == '.':
                return 'S3'
            
        elif self.estado_atual == 'S2':
            if simbolo.isdigit():
                return 'S2'
            elif simbolo == '.':
                return 'S4'
            elif simbolo.upper() == 'E':
                return 'S5'
            
        elif self.estado_atual == 'S3':
            if simbolo.isdigit():
                return 'S4'
            
        elif self.estado_atual == 'S4':
            if simbolo.isdigit():
                return 'S4'
            elif simbolo.upper() == 'E':
                return 'S5'
            
        elif self.estado_atual == 'S5':
            if simbolo.isdigit():
                return 'S7'
            elif simbolo == '-':
                return 'S6'
            elif simbolo == '+':
                return 'S6'
            
        elif self.estado_atual == 'S6':
            if simbolo.isdigit():
                return 'S7'
            
        elif self.estado_atual == 'S7':
            if simbolo.isdigit():
                return 'S7'
            
        return None
    
    def reconhecer(self, cadeia:str):
        self.estado_atual = "S0"
        for simbolo in cadeia:
            proximo_estado = self.transicao(simbolo)
            if proximo_estado is None:
                return False
            self.estado_atual = proximo_estado
            
        if self.estado_atual in self.estados_finais:
            return True
        else:
            return False
        
    def desenharGrafo(self):
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='8,5')
        dot.attr('node', shape='circle')
        
        # Adiciona os estados ao grafo
        for estado in self.estados:
            if estado in self.estados_finais:
                dot.attr('node', shape='doublecircle')
                dot.node(estado)
                dot.attr('node', shape='circle')
            else:
                dot.node(estado)
        
        # Adiciona o estado vazio ao grafo
        dot.node('V', shape='point')
        
        # Adiciona as transições ao grafo
        for estado in self.estados:
            for simbolo in self.simbolos:
                proximo_estado = self.transicao(simbolo)
                if proximo_estado is not None:
                    if proximo_estado in self.estados_finais:
                        dot.edge(estado, 'V', label=simbolo)
                    else:
                        dot.edge(estado, proximo_estado, label=simbolo)
        
        return dot.render('AFD', view=True)


afd = AFD()

print(afd.reconhecer('4.38E-7'))       # True
print(afd.reconhecer('4.38e-7'))       # False (letra 'e' não está na lista de símbolos)
print(afd.reconhecer('0.00000438'))    # True
print(afd.reconhecer('438E-9'))        # True
print(afd.reconhecer('0.000000438E')) # False


# afd.desenharGrafo()