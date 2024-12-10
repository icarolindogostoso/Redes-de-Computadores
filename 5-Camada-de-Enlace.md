# Camada de Enlace

## Diferenciação entre a Camada Física e a Camada de Enlace

- **Camada Física**: Responsável pela transmissão de bits, codificação e multiplicação (realmente transmitir os bits).
- **Camada de Enlace**: Responsável por delimitar a informação (o que ela significa), detectar erros de transmissão, controlar o acesso ao meio físico e realizar o endereçamento físico.

## Funções da Camada de Enlace

### a) Delimitação da Informação

A camada física transmite uma sequência de bits sem qualquer semântica ou sintaxe associada:
- 10100101011101010010101111 <- Isso pode significar qualquer coisa, dependendo do contexto.

A camada de enlace estrutura a informação a ser transmitida em unidades lógicas chamadas **frames**, que possuem sintaxe e semântica predefinidas:
- 1010010 1011101 010010 101111 <- Cada fragmento será traduzido conforme o protocolo, para que a mensagem seja entendida.

O início e o fim de cada **frame** que passa pela rede podem ser determinados pelos equipamentos, permitindo que todos os dispositivos da rede que implementam a camada de enlace entendam as mensagens.

### b) Controle de Acesso ao Meio

Protocolos de enlace normalmente incluem um conjunto de regras que definem quando as estações podem transmitir no meio físico.

- Se em uma sala todos tentarem falar ao mesmo tempo, não será possível entender, então é necessário estabelecer regras para que apenas uma pessoa fale de cada vez.
  
Na camada de enlace, o "meio físico" pode ser comparado à sala onde as pessoas estão tentando falar, as "estações" são as "pessoas" (computadores, roteadores, etc.), e o controle de acesso ao meio são as regras que determinam quem pode transmitir dados e quando.

O controle de acesso ao meio físico tem grande influência na eficiência da rede.

Historicamente, o controle de acesso ao meio nas redes Ethernet se baseia em técnicas chamadas **CSMA**:

- **CSMA/CA** (para redes sem fio)
- **CSMA/CD** (para redes cabeadas)

#### CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

Quando uma estação deseja transmitir, ela segue os seguintes passos:

1. **"Ouvir"** o meio para verificar se há alguma transmissão em progresso.
2. Se não houver ninguém transmitindo, a estação pode transmitir.
3. Se já houver uma transmissão ocorrendo, ela espera um tempo aleatório e repete o passo 1.

O CSMA/CD detecta colisões durante a transmissão (quando duas estações transmitem ao mesmo tempo):

- Enquanto transmite, a estação continua "escutando".
- Quando o que a estação "escuta" é diferente do que ela está transmitindo, ocorre uma colisão.
  
Após a colisão ser detectada, as estações que estavam transmitindo:

1. Abortam a transmissão.
2. Esperam um tempo, calculado por um algoritmo apropriado, e tentam retransmitir.

Tecnicamente, o CSMA/CD é chamado de **IEEE 802.3**.

## IEEE 802.3 – Endereços MAC

O endereço MAC (Media Access Control) é um identificador único associado a cada interface de rede. Ele possui as seguintes características:

- **Armazenado no hardware**, mas pode ser alterado por software.
- Também chamado de **endereço físico**.

### Estrutura

- O endereço MAC possui **48 bits**, representado por 6 bytes de 2 caracteres hexadecimais:
  
  Exemplo: `01:23:45:67:89:ab`

- Os **3 primeiros bytes** identificam o fabricante.
- Os **3 bytes seguintes** são usados pelo fabricante para identificar cada dispositivo.

Existem faixas de endereços não usados ou com funções especiais, por exemplo:
- `ff:ff:ff:ff:ff:ff` – Usado para enviar um **frame** para todos os dispositivos da rede.

## Hubs Ethernet

- **Hubs** possibilitam a conexão de vários dispositivos.
- Um sinal introduzido em uma porta será enviado para todas as outras.
- Eles realizam a **"repetição"** do sinal.

## Switches Ethernet

- **Switches** operam na camada de enlace.
- Eles montam uma tabela com os endereços MAC dos dispositivos conectados a cada uma de suas portas, permitindo uma comunicação mais eficiente ao direcionar o tráfego de dados diretamente entre estações de destino.

## Resumo

A camada de enlace de dados é responsável por fornecer uma estrutura lógica e funcional à transmissão de dados, diferenciando-se da camada física, que lida apenas com a transmissão de bits.

### Funções da Camada de Enlace:
- **Delimitação da Informação**: Na camada física, os dados são transmitidos como uma sequência de bits sem significado. A camada de enlace organiza esses bits em unidades lógicas chamadas **frames**, com sintaxe e semântica predefinidas, permitindo que todos os dispositivos da rede compreendam a mensagem.
  
- **Controle de Acesso ao Meio**: Define regras para determinar quando as estações podem transmitir dados, garantindo que não haja colisões no meio físico. Protocolos **CSMA/CD** (para redes cabeadas) e **CSMA/CA** (para redes sem fio) são usados para gerenciar esse controle.
  
  - **CSMA/CD**: A estação escuta o meio para verificar se está livre. Se houver uma colisão (duas estações transmitindo ao mesmo tempo), a transmissão é abortada e reprogramada após um intervalo aleatório.

- **Endereçamento Físico (Endereço MAC)**: Cada interface de rede tem um endereço MAC único, um identificador de 48 bits usado para identificar dispositivos na rede. Os primeiros 3 bytes identificam o fabricante, e os últimos 3 são usados pelo fabricante para individualizar os dispositivos.

- **Hubs Ethernet**: Dispositivos que conectam múltiplos dispositivos, repetindo o sinal recebido em uma porta para todas as outras, sem distinguir entre os dispositivos conectados.

- **Switches Ethernet**: Funcionam na camada de enlace, criando uma tabela com os endereços MAC dos dispositivos conectados a suas portas, o que permite uma comunicação mais eficiente ao direcionar o tráfego de dados diretamente entre estações de destino.
