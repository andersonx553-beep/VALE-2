# Missões e cenas canônicas

Os registros JSON correspondentes estão em `conteudo/historia.json`. Os objetivos são especificações semânticas para implementar, não scripts executáveis. Não executar strings ou usar eval. Traduzir cada objetivo para condições e eventos tipados.

## Campanha principal

### Q01 — Duas cadeiras

**Ato:** Prólogo. **Local:** Fazenda. **Pré-requisitos:** novo jogo ou introdução em save migrado.

**Objetivo:** Conhecer Rainara, entrar na casa e guardar a mala no ponto marcado.

- **Rainara:** Você chegou. Eu ia buscar você na estrada, mas o Bento resolveu mudar minha luva de lugar.
- **Jogador:** Você já estava trabalhando aqui?
- **Rainara:** Só arrumando o que dava. Tem uma cadeira para você na varanda.
- **Rainara:** O que trouxe você até aqui?
- **Jogador:** Escolha: quero recomeçar; quero aprender; quero criar raízes.
- **Rainara:** Então começamos por hoje. Amanhã a gente descobre junto.

**Efeitos:** `{"flags": ["story_started", "rainara_companion"], "trust": 3}`.

**Aceite:** Nome do jogador aplicado, motivo salvo; Rainara pode acompanhar e a casa tem entrada e saída.

**Proteção de progressão:** Save antigo: não reposicionar construções; oferecer apresentação ao sair de casa e preservar itens.

### Q02 — Raiz antes da pressa

**Ato:** I. **Local:** Fazenda. **Pré-requisitos:** Q01.

**Objetivo:** Preparar, plantar e regar 3 tiles com uma cultura da estação. Plantas existentes válidas contam.

- **Rainara:** Não precisa transformar o terreno inteiro hoje. Vamos começar com três espaços.
- **Jogador:** E se alguma não crescer?
- **Rainara:** A gente olha a água, a terra, a época. Planta não conhece cobrança; conhece cuidado.
- **Rainara:** Guardei no caderno o que fizemos. Assim amanhã ninguém precisa adivinhar.

**Efeitos:** `{"flags": ["garden_started"], "trust": 3, "items": {"racao": 3}}`.

**Aceite:** Três tiles únicos válidos registrados; gastar água/semente uma vez; diário indica o próximo passo.

**Proteção de progressão:** Dar apenas sementes sazonais necessárias para completar 3, uma vez; reserva tutorial de água disponível.

### Q03 — A panela de Marta

**Ato:** I. **Local:** Praça. **Pré-requisitos:** Q02.

**Objetivo:** Entregar 3 nabos OU 3 cenouras OU 3 espinafres à Marta. A missão antiga equivalente concluída satisfaz esta etapa.

- **Marta:** Trouxe a colheita? A panela é grande, mas a primeira sopa sempre cabe nela.
- **Rainara:** Se sobrar, a gente leva para o Tião.
- **Marta:** Ele diz que não precisa. Leve assim mesmo e pergunte como está.
- **Marta:** Receita é para circular. Anote esta aqui.

**Efeitos:** `{"flags": ["marta_soup_story"], "recipes": ["sopa"], "money": 120}`.

**Aceite:** Consumo do conjunto escolhido e recompensa atômicos; se legado já pagou, não pagar novamente.

**Proteção de progressão:** Marta vende o vegetal sazonal; caderno informa alternativas antes da entrega.

### Q04 — Um lugar para Pipoca

**Ato:** I. **Local:** Fazenda. **Pré-requisitos:** Q03.

**Objetivo:** Ter galinheiro, água e 1 ração; receber ou apresentar uma galinha existente e concluir primeiro cuidado.

- **Celina:** Antes de trazer a Pipoca, vamos olhar o lugar onde ela vai dormir.
- **Rainara:** Tem abrigo, água e um ninho. Falta alguém que respeite o jeito dela.
- **Celina:** Aproxime sem pressa. Deixe que ela conheça sua voz.
- **Rainara:** Ela já encontrou o canto mais confortável. Eu levaria mais tempo.

**Efeitos:** `{"flags": ["poultry_care_known"], "animal_if_missing": "chicken", "items": {"racao": 5}, "trust": 3}`.

**Aceite:** Animal recebe ID e abrigo livre; não gerar galinha extra se jogador usar uma existente.

**Proteção de progressão:** Kit único de construção cobre déficit até 12 madeiras e 6 pedras; Celina subsidia até 80 G para o primeiro galinheiro se necessário.

### Q05 — A tampa entre raízes

**Ato:** I. **Local:** Fazenda. **Pré-requisitos:** Q04.

**Objetivo:** Examinar marca do canal e limpar galhos do ponto de inspeção com 3 ações.

- **Rainara:** Espera. Essa pedra tem uma marca. Minha mãe desenhava isso nas margens do caderno.
- **Jogador:** Uma folha?
- **Rainara:** Duas linhas de água. Uma passa aqui. Ou passava.
- **Rainara:** Vamos mostrar ao Tião antes de mexer mais.

