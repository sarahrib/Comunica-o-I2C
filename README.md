# Comunicação I2C

## Resumo
Essa documentação tem como objetivo explicar e exemplificar o funcionamento e as características da comunicação I2C (Inter-Integrated Circuit). Foi desenvolvido um projeto pessoal que utilizou o Raspberry Pi Pico W, o sensor de humidade e temperatura DHT11 e um LCD 16x2.

## Introdução
O protocolo I2C, ou Inter-Integrated Circuit, destaca-se como uma das formas fundamentais de comunicação entre sistemas. Ao utilizar esse protocolo, diferentes dispositivos, independentemente de sua composição, podem estabelecer comunicação entre si por meio de um barramento compartilhado. Desenvolvido pela Phillips em 1982, o I2C permanece relevante até os dias de hoje, sendo amplamente empregado para conectar dispositivos periféricos de baixa velocidade a seus controladores correspondentes, assegurando uma comunicação eficiente em curtas distâncias. Seu propósito principal é fornecer uma interface de comunicação de baixo custo e baixa complexidade para a troca de dados entre dispositivos em uma placa de circuito.

Entre suas vantagens podemos citar:
- Simplicidade
- Suporte a Diferentes Velocidades
- Flexibilidade na Implementação
- Compatibilidade com Diferentes Dispositivos
- Baixo Consumo de Energia

## Características
Para a comunicação I2C ser eficaz, são necessárias configurações físicas muito específicas como:

**- SDA (Serial Data Line):**

A SDA é a linha de dados serial bidirecional no barramento I2C. Ela é usada para transmitir dados entre os dispositivos mestre e escravo e pode ser operada em níveis lógicos de 0V (terra) e Vcc (tensão de alimentação).

**- SCL (Serial Clock Line):**

*clock: sinal periódico que serve como uma referência de tempo para coordenar a execução de operações em um sistema.*

A SCL é a linha de clock no barramento I2C. Ela é usada para sincronizar a comunicação entre os dispositivos mestre e escravo e pode ser operada em níveis lógicos de 0V (terra) e Vcc (tensão de alimentação).

**Resistores de Pull-Up:**

Resistor de pull-up é frequentemente utilizado nas linhas SDA e SCL para garantir que as linhas retornem ao nível lógico alto quando não estão sendo conduzidas ativamente por um dispositivo.
O valor típico para esses resistores de pull-up é de 2.2k ohms, mas pode variar dependendo dos requisitos específicos do sistema.

## Funcionamento
O protocolo de comunicação I2C funciona com base na interação dos elementos presentes seguindo uma hierarquia denominada de “mestre/escravo”. Ou seja, esse protocolo garante que vários dispositivos conectados “conversem” entre si, desde que um deles seja designado como “mestre”, enviando e requisitando as informações e dados que devem passar pelos “escravos”. 

**Início da Comunicação**
O mestre envia um sinal de START (início) pela linha SDA, enquanto a linha SCL permanece em nível lógico alto. Esse procedimento indica o começo de uma transação.

**Seleção do dispositivo escravo**
O mestre seleciona o dispositivo escravo desejado ao enviar o endereço correspondente. Cada dispositivo no barramento I2C possui um endereço único. O envio do endereço ocorre após o bit de START e inclui bits de endereço, juntamente com um bit de leitura/escrita.

**Resposta do dispositivo escravo**
O dispositivo escravo, cujo endereço coincide, responde ao mestre com um sinal de ACK (acknowledge). O mestre, ao receber o ACK, entende que o dispositivo escravo está pronto para a transmissão de dados.

**Transmissão de dados**
Tanto o mestre quanto o escravo (dependendo da direção da transmissão, seja leitura ou escrita) transmitem dados pela linha SDA, sincronizados pelos pulsos de clock provenientes da linha SCL. Cada byte de dados é sucedido por um sinal de ACK ou NACK (no acknowledge).

**Parada da Comunicação**
Após a transmissão dos dados, o mestre emite um sinal de STOP (parada) na linha SDA, enquanto a linha SCL permanece em nível lógico alto. Esse sinal indica o término da transação.

## Aplicação no projeto
Como forma de facilitar e reaproveitar projetos ja desenvolvidos anteriormente, foi utilizada uma estrutura normal de comunicação entre o sensor de humidade e temperatura DHT11 e o Raspberry Pi Pico W, com o adendo do display LCD 16x2. 

O painel LCD 16x2 se destaca como um elemento que proporciona uma interface visual descomplicada para apresentar dados em duas linhas de 16 caracteres cada. Ao conectar o LCD com o Raspberry Pi Pico W através do protocolo I2C, alcançamos uma simplificação tanto na conexão física quanto na programação, isso devido ao reduzido número de pinos necessários para controlar o display, bastam 2 pinos para que a configuração realizada no microcontrolador seja exibida na tela.

No projeto em questão, a informação que será exibida na tela lcd serão os valores de humidade e temperatura captados pelo sensor DHT11. Segue vídeo de demonstração:
[Vídeo](https://drive.google.com/file/d/1KQMjkccVq3FWQfOO4QVEAesZUEnKkuIP/view?usp=sharing).

Como objeto de inspiração e para maior entendimento do hardware utilizado, foi desenvolvido um projeto no Wokiwe:
[Vídeo](https://wokwi.com/projects/379310165832565761).
