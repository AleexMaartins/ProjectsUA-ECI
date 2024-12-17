create index idxParagemRodoviaria on EAP.Paragem (rodoviaria)
create index idxParagemViagem on EAP.Paragem (viagem_id)
create index idxModelo on EAP.Modelo_autocarro (nome_modelo)
create index idxAutocarroMatricula on EAP.Autocarro (matricula)
create index idxPessoaEmail on EAP.Pessoa (email)
create index idxBilheteAssento on EAP.Bilhete (num_assento)