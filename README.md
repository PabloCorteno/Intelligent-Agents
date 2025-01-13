# Intelligent-Agents

Proyecto
							
							
Tendrán que realizar un programa en Python que simule la exploración del planeta Marte. El proyecto se realizará de forma individual. El diseño de la interface queda abierto a tu creatividad, sin embargo es necesario que el mapa, los recursos y los agentes sean visibles de alguna forma.

La misión espacial Cerberus ha sido enviada a Marte para recoger muestras geológicas las cuales serán extraídas para su estudio en la tierra. Sin embargo este viaje no puede ser tripulado puesto que aún no se cuenta con la tecnología adecuada. Por esta razón se ha optado por utilizar robots para la extracción de los materiales geológicos. La nave espacial cuenta con 3 robots que tienen la forma de pequeños carros, cuyas llantas les permitirá moverse a través del terreno inhóspito de Marte.
Se te ha solicitado realizar la programación de los robots (agentes), para ello mostrarás una simulación de su funcionamiento, para después ser implementada en los robots.
Los agentes saldrán de la nave y no tendrán conocimiento alguno del terreno que estarán explorando. Por ello tendrán que moverse en diferentes direcciones y explorar.

Para la facilidad del desarrollo de este prototipo se cuentan con las siguientes reglas:

1.	Los agentes solo se pueden mover en 4 direcciones (norte, sur, este y oeste).
2.	Los recursos pueden variar de tamaño (1 a 4 unidades).
3.	Los agentes solo pueden cargar 1 unidad a la vez.
4.	Cuando un agente encuentre un recurso deberá regresarlo a la nave.
5.	La nave terminará su misión cuando tenga 20 unidades. En este momento todos los agentes deberán regresar a la nave para preparar el regreso a la tierra.
6.	El diseño inicial del mapa donde los agentes se moverán, queda abierto a tu discreción
   
Para implementar el algoritmo se ha propuesto separar su desarrollo en diferentes fases

	1) Comportamiento reactivo
En esta primera fase los agentes no tendrán conocimiento de los otros agentes, y realmente no serán inteligentes. Ellos se moverán en una dirección aleatoria, que previamente no hayan explorado. Si encuentran un obstáculo se moverán en una dirección diferente de forma aleatoria.
Si encuentran un recurso, recogerán el recurso y regresarán a la nave para depositarlo. Si el recurso contaba con más unidades, el agente regresará a recogerlas.
El agente deberá ir almacenando el conocimiento del mapa que haya explorado en una estructura de datos, de esta forma sabrá donde están los obstáculos y en qué dirección no ha explorado.
	2) Comportamiento colaborativo - mapa
En esta fase los agentes compartirán el conocimiento adquirido del mapa con el resto de los agentes. De esta forma los agentes compartirán el conocimiento que han adquirido conforme han explorado la superficie del planeta. La frecuencia con la que ellos comparten el conocimiento del mapa, queda abierto a tu criterio.
	3) Comportamiento colaborativo – inteligencia
En esta fase un agente que encuentre un recurso que sea muy grande (mayor a 2) puede pedir ayuda a otros agentes libres para que lo puedan ayudar a recoger el recurso. Un agente libre es aquel agente que no se encuentra actualmente cargando un recurso o no se encuentra en camino a ayudar a un agente.