**Efeitos:** `{"flags": ["channel_marker_found"], "story_items": ["inspecao_desenho"]}`.

**Aceite:** Objeto persistente muda para aberto; não invade terreno ocupado: localizar em margem pública reservada.

**Proteção de progressão:** Sem ferramenta equipada, ação remove galhos à mão; missão não exige machado melhorado.

### Q06 — Onde havia correnteza

**Ato:** II. **Local:** Lago. **Pré-requisitos:** Q05.

**Objetivo:** Conversar com Tião e observar duas marcas de nível na margem.

- **Tião:** Eu conheço essa marca. A água chegava até aquele risco.
- **Jogador:** Por que parou?
- **Tião:** Teve uma tempestade. Depois, teve muito dia em que a gente deixou para amanhã.
- **Rainara:** A gente pode olhar o caminho?
- **Tião:** Pode. Mas a ponte precisa de um reparo primeiro.

**Efeitos:** `{"flags": ["old_route_known"], "story_items": ["mapa_ponte"]}`.

**Aceite:** Duas observações distintas e fala registrada; diário mostra ponte sem revelar toda a história.

**Proteção de progressão:** Tião oferece a fala na varanda durante chuva; não esperar clima específico.

### Q07 — Tábuas para atravessar

**Ato:** II. **Local:** Bosque. **Pré-requisitos:** Q06.

**Objetivo:** Entregar 10 madeiras e 6 pedras a Augusto; acionar o reparo da ponte.

- **Augusto:** A travessa está boa. São as tábuas que cansaram.
- **Rainara:** Podemos ajudar?
- **Augusto:** Podem. E vou mostrar onde encaixa, para não dependerem de mim na próxima.
- **Rainara:** Essa parte eu gostei.

**Efeitos:** `{"flags": ["bridge_repaired"], "unlock_regions": ["bosque"]}`.

**Aceite:** Ponte ganha colisão transitável; recursos debitados uma vez; Rainara atravessa com pathfinding.

**Proteção de progressão:** Materiais vendidos por Marta e obtidos em coleta renovável; interromper cena não duplica custo.

### Q08 — O sino de Mimosa

**Ato:** II. **Local:** Estação animal. **Pré-requisitos:** Q07.

**Objetivo:** Ajudar Celina a escovar e abastecer a água de Mimosa, vaca comunitária, ou de uma vaca própria.

- **Celina:** Mimosa se assusta com barulho de metal. Por isso vamos deixar as ferramentas ali.
- **Rainara:** Ela olhou quando você chamou pelo nome.
- **Celina:** Conhecer o animal vem antes de pedir alguma coisa a ele.
- **Rainara:** Acho que ela decidiu que sua manga é uma boa toalha.

**Efeitos:** `{"flags": ["large_animal_care_known"], "items": {"leite": 1}, "unlock_species": ["cow"]}`.

**Aceite:** Escovação e água visíveis; leite de demonstração recebido uma vez, sem criar vaca gratuita.

**Proteção de progressão:** Vaca comunitária garante acesso à missão sem exigir compra ou estábulo próprio.

### Q09 — Três versões da chuva

**Ato:** II. **Local:** Praça. **Pré-requisitos:** Q07.

**Objetivo:** Pedir licença e ouvir Marta, Augusto e Iara; mostrar registros a Luna.

- **Luna:** Quero desenhar o que aconteceu. Mas primeiro preciso escutar.
- **Marta:** Naquela noite, o importante era tirar as pessoas das casas baixas.
- **Iara:** Depois, as flores da margem não voltaram. Cada um percebeu uma perda diferente.
- **Augusto:** Há coisas que eu devia ter explicado antes.
- **Luna:** Vou guardar as versões juntas. Uma não apaga a outra.

**Efeitos:** `{"flags": ["testimonies_recorded"], "story_items": ["relatos_tempestade"]}`.

**Aceite:** Cada morador aceita registro; não repetir conversa da campanha no diálogo cotidiano.

**Proteção de progressão:** Permitir ouvir em vários dias; moradores em casa atendem a conversa de história pela porta.

### Q10 — Flores para voltar

**Ato:** II. **Local:** Bosque. **Pré-requisitos:** Q08, Q09.

**Objetivo:** Plantar 3 mudas nativas em pontos públicos indicados por Iara.

- **Iara:** Antes eu tinha colmeias aqui. Depois aprendi a cozinhar com o que ainda crescia.
- **Rainara:** A gente não precisa esperar tudo ficar pronto para começar um canteiro.
- **Iara:** Três mudas, então. Já é uma conversa com o futuro.
- **Iara:** As mudas eu trouxe. Vocês escolhem a ordem.

**Efeitos:** `{"flags": ["bank_flowers_planted"], "unlock_species": ["bee"]}`.

