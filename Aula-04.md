# Modos de Transmissão e Topologias de Redes

As linhas de comunicação (enlaces) que interligam os computadores de uma rede podem ser linhas que utilizam **meios metálicos** ou **meios óticos** (cabos metálicos ou fibras óticas).

Esses meios de comunicação são definidos como **meios guiados** → os sinais elétricos são guiados pelos fios.

Existem enlaces que são por sistemas de rádio, não tendo fio (Wi-Fi, Bluetooth).

## Linhas de Comunicação
- **Padrão de codificação dos dados**: Codificação dos dados diz respeito à modificação do sinal digital para conseguir benefícios na transmissão (melhoria no sincronismo).
- **Modulação dos dados**: Transforma o sinal analógico, conseguindo tornar o meio, ou seja, tornar a banda de transmissão mais larga.
- **Modo de transmissão**: Como os dados são transmitidos (simplex, half-duplex, full-duplex).
- **Topologia de rede**: Classificação das redes (barramento, rede estrela, em malha).

## Modos de Transmissão

### Modo Simplex
- A informação percorre o meio em um único sentido, ou seja, sai de um ponto e chega a outro ponto, **só em um sentido**. Um dispositivo será sempre o transmissor e o outro sempre será o receptor.
- **Pouco utilizado em redes de computadores**, já que exige comunicação nos dois sentidos.

### Modo Half-Duplex
- A informação percorre o meio físico em ambos os sentidos, mas **alternadamente**, ou seja, apenas uma estação pode obter a posse do meio por vez.
- **Modo de transmissão das redes Ethernet**.

### Modo Full-Duplex
- A informação é transmitida e recebida **simultaneamente**, ou seja, ao mesmo tempo, trazendo como benefício a melhor velocidade das interfaces.
- **Mais comum nas redes que têm o switch**.

## Topologia de Rede

A **topologia de rede** refere-se à forma como os enlaces físicos estão organizados, determinando os caminhos físicos existentes e utilizáveis entre quaisquer pares de estações conectadas a essa rede. Exemplos de topologias incluem barramento, anel, estrela e mista.

### Tipos de Topologia
- **Ponto a ponto**: Só tem 2 nós (uma máquina e outra máquina) interligadas pelos elementos de comunicação, que podem ser cabo metálico, ótico ou de rádio.
- **Multiponto**: Vários nós e equipamentos em cada enlace.

### Tipos de Redes e Suas Características
- **Redes locais**: Baixo custo (rede do usuário), alta confiabilidade (não há meio de degradação).
  - A topologia mais comum é a **estrela** (elementos interligados por um elemento central, como um switch ou hub).
  
- **Redes WANs (geograficamente distribuídas)**: Altíssimo custo para alcançar longas distâncias, com uma confiabilidade menor (mais sujeitas a fatores de degradação), mas com alta velocidade.
  - A topologia mais usada é a **mista**, onde o custo é equilibrado com a redundância (não se deve fazer uma rede sem redundância para segurança).

### Topologia Lógica vs. Topologia Física
- **Topologia Lógica**: Forma de se definir a rede a nível de configuração. Como a rede funciona.
- **Topologia Física**: Disposição física dos elementos, como os cabos estão organizados.

## Resumo

As redes de comunicação podem usar **meios guiados** (como cabos metálicos ou fibras óticas) ou **meios não guiados** (como sistemas de rádio, Wi-Fi e Bluetooth).

### Modos de Transmissão
Os **modos de transmissão** definem como os dados são enviados entre dispositivos:

- **Modo Simplex**: A informação percorre o meio em um único sentido, ou seja, sai de um ponto e chega a outro ponto, **só em um sentido**. Um dispositivo será sempre o transmissor e o outro sempre será o receptor. Esse modo quase não é usado em redes de computadores, já que exige comunicação nos dois sentidos.
- **Modo Half-Duplex**: A informação percorre o meio físico em ambos os sentidos, mas **alternadamente**, ou seja, apenas uma estação pode obter a posse do meio por vez. É o modo de transmissão das redes Ethernet.
- **Modo Full-Duplex**: A informação é transmitida e recebida **simultaneamente**, ou seja, ao mesmo tempo, trazendo como benefício a melhor velocidade das interfaces. Esse tipo é mais comum nas redes que têm o switch.

### Topologia de Rede
A **topologia de rede** refere-se à organização dos enlaces físicos e ao caminho entre os dispositivos conectados:

- **Ponto a Ponto**: Só tem 2 nós (uma máquina e outra máquina) interligadas pelos elementos de comunicação, que podem ser cabo metálico, ótico ou de rádio.
- **Multiponto**: Vários nós e equipamentos em cada enlace.
- **Topologia Estrela**: Todos os dispositivos são conectados a um ponto central (como um switch ou hub), sendo comum em redes locais.
- **Topologia Mista**: Combinação de diferentes topologias, equilibrando custo e redundância, comum em redes geograficamente distribuídas (WANs).

Além disso, há a distinção entre **topologia lógica** (como a rede é configurada e funciona) e **topologia física** (disposição real dos cabos e equipamentos).

Cada tipo de rede, seja local ou geograficamente distribuída, tem suas vantagens e desvantagens em termos de custo, confiabilidade e velocidade.
