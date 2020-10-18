#https://hastebin.com/raw/ezolofojev
import configparser
import subprocess

config = configparser.ConfigParser()
config.read('config.ini')

if config['firefox'].getboolean('install-newest'):
    print("Config testing")
    #subprocess.call(['sudo', 'add-apt-repository', 'ppa:ubuntu-mozilla-security/ppa'])
    #subprocess.call(['sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'install', 'firefox'])