**Aceite:** Três posições únicas, fases iniciais de crescimento e contribuição para o apiário.

**Proteção de progressão:** Mudas narrativas toleram qualquer estação; não são sementes de inventário vendáveis.

### Q11 — A peça que ficou

**Ato:** II. **Local:** Oficina. **Pré-requisitos:** Q10.

**Objetivo:** Conversar com Augusto e examinar a peça de controle e sua marca.

- **Augusto:** Eu tirei essa peça para ninguém abrir a comporta por impulso.
- **Jogador:** Por que não contou?
- **Augusto:** Achei que explicar depois seria mais fácil. Fui ficando sem jeito de começar.
- **Rainara:** Então começa agora. Mostra como ela funciona.

**Efeitos:** `{"flags": ["gate_piece_found"], "story_items": ["peca_comporta"]}`.

**Aceite:** Peça entra na bolsa de história, sem ser vendável ou consumida por receita.

**Proteção de progressão:** Não requer amizade alta; o contexto da missão libera a conversa.

### Q12 — O primeiro banco de mudas

**Ato:** II. **Local:** Viveiro. **Pré-requisitos:** Q11.

**Objetivo:** Entregar 12 madeiras e 8 pedras; construir a primeira bancada e regar uma muda com Rainara.

- **Rainara:** Eu planejei este banco umas vinte vezes. Sempre faltava alguma coisa.
- **Jogador:** O que faltava hoje?
- **Rainara:** Eu dizer que precisava de ajuda.
- **Rainara:** Segura desse lado. Agora vai.

**Efeitos:** `{"flags": ["nursery_open"], "trust": 8, "unlock_buildings": ["viveiro"]}`.

**Aceite:** Viveiro muda visualmente e recebe interação; Rainara ganha rotina de trabalho real.

**Proteção de progressão:** Materiais comuns, sem cultura sazonal obrigatória; construção fora da fazenda migrada.

### Q13 — Uma página de Helena

**Ato:** II. **Local:** Varanda. **Pré-requisitos:** Q12.

**Objetivo:** Ler a carta entregue na caixa e abrir o mapa do alto com Rainara.

- **Rainara:** Minha mãe reconheceu a peça no desenho que mandamos.
- **Helena:** O desvio salvou casas naquela noite. Depois dele, faltou o trabalho que deveria vir junto.
- **Helena:** No alto existe um vertedouro. Não abram tudo de uma vez. Observem o que nasceu no caminho.
- **Rainara:** Ela deixou espaço na página. Disse que agora é a nossa vez de anotar.

**Efeitos:** `{"flags": ["helena_letter_read"], "story_items": ["mapa_alto"]}`.

**Aceite:** Carta permanece legível no diário; mapa mostra rota e aviso de segurança.

**Proteção de progressão:** Caixa não exige passar mais um dia; carta disponível imediatamente após Q12.

### Q14 — Subida acompanhada

**Ato:** III. **Local:** Alto. **Pré-requisitos:** Q13.

**Objetivo:** Convidar Rainara e seguir três marcos na trilha do alto.

- **Rainara:** Eu vinha até a primeira curva quando era pequena. A mata parece maior agora.
- **Jogador:** Vamos devagar.
- **Rainara:** Se eu começar a andar na frente demais, me chama.
- **Rainara:** Olha a pedra. A mesma marca da fazenda.

**Efeitos:** `{"flags": ["upper_route_walked"], "unlock_regions": ["alto"], "trust": 3}`.

**Aceite:** Companheira acompanha transições; contador de marcos não reseta ao voltar.

**Proteção de progressão:** Rainara pode ser chamada no início da trilha; nenhuma penalidade por sair para cuidar da fazenda.

### Q15 — A água encontrou outro lugar

**Ato:** III. **Local:** Zona úmida. **Pré-requisitos:** Q14.

**Objetivo:** Observar fluxo, vegetação e marcas de aves em três pontos; anotar com Rainara.

- **Rainara:** A nascente ainda está aqui. A água saiu pelo outro lado.
- **Jogador:** E este lugar cresceu em volta dela.
- **Rainara:** Se puxarmos tudo de volta, vamos secar isso aqui.
- **Rainara:** O desenho antigo ajuda. Mas ele não mostra tudo que existe hoje.

**Efeitos:** `{"flags": ["wetland_discovered"], "story_items": ["mapa_fluxo_atual"]}`.

**Aceite:** Diário registra habitat e motivo do fluxo controlado; ambiente não é coletável até desaparecer.

**Proteção de progressão:** Observações disponíveis em qualquer clima e hora; contraste indica os três pontos.

### Q16 — O que Tião não disse

**Ato:** III. **Local:** Ponte. **Pré-requisitos:** Q15.

**Objetivo:** Ouvir Tião e Augusto juntos na ponte, convocados pelo caderno.

