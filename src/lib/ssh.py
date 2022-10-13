from paramiko import *
import yaml

class SSH:
    client = None

    def connect(self, environment=''):
        with open("../../hosts.yaml", "r") as stream:
            try:
                file = yaml.safe_load(stream)
                access = file[environment]
                print(access)
            except yaml.YAMLError as exc:
                print(exc)

        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.client.connect(access['host'], 22, access['user'], access['password'])
        print(self.client)

    def run(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        print(stdout.read().decode())

ssh = SSH()
ssh.connect('carrefour-dev')
ssh.run('ls -l')
