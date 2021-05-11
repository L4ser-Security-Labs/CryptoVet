'''
      __author__ = "L4ser Security Labs"
      __email__ = "l4sersec@gmail.com"
      __contributors__ = "SeunIT"
'''

import pyfiglet
import pprint
from colorama import Fore, Back, Style
import time
import os
# from domain_infrastructure_analysis import domain_infrastructure_analysis
# from ssl_certificates_chain import ssl_certificates_chain
# from ssl_configuration_analysis import ssl_configuration_analysis
# from domain_malware_check import domain_malware_check
# from domain_reputation import domain_reputation
# from connected_domains import connected_domains
from modules.general_info import domain_malware_check
import socket


def is_connected():
    try:
        # connect to the host
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def main_banner():
      """ prints main menu, based on user choice calls respective banner menu """
      os.system("clear")
      print(Fore.RED+ Back.BLACK+ pyfiglet.figlet_format("Crypto", font="roman"))
      print(Fore.RED + pyfiglet.figlet_format("Vet", font="roman"))
      print(Fore.GREEN, "    v1.0 By L4ser security Labs (@l4sec) ")
      print(Style.RESET_ALL + Fore.YELLOW)
      print("   {1} -- General Information")
      print("   {2} -- Transactions")
      print("   {3} -- Abuse Check")
      print("   {4} -- Report Abuse")
      print("   {0} -- Update CryptoVet")
      print("   {99} -- Exit\n")
      print(Fore.RED)
      #check for internet connection
      if is_connected():
            pass
      else:
            print("Please connect to internet first!")
            time.sleep(4)
            main_banner()
      key = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      if key == "1":
            general_info_banner()
      elif key == "2":
            transactions_check_banner()       
      elif key == "3":
            abuse_check_banner()       
      elif key == "4":
            report_abuse_banner()     
      elif key == "0":
            try:
                  os.system("git pull origin master")
            except:
                  print("You dont have git installed!\nvisit source to update: https://github.com/L4ser-Security-Labs/CryptoVet")
            time.sleep(3)
            main_banner()
      elif key == "99":
            os.system("rm -rf __pycache__")
            print("Bye ;_;")
      else:
            print("Please make a selection!")
            time.sleep(2)
            main_banner()


def general_info_banner():
      """ General Information Check Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("General Info", font="banner"))
      print(Style.RESET_ALL)
      print("Enter wallet address:")
      print(Fore.RED)
      ip = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      domain_malware_check(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another General Information Check")
      print("   {Any Other Key} -- Go to Main Menu")
      print(Fore.RED)
      option = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      if option == "1":
            general_info_banner()
      else:
            main_banner()


def transactions_check_banner():
      """ Transactions Check Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Transactions Check", font="banner"))
      print(Style.RESET_ALL)
      print("Enter wallet address :")
      print(Fore.RED)
      ip = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      domain_malware_check(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Transactions Check")
      print("   {Any Other Key} -- Go to Main Menu")
      print(Fore.RED)
      option = input("CryptoVet~# ")
      if option == "1":
            transactions_check_banner()
      else:
            main_banner()
            

def abuse_check_banner():
      """ Abuse Check Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Abuse Check", font="banner"))
      print(Style.RESET_ALL)
      print("Enter wallet address :")
      print(Fore.RED)
      ip = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      domain_malware_check(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Do Another Abuse Check")
      print("   {Any Other Key} -- Go to Main Menu")
      print(Fore.RED)
      option = input("CryptoVet~# ")
      if option == "1":
            abuse_check_banner()
      else:
            main_banner()


def report_abuse_banner():
      """ Report Abuse Banner """
      os.system("clear")
      print(Fore.GREEN+ Back.BLACK + pyfiglet.figlet_format("Report Abuse", font="banner"))
      print(Style.RESET_ALL)
      print("Enter wallet address :")
      print(Fore.RED)
      ip = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      domain_malware_check(ip)
      print("\n")
      print(Fore.YELLOW)
      print("   {1} -- Report Another Abuse")
      print("   {Any Other Key} -- Go to Main Menu")
      print(Fore.RED)
      option = input("CryptoVet~# ")
      print(Style.RESET_ALL)
      if option == "1":
            report_abuse_banner()
      else:
            main_banner()

if __name__ == "__main__":
      main_banner()