- **Tião:** Fui eu quem abriu o desvio. Havia gente nas casas baixas.
- **Augusto:** Eu ajudei. Depois achei que bastava impedir alguém de mexer.
- **Tião:** Quando o barro baixou, eu devia ter voltado. Fiquei esperando que outra pessoa soubesse o que fazer.
- **Rainara:** A gente sabe o que aconteceu agora. Precisa decidir o que faz daqui para a frente.

**Efeitos:** `{"flags": ["storm_truth_known"], "trust": 4}`.

**Aceite:** Cena marca verdade descoberta; NPCs retornam à rotina, sem bloquear a ponte.

**Proteção de progressão:** Convocação reúne NPCs apenas durante a cena, respeitando retorno e save.

### Q17 — Deixar espaço para a ajuda

**Ato:** III. **Local:** Viveiro. **Pré-requisitos:** Q16.

**Objetivo:** Conversar com Rainara e escolher como organizar o trabalho: medir juntos, chamar o grupo ou conversar primeiro.

- **Rainara:** Eu queria abrir antes da semana seca. Já estava fazendo a lista sozinha de novo.
- **Jogador:** Escolha: vamos medir juntos; vamos chamar os outros; primeiro me conta como você está.
- **Rainara:** Eu fico com medo de parar e ninguém continuar.
- **Jogador:** Eu estou aqui. Mas preciso fazer parte da decisão.
- **Rainara:** Está bem. Vamos escrever um plano que caiba em mais mãos.

**Efeitos:** `{"flags": ["shared_plan_agreed"], "trust": 8}`.

**Aceite:** Salvar escolha de conversa; todas as opções mantêm parceria e conduzem ao plano seguro.

**Proteção de progressão:** Nenhuma resposta afasta Rainara ou tranca final; rever diálogo no diário.

### Q18 — O quadro do mutirão

**Ato:** IV. **Local:** Praça. **Pré-requisitos:** Q17.

**Objetivo:** Participar da reunião e confirmar tarefas de água, margens e refeição.

- **Marta:** Eu cuido da comida. Mas desta vez todo mundo vai saber quanto precisa trazer.
- **Celina:** Eu olho os bebedouros e a passagem dos animais.
- **Iara:** Eu fico com as margens. A água precisa chegar sem levar a terra embora.
- **Augusto:** Tião e eu montamos o controle. Vocês acompanham a leitura.
- **Rainara:** E no fim do dia, todo mundo descansa. Está no quadro.

**Efeitos:** `{"flags": ["workboard_open"], "unlock_ui": ["mutirao"]}`.

**Aceite:** Quadro mostra 3 contribuições, saldos e conclusão; progresso persiste por tarefa.

**Proteção de progressão:** Sem cobrança por dia; itens doados são registrados e nunca exigidos de novo.

### Q19 — O trabalho de muitas mãos

**Ato:** IV. **Local:** Praça e Alto. **Pré-requisitos:** Q18.

**Objetivo:** Contribuir 20 madeiras + 12 pedras; entregar 2 comidas prontas de qualquer receita válida; plantar 3 mudas fornecidas.

- **Luna:** Desenhei as placas. Esta seta estava mandando todo mundo para o quintal da Marta.
- **Marta:** Podia ser pior. Eu ia cobrar o almoço.
- **Rainara:** Cada parte pronta ficou marcada. Dá para ver o vale trabalhando.
- **Augusto:** Agora podemos testar sem apostar tudo numa puxada.

**Efeitos:** `{"flags": ["spillway_built", "banks_ready", "meal_ready"], "trust": 6}`.

**Aceite:** Três grupos independentes; doação parcial permitida; não consumir comida reservada sem confirmar.

**Proteção de progressão:** Comidas podem ser compradas; flores são fornecidas; fontes renováveis impedem falta definitiva de madeira.

### Q20 — A primeira abertura

**Ato:** IV. **Local:** Comporta. **Pré-requisitos:** Q19.

**Objetivo:** Confirmar teste com Rainara; usar ação para abrir 1/3; observar água turva; fechar e limpar o filtro com 3 ações.

- **Tião:** Primeiro só um pouco. Olhem a marca clara na pedra.
- **Rainara:** Estou vendo daqui. Pode abrir.
- **Rainara:** A água turvou. Fecha um instante; tem galho no filtro.
- **Augusto:** Foi para isso que fizemos o teste.
- **Rainara:** Desta vez a gente parou na hora certa.

**Efeitos:** `{"flags": ["filter_cleared", "first_flow_tested"]}`.

**Aceite:** Ação sem timing punitivo; Rainara assume observação; filtro limpo persiste e teste não destrói nada.

**Proteção de progressão:** Ao recarregar no meio, voltar à etapa segura com comporta fechada; não reiniciar recursos do mutirão.

### Q21 — O primeiro excedente

**Ato:** IV. **Local:** Comporta. **Pré-requisitos:** Q20.

**Objetivo:** Escolher pomar comunitário OU área sombreada dos animais como primeiro projeto beneficiado.

