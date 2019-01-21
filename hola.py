#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: Diego Caraballo
# www.pythondiario.com
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return "Aplicacion en Flask!"

#@app.route("/hola/<string:name>")
@app.route("/hola/<string:name>/")
def hola(name):
#    return name
    quotes = [ u"'Un buen diseño aporta un valor añadido más rápido de lo que agrega costo.' -- Thomas C. Gale  ",
               u"'Hablar es barato. Enséñame el código' --  Linus Torvalds  ",
               u"'Siempre codifica como si la persona que finalmente mantendrá tu código fuera un psicópata violento que sabe dónde vives...' -- Martin Golding ",
               u"'Si la depuración es el proceso de eliminar errores, entonces la programación debe ser el proceso de introducirlos.' -- Edsger Dijkstra"
             ]
    randomNumber = randint(0,len(quotes)-1)
    quote = quotes[randomNumber]

    return render_template(
        'test.html',**locals())

if __name__ == "__main__":
    app.run()
    
