from datetime import datetime
import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    fecha_hora = datetime.now().strftime("%Y%m%d_%H_%M_%S")
    nombre = f"reports/{fecha_hora}_reporte.html"
    config.option.htmlpath = str(config.rootpath / nombre)