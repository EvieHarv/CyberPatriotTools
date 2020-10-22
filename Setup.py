# Based on my notes https://hastebin.com/raw/ezolofojev
# Recommended run command: sudo python3 Setup.py | tee SetupOutput.txt

import configparser
import subprocess

config = configparser.ConfigParser()
config.read('config.ini')

print("ARE YOU SURE YOU HAVE A PASSWORD WITH 1 CREDIT IN ALL CATEGORIES?")
print("(At least 1 uppercase, 1 lowercase, 1 number, 1 special, 8+ characters total.)")

confirm = input('\nAre you sure? y/n: ')
confirm = confirm.lower()

if (not (confirm == "yes" or confirm == 'y')):
    print("Quitting")
    exit()

if config['firefox'].getboolean('install-newest'):
    print("================================================")
    print("Firefox: Installing Newest Version")
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
    subprocess.call(['sudo', 'cp', '-a', 'Roles/.', '/etc/ansible/roles/'])

if config['ansible'].getboolean('run-roles'):
    print("================================================")
    print("Ansible: Running Roles")
    print("================================================")
    subprocess.call(['sudo', 'ansible-playbook', '/etc/ansible/roles/Harden.yml'])

if config['lynis'].getboolean('install'):
    print("================================================")
    print("Lynis: Installing")
    print("================================================")
    subprocess.call(['sudo', 'apt-key', 'adv', '--keyserver', 'keyserver.ubuntu.com', '--recv-keys', 'C80E383C3DE9F082E01391A0366C67DE91CA5D5F'])
    subprocess.run('sudo apt-add-repository "deb [arch=amd64] https://packages.cisofy.com/community/lynis/deb/ xenial main"', shell=True) # Dunno *why* it has to be different here, the quotes just wouldn't play nicely with subprocess.call()
    subprocess.call(['sudo', 'apt', 'update',])
    subprocess.call(['sudo', 'apt', 'install', 'lynis'])

if config['lynis'].getboolean('audit'):
    print("================================================")
    print("Lynis: Auditing")
    print("================================================")
    subprocess.call(['sudo', 'lynis', 'audit', 'system'])




print("================================================")
print("Assuming all went well, things left to do:")
print(" - Block firefox popups")
print(" - Ensure there are no unauthorized users")
print(" - Ensure there are no unauthorized admins")
print(" - Ensure all passwords are up to spec")
print(" - Ensure firewall is active (gufw is easy)")
print(" - Set daily updates & install security updates & recommended updates")
print(" - Remove bad software (nmap, zenmap, compilers, etc.)")
print("================================================")
