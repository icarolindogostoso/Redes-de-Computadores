# Camada de Transporte

## Camada Física:
- Transmissão de bits seja pelo ar, sem fio, com fio.

## Camada de Enlace:
- Delimitação da informação.

## Camada de Rede:
- Endereçamento.

## Camada de Transporte:
- Multiplexação dos fluxos de dados.
- Confiabilidade.
- Controle de erros e fluxos.

A camada de transporte da máquina de origem se comunica diretamente com a camada de transporte da máquina de destino, sem depender dos sistemas intermediários que existem entre elas.

Isso significa que, quando uma máquina envia dados para outra, as camadas de transporte de ambas as máquinas trocam informações de forma direta e sem se preocupar com o que acontece nas camadas inferiores, como física, de enlace ou de rede.

**Exemplo:**
Se você está enviando uma mensagem de texto de um celular para outro, a camada de transporte do seu celular vai se comunicar diretamente com a camada de transporte do celular destino, sem se importar com as redes, roteadores ou cabos que estão no caminho. Agora, se estivermos falando das camadas física, de enlace ou de rede, aí sim a comunicação depende dos sistemas intermediários, como os fios ou sinais sem fio, porque esses níveis lidam com a transmissão dos dados de um ponto a outro de forma física.

---

## Modelo Internet TCP/IP

### Protocolos de Transporte:
- **a)** TCP (Transmission Control Protocol).
- **b)** UDP (User Datagram Protocol).

### TCP x UDP

#### Diferenças:
- **Complexidade:** O TCP é mais complexo por garantir que os dados cheguem corretamente ao destino, controlando possíveis erros, perdas e a origem de chegada. Já o UDP é mais simples, porque não se preocupa com isso, apenas enviando os dados.
- **Conjunto de Funcionalidades:** O TCP oferece várias funcionalidades extras, como confirmação de recebimento de dados e reorganização das mensagens na ordem certa. O UDP é mais direto, enviando os dados de forma rápida e sem garantias.
- **Aplicações Usuais:** O TCP é usado em aplicações onde é importante que os dados cheguem com precisão, como em navegadores de internet (HTTP), e-mails (SMTP), ou transferência de arquivos (FTP). Já o UDP é usado em situações onde a velocidade é mais importante que a precisão, como em jogos online, chamadas de vídeo ou streaming de vídeo, onde pode ser aceitável perder alguns pacotes de dados, mas a comunicação precisa ser rápida.

#### Semelhanças:
- **Multiplexação e Demultiplexação:** Ambos têm o processo de multiplexação e demultiplexação, o que significa que ambos podem lidar com múltiplas conexões de rede ao mesmo tempo. Elas usam **PORTAS** para identificar diferentes tipos de comunicação, como um número de um quarto de hotel.

**Exemplo:** No TCP e no UDP, a porta 80 é geralmente usada para comunicação de sites (HTTP), enquanto a porta 443 é usada para conexões seguras (HTTPS).

---

## Portas

As portas podem ser entendidas como números de identificação, como se cada aplicação fosse um escritório dentro de um prédio. Mesmo que todas as aplicações estejam no mesmo computador (o prédio), cada uma precisa de um número específico (a porta) para saber por onde receber e enviar dados, sem confundir com outras.

Cada conexão feita entre duas máquinas é identificada por uma **QUADRUPLA** única:
- **IP de origem:** O endereço do computador de onde os dados estão saindo.
- **Porta de origem:** O número da porta do computador de origem, identificando a aplicação que está enviando os dados.
- **IP de destino:** O endereço do computador para onde os dados estão indo.
- **Porta de destino:** A porta da aplicação no computador de destino, para onde os dados devem ser entregues.

**Exemplo:** Se o IP do seu computador for `192.168.1.10` e a porta `12345` e o IP do servidor for `203.0.113.20` com a porta `80`, isso permite que seu computador saiba que está se conectando ao servidor de sites e qual aplicação está fazendo a conexão.

Cada identificador de porta possui 16 bits de comprimento, podendo variar de 0 a 65535.

