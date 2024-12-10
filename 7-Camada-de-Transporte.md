# Camada de Transporte

## Camada Física:
- Transmissão de bits seja pelo ar, sem fio, com fio.

## Camada de Enlace:
- Delimitação da informação.

## Camada de Rede:
- Endereçamento.

## CAMADA DE TRANSPORTE:
- Multiplexação dos fluxos de dados.
- Confiabilidade.
- Controle de erros e fluxos.

A camada de transporte da máquina de origem se comunica diretamente com a camada de transporte da máquina de destino, sem depender dos sistemas intermediários que existem entre elas.

Isso significa que, quando uma máquina envia dados para outra, as camadas de transporte de ambas as máquinas trocam informações de forma direta e sem se preocupar com o que acontece nas camadas inferiores, como física, de enlace ou de rede.

### Exemplo:
Se você está enviando uma mensagem de texto de um celular para outro, a camada de transporte do seu celular vai se comunicar diretamente com a camada de transporte do celular destino, sem se importar com as redes, roteadores ou cabos que estão no caminho.

Agora, se estivermos falando das camadas física, de enlace ou de rede, aí sim a comunicação depende dos sistemas intermediários, como os fios ou sinais sem fio, porque esses níveis lidam com a transmissão dos dados de um ponto a outro de forma física.

## Modelo Internet TCP/IP
Patronizado dois protocolos de transporte:
- a) **TCP** (Transmission Control Protocol)
- b) **UDP** (User Datagram Protocol)

## TCP X UDP

### Diferenças:
- **COMPLEXIDADE**: O TCP é mais complexo por garantir que os dados cheguem corretamente ao destino, controlando possíveis erros, perdas e a ordem de chegada. Já o UDP é mais simples, porque não se preocupa com isso, apenas enviando os dados.
- **CONJUNTO DE FUNCIONALIDADES**: O TCP oferece várias funcionalidades extras, como confirmação de recebimento de dados e reorganização das mensagens na ordem certa. O UDP é mais direto, enviando os dados de forma rápida e sem garantias.
- **APLICAÇÕES USUÁRIAS**: O TCP é usado em aplicações onde é importante que os dados cheguem com precisão, como em navegadores de internet (HTTP), e-mails (SMTP) ou transferência de arquivos (FTP). Já o UDP é usado em situações onde a velocidade é mais importante que a precisão, como em jogos online, chamadas de vídeo ou streaming de vídeo, onde pode ser aceitável perder alguns pacotes de dados, mas a comunicação precisa ser rápida.

### Semelhanças:
- Ambos têm o processo de **MULTIPLEXAÇÃO** e **DEMULTIPLEXAÇÃO**, o que significa que ambos podem lidar com múltiplas conexões de rede ao mesmo tempo. Elas usam **PORTAS** para identificar diferentes tipos de comunicação, como um número de um quarto de hotel.

**Exemplo**: No TCP e no UDP, a porta 80 é geralmente usada para comunicação de sites (HTTP), enquanto a porta 443 é usada para conexões seguras (HTTPS).

## Portas
As portas podem ser entendidas como números de identificação, como se cada aplicação fosse um escritório dentro de um prédio. Mesmo que todas as aplicações estejam no mesmo computador (o prédio), cada uma precisa de um número específico (a porta) para saber por onde receber e enviar dados, sem confundir com outras.

Cada conexão feita entre duas máquinas é identificada por uma **QUADRUPLA única**:
- IP de origem → o endereço do computador de onde os dados estão saindo.
- Porta de origem → o número da porta do computador de origem, identificando a aplicação que está enviando os dados.
- IP de destino → o endereço do computador para onde os dados estão indo.
- Porta de destino → a porta da aplicação no computador de destino, para onde os dados devem ser entregues.

Exemplo: Se o IP do seu computador for `192.168.1.10` e a porta `12345` e o IP do servidor for `203.0.113.20` com a porta `80`, isso permite que seu computador saiba que está se conectando ao servidor de sites e qual aplicação está fazendo conexão.

Cada identificador de porta possui 16 bits de comprimento, podendo variar de 0 a 65535.

Portas de origem e destino são selecionadas aleatoriamente para uso pelo TCP e UDP, mas em servidores, portas utilizadas por aplicações "comuns" utilizam valores fixos. Ex:  
- 22: **SSH**
- 25: **SMTP**
- 53: **DNS**
- 80: **HTTP**
- 443: **HTTPS**

Essas portas também são chamadas de **portas baixas** por estarem abaixo de 1024.

## UDP
Tipo de protocolo de comunicação definido na **RFC 768**.

Ele oferece um serviço de **MELHOR ESFORÇO**, o que significa que ele vai tentar enviar os dados da melhor forma possível, mas não garante que os dados vão chegar corretamente ou que cheguem na ordem certa. Ou seja, ele faz o possível, mas sem promessas.

O UDP **NÃO É ORIENTADO A CONEXÃO**, o que significa que não há uma conversa contínua entre as duas máquinas antes de começar a trocar de dados. Ele simplesmente envia os dados e espera que o destinatário os receba (sem garantia).

