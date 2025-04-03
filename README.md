# ETLBCB

A função "requestApiBcb" serve para extrair e processar dados da API do banco central, especificamente os dados trimestrais dos meios de pagamentos.

A função "salvarCsv" serve para salvar um dataframe do pandas em um arquivo CSV, personalizando o separador e o decimal.

# Dicionário de meios de pagamentos trimestrais

| Nome                           | Tipo     | Título                              | Descrição |
|--------------------------------|---------|--------------------------------------|-----------|
| datatrimestre                | texto   | Trimestre                            | - |
| valorPix                      | decimal | Valor Pix                            | Volume financeiro (R$ milhões) de transações Pix liquidadas trimestralmente no SPI e fora do SPI. |
| #valorTED                      | decimal | Valor TED                            | Montante financeiro (R$ milhões) trimestral transferido por meio de TED. |
| #valorTEC                      | decimal | Valor TEC                            | Montante financeiro (R$ milhões) trimestral transferido por meio de TEC. |
| #valorCheque                   | decimal | Valor Cheque                         | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente. |
| #valorBoleto                   | decimal | Valor Boleto                         | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente. |
| #valorDOC                      | decimal | Valor DOC                            | Montante financeiro (R$ milhões) trimestral transferido por meio de DOC. |
| #valorCartaoCredito            | decimal | Valor Cartão de Crédito              | Valor (R$ milhões) de transações realizadas com cartão de crédito. |
| #valorCartaoDebito             | decimal | Valor Cartão de Débito               | Valor (R$ milhões) de transações realizadas com cartão de débito trimestralmente. |
| #valorCartaoPrePago            | decimal | Valor Cartão Pré-pago                | Valor (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente. |
| #valorTransIntrabancaria       | decimal | Valor Transferência Intrabancária    | Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes. |
| #valorConvenios                | decimal | Valor Convênio                       | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais e não-governamentais. |
| #valorDebitoDireto             | decimal | Valor Débito Direto                  | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente. |
| #valorSaques                   | decimal | Valor Saque                          | Montante sacado (R$ milhões) nos caixas eletrônicos trimestralmente. |
| #quantidadePix                 | decimal | Quantidade Pix                       | Quantidade (em milhares) de transações Pix liquidadas trimestralmente. |
| #quantidadeTED                 | decimal | Quantidade TED                       | Quantidade (em milhares) de TED realizadas trimestralmente. |
| #quantidadeTEC                 | decimal | Quantidade TEC                       | Quantidade (em milhares) de TEC realizadas trimestralmente. |
| #quantidadeCheque              | decimal | Quantidade Cheque                    | Quantidade (em milhares) de cheques interbancários e intrabancários compensados trimestralmente. |
| #quantidadeBoleto              | decimal | Quantidade Boleto                    | Quantidade (em milhares) de boletos interbancários e intrabancários compensados trimestralmente. |
| #quantidadeDOC                 | decimal | Quantidade DOC                       | Quantidade (em milhares) de DOC realizados trimestralmente. |
| #quantidadeCartaoCredito       | decimal | Quantidade Cartão de Crédito         | Quantidade (em milhares) de transações realizadas com cartão de crédito trimestralmente. |
| #quantidadeCartaoDebito        | decimal | Quantidade Cartão de Débito          | Quantidade (em milhares) de transações realizadas com cartão de débito trimestralmente. |
| #quantidadeCartaoPrePago       | decimal | Quantidade Cartão Pré-pago           | Quantidade (em milhares) de transações realizadas com cartão pré-pago trimestralmente. |
| #quantidadeTransIntrabancaria  | decimal | Quantidade Transferência Intrabancária | Quantidade (em milhares) de transferências realizadas trimestralmente entre contas de clientes da instituição. |
| #quantidadeConvenios           | decimal | Quantidade Convênio                  | Quantidade (em milhares) de transações referentes a arrecadações trimestrais governamentais e não-governamentais. |
| #quantidadeDebitoDireto        | decimal | Quantidade Débito Direto             | Quantidade (em milhares) de transações trimestrais referentes a débitos previamente autorizados pelo cliente. |
| #quantidadeSaques              | decimal | Quantidade de Saque                  | Quantidade (em milhares) de saques realizados nos caixas eletrônicos trimestralmente. |
