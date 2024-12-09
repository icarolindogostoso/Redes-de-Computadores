# Padrões das Arquiteturas de Rede (Organização OSI e TCP/IP)

As estruturas de redes de computadores são muito complexas devido aos diversos componentes de hardware e software envolvidos. Dentre esses componentes, temos:

- **Computadores**: Podem estar executando aplicações clientes, servidoras ou ambos.
- **Equipamentos**: Roteadores e switches, com um nível de complexidade elevado.
- **Enlaces de ligação**: Várias categorias de cabos diferentes.
- **Protocolos e Aplicações**: Executando funcionalidades para permitir a comunicação.

## Como Organizar o Funcionamento de uma Rede de Computadores?

Quando temos uma atividade complexa para realizar, costumamos dividi-la em passos, por exemplo, no caso de uma viagem:

1. Chegar ao aeroporto (início)
2. Despachar a bagagem
3. Embarcar
4. Decolar
5. Fazer a navegação aérea
6. Fazer o voo até o ponto distante

E o processo inverso:

1. Navegação aérea
2. Aterrissagem
3. Desembarque
4. Recebimento de bagagens
5. Saída do aeroporto (fim)

Além de dividir em partes, também podemos organizar por funcionalidades, ou seja, em **camadas**:

- Facilita a definição e o relacionamento das partes de um sistema complexo.
- Camadas são implantadas em conjunto com suas funcionalidades.

### Exemplo de Organização em Camadas (viagem):

- Chegar ao aeroporto / Sair do aeroporto
- Despachar bagagem / Receber bagagem
- Embarcar / Desembarcar
- Decolar / Aterrissar

Assim, é possível modificar ou readequar uma parte sem influenciar nas outras partes. Por exemplo, no processo de embarque, pode-se separar pessoas com deficiência, pessoas idosas ou aquelas nas janelas sem afetar o processo de bagagem.

### Arquiteturas de Redes de Computadores

Todas as arquiteturas de redes de computadores utilizam o conceito de dividir o conjunto de funcionalidades em camadas. Cada camada reúne um conjunto de funções semelhantes, prestando serviços à camada superior e recebendo serviços da camada inferior.

**Protocolos** são entidades de uma camada que permitem a interação entre instâncias da mesma camada, mas em equipamentos ou hosts distintos. Os protocolos de uma camada prestam serviços aos protocolos da camada superior e se relacionam com os da mesma camada em equipamentos distintos.

## Modelos de Arquitetura: RM-OSI e TCP/IP

### RM-OSI (Modelo de Referência de Interconexão de Sistemas Abertos)

Criado pela ISO, o RM-OSI tinha como objetivo criar um "modelo de referência" para todas as arquiteturas de rede. Ele é um modelo conceitual com a premissa de servir como referência para implementações reais, e se divide em 7 camadas:

1. **Física**: Estabelece os padrões de conectores, cabos, e representação de bits.
2. **Enlace**: Define protocolos para controlar a troca de informações (bits ou sinais) através do meio de transmissão (controle da informação no meio físico).
3. **Rede**: Promove a interconexão entre várias redes.
4. **Transporte**: Permite o transporte de informações fim a fim (máquina origem a máquina destino, sem se preocupar com o que veio anteriormente).
5. **Sessão**: Controla a transmissão, prevenindo que se perca todo o trabalho em caso de problemas de conexão.
6. **Apresentação**: Cria um contexto comum entre máquinas distintas (seja em hardware ou software, compatibilizando diferentes sistemas).
7. **Aplicação**: Faz a interface dos serviços com os usuários.

### Modelo TCP/IP

Criado pelo Departamento de Defesa dos EUA, o modelo TCP/IP é a arquitetura dos protocolos que define o funcionamento da internet e não deve ser confundido com a própria internet.

Ele define 5 camadas:

1. **Física**: Como no OSI, define os meios de transmissão (cabos, fibras).
2. **Enlace**: Similar ao OSI, controla o acesso e a transferência de dados dentro de uma rede local.
3. **Rede**: Realiza o roteamento de pacotes e determina o melhor caminho entre redes distintas.
4. **Transporte**: Garante a comunicação entre máquinas, controlando fluxo e erros (ex: TCP, UDP).
5. **Aplicação**: Engloba as funções de sessão, apresentação e aplicação do modelo OSI, proporcionando a interface com o usuário (ex: HTTP, SMTP).

### Diferença entre os Modelos OSI e TCP/IP

No TCP/IP, as camadas de **Sessão**, **Apresentação** e **Aplicação** do modelo OSI estão todas reunidas dentro da camada de **Aplicação**, e existe a funcionalidade de definir um contexto comum entre máquinas distintas, tanto no hardware quanto no software.

## Funções das Camadas

1. **Camada Física**:
   - Implementada em hardware.
   - Especifica os sinais elétricos e eletrônicos de cabos, fibras, pinos e outros.
   - Define como os bits são transmitidos nos meios físicos (se são modulados ou codificados, etc.).

2. **Camada de Enlace**:
   - Controla o acesso ao meio de transmissão (mesma rede).
   - Possui endereço físico, chamado **endereço MAC** (controle de acesso ao meio).
   - Transfere dados entre dois equipamentos da mesma rede, detectando e corrigindo erros e controlando o fluxo de dados.

3. **Camada de Rede**:
   - Transfere dados entre entidades localizadas em redes distintas.
   - Utiliza **endereço IP**.
   - Realiza o roteamento entre redes. O pacote que chega em um roteador descobre o melhor caminho a ser seguido no momento.