- **Celina:** O fluxo está estável. Temos água para começar mais um espaço.
- **Iara:** Podemos preparar o pomar.
- **Celina:** Ou a área de sombra dos animais.
- **Rainara:** Os dois cabem no futuro. Qual a gente começa agora?

**Efeitos:** `{"flags": ["first_project_chosen"], "choice": "pomar|sombra"}`.

**Aceite:** Salvar escolha; aplicar só um projeto gratuito e abrir o outro no pós-jogo.

**Proteção de progressão:** Mostrar função de cada projeto; cancelar menu não confirma escolha; nenhuma opção elimina conteúdo.

### Q22 — Duas águas outra vez

**Ato:** IV. **Local:** Comporta e Fazenda. **Pré-requisitos:** Q21.

**Objetivo:** Abrir fluxo definitivo gradual, confirmar observação com Rainara e visitar a confluência na fazenda.

- **Rainara:** A marca parou de subir. A outra passagem continua correndo.
- **Tião:** Então deixem assim. Amanhã a gente mede de novo.
- **Jogador:** Dá para ouvir as duas daqui.
- **Rainara:** Eu tinha esquecido que eram sons diferentes.

**Efeitos:** `{"flags": ["water_restored"], "trust": 10, "unlock_projects": ["postgame_second_project"]}`.

**Aceite:** Visual e som do canal mudam, habitat preservado, flag global propagada nas regiões.

**Proteção de progressão:** Restauro idempotente; recarregar não fecha fluxo nem reaplica recompensa.

### Q23 — A mesa comprida

**Ato:** Epílogo. **Local:** Praça. **Pré-requisitos:** Q22.

**Objetivo:** Escolher quando iniciar o Festival das Duas Águas e levar um alimento qualquer, inclusive comprado.

- **Marta:** A mesa cresceu. A panela também.
- **Luna:** Todo mundo autorizou o desenho. Bento não ficou parado, mas isso faz parte.
- **Augusto:** Deixei parafusos comuns. Se soltar, qualquer um consegue apertar.
- **Iara:** Tem pão, tem mel e tem lugar.
- **Rainara:** Minha mãe mandou uma carta. Vou guardar para ler com você depois.

**Efeitos:** `{"flags": ["festival_completed"], "decor": ["retrato_comunidade"]}`.

**Aceite:** Festival inicia por confirmação, preserva animais, pausa relógio e retorna ao ponto seguro.

**Proteção de progressão:** Marta oferece um pão se inventário sem alimento e saldo insuficiente; não bloquear conclusão.

### Q24 — Fica mais um pouco

**Ato:** Epílogo. **Local:** Varanda. **Pré-requisitos:** Q23.

**Objetivo:** Sentar com Rainara, ler a última carta e escolher uma fala de parceria; ver ou pular créditos.

- **Rainara:** Quando trouxe a segunda cadeira, pensei que talvez ela ficasse vazia de novo.
- **Jogador:** Escolha: ainda temos muito para aprender; quero construir essa vida com você; esta já é a nossa casa.
- **Rainara:** Agora coloquei outra ali. Para quando alguém vier visitar.
- **Helena:** Vocês não devolveram o vale ao que era. Deram a ele um jeito de continuar.
- **Rainara:** Amanhã a gente vê o que precisa de cuidado. Hoje, fica mais um pouco.

**Efeitos:** `{"flags": ["campaign_complete", "postgame_open"], "trust": 10}`.

**Aceite:** Créditos puláveis, controle retorna na manhã seguinte; Rainara presente; final não se repete.

**Proteção de progressão:** Fala romântica só recebe tratamento romântico se romance opt-in; parceria sempre permite final completo.

## Eventos pessoais e animais

Eventos são únicos por ID. Condições de amizade não são bloqueios para a campanha principal. Valores de confiança dos eventos somam no máximo uma vez. Missões M01 a I01 usam amizade normalizada em escala 0–5; preservar valores maiores se o jogo atual já os suportar.

### R01 — A muda torta

**Condição:** Confiança >=10; Q02 concluída. **Local:** Viveiro.

- **Rainara:** Esta muda inclinou para a luz. Eu estava chamando de torta o que era só uma procura.
- **Jogador:** Vamos virar o vaso?
- **Rainara:** Vamos. Um pouco por dia.

**Efeito único:** `{"trust": 8, "memory": "muda_torta"}`. Interrupção: retomar do último checkpoint seguro.

### R02 — Debaixo da mesa

**Condição:** Confiança >=25; Q04 concluída; após 18h; chuva OU 2 dias de espera. **Local:** Casa.

- **Rainara:** Bento não quer sair daí. Trouxe uma manta.
- **Jogador:** Posso sentar aqui?
- **Rainara:** Pode. A gente não precisa convencer ninguém de que o trovão é bonito.
- **Rainara:** Olha. Ele já soltou a orelha.

**Efeito único:** `{"trust": 8, "memory": "abrigo_bento"}`. Interrupção: retomar do último checkpoint seguro.

