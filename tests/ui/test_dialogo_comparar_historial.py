from chuspacalc.ui.dialogo_comparar_historial import DialogoCompararHistorial


def test_dialogo_formatea_entradas_sin_identificador(qtbot):
    dialogo = DialogoCompararHistorial({"id": 7, "valor": 12}, {})
    qtbot.addWidget(dialogo)
    assert dialogo._formatear_entrada({"id": 7, "valor": 12}) == "<b>valor:</b> 12"


def test_dialogo_escapa_contenido_html(qtbot):
    dialogo = DialogoCompararHistorial({}, {})
    qtbot.addWidget(dialogo)
    texto = dialogo._formatear_entrada({"<clave>": "<script>"})
    assert "&lt;clave&gt;" in texto
    assert "&lt;script&gt;" in texto
    assert "<script>" not in texto


def test_dialogo_informa_entrada_vacia(qtbot):
    dialogo = DialogoCompararHistorial({}, {})
    qtbot.addWidget(dialogo)
    assert dialogo._formatear_entrada({}) == "No hay datos disponibles."
