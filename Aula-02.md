# Classificação quanto à Abrangência

## Definição 1
"Redes de computadores são um conjunto de módulos processadores capazes de trocar informações e compartilhar recursos, interligados por um sistema de comunicação."

## Definição 2
"Redes de computadores são um conjunto de máquinas autônomas e interconectadas que trocam informações."

---

### Elementos Fundamentais
Seja qual for o conceito, estarão sempre presentes os dois elementos fundamentais:

#### a) Computadores (módulos processadores)
Dispositivos capazes de enviar ou receber dados utilizando o **Sistema de Comunicação**.

#### b) Sistema de Comunicação (a rede em si)
Um arranjo topológico que interliga vários equipamentos através de enlaces físicos e de um conjunto de regras que organizam a comunicação (**protocolos**).

---

## Protocolos
Conjunto de regras semânticas e sintáticas que devem ser seguidas para possibilitar a comunicação de duas entidades (pessoas, computadores, etc.).

#### a) Protocolos Humanos
Regras de relação entre as pessoas:
- "Que horas são?"
- "Onde você trabalha?"
- "Qual seu nome?"

#### b) Protocolos de Rede
Máquinas, ao invés de humanos, governam a comunicação. Toda a comunicação na internet é governada por protocolos, isto é, regras. Protocolos definem o formato e a ordem das mensagens enviadas e recebidas, além das ações a serem tomadas durante o envio e recepção das mensagens entre os computadores.

### Exemplo:
1. Uma máquina cliente pede uma conexão ao servidor.
2. O servidor abre a conexão.
3. O cliente pede uma página.
4. O servidor envia a página ao cliente, que a vê em sua tela.

---

## Internet
A internet é formada por milhões de elementos interligados através de redes que são conectadas por roteadores. Ela executa aplicações distribuídas, ou seja, serviços prestados de forma distribuída, sem uma máquina central gerenciadora.

### Forma Distribuída
A internet é formada por enlaces de comunicação, que são meios físicos de transmissão que interligam redes de computadores através de equipamentos chamados **roteadores**. Essas redes se comunicam enviando e recebendo pacotes de dados.

### Estrutura da Internet
- **Equipamentos da borda da rede:** Clientes e servidores que rodam aplicações. Clientes solicitam serviços e servidores os fornecem.
- **Núcleo da rede:** Roteadores e equipamentos que permitem a conexão entre as diversas redes através dos acessos (meios físicos).
- **Acesso, Meio Físico:** Enlaces e fibras ópticas.

---

## Borda da Rede
- **Hosts (sistemas finais):** Equipamentos que executam os aplicativos, localizados na extremidade da rede, podendo ser cliente ou servidor.
  
### Modelos de Comunicação:
- **Modelo Cliente/Servidor:** O cliente toma a iniciativa de pedir algum serviço ao servidor, que disponibiliza esse serviço utilizando a infraestrutura das redes que compõem a internet.
- **Modelo Peer-to-Peer (P2P):** A máquina tanto é cliente quanto servidora, ou seja, há uma simetria de comunicação, podendo tanto solicitar como fornecer serviços.

---

## Núcleo da Rede
Basicamente formada por roteadores e redes de roteadores, que encontram o melhor caminho para encaminhar pacotes de uma rede a outra. Esses equipamentos não rodam as aplicações web ou eletrônicas, apenas encaminham pacotes de dados por determinados caminhos, levando em consideração o congestionamento na rede. As tabelas de roteamento são atualizadas para garantir o melhor caminho a cada momento.

---

## Classificação das Redes Quanto à Abrangência

### a) Redes Pessoais (PANs)
- **Abrangência:** Aproximadamente 10 metros.
- **Características:** Sem fio, móveis e com restrições de consumo de energia.
- **Exemplo:** Bluetooth.

### b) Redes Locais (LANs)
- **Abrangência:** De 100 metros a milhares de metros.
- **Características:** Dispositivos com e sem fios, móveis ou não, que podem trocar grandes volumes de dados. São comuns em empresas e prédios.
- **Exemplo:** Ethernet, Wi-Fi, dados móveis.

### c) Redes Metropolitanas (MANs)
- **Abrangência:** Vários quilômetros.
- **Características:** Conectam LANs de empresas ou funcionam como rede de acesso para residências ou empresas.
- **Exemplo:** xDSL (cabos metálicos de telefones), HFC (cabos de fibra ótica).

### d) Redes Geograficamente Distribuídas (WANs)
- **Abrangência:** Milhares de quilômetros.
- **Características:** Usadas por operadoras de telefonia e grandes provedores de internet.
- **Exemplo:** MPLS, HDLC, Frame Relay.

---

# Resumo

### Conceitos Essenciais sobre Redes de Computadores, Sua Definição, Protocolos de Comunicação e a Estrutura da Internet:

- **Definições de Redes de Computadores:**
  - Conjunto de processadores (computadores) interligados por um sistema de comunicação para trocar informações e compartilhar recursos.
  - A rede é formada por computadores que enviam e recebem dados por meio de um sistema de comunicação, que organiza essa troca através de enlaces físicos e protocolos.

- **Protocolos:**
  - Regras para comunicação entre entidades, como pessoas ou computadores.
  - Existem protocolos humanos (como perguntas e respostas) e protocolos de rede (que governam as interações entre máquinas na internet, definindo o formato, ordem das mensagens e ações durante a comunicação).

- **A Internet:**
  - A internet é uma rede de redes interconectadas por roteadores, formada por dispositivos distribuídos (sem uma máquina central) que prestam serviços uns aos outros.
  - A estrutura da internet é dividida em duas partes:
    - **Borda da Rede:** Onde estão os clientes e servidores.
    - **Núcleo da Rede:** Onde os roteadores conectam diferentes redes, encaminhando pacotes de dados.

- **Modelos de Comunicação:**
  - **Modelo Cliente/Servidor:** O cliente solicita serviços ao servidor, que os fornece usando a infraestrutura da rede.
  - **Modelo Peer-to-Peer (P2P):** As máquinas atuam simultaneamente como clientes e servidores, com uma comunicação simétrica.

- **Classificação das Redes Quanto à Abrangência:**
  - **PANs (redes pessoais):** Alcance de até 10 metros, geralmente sem fio e móveis, como o Bluetooth.
  - **LANs (redes locais):** Alcance de até milhares de metros, usadas em empresas e prédios, permitindo troca de grandes volumes de dados (ex: Ethernet, Wi-Fi).
  - **MANs (redes metropolitanas):** Alcance de vários quilômetros, conectando LANs de empresas ou funcionando como rede de acesso para residências (ex: xDSL, HFC).
  - **WANs (redes de longa distância):** Alcance de milhares de quilômetros, conectando operadoras e grandes provedores de internet (ex: MPLS, HDLC).