### R03 — Uma lista menor

**Condição:** Confiança >=40; Q12 concluída. **Local:** Varanda.

- **Rainara:** Minha lista ocupou as duas páginas.
- **Jogador:** O que precisa mesmo ser hoje?
- **Rainara:** Água, comida e esta conversa.
- **Rainara:** O resto a gente divide. Acho que cabem dois combinados por dia, se um de nós puder dizer chega.

**Efeito único:** `{"trust": 8, "companion_tasks_per_day": 2}`. Interrupção: retomar do último checkpoint seguro.

### R04 — Escolher ficar

**Condição:** Confiança >=60; Q17 concluída. **Local:** Mirante.

- **Rainara:** Eu sempre dizia que fiquei porque alguém precisava cuidar daqui.
- **Rainara:** Hoje eu consigo dizer outra coisa. Eu gosto da vida que estamos fazendo.
- **Jogador:** Escolha: nossa amizade importa para mim; quero conversar sobre nós como casal.
- **Rainara:** Podemos conversar sem pressa. Nenhuma resposta apaga o que já construímos.

**Efeito único:** `{"trust": 8, "romance": "explicit_choice_only"}`. Interrupção: retomar do último checkpoint seguro.

### R05 — Um espaço na varanda

**Condição:** Confiança >=80; Q24 concluída. **Local:** Varanda.

- **Rainara:** Pensei em aumentar a mesa. Sem tirar nossas cadeiras do lugar.
- **Jogador:** Quem você quer chamar primeiro?
- **Rainara:** Luna. Ela já desenhou a varanda nova antes de perguntar.
- **Rainara:** Depois a gente combina um dia só nosso, sem lista.

**Efeito único:** `{"trust": 8, "decor": "mesa_varanda", "memory": "espaco_para_visitas"}`. Interrupção: retomar do último checkpoint seguro.

### M01 — Livro de fiados

**Condição:** Amizade >=2; Q09 concluída; entregar 1 sopa. **Local:** Armazém.

- **Marta:** Eu anotava a dívida de todo mundo e esquecia de anotar quando precisava de ajuda.
- **Jogador:** Podemos organizar uma contribuição conjunta?
- **Marta:** Podemos. Mas vamos escrever um valor que caiba no bolso de cada um.
- **Marta:** Leve esta receita. Essa conta já está paga.

**Efeito único:** `{"recipe": "pao_milho", "decor": "prateleira"}`. Interrupção: retomar do último checkpoint seguro.

### T01 — Banco da margem

**Condição:** Amizade >=2; Q16 concluída; doar 6 madeiras. **Local:** Lago.

- **Tião:** Este banco era para duas pessoas. Eu vivia deixando a caixa de pesca no outro lugar.
- **Jogador:** Posso tirar a caixa?
- **Tião:** Pode. Hoje eu não trouxe assunto para fugir da conversa.

**Efeito único:** `{"recipe": "isca_simples", "decor": "banco_margem"}`. Interrupção: retomar do último checkpoint seguro.

### L01 — Retratos com licença

**Condição:** Amizade >=2; Q09 concluída; recolher consentimento de 3 moradores. **Local:** Atelier.

- **Luna:** Marta pediu para eu desenhar as mãos também. Disse que trabalham mais que o rosto.
- **Jogador:** E o seu retrato?
- **Luna:** Ainda falta. Acho que quero me desenhar com uma mala e uma chave.
- **Luna:** Para lembrar que estudar fora e ter para onde voltar podem ser a mesma vida.

**Efeito único:** `{"decor": "retrato_luna", "memory": "exposicao"}`. Interrupção: retomar do último checkpoint seguro.

### C01 — Plantão dividido

**Condição:** Amizade >=2; Q08 concluída; 3 dias distintos de cuidado em qualquer animal. **Local:** Estação.

- **Celina:** Cheguei e vocês já tinham notado que faltava água.
- **Rainara:** Aprendemos com alguém bastante insistente.
- **Celina:** Estou tentando aprender a não fazer a mesma explicação cinco vezes.
- **Celina:** Vou deixar o quadro aqui. Quem observa primeiro anota.

**Efeito único:** `{"unlock": "adoption_and_breeding", "item": "escova"}`. Interrupção: retomar do último checkpoint seguro.

### A01 — A cadeira que balança

**Condição:** Amizade >=2; Q11 concluída; doar 4 madeiras. **Local:** Oficina.

- **Augusto:** Esta perna ficou curta. Em vez de corrigir, eu guardei a cadeira.
- **Jogador:** Ainda dá para usar?
- **Augusto:** Dá. Às vezes a parte difícil é tirar do canto.
- **Augusto:** Você segura enquanto eu marco?

**Efeito único:** `{"decor": "cadeira_balanco", "unlock": "furniture_catalog"}`. Interrupção: retomar do último checkpoint seguro.

