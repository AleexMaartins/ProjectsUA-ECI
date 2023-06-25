function getBotResponse(input) {
    if (input.toLowerCase().includes("olá") || input.toLowerCase().includes("ola") || input.toLowerCase().includes("oi") || input.toLowerCase().includes("boa tarde") || input.toLowerCase().includes("boa noite") || input.toLowerCase().includes("bom dia") || input.toLowerCase().includes("boas")) {
        return "Olá! Como posso ajudar?";

    } else if (input.toLowerCase().includes("tripplaner") || input.toLowerCase().includes("triplaner") || input.toLowerCase().includes("triplanner")) {
        return "A TriPlaner é uma plataforma que permite aos utilizadores planear as suas viagens de forma simples e intuitiva. <br><br>Podes pesquisar por destinos, ver as opções de voos, hospedagem e de alguer de carros, e reservar tudo no mesmo lugar! <br><br>Para além disso, tens acesso aos locais mais populares assim como sugestões personalizadas!<br><br>E claro a um chatbot que te pode ajudar a qualquer momento :) !";

    } else if ((input.toLowerCase().includes("perguntas") || input.toLowerCase().includes("pergunta")) || input.toLowerCase().includes("ajuda")) {
        return "Aqui estão as perguntas mais frequentes:<br><br>-Quais são os destinos mais populares neste momento?<br>-Quais são as opções de voos para viajar de \"Y destino\" para \"X destino\"?<br>-Qual é o melhor período do ano para visitar \"X destino\"?<br>-Quais são as opções de hospedagem disponíveis em \"X destino\"?<br>-Que tipo de atividades posso fazer em \"X destino\"?<br>-Posso reservar um carro para alugar em \"X destino\"?<br>-Qual é o melhor meio de transporte para me deslocar em \"X destino\"?";

    } else if (input.toLowerCase().includes("populares")) {
        return "Os destinos mais populares no momento são Bali, Bora Bora, Hawaii, Whitehaven, Hvar.";

    } else if ((input.toLowerCase().includes("opções") || (input.toLowerCase().includes("opçoes")) && input.toLowerCase().includes("voos")) && input.toLowerCase().includes("porto") && input.toLowerCase().includes("lisboa")) {
        return "Existem várias companhias aéreas que oferecem voos para Lisboa a partir do Porto. Algumas opções incluem TAP Air Portugal, Ryanair e easyJet.";

    } else if ((input.toLowerCase().includes("melhor") && (input.toLowerCase().includes("período") || input.toLowerCase().includes("periodo") || input.toLowerCase().includes("epoca") || input.toLowerCase().includes("época")) && input.toLowerCase().includes("lisboa"))) {
        return "Lisboa tem um clima agradável durante o ano todo, no entanto os meses de primavera e outono são especialmente recomendados, visto que as temperaturas são mais amenas e há menos turistas.";

    } else if (((input.toLowerCase().includes("opções")) || (input.toLowerCase().includes("opçoes")) && input.toLowerCase().includes("hospedagem") && input.toLowerCase().includes("lisboa"))) {
        return "Lisboa oferece uma ampla variedade de opções de hospedagem, desde hotéis luxuosos até pousadas acolhedoras e apartamentos para alugar. Algumas recomendações populares incluem o Hotel Avenida Palace, o Lisboa Carmo Hotel e o Lisbon Destination Hostel.";

    } else if ((input.toLowerCase().includes("atividades") && input.toLowerCase().includes("lisboa"))) {
        return "Em Lisboa, podes desfrutar de passeios pelos bairros históricos, como Alfama e Bairro Alto, visitar museus fascinantes, como o Museu Nacional do Azulejo e o Museu de Arte Antiga, provar a deliciosa culinária local e fazer passeios de barco pelo Rio Tejo.";

    } else if ((input.toLowerCase().includes("alugar") || input.toLowerCase().includes("reservar") || input.toLowerCase().includes("carro") && input.toLowerCase().includes("lisboa"))) {
        return "Sim, oferecemos serviços de aluguer de carros em muitas cidades devido à nossa colaboração com a Guerin, incluindo Lisboa.";

    } else if ((input.toLowerCase().includes("melhor") && input.toLowerCase().includes("transporte") && input.toLowerCase().includes("lisboa"))) {
        return "Em Lisboa, podes utilizar o eficiente sistema de transporte público, que inclui autocarros, metros e elétricos. Além disso, os táxis são amplamente disponíveis e há serviços de partilha de bicicletas para explorar a cidade de forma mais sustentável.";
    } else if (input.toLowerCase().includes("museus") || input.toLowerCase().includes("museu") || input.toLowerCase().includes("idoso") || input.toLowerCase().includes("idoso")) {
        return "Lisboa tem muitos museus interessantes, excelentes opções de hospedagem e atrações para todas as idades, incluindo o Museu Nacional de Arte Antiga, o Museu Nacional do Azulejo, o Museu Calouste Gulbenkian e o Oceanário de Lisboa. Há muitas opções de hotéis e apartamentos dentro do seu orçamento, como o Hotel Portugal, o Hotel Mundial e o Lisbon Arsenal Suites. A cidade fala português e inglês, então a comunicação não deve ser um problema. Aproveite sua viagem a Lisboa!";

    } else if (input.toLowerCase().includes("subidas") || input.toLowerCase().includes("ideia") || input.toLowerCase().includes("subidas") || input.toLowerCase().includes("má") || input.toLowerCase().includes("ma") || input.toLowerCase().includes("colinas")) {
        return "Lisboa apresenta muitas colinas íngremes que podem ser um desafio para pessoas com deficiência motora. No entanto, muitos hotéis, museus e atrações na cidade são acessíveis para cadeiras de rodas e outros equipamentos de mobilidade. Além disso, há serviços de transporte público acessíveis e táxis adaptados disponíveis. Com planeamento adequado, é possível fazer uma viagem confortável e acessível em Lisboa.";

    } else if ((input.toLowerCase().includes("link") || input.toLowerCase().includes("pacotes") || input.toLowerCase().includes("pacote")) && input.toLowerCase().includes("lisboa")) {
        var link = document.createElement("a");
        link.href = "voo.html";
        link.innerHTML = "Sugestão para uma viajem a lisboa";
        link.target = "_blank"; // Abre o link em uma nova aba (opcional)
        link.classList.add("bot-link");

        var botResponse = document.createElement("p");
        botResponse.classList.add("botText", "text-left"); // Adiciona a classe "text-left" para alinhar à esquerda
        botResponse.appendChild(link);

        document.getElementById("chatbox").appendChild(botResponse);

        return "Ao clicares no link, serás reencaminhado para a página de escolha de voos e posterirmente de escolha de hotel!";

    } else if ((input.toLowerCase().includes("link") || input.toLowerCase().includes("pacotes") || input.toLowerCase().includes("pacote")) && input.toLowerCase().includes("hawaii")) {
        var link = document.createElement("a");
        link.href = "voo2.html";
        link.innerHTML = "A nossa sugestão para uma viajem ao hawaii";
        link.target = "_blank"; // Abre o link em uma nova aba (opcional)
        link.classList.add("bot-link");

        var botResponse = document.createElement("p");
        botResponse.classList.add("botText", "text-left"); // Adiciona a classe "text-left" para alinhar à esquerda
        botResponse.appendChild(link);

        document.getElementById("chatbox").appendChild(botResponse);

        return "Ao clicares no link, serás reencaminhado para a página de escolha de voos e posterirmente de escolha de hotel!";

    } else if (input.toLowerCase().includes("obrigado")) {
        return "De nada! Foi um prazer ajudar! Se precisares de mais alguma coisa, não hesites em perguntar!";

    }

    else {
        return "Desculpa, não comprendi. Consegues reformular a pergunta? Obrigado!";
    }
}






