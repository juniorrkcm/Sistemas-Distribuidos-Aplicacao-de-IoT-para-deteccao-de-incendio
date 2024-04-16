import pika
import random
import sys
import time

def generate_temperature():
    # Gerar um valor aleatório entre 70 e 100 graus Celsius (condição de incêndio)
    return random.uniform(20, 100)

def publish_temperature(channel, temperature):
    message = f'Temperatura: {temperature:.2f}°C'
    channel.basic_publish(exchange='', routing_key='cpu_temperature', body=message)
    print(f" [x] {message}")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cpu_temperature')

    if len(sys.argv) > 1:
        try:
            desired_temperature = float(sys.argv[1])
            publish_temperature(channel, desired_temperature)
        except ValueError:
            print("Error: Invalid temperature value. Using random temperature generation.")
            while True:
                temperature = generate_temperature()
                publish_temperature(channel, temperature)
                time.sleep(1)
    else:
        while True:
            temperature = generate_temperature()
            publish_temperature(channel, temperature)
            time.sleep(1)

    connection.close()

if __name__ == "__main__":
    main()
