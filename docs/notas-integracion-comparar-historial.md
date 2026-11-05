Dentro del __init__, después de crear la lista de historial:

python
# Botón para comparar
self.btn_comparar = QPushButton("Comparar")
self.btn_comparar.clicked.connect(self._comparar_seleccion)
self.btn_comparar.setEnabled(False)
layout.addWidget(self.btn_comparar)
Conectar la selección:

python
self.lista_historial.itemSelectionChanged.connect(self._on_seleccion_cambiada)
Agregar estos métodos al final de la clase:

python
def _on_seleccion_cambiada(self):
    seleccionados = self.lista_historial.selectedItems()
    self.btn_comparar.setEnabled(len(seleccionados) == 2)

def _comparar_seleccion(self):
    from src.chuspacalc.ui.dialogo_comparar_historial import DialogoCompararHistorial
    seleccionados = self.lista_historial.selectedItems()
    if len(seleccionados) == 2:
        entrada1 = self._obtener_datos(seleccionados[0])
        entrada2 = self._obtener_datos(seleccionados[1])
        dialogo = DialogoCompararHistorial(entrada1, entrada2, self)
        dialogo.exec()

def _obtener_datos(self, item):
    return {"texto": item.text()}  # ajusta según tu estructura
