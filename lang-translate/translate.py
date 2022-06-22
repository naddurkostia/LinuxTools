#!/usr/bin/env python3

from cgitb import text
from translate import Translator

text = input("Enter text to translate: ")

lang = input("Enter language(Spanish, German, etc): ")

translator= Translator(to_lang=lang)
translation = translator.translate(text)
print (translation)