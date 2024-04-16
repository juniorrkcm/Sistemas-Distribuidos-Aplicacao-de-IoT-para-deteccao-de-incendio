import pika

def callback(channel, method, properties, body):
    try:
        temperature_str = body.decode('utf-8')  # Converte bytes para string
        temperature = float(temperature_str.split(":")[1].split("°")[0])  # Extrai o valor da temperatura
        print(f" [x] Temperatura recebida: {temperature:.2f}°C")

        # Verifique se a temperatura está acima do limite e tome as ações necessárias
        if temperature > 70:
            # Publicar uma mensagem indicando detecção de incêndio em um novo tópico
            channel.basic_publish(exchange='', routing_key='fire_detection', body='Incêndio detectado!')
            print(" [x] Incêndio detectado.")
        else:
            print(" [x] Incêndio não detectado.")

    except Exception as e:
        print(f"Erro ao processar mensagem: {str(e)}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cpu_temperature')
    channel.queue_declare(queue='fire_detection')

    channel.basic_consume(queue='cpu_temperature', on_message_callback=callback, auto_ack=True)

    print('Aguardando temperatura da CPU...')

    channel.start_consuming()

if __name__ == "__main__":
    main()
