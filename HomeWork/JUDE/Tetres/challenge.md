# TETRÊS

Autor: Antônio Dias

    Graças ao bom trabalho que você fez “Ordenando o Placar”,
    uma nova tarefa foi atribuída à você na empresa de games®. Agora
    você deve desenvolver um jogo similar ao Tetris.

    Sua tarefa é implementar uma versão simplificada do jogo, na
    qual a torre terá uma altura máxima M e o comprimento de cada
    bloco fixado em 3. Portanto, cada bloco terá um formato 1x3 e será
    representado por uma string composta por zeros e uns (0 para os
    espaços pretos e 1 para os cinzas).

    Existem então 6 tipos de bloco, os identificados na imagem ao lado. Caso a
    cobinação entre dois blocos consecutivos (topo da torre e o atual) seja perfeita, isto é, um
    bloco seja o inverso do outro – como acontece entre os blocos “100” e “011” –, os dois
    blocos devem desaparecer do topo da torre e a pontuação do jogador é acrescida em 10.

    Em qualquer outra situação, o bloco atual é apenas colocado no topo da torre (mesmo
    que isso implique em partes cinzas flutuando).
    O jogo acaba caso a torre alcance a altura máxima ou não existam mais blocos a
    serem empilhados.
    
## Entrada

    A entrada é composta por várias linhas. A primeira linha é composta por dois
    inteiros N e M, respectivamente, o número de blocos a serem empilhados e a altura
    máxima permitida da torre. Cada linha i seguinte contém a string identificadora do i-ésimo
    bloco.

## Saída

    Seu programa deve imprimir uma única linha contendo a pontuação final do
    jogador ou “game over” caso a torre tenha alcançado a altura máxima em algum
    momento.

## Limites

- 1 ≤ N < 100
- 1 ≤ M < 100
- 1 ≤ i ≤ N

| Entrada       | Saída       |
|---------------|-------------|
| 5 3 <br> 100 <br> 011 <br> 110 <br> 010 <br> 101 | 20          |
| 6 6 <br> 101 <br> 011 <br> 110 <br> 010 <br> 001 <br> 100 | game over   |