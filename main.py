import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQlite, salvarMySQL

dadosBcb = requestApiBcb("20191")
salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";", ".")

salvarSQlite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySQL(dadosBcb, "root", "root", "localhost", "etlbcb", "meios_pagamentos_tri")
