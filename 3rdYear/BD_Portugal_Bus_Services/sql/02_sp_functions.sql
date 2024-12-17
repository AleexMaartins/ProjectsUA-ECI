-- STORED PROCEDURES
create procedure EAP.addModelo (@nome_modelo varchar(20), @marca varchar(20) = null, @ano date = null)
as
	insert into EAP.Modelo_autocarro(nome_modelo, marca, ano) values (@nome_modelo, @marca, @ano)
go

create procedure EAP.addModeloCombustao (@nome_modelo varchar(20), @marca varchar(20) = null, @ano date = null, @cilindrada int = null, @combustivel varchar(8))
as
	set nocount on

	begin try
		begin transaction;
		disable trigger EAP.Total_Modelo on EAP.Modelo_autocarro
		exec EAP.addModelo @nome_modelo, @marca, @ano
		alter table EAP.Modelo_autocarro enable trigger Total_Modelo
		declare @modelo_id int
		select @modelo_id = max(id) from EAP.Modelo_autocarro

		insert into EAP.Combustao(modelo_id,cilindrada,combustivel) values (@modelo_id, @cilindrada, @combustivel)
		commit transaction
	end try
	begin catch
		rollback transaction
	end catch
go

create procedure EAP.addModeloEletrico (@nome_modelo varchar(20), @marca varchar(20) = null, @ano date = null, @autonomia int = null)
as
	set nocount on;
	
	begin try
		begin transaction;
		disable trigger EAP.Total_Modelo on EAP.Modelo_autocarro
		exec EAP.addModelo @nome_modelo, @marca, @ano
		alter table EAP.Modelo_autocarro enable trigger Total_Modelo

		declare @modelo_id int
		select @modelo_id = max(id) from EAP.Modelo_autocarro
		insert into EAP.Eletrico(modelo_id,autonomia) values (@modelo_id, @autonomia)
		commit transaction
	end try
	begin catch
		rollback transaction
	end catch
go

create procedure EAP.addPessoa (@nome varchar(20), @apelido varchar(20), @email varchar(20) = null, @nif char(9) = null)
as
	insert into EAP.Pessoa (nome, apelido, email, nif) values (@nome, @apelido, @email, @nif)
go

create procedure EAP.addPassageiro (@nome varchar(20), @apelido varchar(20), @email varchar(20) = null, @nif char(9) = null, @faixa_etaria varchar(7))
as
	set nocount on;
	
	begin try
	begin transaction;
		disable trigger EAP.Total_Pessoa on EAP.Pessoa
		exec EAP.addPessoa @nome, @apelido, @email, @nif
		alter table EAP.Pessoa enable trigger Total_Pessoa

		declare @pessoa_id int
		select @pessoa_id = max(id) from EAP.Pessoa
		insert into EAP.Passageiro(pessoa_id, faixa_etaria) values (@pessoa_id, @faixa_etaria)
		commit transaction
	end try
	begin catch
		rollback transaction
	end catch
go

create procedure EAP.addCondutor (@nome varchar(20), @apelido varchar(20), @email varchar(20) = null, @nif char(9) = null, @carta_conducao char(12))
as
begin
	set nocount on;
	
	begin try
		begin transaction;
		disable trigger EAP.Total_Pessoa on EAP.Pessoa
		exec EAP.addPessoa @nome, @apelido, @email, @nif
		alter table EAP.Pessoa enable trigger Total_Pessoa

		declare @pessoa_id int
		select @pessoa_id = max(id) from EAP.Pessoa
		insert into EAP.Condutor(pessoa_id, carta_conducao) values (@pessoa_id, @carta_conducao)
		commit transaction
	end try
	begin catch
		rollback transaction
	end catch
end
go

create procedure EAP.ComprarBilhete (@passageiro_id int, @viagem_id int, @origem varchar(15), @destino varchar(15) )
as
begin
	set nocount on;
	declare @hora_compra time
	set @hora_compra = getdate()

	declare @num_assento int
	set @num_assento = EAP.proximo_assento_livre (@viagem_id, @origem, @destino)
	if @num_assento <> 0
	begin
		begin try
			begin transaction
			exec EAP.addBilhete @num_assento, @hora_compra, @passageiro_id
			declare @bilhete_id int
			select @bilhete_id = max(id) from EAP.Bilhete

			declare @numero int
			select @numero = count(*)+1 from EAP.Bilhete join EAP.Escala on id = bilhete_id

			exec EAP.addEscala @bilhete_id, @numero, @origem, @destino, @viagem_id
			commit transaction
		end try
		begin catch
			rollback transaction
		end catch
	end
	else print('Viagem sem espaço')
end

create procedure EAP.addBilhete (@num_assento int, @hora_compra time, @passageiro_id int)
as
begin
	set nocount on
		insert into EAP.Bilhete(num_assento, hora_compra, passageiro_id) 
		values (@num_assento, @hora_compra, @passageiro_id)
end

create procedure EAP.addEscala (@bilhete_id int, @numero int, @origem varchar(15), @destino varchar(15), @viagem_id int)
as
begin
	set nocount on
		insert into EAP.Escala(bilhete_id, numero, origem, destino, viagem_id)
		values (@bilhete_id, @numero, @origem, @destino, @viagem_id)
end

