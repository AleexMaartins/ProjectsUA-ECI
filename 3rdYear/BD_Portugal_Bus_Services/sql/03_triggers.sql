create trigger EAP.Total_Modelo on EAP.Modelo_autocarro
instead of insert
as
	if not exists(select * from inserted where id in (select modelo_id from EAP.Combustao) or id in (select modelo_id from EAP.Eletrico))
	begin
		raiserror('Erro! Nao é possivel adicionar Modelo sem especialização',16,1)
	end
	else
		insert into EAP.Modelo_autocarro select nome_modelo,marca,ano from inserted
go

create trigger EAP.Combustao_Disjunta on EAP.Combustao
after update, insert
as
	if exists(Select * from EAP.Eletrico where modelo_id in (select modelo_id from inserted))
	begin
		raiserror('Erro! Nao é possivel existir Modelo com mais que uma especialização',16,1)
		rollback transaction
	end
go

create trigger EAP.Eletrico_Disjunta on EAP.Eletrico
after update, insert
as
	if exists(Select * from EAP.Combustao where modelo_id in (select modelo_id from inserted))
	begin
		raiserror('Erro! Nao é possivel existir Modelo com mais que uma especialização',16,1)
		rollback transaction
	end
go

create trigger EAP.Total_Pessoa on EAP.Pessoa
instead of insert
as
	if not exists(select * from inserted where id in (select pessoa_id from EAP.Passageiro) or id in (select pessoa_id from EAP.Condutor))
	begin
		raiserror('Erro! Nao é possivel adicionar Pessoa sem especialização',16,1)
	end
	else
		insert into EAP.Pessoa select nome,apelido,email,nif from inserted
go