### I01 — Receita sem medida

**Condição:** Amizade >=2; Q10 concluída; entregar 1 mel comprado ou produzido. **Local:** Cozinha.

- **Iara:** Minha receita dizia um tanto de mel. Péssima instrução para quem está começando.
- **Jogador:** Vamos medir agora?
- **Iara:** Vamos. E depois cada pessoa encontra o seu tanto.
- **Iara:** Sobrou uma fatia. A Rainara está no viveiro?

**Efeito único:** `{"recipe": "pao_mel", "unlock": "apiary_upgrade"}`. Interrupção: retomar do último checkpoint seguro.

### B01 — O ninho escolhido

**Condição:** Galinha existente; vínculo >=10; construir ninho. **Local:** Galinheiro.

- **Rainara:** Pipoca escolheu o cesto das luvas.
- **Jogador:** Podemos oferecer outro cesto?
- **Rainara:** Trouxe palha. Vamos deixar perto do lugar que ela já escolheu.

**Efeito único:** `{"animal_behavior": "nest_preference", "memory": "pipoca_ninho"}`. Interrupção: retomar do último checkpoint seguro.

### B02 — Sem pressa com Mimosa

**Condição:** Vaca existente; 3 interações de escova em dias diferentes. **Local:** Estábulo.

- **Celina:** Hoje ela veio antes de você chamar.
- **Rainara:** Augusto combinou de martelar depois. Acho que todo mundo está aprendendo.
- **Celina:** Confiança também tem horário e silêncio.

**Efeito único:** `{"animal_affinity": 8, "memory": "mimosa_confianca"}`. Interrupção: retomar do último checkpoint seguro.

### B03 — Um lugar alto

**Condição:** Cabra existente; construir plataforma segura. **Local:** Estábulo.

- **Rainara:** Ela subiu no caixote outra vez.
- **Augusto:** Posso fazer um lugar próprio para isso.
- **Rainara:** Você ouviu, Jujuba? Vai ganhar uma varanda antes de mim.

**Efeito único:** `{"animal_behavior": "climb_platform"}`. Interrupção: retomar do último checkpoint seguro.

### B04 — A escova de Brisa

**Condição:** Ovelha existente; escovar em 3 dias distintos. **Local:** Estábulo.

- **Rainara:** Brisa ouviu a escova na caixa e veio andando.
- **Jogador:** Ela já conhece o som.
- **Rainara:** E eu já sei que preciso trazer mais tempo do que pressa.

**Efeito único:** `{"animal_behavior": "approach_brush"}`. Interrupção: retomar do último checkpoint seguro.

### B05 — A volta de Pingo

**Condição:** Pato existente; lago e rampa construídos. **Local:** Lago dos patos.

- **Rainara:** Bento mostrou a água. Esqueceu de mostrar o caminho de volta.
- **Celina:** Com a rampa, ele entra e sai sozinho.
- **Rainara:** Agora os dois estão satisfeitos com a visita.

**Efeito único:** `{"animal_behavior": "swim_loop"}`. Interrupção: retomar do último checkpoint seguro.

### B06 — A cadeira da Amora

**Condição:** Cozinha disponível; cama, água e alimento preparados. **Local:** Casa.

- **Rainara:** A visita escolheu sua cadeira.
- **Jogador:** E esta cama perto da janela?
- **Rainara:** Podemos oferecer. A palavra final parece ser dela.
- **Rainara:** Olha só. Aceitou. Por enquanto.

**Efeito único:** `{"pet": "cat", "memory": "amora_adotada"}`. Interrupção: retomar do último checkpoint seguro.

## Pós-jogo

### P01 — O outro projeto

**Pré-requisitos:** Q24. **Objetivo:** Construir o projeto não escolhido em Q21 com 250 G, 15 madeira e 10 pedra.

**Recompensa:** Pomar OU sombra completos; ambos agora presentes.

- **Rainara:** Desta vez não precisamos escolher qual fica para depois.
- **Jogador:** Tem espaço para os dois.
### P02 — Uma parede de histórias

**Pré-requisitos:** Q24, L01. **Objetivo:** Pendurar três retratos autorizados na praça.

**Recompensa:** Exposição permanente e falas pós-campanha.

- **Luna:** Este espaço ficou vazio de propósito. Ainda tem história chegando.
- **Rainara:** Então não guarde o lápis.
### P03 — A primeira feira

**Pré-requisitos:** Q24. **Objetivo:** Levar três categorias de produto, compradas ou produzidas, sem mínimo de qualidade.

**Recompensa:** Banca pessoal decorativa e feira semanal.

- **Marta:** Tem produto seu, do vale e de vizinho. Assim começa uma feira.
- **Iara:** Eu vim pela conversa. E pelo queijo.
### P04 — Um dia sem lista

**Pré-requisitos:** Q24, R05. **Objetivo:** Convidar Rainara para um passeio opcional; nenhuma coleta obrigatória.

