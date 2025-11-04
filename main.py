import flet as ft
from model.model import Autonoleggio
from UI.view import View
from UI.controller import Controller

'''
DA ESEGUIRE
'''

def main(page: ft.Page):
    my_model = Autonoleggio("Polito Rent", "Alessandro Visconti")
    my_view = View(page) #creo una variabile view (interfaccia), una controller (gestione) e una model (tenere i dati)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()

ft.app(target=main)
