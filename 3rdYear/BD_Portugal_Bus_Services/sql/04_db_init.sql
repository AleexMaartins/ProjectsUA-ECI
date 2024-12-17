exec EAP.addCondutor 'Rafael', 'Junior', 'rafa@gmail.com','123456789','AB1234567890'
exec EAP.addCondutor 'Marcelo', 'Semedo', 'marcelo@gmail.com','987654321','CD9876543210'
exec EAP.addCondutor 'Carlos', 'Pereira', 'pereira@gmail.com', '192837465',	'EF1928374650'
exec EAP.addCondutor 'Ana', 'Costa', 'ana.costa@gmail.com', '564738291', 'GH5647382910'
exec EAP.addCondutor 'Jo�o', 'Silva', 'js@gmail.com', '837291987', 'IJ5647382910'

exec EAP.addPassageiro 'Daniel','Santos',null,'192865748','crianca'

exec EAP.addModeloCombustao 'Civic', 'Honda', '2022-01-01',2000,'gasolina'
exec EAP.addModeloCombustao 'Corolla', 'Ford', '2022-01-01',2000,'gasoleo'
exec EAP.addModeloCombustao 'Fusion','Ford','2020-01-01',2000,'gasoleo'

exec EAP.addModeloEletrico 'Model S', 'Tesla', '2022-03-20',652

exec EAP.addAutocarro 
	@num_lugares = 55,
	@matricula = 'XX-01-OP',
	@capacidade = 20,
	@modelo_id = 1

exec EAP.addViagem
	@autocarro_id = 1,
	@condutor_id = 1

exec EAP.addTerminal 'Lisboa Sete Rios'
exec EAP.addTerminal 'Lisboa Oriente'
exec EAP.addTerminal 'Aveiro'
exec EAP.addTerminal 'Setubal'
exec EAP.addTerminal 'Braga'
exec EAP.addTerminal 'Porto Campanh�'
exec EAP.addTerminal 'Coimbra'
exec EAP.addTerminal 'Nazar�'

exec EAP.addParagem
	@viagem_id = 1,
	@rodoviaria = 'Lisboa Sete Rios',
	@arrival_time = '07:00',
	@departure_time = '07:00'
exec EAP.addParagem
	@viagem_id = 1,
	@rodoviaria = 'Coimbra',
	@arrival_time = '08:30',
	@departure_time = '08:40'
exec EAP.addParagem
	@viagem_id = 1,
	@rodoviaria = 'Aveiro',
	@arrival_time = '10:20',
	@departure_time = '10:30'
exec EAP.addParagem
	@viagem_id = 1,
	@rodoviaria = 'Porto Campanh�',
	@arrival_time = '11:20',
	@departure_time = '11:20'

exec EAP.ComprarBilhete 1, 1, 'Coimbra', 'Aveiro'