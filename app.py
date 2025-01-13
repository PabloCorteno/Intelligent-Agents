import random
import time

ancho_mapa = 15
altura_mapa = 10
contador_recursos = 0

class Agent:
    def __init__(self, x, y, mapa, numero_agente):
        self.x = x
        self.y = y
        self.state = "exploring"
        self.objective = None
        self.explored_map = [['-' for _ in range(ancho_mapa)] for _ in range(altura_mapa)]
        self.posicion_inicial = (x, y)
        self.update_knowledge(mapa)
        self.numero_agente = numero_agente

    def update_knowledge(self, mapa):
        self.explored_map[self.y][self.x] = mapa[self.y][self.x]

    def share_knowledge(self, agents):
        for agent in agents:
            if agent.numero_agente != self.numero_agente:
                for y in range(altura_mapa):
                    for x in range(ancho_mapa):
                        if self.explored_map[y][x] != '-':
                            agent.explored_map[y][x] = self.explored_map[y][x]

    def move(self, mapa, agents):
        if self.state in ["returning_to_base", "returning_to_resource"]:
            self.return_to_target(mapa)
        else:
            direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(direcciones)

            for dx, dy in direcciones:
                new_x = self.x + dx
                new_y = self.y + dy

                if 0 <= new_x < ancho_mapa and 0 <= new_y < altura_mapa:
                    if mapa[new_y][new_x] != '/' and mapa[new_y][new_x] != '#' and mapa[new_y][new_x] != self.explored_map[self.y][self.x]:
                        if (self.x, self.y) != self.posicion_inicial:
                            mapa[self.y][self.x] = '0'
                        self.x = new_x
                        self.y = new_y
                        self.update_knowledge(mapa)
                        self.share_knowledge(agents)
                        return

            # Si no hay celdas no exploradas, moverse a celdas exploradas
            for dx, dy in direcciones:
                new_x = self.x + dx
                new_y = self.y + dy

                if 0 <= new_x < ancho_mapa and 0 <= new_y < altura_mapa:
                    if mapa[new_y][new_x] != '/' and mapa[new_y][new_x] != '#':
                        if (self.x, self.y) != self.posicion_inicial:
                            mapa[self.y][self.x] = '0'
                        self.x = new_x
                        self.y = new_y
                        self.update_knowledge(mapa)
                        self.share_knowledge(agents)
                        return


    def return_to_target(self, mapa):
        global contador_recursos
        if self.state == "returning_to_base":
            target = self.posicion_inicial
        elif self.state == "returning_to_resource":
            target = self.objective



        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direcciones.sort(key=lambda d: (self.x + d[0] - target[0])**2 + (self.y + d[1] - target[1])**2) #Función para calcular regreso, se usa al cuadrado para calcular la distancia entre el agente y el target, que previamente definimos de acuerdo al estado del agente

        for dx, dy in direcciones:
            new_x = self.x + dx
            new_y = self.y + dy

            if 0 <= new_x < ancho_mapa and 0 <= new_y < altura_mapa:
                if mapa[new_y][new_x] == '0' or (new_x, new_y) == target:
                    self.x = new_x
                    self.y = new_y
                    if (self.x, self.y) == target:
                        if self.state == "returning_to_base":
                            print(f'Agente {self.numero_agente} ha dejado el recurso en la nave')
                            self.state = "exploring"
                            contador_recursos += 1
                            if self.objective and isinstance(mapa[self.objective[1]][self.objective[0]], int) and mapa[self.objective[1]][self.objective[0]] > 0:
                                self.state = "returning_to_resource"
                        elif self.state == "returning_to_resource":
                            print(f'Agente {self.numero_agente} ha llegado al recurso para recoger más unidades.')
                            self.state = "exploring"
                            #self.explore(mapa)
                    break

    def explore(self, mapa, agents):
        global contador_recursos
        if isinstance(mapa[self.y][self.x], int) and mapa[self.y][self.x] > 0:
            # Si el recurso es grande, solicitar ayuda
            if mapa[self.y][self.x] >= 2:
                print(f"Agente {self.numero_agente} ha encontrado un recurso grande en ({self.x + 1}, {self.y + 1}) y solicita ayuda.")
                self.help(agents, (self.x, self.y))

            mapa[self.y][self.x] -= 1
            print(f"Agente {self.numero_agente} recogió una unidad de recurso en ({self.x + 1}, {self.y + 1}) y regresará a dejarlo en la nave.")
            self.state = "returning_to_base"
            if mapa[self.y][self.x] > 0:
                self.objective = (self.x, self.y)

    def help(self, agents, location):
        for agent in agents:
            if agent.state == "exploring" and agent.numero_agente != self.numero_agente:
                agent.state = "returning_to_resource"
                agent.objective = location
                print(f"Agente {agent.numero_agente} va a ayudar a recoger recursos.")


def create_map():
    mapa = [['-' for _ in range(ancho_mapa)] for _ in range(altura_mapa)]
    mapa[0][0] = '#'
    mapa[0][1] = '#'
    for _ in range(10):
        x, y = random.randint(0, ancho_mapa - 1), random.randint(1, altura_mapa - 1)
        mapa[y][x] = '/'

    for _ in range(40):
        x, y = random.randint(0, ancho_mapa - 1), random.randint(1, altura_mapa - 1)
        if mapa[y][x] == '-':
            mapa[y][x] = random.randint(1, 4)

    return mapa

def display_map(mapa, agents):
    display_map = [row[:] for row in mapa]
    for agent in agents:
        if not (agent.x == 0 and agent.y == 0):
            display_map[agent.y][agent.x] = f'({agent.numero_agente})'

    for row in display_map:
        print(" ".join(str(cell) for cell in row))
    print()

def simulation():
    global todos_en_base
    mapa = create_map()
    agents = [Agent(0, 0, mapa, 1), Agent(0, 0, mapa, 2), Agent(0, 0, mapa, 3)]

    print('Mapa Inicial')
    display_map(mapa, agents)
    movimiento = 0

    while contador_recursos < 20:
        #time.sleep(.9)
        movimiento += 1
        print(f"Movimiento {movimiento}: \nRecursos recolectados: {contador_recursos}")
        for agent in agents:
            agent.move(mapa, agents)
            agent.explore(mapa, agents)
        display_map(mapa, agents)

    print('La misión ha terminado. Recursos recolectados:', contador_recursos , '\nLos agentes regresaron a la nave' )
    for agent in agents:
        agent.x,agent.y = agent.posicion_inicial
    display_map(mapa, agents)



simulation()