Além disso, **CADA PACOTE UDP É TRATADO DE FORMA INDEPENDENTE**, ou seja, ele não se preocupa com outros pacotes que possam estar sendo enviados. Cada pacote é enviado como uma mensagem isolada, sem depender dos anteriores ou dos seguintes.

Exemplo: Em um jogo online, o UDP vai enviar dados como movimentos do personagem. O jogo não espera ou verifica se todos os pacotes chegaram corretamente, só se importando com a velocidade e se, caso algum dado seja perdido, é ignorado.

### Formato do Segmento:
- **Porta origem / porta destino** → 32 bits
- **Tamanho / checksum** → 32 bits
- **Dados da aplicação**

**Tamanho** → é o tamanho em bytes do segmento UDP, incluindo o cabeçalho.  
**Checksum** → é usado para garantir que os dados não foram corrompidos durante a transmissão, em caso de haver erro, o pacote com erro é descartado sem qualquer tentativa de correção ou retransmissão.

Se uma aplicação usa UDP, partes do fluxo de dados entre origem e destino podem:
- Ser perdidos.
- Chegar fora de ordem.
- Chegar com erros.

Se a aplicação precisar garantir que os dados cheguem corretamente, na ordem certa e sem erros, ela tem que implementar essas verificações e correções por conta própria. O UDP apenas envia os dados sem fazer nenhuma verificação ou correção.

**Utilizado por**:
- Aplicações onde o volume de dados trocado é pequeno (ex: DNS).
- Aplicações que não exigem alta confiabilidade: transmissão de vídeo e áudio.

## TCP
Implementa um serviço:
- **Orientado a Conexão** → Antes de começar a enviar os dados, o TCP estabelece uma "conversa" entre o remetente e o destinatário para garantir que ambos estão prontos para a troca de dados. Só depois que essa conexão é estabelecida é que os dados começam a ser enviados.
- **Confiável** → O TCP se preocupa em garantir que os dados cheguem corretamente. Se algum dado se perder ou tiver erro no caminho, o TCP vai detectar e pedir para reenviar aquele dado até que ele chegue de forma correta.
- **Controle de Erros** → Há uma verificação se os dados chegaram completos e sem alterações. Se algum erro for detectado, ele solicita que o pacote com o erro seja reenviado.
- **Controle de Fluxo** → Há um controle da quantidade de dados que pode ser enviada de uma só vez, para evitar que o destinatário fique sobrecarregado com muitos dados de uma vez só. Isso é como se fosse um limite de velocidade para garantir que tudo chegue de forma ordenada e sem pressa.

### Formato do Segmento:
- **Porta origem / porta destino** → 32 bits
- **Número de sequência** → 32 bits
- **Número de reconhecimento** → 32 bits
- **Tam cabec / não usado / U / A / P / R / S / F / janela de recepção** → 32 bits
- **Checksum / dados urgentes** → 32 bits
- **Opções** → Tamanho variável.
- **Dados de aplicação**

### Detalhes:
- **Número de sequência** e **número de reconhecimento** → Utilizados para sequenciamento e confiabilidade.
- **A** - ACK - Confirmações.
- **R, S, F** - RST, SYN, FIN - Abertura e encerramento de conexão.
- **Janela de recepção** → Número de bytes que o receptor está pronto para aceitar.

### Processo:

#### a) Estabelecimento de Conexão:
Antes que o cliente e o servidor possam começar a trocar dados, eles precisam primeiro estabelecer uma conexão. Isto é como fazer um acordo ou um aperto de mão entre os dois para garantir que ambos estão prontos para a comunicação.

- O cliente faz algumas preparações antes de começar, como escolher uma porta de origem, que é como um número de identificação para a aplicação que está fazendo a solicitação.

Esse processo de abrir a conexão é chamado de **THREE-WAY HANDSHAKE**, funcionando assim:
1. O cliente manda um pedido para o servidor dizendo que quer se conectar (bit SYN = 1).
2. O servidor responde dizendo "ok, estou pronto para me conectar" (bit SYN e ACK = 1).
3. O cliente confirma que recebeu a resposta e que está pronto para começar a trocar dados (bit ACK = 1).

#### b) Encerramento de Conexão:
Quando o cliente ou o servidor deseja encerrar a conexão, ele envia os bits **FIN** e **ACK** ativados (= 1). Isso é como se fosse um aviso dizendo "estou pronto para terminar nossa conversa".

Depois o outro lado precisa responder com um **ACK** que é um "ok, podemos encerrar".

Esse processo garante que ambos os lados saibam que a conexão vai ser encerrada corretamente sem deixar nada pendente.

#### c) Transferência de Dados:
Cada pacote de dados enviado possui um **NÚMERO DE SEQUÊNCIA**. Esse número serve como uma identificação única para cada pedaço de dados que está sendo transmitido.

Esses números de sequência ajudam a **REORGANIZAR** os dados na ordem correta.