Portas de origem e destino são selecionadas aleatoriamente para uso pelo TCP e UDP, mas em servidores, portas utilizadas por aplicações "comuns" utilizam valores fixos. **Exemplo:**
- **22:** SSH
- **25:** SMTP
- **53:** DNS
- **80:** HTTP
- **443:** HTTPS

Essas portas também são chamadas de **portas baixas** por estarem abaixo de 1024.

---

## UDP

O **UDP** (User Datagram Protocol) é um tipo de protocolo de comunicação definido na RFC 768. Ele oferece um serviço de **melhor esforço**, o que significa que ele vai tentar enviar os dados da melhor forma possível, mas não garante que os dados vão chegar corretamente ou que cheguem na ordem certa. Ou seja, ele faz o possível, mas sem promessas.

### Características:
- **Não orientado a conexão:** O UDP não estabelece uma conversa contínua entre as duas máquinas antes de começar a trocar dados. Ele simplesmente envia os dados e espera que o destinatário os receba (sem garantia).
- **Tratamento independente dos pacotes:** Cada pacote UDP é tratado de forma independente, ou seja, ele não se preocupa com outros pacotes que possam estar sendo enviados. Cada pacote é enviado como uma mensagem isolada, sem depender dos anteriores ou dos seguintes.

**Exemplo:** Em um jogo online, o UDP vai enviar dados como movimentos do personagem. O jogo não espera ou verifica se todos os pacotes chegaram corretamente, só se importando com a velocidade e, caso algum dado seja perdido, ele é ignorado.

### Formato do segmento:
- **Porta de origem / Porta de destino:** 32 bits
- **Tamanho / Checksum:** 32 bits
- **Dados da aplicação**

- **Tamanho:** É o tamanho em bytes do segmento UDP, incluindo o cabeçalho.
- **Checksum:** É usado para garantir que os dados não foram corrompidos durante a transmissão. Em caso de erro, o pacote com erro é descartado sem qualquer tentativa de correção ou retransmissão.

Se uma aplicação usa UDP, partes do fluxo de dados entre origem e destino podem:
- Ser perdidos.
- Chegar fora de ordem.
- Chegar com erros.

Se a aplicação precisar garantir que os dados cheguem corretamente, na ordem certa e sem erros, ela tem que implementar essas verificações e correções por conta própria. O UDP apenas envia os dados sem fazer nenhuma verificação ou correção.

### Usado por:
- Aplicações onde o volume de dados trocado é pequeno, como **DNS**.
- Aplicações que não exigem alta confiabilidade, como **transmissão de vídeo** e **áudio**.

---

## TCP

O **TCP** (Transmission Control Protocol) implementa um serviço:

- **Orientado a conexão:** Antes de começar a enviar os dados, o TCP estabelece uma "conversa" entre o remetente e o destinatário para garantir que ambos estão prontos para a troca de dados. Só depois que essa conexão é estabelecida é que os dados começam a ser enviados.
- **Confiável:** O TCP se preocupa em garantir que os dados cheguem corretamente. Se algum dado se perder ou tiver erro no caminho, o TCP vai detectar e pedir para reenviar aquele dado até que ele chegue de forma correta.
- **Controle de erros:** Há uma verificação se os dados chegaram completos e sem alterações. Se algum erro for detectado, ele solicita que o pacote com o erro seja reenviado.
- **Controle de fluxo:** Há um controle da quantidade de dados que pode ser enviada de uma só vez, para evitar que o destinatário fique sobrecarregado com muitos dados de uma vez só. Isso é como se fosse um limite de velocidade para garantir que tudo chegue de forma ordenada e sem pressa.

### Formato do segmento:
- **Porta de origem / Porta de destino:** 32 bits
- **Número de sequência:** 32 bits
- **Número de reconhecimento:** 32 bits
- **Tamanho do cabeçalho / Não usado / U / A / P / R / S / F / Janela de recepção:** 32 bits
- **Checksum / Dados urgentes:** 32 bits
- **Opções:** Tamanho variável
- **Dados da aplicação**

