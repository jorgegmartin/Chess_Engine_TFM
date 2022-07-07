# CREACION DE UN MOTOR DE JUEGO PARA AJEDREZ CON REDES NEURONALES Y Q-LEARNING

Memoria del Trabajo de fin de Master.

_KSCHOOL 2022._

# Introduccion

El objetivo del proyecto es la creacion de un motor de juego para ajedrez basado en redes neuronales
y aprendizaje autonomo por medio de recompensas.

Los pasos a seguir son:

1. Descarga de base de datos
2. Evaluacion y limpieza de la base de datos
3. Motor #1 Red neuronal sencilla alimentada por la base de datos 
4. Motor #2 entrenamiento a base de recompensas de un segundo motor contra el primer motor
5. Generacion de visualizaciones
   

# Investigacion

### Monte Carlo Decision Tree

Para la optimizacion del modelo es quizas necesario realizar un prunning del arbol de decision resultante
de la profundidad de calculo de nuestra partida.

_DUDAS:_
1. Como introduzco esto en base a una red neuronal?
1. Es quizar mejor realizar un algoritmo sencillo de evaluacion que evalue posiciones y a partir de ahi realizar un prunning del arbol de decision resultante?

---
___Enlaces___

[Monte Carlo Tree Search in Chess Programming](https://www.chessprogramming.org/Monte-Carlo_Tree_Search)

[Explicacion visual del Monte Carlo Tree Search](https://www.youtube.com/watch?v=UXW2yZndl7U&feature=emb_title)

---

# Primer motor, red neuronal y aprendizaje de base de datos

# Segundo motor, aprendizaje autonomo a base de recompensas