Mesmo o nome sendo "número de sequência", ele não segue uma contagem simples e sequencial. O número não é necessariamente o próximo número em ordem crescente, mas sim uma forma de identificar os dados corretamente.

**Importante**: O número de sequência é atribuído **AOS DADOS** e não aos **PACOTES**. Isso significa que mesmo que o TCP envie vários pacotes, o número de sequência se refere ao conteúdo dos dados e ajuda a juntar tudo de forma certa.

Exemplo: Suponha que um servidor irá enviar um arquivo de 4278 bytes para o cliente em pedaços de 800 bytes. Neste caso, os números de sequência dos segmentos TCP serão: `0, 800, 1600, 2400, 3200, 4000`.

#### ACK
Quando o servidor ou cliente recebe um pedaço de informação, ele envia de volta uma confirmação (**ACK**) dizendo "ok, recebi" que indica que o dado foi recebido corretamente.

O número de reconhecimento que está no ACK é o próximo dado que o servidor ou cliente espera receber. Por exemplo, se o servidor recebeu até o byte 100, ele enviaria um **ACK** com o número 101, sinalizando que está esperando o próximo byte a partir desse número.

Esse processo de confirmação é chamado **RECONHECIMENTO PASSIVO**. Ou seja, cada vez que um dado é recebido corretamente, uma resposta positiva é enviada. Caso o servidor ou cliente não receba o **ACK** dentro de um tempo determinado, ele entende que o dado não chegou corretamente e tenta enviar novamente.

#### Controle de Fluxo e Congestionamento
Para isso, é ajustado automaticamente a quantidade de dados enviados com base em alguns fatores importantes:
- Primeiro ele observa quanto tempo leva para receber as confirmações (ACKs). Se os ACKs estão chegando rapidamente, o TCP pode aumentar o ritmo de envio. Se demorar mais, ele pode reduzir a velocidade (**TCP SlowStart**).
- Outro fator que o TCP leva em conta é a quantidade de vezes que ele precisa reenviar dados. Se ele está tendo que retransmitir muitos pacotes porque eles não foram recebidos corretamente, isso pode ser um sinal de congestionamento, e o TCP vai reduzir a velocidade para evitar sobrecarregar a rede.

O controle garante que tanto o computador que está enviando quanto o que está recebendo funcionem de maneira equilibrada, se ficar nem parados esperando informações, nem sobrecarregados com dados demais.

## RESUMO

A camada de transporte do modelo OSI ou TCP/IP é responsável pela comunicação direta entre as camadas de transporte das máquinas de origem e destino, sem depender das camadas inferiores (física, de enlace ou rede). Ela cuida da multiplexação de dados, confiabilidade e controle de erros e fluxo.

### Principais Protocolos:
- **TCP**
  - a) Orientado a conexão → Estabelece uma conexão entre o remetente e o destinatário antes de enviar os dados.
  - b) Confiabilidade → Garante que os dados cheguem corretamente e na ordem certa, realizando controle de erros e retransmissões se necessário.
  - c) Controle de fluxo → Gerencia a quantidade de dados enviados para evitar sobrecarregar o receptor.
  - d) Exemplos de uso → Navegação na web (HTTP), envio de emails (SMTP), FTP.
  - e) Estabelecimento de conexão → Utiliza o processo **three-way handshake** para garantir que ambos os lados estão prontos para a comunicação.
  - f) Encerramento da conexão → Finaliza a comunicação de forma ordenada usando bits **FIN** e **ACK**.

- **UDP**
  - a) Sem conexão → Não estabelece uma conversa antes de enviar dados. Envia pacotes de dados de forma independente, sem garantir a entrega ou a ordem correta.
  - b) Menos confiável → Não realiza verificações ou retransmissões. Ideal para aplicações onde a velocidade é mais importante que a precisão.
  - c) Exemplo de uso → Jogos online, streaming de vídeo, chamadas de voz.
  - d) Formato do pacote → Contém dados de aplicação, portas de origem/destino e um **checksum** para verificar erros.

### Portas:
As portas identificam as diferentes aplicações em uma máquina, funcionando como número de identificação para troca de dados. Cada conexão é identificada por uma **QUADRUPLA única**: IP de origem, porta de origem, IP de destino e porta de destino.

### Diferenças entre TCP e UDP:
- **TCP** → Mais complexo, garante entrega correta, reorganização de pacotes, controle de fluxo e erros. Usado em aplicações que requerem confiabilidade.
- **UDP** → Mais simples, sem garantias de entrega ou ordem dos pacotes. Usado quando a velocidade é mais importante, como em transmissão de vídeo e jogos.

### Controle de Fluxo e Congestionamento no TCP:
O TCP ajusta automaticamente a quantidade de dados enviados com base na recepção de confirmações (**ACKs**) e na quantidade de pacotes retransmitidos, ajudando a evitar congestionamento da rede.

### Exemplos de Portas Fixas:
- 22: **SSH**
- 25: **SMTP**
- 53: **DNS**
- 80: **HTTP**
- 443: **HTTPS**