4. **Camada de Transporte**:
   - Possibilita a comunicação fim-a-fim (máquina origem a máquina destino), abstraindo o que aconteceu nos meios intermediários (roteadores, switches).
   - Permite o envio e recebimento de dados para várias aplicações de forma simultânea, utilizando **portas**.
   - Pode controlar o fluxo, detectar erros e garantir a sequência da informação (opcionalmente).

5. **Camada de Aplicação**:
   - Prestam serviços diretamente ao usuário (parte visível).
   - Exemplos: HTTP, FTP, SMTP e outros.

## Exemplos de Protocolos

- **Aplicação**: HTTP, SMTP, DNS – Prestam serviço diretamente ao usuário, geralmente se utilizando de um protocolo da camada de transporte.
- **Transporte**: TCP, UDP, RTP.
- **Rede**: IPv4, IPv6 – Funciona para encontrar o melhor caminho para enviar os pacotes pela rede.
- **Enlace**: Wi-Fi, Ethernet, Bluetooth – Protocolos de rede local e metropolitana.
- **Física**: 10BaseT, 100BaseT – Tecnologias de rede física para transmissões de curta ou longa distância, como cabos de TV ou telefonia.

## Fluxo de Dados nas Redes

- Os dados passam por várias camadas, sendo **encapsulados de baixo para cima**:
    1. Da **camada de aplicação** para **transporte** (adicionando cabeçalhos de controle).
    2. Da **transporte** para **rede** (com endereço IP).
    3. Da **rede** para **enlace** (com controle de fluxo e erro).
    4. Da **enlace** para **física** (transmissão via meio físico).

- Nos **roteadores**, os protocolos de **física**, **enlace** e **rede** são usados para encaminhar os pacotes. Já **transporte** e **aplicação** só são processados pelos **hosts** finais.

### Exemplo do Fluxo de Dados

1. **Na Máquina de Origem**: 
   - A camada de **transporte** recebe dados da **aplicação**, acrescenta um cabeçalho e parâmetros de verificação, e entrega o protocolo à camada de **rede**.
   - A camada de **rede** utiliza o **endereço IP** para enviar os dados para a rede distante.
   - A camada de **enlace** cuida da transferência do pacote através dos meios físicos.

2. **No Roteador**: 
   - A camada **física** recebe os pacotes e checa se há erros na camada de **enlace**.
   - O roteador verifica em sua tabela de roteamento qual o melhor caminho para os pacotes, levando-os para a próxima rede.

3. **Na Máquina de Destino**: 
   - O pacote chega e é entregue à camada de **transporte**.
   - O protocolo de **transporte** identifica a aplicação de destino através da porta e entrega os dados corretamente.

---

### Resumo

A exploração das arquiteturas de rede e como elas são organizadas, abordando os modelos de referência **OSI** e **TCP/IP** e suas respectivas camadas:

- **Arquiteturas de Rede**:
  - Redes de computadores envolvem **computadores**, **equipamentos de rede** (roteadores, switches), **enlaces de ligação** (cabos, fibras) e **protocolos e aplicações**.
  - Para organizar o funcionamento de uma rede complexa, as funcionalidades são divididas em **camadas**, facilitando a definição, modificação e manutenção de diferentes partes sem impactar outras.

- **Modelo OSI:**
  O modelo OSI define a comunicação em 7 camadas:

  1. **Física**: Estabelece os padrões de conectores, cabos e transmissão de bits.
  2. **Enlace**: Define protocolos para controlar a troca de informações, bits ou sinais através do meio de transmissão (controle da informação no meio físico).
  3. **Rede**: Promove a interconexão entre as várias redes.
  4. **Transporte**: Permite o transporte de informação fim a fim (máquina origem a máquina destino, sem se preocupar com o que veio anteriormente).
  5. **Sessão**: A premissa principal é controlar a transmissão (controlar um erro), não perdendo todo o trabalho caso aconteça algum problema de conexão.
  6. **Apresentação**: Cria um contexto comum entre máquinas que sejam distintas (seja em hardware ou em software, compatibilizando máquinas distintas).
  7. **Aplicação**: Faz a interface dos serviços com os usuários.

- **Modelo TCP/IP:**
  O modelo TCP/IP define a comunicação em 5 camadas:

  1. **Física**: Como no modelo OSI, define os meios de transmissão (cabos, fibras).
  2. **Enlace**: Similar ao OSI, controla o acesso e a transferência de dados dentro de uma rede local.
  3. **Rede**: Realiza o roteamento de pacotes e determina o melhor caminho entre redes distintas.
  4. **Transporte**: Possibilita a comunicação entre máquinas, controlando fluxo e erros (ex: TCP, UDP).
  5. **Aplicação**: Engloba as funções de sessão, apresentação e aplicação do modelo OSI, proporcionando a interface com o usuário (ex: HTTP, SMTP).

- **Função das Camadas**:
  - A camada **física** cuida da transmissão de bits.
  - A camada de **enlace** gerencia a comunicação dentro da mesma rede.
  - A camada de **rede** realiza a comunicação entre redes distintas.
  - A camada de **transporte** garante a comunicação fim-a-fim.
  - A camada de **aplicação** interage diretamente com o usuário.

- **Exemplos de Protocolos**:
  - **Aplicação**: HTTP, SMTP, DNS.
  - **Transporte**: TCP, UDP, RTP.
  - **Rede**: IPv4, IPv6.
  - **Enlace**: Wi-Fi, Ethernet, Bluetooth.
  - **Física**: 10BaseT, 100BaseT.

- **Fluxo de Dados nas Redes**:
  - Os dados são encapsulados de **baixo para cima** e passados por várias camadas antes de serem entregues ao destino final.
  - Nos **roteadores**, apenas as camadas **física**, **enlace** e **rede** são processadas. Já nas **máquinas finais**, todos os protocolos são processados para garantir a comunicação correta.