**Recompensa:** Memória de convivência e retrato da dupla.

- **Rainara:** Trouxe comida, uma manta e nada para consertar.
- **Jogador:** Nem uma ferramenta?
- **Rainara:** Só uma colher. Pretendo usar bastante.

## Encenação e continuidade

Toda cena começa com personagens posicionados em tiles livres, câmera alinhada e controle comum pausado. A animação de ambiente pode continuar. Ações, falas e escolhas possuem IDs; um checkpoint ocorre após cada efeito permanente. Pular uma cena aplica os efeitos narrativos obrigatórios uma vez e preserva escolhas ainda não respondidas em um menu breve. A cena pode ser relida no diário sem repetir recompensas.

Q01: Bento passa com a luva; Rainara olha para ele e depois para o jogador. Q05: ela se agacha junto à pedra e abre o caderno. Q12: protagonista segura a bancada enquanto Rainara encaixa uma peça. Q15: câmera mostra as duas saídas da água e retorna à dupla. Q17: silêncio curto; Rainara fecha o caderno antes de ouvir a resposta. Q20: a água muda para turva, Rainara sinaliza parar; o estado seguro é comporta fechada. Q22: mostrar sucessivamente a fonte, o canal e a confluência por transições curtas puláveis. Q23: moradores ocupam pontos da mesa, sem colisões entre eles. Q24: ambos sentados, Bento dorme; câmera parada, som de água baixo, créditos sobre fade.

Falas marcadas como “Escolha” são opções de interface, não texto a ser dito pelo jogador automaticamente. A fala seguinte usa a escolha registrada. Q01 grava motive=restart/learn/roots. Q17 grava sharedPlan=measure/group/listen. Q21 grava firstProject=orchard/shade. R04 grava relationship=friendship ou abre confirmação romance; não inferir romance de presentes. Q24 adapta a palavra “parceria” ou “amor” somente se relationship=romance explícito.

## Falas de variação para Rainara

As falas abaixo são condicionais, com máximo de um comentário espontâneo a cada 90 segundos e um por condição por dia. Diálogos acionados pelo jogador não entram nesse limite. Prioridade: missão > evento > rotina > comentário ambiental. Não repetir a mesma fala nas três últimas interações.

| Condição | Fala |
| --- | --- |
| Primeira chuva | “Hoje o céu pegou o regador emprestado.” |
| Inverno | “A terra descansa. A gente também pode aprender isso.” |
| Colheita grande | “Cabe no cesto. Na minha empolgação, ainda não.” |
| Animal se aproxima | “Olha quem já estava esperando sua visita.” |
| Viveiro aberto | “Tem lugar para mais uma muda. Eu conferi duas vezes.” |
| Primeira conversa do dia | “Bom dia. O que fazemos juntos hoje?” |
| Tarefa sem ração | “A ração acabou. Deixei anotado quem ainda falta alimentar.” |
| Tarefa sem água | “Preciso encher o regador antes de continuar.” |
| Comporta restaurada | “Às vezes eu paro só para ouvir. Ainda parece novidade.” |
| Caminho bloqueado | “Vou dar a volta. Espero você ali adiante.” |
| Depois da discussão | “Hoje eu trouxe uma pergunta antes da lista.” |
| Romance aceito | “Gosto de dividir os dias comuns com você.” |
| Amizade escolhida | “Tem parceria que vira casa. A nossa é assim.” |
| Festival | “Guardei um lugar na mesa. Você escolhe a conversa.” |
| Pós-jogo, noite | “Nada urgente agora. Quer sentar um pouco?” |

## Festivais recorrentes com diálogo

F01 Feira das Mudas, primavera dia 10. Iara: “Cada muda tem um jeito. Troque uma dica junto com ela.” Rainara: “Esta veio do nosso primeiro banco.” Interação: selecionar uma muda comum e receber variante decorativa; uma troca especial por edição anual.

F02 Noite das Lanternas, verão dia 10. Luna: “Desenhei a luz antes de acender. Ficou diferente. Ainda bem.” Rainara: “Vamos pelo caminho da ponte?” Interação: acompanhar percurso sem tempo limite, pendurar uma lanterna de tecido recuperável; recompensa visual, sem jogar lixo no lago.

F03 Mesa da Colheita, outono dia 10. Marta: “Quem trouxe pouco senta perto de quem trouxe muito. A mesa resolve.” Interação: doar um alimento qualquer; reconhecer variedade com comentários, sem ranking humilhante; uma receita por primeira participação.

F04 Varanda Acesa, inverno dia 10. Tião: “Está frio para pescar e bom para ouvir história.” Rainara: “Vou buscar mais uma manta.” Interação: presente opcional com preferência indicada; carta e bebida quente gratuitas; receber enfeite de janela.

Cada festival guarda edição por ano para impedir recompensas duplicadas. Eventos perdidos retornam no ano seguinte. A campanha não requer ter participado de nenhum deles.
