import pika
import psutil
import sys
import time

def get_cpu_temperature():
    # Usar psutil para obter a temperatura da CPU
    temperature = psutil.sensors_temperatures().get('cpu')
    if temperature:
        return temperature[0].current
    else:
        return None

def publish_temperature(channel, temperature):
    message = f'Temperature: {temperature:.2f}°C'
    channel.basic_publish(exchange='', routing_key='cpu_temperature', body=message)
    print(f" [x] Sent '{message}'")

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cpu_temperature')

    # Verificar se um valor de temperatura de simulação foi fornecido como argumento de linha de comando
    if len(sys.argv) > 1:
        try:
            desired_temperature = float(sys.argv[1])
            publish_temperature(channel, desired_temperature)
        except ValueError:
            print("Error: Invalid temperature value.")
            sys.exit(1)
    else:
        # Se nenhum valor de temperatura de simulação for fornecido, tentar obter a temperatura da CPU
        temperature = get_cpu_temperature()
        if temperature is not None:
            publish_temperature(channel, temperature)
        else:
            print("Error: Unable to obtain CPU temperature.")
            sys.exit(1)

    connection.close()

if __name__ == "__main__":
    main()
