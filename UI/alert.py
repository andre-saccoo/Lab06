#classe che si occupa delle finestre di alert, vengono create delle finestre modali per la gestione degli errori
import flet as ft

class AlertManager:
    def __init__(self, page: ft.Page):
        self._page = page
        # finestra di errore contente il bottone ok per chiuderla
        self._alert_dialog = ft.AlertDialog(
            title=ft.Text(""),
            actions=[ft.TextButton("OK", on_click=self.close)]
        )

    #funzione per mostrare l'errore
    def show_alert(self, message: str):
        self._alert_dialog.title.value = message # quale titolo dare all'errore
        if self._alert_dialog not in self._page.overlay:
            self._page.overlay.append(self._alert_dialog)
        self._alert_dialog.open = True
        self._page.update()

    #funzione che chiude la finestra e riaggiorna la pagina
    def close(self, e):
        self._alert_dialog.open = False
        self._page.update()