create procedure EAP.addTerminal (@nome varchar(15), @latitude float = null, @longitude float = null)
as
begin
	set nocount on
	begin transaction
		insert into EAP.Terminal_rodoviario(nome, latitude, longitude) values (@nome, @latitude, @longitude)
	commit transaction
end

create procedure EAP.addCais (@rodoviaria varchar(15), @numero int)
as
begin
	set nocount on
		insert into EAP.Cais (rodoviaria, numero, is_Empty) 
		values (@rodoviaria, @numero, 1)
end

create procedure EAP.addParagem (@viagem_id int, @rodoviaria varchar(15), @arrival_time time, @departure_time time)
as
begin
	set nocount on
		declare @ordem int
		select @ordem = count(*)+1 from EAP.Paragem where viagem_id = @viagem_id
		insert into EAP.Paragem (viagem_id, ordem, rodoviaria, arrival_time, departure_time) 
		values (@viagem_id, @ordem, @rodoviaria, @arrival_time, @departure_time)
end

create procedure EAP.addViagem (@autocarro_id int, @condutor_id int)
as
begin
	set nocount on
		insert into EAP.Viagem (autocarro_id, condutor_id)
		values (@autocarro_id, @condutor_id)
end

create procedure EAP.addAutocarro (@kms int = 0, @num_lugares int, @matricula char(8), @capacidade int, @modelo_id int)
as
begin
	set nocount on
		insert into EAP.Autocarro (kms, num_lugares, matricula, capacidade, modelo_id)
		values (@kms, @num_lugares, @matricula, @capacidade, @modelo_id)
end

create procedure EAP.addBagagem (@tipo varchar(5), @peso float, @volume float)
as
begin
	set nocount on
		insert into EAP.Bagagem (tipo, peso, volume)
		values (@tipo, @peso, @volume)
end

-- FUNCTIONS
create function EAP.Viagem_paragens (@viagem_id int) returns table
as
	return (
	select * from EAP.Paragem where viagem_id = @viagem_id
	)
go

create function EAP.ordem_paragem (@viagem_id int, @rodoviaria varchar(15)) returns int
as
begin
	declare @ordem int
	select @ordem = ordem from EAP.Paragem where viagem_id = @viagem_id and rodoviaria = @rodoviaria
	return @ordem
end
go

create function EAP.Viagens_por_Origem_Destino (@origem varchar(15), @destino varchar(15)) returns table
as
	return (
	select *
	from EAP.Viagem
	where @origem in (select rodoviaria from EAP.Viagem_paragens(id)) 
		and @destino in (select rodoviaria from EAP.Viagem_paragens(id))
		and EAP.ordem_paragem(id, @origem) < EAP.ordem_paragem(id, @destino)
	)
go

create function EAP.proximo_assento_livre (@viagem_id int, @origem varchar(15), @destino varchar(15) ) returns int
as
begin
	declare @num_assento int = 1
	declare @next_assento int
	declare @max_assento int

	select @max_assento = num_lugares 
	from EAP.Autocarro
	where id in (select id from EAP.Viagem where id = @viagem_id)

	declare assento_cursor cursor for
	select num_assento
	from EAP.Bilhete join EAP.Escala on id = bilhete_id and viagem_id = @viagem_id
	where @origem in (select rodoviaria from EAP.Escala_paragens(@viagem_id, origem, destino) )
		or @destino in (select rodoviaria from EAP.Escala_paragens(@viagem_id, origem, destino) )
	order by num_assento

	open assento_cursor
	fetch assento_cursor into @next_assento

	while @@fetch_status = 0
	begin
		
		if @num_assento <> @next_assento
		begin
			break
		end
		set @num_assento = @num_assento+1
		fetch assento_cursor into @next_assento
	end

	if @num_assento > @max_assento
	begin
		set @num_assento = 0
	end

	close assento_cursor
	deallocate assento_cursor
	return @num_assento	
end
go

create function EAP.Escala_paragens (@viagem_id int, @origem varchar(15), @destino varchar(15)) returns table
as
	return (
		select *
		from EAP.Viagem_paragens(@viagem_id) as Viagem_p
		where Viagem_p.viagem_id in (select viagem_id from EAP.Escala
		where ordem >= EAP.ordem_paragem(@viagem_id, @origem) and ordem <= EAP.ordem_paragem(@viagem_id, @destino))
	)
go

create function EAP.Passageiro_Bilhete (@passageiro_id int) returns table
as
	return (
	select * from EAP.Bilhete
	where passageiro_id = @passageiro_id
	)
go

create function EAP.Origem(@origem varchar(15), @destino varchar(15)) returns table
as
	return (
	select rodoviaria as origem, departure_time
	from EAP.Viagens_por_Origem_Destino(@origem, @destino) join EAP.Paragem on id = viagem_id
	where rodoviaria = @origem)
go

create function EAP.Destinos (@origem varchar(15), @destino varchar(15)) returns table
as
	return (
	select arrival_time, rodoviaria as destino, viagem_id
	from EAP.Viagens_por_Origem_Destino(@origem, @destino) join EAP.Paragem on id = viagem_id
	where rodoviaria = @destino)
go

create function EAP.Horarios (@origem varchar(15), @destino varchar(15)) returns table
as
	return (
	select * 
	from EAP.Origem(@origem, @destino), EAP.Destinos(@origem, @destino)
	)
go
