from pydantic import BaseModel
from typing import List


class InputData(BaseModel):
    """
    Input data model for the prediction API.
    """
    montoExigible: float
    # idBanco: int 
    idBanco_AZTECA: bool = False
    idBanco_BABIEN: bool = False
    idBanco_BANAMEX: bool = False
    idBanco_BANCO_DEL_BAJIO: bool = False
    idBanco_BANCO_FAMSA: bool = False
    idBanco_BANCOPPEL: bool = False
    idBanco_BANORTE: bool = False
    idBanco_BANREGIO: bool = False
    idBanco_BBVA_MEXICO: bool = False
    idBanco_BMULTIVA: bool = False
    idBanco_HSBC: bool = False
    idBanco_INBURSA: bool = False
    idBanco_SANTANDER: bool = False
    idBanco_SCOTIABANK: bool = False
    idEmisora_65: bool = False
    idEmisora_67: bool = False
    idEmisora_BANAMEX_CLABE_TRADICIONAL: bool = False
    idEmisora_BANAMEX_CUENTA: bool = False
    idEmisora_BANAMEX_INTERBANCARIO: bool = False
    idEmisora_BANAMEX_TARJETA: bool = False
    idEmisora_BANAMEX_TRADICIONAL_REINTEINTO: bool = False
    idEmisora_BBVA_CLABE_EN_LINEA: bool = False
    idEmisora_BBVA_CLABE_INTERBANCARIA: bool = False
    idEmisora_BBVA_CLABE_MATUTINO: bool = False
    idEmisora_BBVA_CLABE_PARCIAL: bool = False
    idEmisora_BBVA_CLABE_TRADICIONAL: bool = False
    idEmisora_BBVA_CUENTA_EN_LINEA: bool = False
    idEmisora_BBVA_CUENTA_MATUTINO: bool = False
    idEmisora_BBVA_CUENTA_PARCIAL: bool = False
    idEmisora_BBVA_CUENTA_TRADICIONAL: bool = False
    idEmisora_BBVA_TRADICIONAL_REINTENTO: bool = False
    idEmisora_BANAMEX_EXCEPCIONES_CUENTA: bool = False
    idEmisora_BANAMEX_EXCEPCIONES_TARJETA: bool = False
    idEmisora_BANAMEX_REINTENTOS: bool = False
    idEmisora_BANAMEX_TRADICIONAL_TARJETA_PERIODO_ACTUAL: bool = False
    idEmisora_BANCOMER_PARCIAL_CUENTA_EXCEPCIONES: bool = False
    idEmisora_BANCOMER_REINTENTOS: bool = False
    idEmisora_BANCOMER_TRADICIONAL: bool = False
    idEmisora_BANORTE_EXCEPCIONES_CUENTA: bool = False
    idEmisora_SANTANDER_CLABE_INTERBANCARIO: bool = False
    idEmisora_SANTANDER_CLABE_TRADICIONAL: bool = False
    idEmisora_SANTANDER_CUENTA: bool = False    
    idEmisora_SANTANDER_EXCEPCIONES_CUENTA: bool = False    # idEmisora: int
    month: int
    day: int

    