### Campos:
- **Número de sequência** e **número de reconhecimento:** Utilizados para sequenciamento e confiabilidade.
- **A (ACK):** Confirmações.
- **R, S, F (RST, SYN, FIN):** Abertura e encerramento de conexão.
- **Janela de recepção:** Número de bytes que o receptor está pronto para aceitar.

### Processo:

#### a) Estabelecimento de Conexão:
Antes que o cliente e o servidor possam começar a trocar dados, eles precisam primeiro estabelecer uma conexão. Isso é como fazer um acordo ou um aperto de mão entre os dois para garantir que ambos estão prontos para a comunicação. O processo é chamado de **Three-Way Handshake**.

1. O cliente manda um pedido para o servidor dizendo que quer se conectar (**bit SYN = 1**).
2. O servidor responde dizendo "ok, estou pronto para me conectar" (**bit SYN e ACK = 1**).
3. O cliente confirma que recebeu a resposta e que está pronto para começar a trocar dados (**bit ACK = 1**).

#### b) Encerramento de Conexão:
Quando o cliente ou o servidor deseja encerrar a conexão, ele envia os bits **FIN** e **ACK** ativados (= 1). Isso é como se fosse um aviso dizendo "estou pronto para terminar nossa conversa". Depois, o outro lado precisa responder com um **ACK**, indicando que pode encerrar.

#### c) Transferência de Dados:
Cada pacote de dados enviado possui um **número de sequência**. Esse número serve como uma identificação única para cada pedaço de dados que está sendo transmitido. Esses números de sequência ajudam a **reorganizar** os dados na ordem correta.

### Controle de Fluxo e Congestionamento:
O TCP ajusta automaticamente a quantidade de dados enviados com base em alguns fatores importantes:
- **ACKs rápidos:** Se os ACKs estão chegando rapidamente, o TCP pode aumentar o ritmo de envio.
- **Retransmissões:** Se muitos pacotes precisam ser retransmitidos, isso pode ser um sinal de congestionamento e o TCP reduzirá a velocidade para evitar sobrecarregar a rede.

---

## Resumo

A camada de transporte do modelo OSI ou TCP/IP é responsável pela comunicação direta entre as camadas de transporte das máquinas de origem e destino, sem depender das camadas inferiores (física, de enlace ou rede). Ela cuida da multiplexação de dados, confiabilidade e controle de erros e fluxo.

### Principais Protocolos:
- **TCP**
  - Orientado a conexão.
  - Confiabilidade: garante que os dados cheguem corretamente e na ordem certa.
  - Controle de fluxo: gerencia a quantidade de dados enviados.
  - Exemplos de uso: navegação na web (HTTP), envio de e-mails (SMTP), FTP.
  - Estabelecimento de conexão: utiliza o processo **Three-Way Handshake**.
  - Encerramento da conexão: finaliza a comunicação de forma ordenada usando bits **FIN** e **ACK**.

- **UDP**
  - Sem conexão.
  - Menos confiável: não realiza verificações ou retransmissões.
  - Exemplo de uso: jogos online, streaming de vídeo, chamadas de voz.
  - Formato do pacote: contém dados de aplicação, portas de origem/destino e um **checksum** para verificar erros.

### Portas:
As portas identificam as diferentes aplicações em uma máquina, funcionando como número de identificação para troca de dados. Cada conexão é identificada por uma **quadrupla** única: IP de origem, porta de origem, IP de destino e porta de destino.

### Diferenças entre TCP e UDP:
- **TCP:** Mais complexo, garante entrega correta, reordenação de pacotes, controle de fluxo e erros. Usado em aplicações que requerem confiabilidade.
- **UDP:** Mais simples, sem garantias de entrega ou ordem dos pacotes. Usado quando a velocidade é mais importante, como em transmissão de vídeo e jogos.

### Controle de Fluxo e Congestionamento no TCP:
O TCP ajusta automaticamente a quantidade de dados enviados com base na recepção de confirmações (ACKs) e na quantidade de pacotes retransmitidos, ajudando a evitar congestionamento da rede.

### Exemplos de Portas Fixas:
- **22:** SSH
- **25:** SMTP
- **53:** DNS
- **80:** HTTP
- **443:** HTTPS
