from src.lib.logutils import print_msg, LogStatus
import kafka
import yaml
import click

@click.command()
@click.option("-h", prompt="Hostname", default="localhost", help="Path to yaml dummy data")
@click.option("-p", prompt="Port", default="9092", help="Path to yaml dummy data")
@click.option("-f", prompt="Path to file", default="kafka_data.yaml", help="Path to yaml dummy data")
@click.option("-v", default="Verbose", help="Outputs in verbose mode")
def send(h, p, f, v):
    """Inserts data into Kafka."""
    print_msg(LogStatus.OK, "Running Kafka Producer")
    file = load_file(f)
    push(h, p, file)

def push(host, port, file):
    try:
        producer = kafka.KafkaProducer(bootstrap_servers=host + ":" + port)
        print_msg(LogStatus.OK, "Connection with Kafka server.")
        producer.send()
        print_msg(LogStatus.OK, "Connection with Kafka server.")
    except Exception as e:
        print(e)
        print_msg(LogStatus.FAIL, "Connection with Kafka server.")
    return None

def load_file(path):
    try:
        with open("example.yaml", "r") as stream:
            result = yaml.load(stream)
            print_msg(LogStatus.OK, "Load file into Producer.")
    except Exception as e:
        print_msg(LogStatus.FAIL, "Reading from " + path)