# Projeto de Sistemas Distribuidos de IoT de Detecção de Incêndio

## Objetivo
O objetivo deste projeto é desenvolver uma aplicação simples de IoT para simular a detecção de incêndio em um ambiente, utilizando a temperatura da CPU como referência.

## Materiais Utilizados
- Computador com sistema operacional Kali Linux
- Linguagem de programação Python (versão 3.x)
- Biblioteca de cliente RabbitMQ para Python (pika)
- Biblioteca psutil do Python

## Descrição da Atividade
O projeto consiste na criação de três componentes principais: um produtor de mensagens, um consumidor para verificar a temperatura da CPU e outro consumidor para detectar incêndios.

### Produtor de Mensagens (pt2.py)
O produtor de mensagens, desenvolvido em Python, utiliza a biblioteca pika para interagir com o RabbitMQ. Este componente captura a temperatura da CPU (usando a biblioteca psutil) e a publica em um tópico no RabbitMQ chamado "cpu_temperature". Além disso, inclui a opção de fornecer manualmente uma temperatura para simular a temperatura da CPU, permitindo testar a funcionalidade de detecção de incêndio.

![IMAGEM](https://github.com/juniorrkcm/Sistemas-Distribuidos-Aplicacao-de-IoT-para-deteccao-de-incendio/blob/main/imagens/1.png)

### Consumidor para Verificar Temperatura (cdi.py)
Este consumidor recebe mensagens do tópico "cpu_temperature" no RabbitMQ. Ele extrai a temperatura da mensagem recebida, verifica se está acima de um limite predefinido (por exemplo, 70 graus Celsius) e, caso esteja, publica uma mensagem indicando a detecção de incêndio no tópico "fire_detection".

![IMAGEM](https://github.com/juniorrkcm/Sistemas-Distribuidos-Aplicacao-de-IoT-para-deteccao-de-incendio/blob/main/imagens/2.png)

### Consumidor para Detectar Incêndio (cda.py)
O terceiro componente é responsável por receber mensagens do tópico "fire_detection" no RabbitMQ. Quando uma mensagem indicando a detecção de incêndio é recebida, exibe um pop-up de alerta utilizando a biblioteca Tkinter.

![IMAGEM](https://github.com/juniorrkcm/Sistemas-Distribuidos-Aplicacao-de-IoT-para-deteccao-de-incendio/blob/main/imagens/3.png)

## Conclusão
A aplicação desenvolvida demonstra a utilização prática de conceitos de IoT para simular a detecção de incêndio com base na temperatura da CPU. O uso do RabbitMQ como sistema de mensagens e a biblioteca psutil para obter informações da CPU permitiram a criação de um sistema simples, porém funcional, para este propósito específico. A inclusão da opção de fornecer manualmente uma temperatura para simular a temperatura da CPU aumentou a robustez do sistema ao permitir testar a funcionalidade de detecção de incêndio mesmo em ambientes onde não era possível obter a temperatura real da CPU.

___________________________________________________________________________________________________________________________________________________

## Tutorial de Configuração e Execução do Projeto

Este tutorial visa fornecer instruções passo a passo para configurar e executar o projeto de simulação de detecção de incêndio utilizando a temperatura da CPU como referência.

## 1 Iniciar o Serviço do RabbitMQ
Inicie o serviço do RabbitMQ. Em sistemas Linux, você pode fazer isso executando o seguinte comando no terminal:


`sudo rabbitmq-server start`

## 2 Execute o produtor de mensagens:


`python3 pt2.py`

Se desejar fornecer uma temperatura específica, você pode fazer isso como argumento de linha de comando:
Copy code

`python3 pt2.py 80.0`

## 3 Executar o Consumidor para Verificar a Temperatura (cdi.py)
Abra um novo terminal e Execute o consumidor para verificar a temperatura:


`python3 cdi.py`

## 4 Executar o Consumidor para Detectar Incêndio (cda.py)
Abra um novo terminal e Execute o consumidor para detectar incêndio:

`python3 cda.py`

<<<<<<< HEAD
## 5 Observações
Certifique-se de que o RabbitMQ esteja em execução antes de executar os códigos. 
=======
## 5-Observações
Certifique-se de que o RabbitMQ esteja em execução antes de executar os códigos. 
>>>>>>> 3236aea214149ba883da88ee35dcee7a8e7ea67f
