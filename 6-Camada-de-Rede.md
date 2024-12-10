# Camada de Rede

## Camada Física
- Transmissão de bits
- Codificação
- Multiplexação

## Camada de Enlace
- Delimitação da informação
- Detecção de erros de transmissão
- Controle de acesso ao meio físico
- Endereçamento físico

## Camada de Rede
- Endereçamento
- "Tradução" de endereços de enlace
- Roteamento de dados até o destino

Basicamente, a camada de rede provê os meios para a transmissão de dados entre entidades do nível de transporte.

---

# Modelo Internet TCP/IP

- O **Modelo TCP/IP** é um conjunto de regras que define como os dispositivos na internet se comunicam entre si.
- Ele organiza a comunicação em camadas, mas não se preocupa muito com os detalhes de como os dados viajam fisicamente pelos fios ou como as redes locais estão configuradas.
- O modelo **TCP/IP** não especifica como os dados são fisicamente enviados (se por fios, Wi-Fi, etc), deixando esses detalhes para outros modelos como o **OSI**.
- O modelo TCP/IP pode usar diferentes tecnologias de rede física e de enlace enquanto ainda segue as regras de comunicação TCP/IP.
- O modelo é mais simples e flexível, pois não se preocupa com como os dados são fisicamente transmitidos, permitindo que diferentes tipos de rede e tecnologias possam ser usadas, ajudando a internet a crescer de maneira rápida e eficiente.

**Resumo**: O modelo TCP/IP foca na comunicação de dados entre dispositivos, sem se preocupar muito com os detalhes de como os dados são fisicamente transmitidos, facilitando a adaptação de várias tecnologias e promovendo o crescimento da internet.

- **Observação 1**: A partir da camada de rede, a implementação é 100% em software.
- **Observação 2**: No modelo TCP/IP, é definido com clareza quais protocolos devem ser usados nas camadas de rede, transporte e aplicação. Esses protocolos são abertos e públicos, ou seja, qualquer um pode usar ou implementar esses protocolos sem custo.

---

# Funções da Camada de Rede

- **Endereçamento**: Atribuição de endereços lógicos (endereços IP) para cada uma das estações de rede.
  
  *Exemplo*: Imagine que você tem uma rede de computadores em casa, e cada computador precisa de um **ENDEREÇO ÚNICO** para poder se comunicar com os outros. Esse endereço único na rede é o **ENDEREÇO IP**.

- **Tradução de Endereços**: Realização do mapeamento entre todos os endereços lógicos (IP) em endereços físicos (MAC).

  *Exemplo*: Agora imagine que seu computador quer mandar uma mensagem para outro computador na mesma rede, mas para fazer isso ele precisa saber o **ENDEREÇO FÍSICO** do dispositivo de destino, o qual é chamado de **ENDEREÇO MAC**.

- **Roteamento**: Encaminhamento das unidades de dados até o seu destino, passando pelos sistemas intermediários.

  *Exemplo*: Agora imagine que você está tentando acessar um site que está hospedado em outro país. Seu computador precisa enviar dados para o servidor que está lá. A camada de rede encaminha os dados por **ROTEADORES**, que determinam o melhor caminho para que as informações cheguem ao destino, mesmo que o servidor esteja do outro lado do mundo.

---

# Protocolo IP

- O **Protocolo IP** implementa as funções de **ENDEREÇAMENTO** e **ROTEAMENTO**.
- Opera pela transferência de blocos de dados denominados **DATAGRAMAS** (pacotes).
- A origem e destino de cada datagrama são identificados através de endereços presentes no seu cabeçalho.
- **CADA DATAGRAMA É TRATADO DE FORMA INDEPENDENTE** pela rede, não possuindo nenhuma relação com qualquer outro.

**Características**:
- **Não confiável**: Não garante que os pacotes de dados cheguem ao destino ou que eles cheguem na ordem correta. Ele apenas se encarrega de endereçar e enviar os pacotes.
- **Não orientado a conexão**: Não há uma preparação ou "negociação" antes do envio de dados. Não existe uma "conexão" formal entre o remetente e o receptor. Cada pacote de dados enviado é independente e não depende de pacotes anteriores ou posteriores.
- **Não realiza controle de erro**: Não verifica se os dados chegaram corretamente ou se foram corrompidos.
- **Não realiza controle de fluxo**: Não verifica se o dispositivo de destino é capaz de receber os pacotes de dados na velocidade em que estão sendo enviados.

**Observação**: Essas funções são deixadas para serem implementadas na camada de transporte.

---

# Resumo

- **Camada de Rede**: Responsável por:
  - **Endereçamento**: Atribuição de endereços lógicos (endereços IP) a cada estação de rede.
  - **Tradução de Endereços**: Mapeamento entre endereços lógicos (IP) e endereços físicos (MAC).
  - **Roteamento**: Encaminhamento dos dados para o destino através de roteadores.

- **Modelo TCP/IP**:
  - Define como os dispositivos se comunicam na internet, organizando a comunicação em camadas.
  - Não se preocupa com os detalhes físicos da transmissão de dados (como fios ou Wi-Fi), permitindo flexibilidade para usar diferentes tecnologias de rede.
  - Foco na comunicação entre dispositivos, facilitando a adaptação a várias tecnologias e ajudando a internet a crescer rapidamente.

- **Características do TCP/IP**:
  - **Simplicidade e Flexibilidade**: Não se preocupa com os detalhes físicos da transmissão, o que facilita a adaptação a diferentes redes.
  - **Protocolos Abertos e Públicos**: Os protocolos usados são abertos, permitindo que qualquer um os implemente sem custo.

- **Funções da Camada de Rede**:
  - **Endereçamento**: Atribui um endereço IP único a cada dispositivo na rede.
  - **Tradução de Endereços**: Converte endereços IP (lógicos) em endereços MAC (físicos) para a comunicação na rede local.
  - **Roteamento**: Envia os dados para o destino através de roteadores, determinando o melhor caminho, mesmo que o destino esteja em outra parte do mundo.

- **Protocolo IP**:
  - O protocolo IP é responsável por endereçar e rotear dados, usando **DATAGRAMAS** (pacotes).
  - **Características do IP**:
    - **Não confiável**: Não garante que os pacotes cheguem ao destino nem na ordem correta.
    - **Não orientado a conexão**: Cada pacote é independente, sem necessidade de uma conexão prévia.
    - **Sem controle de erro**: Não verifica se os pacotes chegam corretamente ou se foram corrompidos.
    - **Sem controle de fluxo**: Não verifica se o destino pode receber os pacotes na velocidade de fluxo.
  - Essas funções (controle de erro e fluxo) são tratadas na **CAMADA DE TRANSPORTE**.
