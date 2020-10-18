#https://hastebin.com/raw/ezolofojev
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('config.ini')

if config['firefox'].getboolean('install-newest'):
    print("================================================")
    print("Firefox: Installing")
    print("================================================")
    subprocess.call(['sudo', 'add-apt-repository', 'ppa:ubuntu-mozilla-security/ppa'])
    subprocess.call(['sudo', 'apt', 'update',])
    subprocess.call(['sudo', 'apt', 'install', 'firefox'])

if config['ansible'].getboolean('install'):
    print("================================================")
    print("Ansible: Installing")
    print("================================================")
    subprocess.call(['sudo', 'add-apt-repository', 'ppa:ansible/ansible'])
    subprocess.call(['sudo', 'apt', 'update',])
    subprocess.call(['sudo', 'apt', 'install', 'ansible'])

if config['ansible'].getboolean('add-roles'):
    print("================================================")
    print("Ansible: Copying Roles")
    print("================================================")
    subprocess.call(['sudo', 'cp', 'Roles.zip', '/etc/ansible/roles/Roles.zip'])
    subprocess.call(['sudo', 'unzip', 'Roles.zip', '-d', '/etc/ansible/roles/'])

if config['ansible'].getboolean('run-roles'):
    print("================================================")
    print("Ansible: Running Roles")
    print("================================================")
    subprocess.call(['sudo', 'ansible', '/etc/ansible/roles/Harden.yml'])
