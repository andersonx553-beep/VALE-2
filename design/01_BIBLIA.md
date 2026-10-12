# Vale a Dois
## Bíblia narrativa e de jogo

Versão 1.0 — 12 de outubro de 2026. Autor da encomenda: proprietário do projeto VALE-2. Destinatário: Codex e equipe de desenvolvimento. Este documento define a criação original a implementar e amplia o jogo existente. Ele é uma especificação de produção; não afirma que o conteúdo proposto já esteja implementado.

## 1. Visão e promessa ao jogador

Vale a Dois é um jogo individual de fazenda, convivência e descoberta em uma serra brasileira imaginária. O jogador estabelece sua vida na Fazenda Entreáguas ao lado de Rainara, cria animais, conhece os moradores e recupera um sistema de água que se tornou o centro de uma antiga divisão da comunidade.

O prazer central é perceber sinais concretos do próprio cuidado: a primeira muda sobrevivendo, um animal que passa a se aproximar, uma receita preparada por alguém, o viveiro de Rainara ficando cheio e um caminho antes seco recebendo água. Cada sistema deve sustentar uma dessas experiências.

O nome Vale a Dois tem três sentidos: as duas nascentes que formaram a região, a antiga regra de manutenção em dupla e a vida construída pelo protagonista e Rainara. Não depende de multiplayer ou romance.

Tom: afetuoso, curioso e bem-humorado, com conflitos humanos compreensíveis. Classificação criativa pretendida: experiência familiar; sem violência gráfica, abate ou morte punitiva dos animais. Isso não é uma classificação etária oficial. O jogo pode abordar culpa, solidão e despedidas temporárias com leveza e respeito.

### Decisões e complementos já incorporados

- Diário das Duas Águas: reúne missões, mapas, desenhos de Luna, receitas e lembranças das cenas. O jogador pode reler diálogos importantes.
- Ritual da varanda: pequenas cenas de fim de dia com Rainara e Bento. Variam conforme o que aconteceu; não interrompem todo entardecer.
- Pós-jogo: o final resolve o conflito principal e abre festivais recorrentes, criações, decoração e cenas de parceria.
- Cuidado compartilhado: Rainara executa tarefas combinadas de verdade; sua ajuda não gera itens do nada.
- Modo tranquilo: ajustes de velocidade do relógio, janela de pesca e tamanho do texto. Sem penalidade por usar acessibilidade.
- Memória do mundo: moradores reconhecem a nascente restaurada, animais têm nomes preservados e construções se transformam visualmente.

## 2. Cânone do lugar

### Geografia

O Vale das Duas Águas fica numa serra fictícia. O clima mantém as quatro estações de 14 dias já presentes no código. O inverno frio e a neve são convenções desse mundo; não representam uma região brasileira real. O cenário mistura vegetação de altitude, pomares, hortas, mata úmida e pequenas propriedades.

A Nascente Clara desce pelo lado leste e ainda abastece a vila. A Nascente da Sombra percorre um canal de pedra pelo oeste; seu antigo leito ficou seco. Elas se encontram junto à Fazenda Entreáguas. A água é comum e material: os vaga-lumes azuis e os sons noturnos inspiram histórias, mas não substituem reparos, manejo ou decisões humanas.

O mapa atual de 80 × 60 tiles é a região Fazenda. Preserve seu terreno e coordenadas na migração. Adicione Praça, Bosque, Alto das Nascentes e interiores como regiões separadas, por transições visíveis nas bordas ou portais. Não comprima todos os novos edifícios na fazenda existente.

### Linha do tempo

| Momento | Fato canônico |
| --- | --- |
| Há 70 anos | Famílias da serra constroem canais e um pequeno viveiro comunitário. Duas pessoas operam a distribuição: uma na comporta e outra observando o nível a jusante. |
| Há 28 anos | Helena, mãe de Rainara, começa um caderno com mapas, mudas e rotinas de manutenção. Tião acompanha as medições; Augusto repara as estruturas. |
| Há 12 anos | Uma tempestade ameaça casas baixas. Tião e Augusto abrem um desvio de emergência. A vila é protegida, mas lama bloqueia parte do canal da Sombra. |
| Nos meses seguintes | A manutenção é adiada por falta de materiais e por discordâncias. A produção das terras de oeste cai. Versões incompatíveis sobre o incidente circulam. |
| Há 8 anos | O viveiro fecha. Helena conserva o caderno; Iara muda suas colmeias e outras famílias deixam propriedades. |
| Há 3 anos | Helena passa a viver em outra cidade para ajudar a irmã. Continua escrevendo para Rainara. Celina inicia visitas regulares ao vale. |
| Hoje | A associação oferece a propriedade Entreáguas em cessão de uso para quem cuidar dela. O protagonista aceita e Rainara assume a parceria no viveiro e nos cuidados. |

Helena está viva. Não há desaparecimento a resolver nem morte secreta de Rainara. A campanha revela uma decisão de emergência seguida de omissões, culpa e falta de cooperação. Nenhum personagem é um vilão corporativo ou um escolhido mágico.

### A verdade da segunda nascente

A fonte nunca secou por completo. Sedimentos bloquearam a entrada do canal; a água passou a escorrer por uma fenda, alimentando uma pequena zona úmida escondida. Abrir a comporta de uma vez inundaria os terrenos baixos e prejudicaria esse novo habitat. O final exige limpar o canal, reconstruir um vertedouro e ajustar o fluxo gradualmente, preservando a zona úmida.

Rainara encontra o desenho; Tião interpreta as marcas de nível; Augusto reconhece a peça retirada; Marta apresenta as contas que explicam a manutenção interrompida; Luna organiza os relatos; Celina e Iara observam os efeitos sobre animais e plantas. O jogador reúne os recursos e participa das decisões. A recuperação depende de toda a comunidade.

## 3. História completa

### Prólogo — Duas cadeiras

O protagonista chega à Entreáguas com uma mala e o termo de cessão. Rainara tenta endireitar uma cerca enquanto Bento rouba uma luva. Ela já trouxe sementes e instalou uma segunda cadeira na varanda. O primeiro objetivo é guardar a mala, conhecer o terreno e plantar três nabos. À noite, a dupla divide uma refeição simples. Rainara aponta um canal seco e comenta que antes era possível ouvir duas águas da varanda.

A personalização permite nome, aparência e pronomes do protagonista; o código deve usar flexões neutras por construção quando não houver configuração. O passado não determina profissão, gênero ou romance. A motivação é escolhida na conversa inicial: recomeçar, aprender ou criar raízes. A escolha altera falas e uma lembrança do diário, sem vantagens mecânicas.

### Ato I — O que fica de pé

Marta ajuda com sementes; Tião ensina a observar o lago; Luna pede autorização para desenhar a fazenda. Celina entrega uma galinha adulta de acolhimento, Pipoca, quando existe abrigo e comida. Rainara deseja reabrir o viveiro, mas tenta fazer tudo sozinha. O jogador encontra uma tampa de inspeção entre raízes. A primeira conquista coletiva é uma sopa compartilhada, usando a missão original de Marta como ponte para a nova campanha.

Conclusão: o caderno de Helena indica que o canal da Sombra atravessa a fazenda. Um pedaço do mapa foi separado para orientar uma manutenção que nunca terminou.

### Ato II — Vozes do mesmo lugar

Cada morador tem uma versão da tempestade. Tião afirma que foi necessário abrir o desvio. Augusto evita mostrar uma peça guardada na oficina. Iara lembra das flores desaparecendo. Marta manteve o armazém funcionando com estoques que não foram pagos. Luna quer registrar os relatos sem transformar uma pessoa em culpada por todos.

A busca integra a vida normal: fornecer uma refeição para uma caminhada, recuperar uma passagem, cuidar da primeira vaca com Celina e plantar flores próximas ao viveiro. No fim do ato, Helena envia uma carta: a tarefa era restabelecer o sistema depois da emergência, não retornar a um passado perfeito.

Conclusão: Rainara e o jogador encontram a peça de controle e localizam o acesso à fonte. O viveiro volta a funcionar em escala pequena.

### Ato III — A pressa e a confiança

Rainara quer abrir o canal antes da próxima semana seca; o jogador e a comunidade precisam medir os riscos. Acompanhá-la ao alto mostra a zona úmida que nasceu do desvio. Tião admite que não voltou para terminar a manutenção por vergonha e medo de ser responsabilizado. Augusto admite que escondeu a peça para impedir uma abertura improvisada, mas nunca explicou isso aos vizinhos.

Rainara sente que as explicações chegam sempre depois de alguém desistir. Sua discussão com o protagonista trata de divisão de responsabilidade. Há três respostas válidas: medir juntos, pedir ajuda ou conversar antes de agir. Todas levam a um plano seguro; mudam o diálogo de reconciliação, não expulsam a personagem do jogo.

Conclusão: a dupla deixa de tentar resolver o vale sozinha. Um quadro de tarefas divide trabalho, materiais e observação de campo.

### Ato IV — O trabalho de muitas mãos

A comunidade organiza um mutirão. Celina verifica acesso a bebedouros; Iara cuida do plantio junto às margens; Luna sinaliza caminhos; Marta cozinha; Augusto monta o vertedouro; Tião acompanha os níveis. Rainara e o jogador testam a distribuição em etapas. A cena de duas alavancas é uma interação individual com Rainara controlada pelo jogo, sem networking.

Na primeira abertura a água fica turva. É preciso pausar e limpar um filtro de galhos. Esse obstáculo demonstra o aprendizado, sem destruir a fazenda ou penalizar animais. A segunda abertura estabiliza o fluxo. O jogador escolhe qual projeto receberá o primeiro excedente: o pomar comunitário ou a área de sombra dos animais. O outro projeto continua disponível no pós-jogo com custo equivalente.

Conclusão: água corrente no canal, mudança no ambiente sonoro, novas plantas ao longo das margens e moradores usando o caminho recuperado.

### Epílogo — A mesa comprida

O Festival das Duas Águas acontece quando o jogador confirma que está pronto. Não depende de esperar uma estação específica. Cada morador traz algo: Marta a panela, Tião um banco, Luna um retrato coletivo, Celina um sino para o abrigo, Augusto uma mesa e Iara pão com mel. Helena envia uma receita e uma mensagem de orgulho; sua ausência física não exige novo sprite.

Rainara conta que tinha preparado a segunda cadeira para uma pessoa que talvez fosse embora. Agora deixou um espaço para visitantes ao lado das duas. O jogador escolhe a fala final conforme a relação: amizade, parceria ou romance já declarado. A dupla observa os canais ao entardecer; Bento dorme perto. Os créditos podem ser pulados e o save retorna à manhã seguinte.

Última fala de Rainara: “Amanhã a gente vê o que precisa de cuidado. Hoje, fica mais um pouco.”

## 4. Personagens completos

### Protagonista

Nome escolhido; adulto. Visual padrão: cabelo preto, pele morena clara, jaqueta creme, camiseta branca, calça escura e botas castanhas. O conceito enviado pelo usuário orienta proporção e rosto. Personalizações futuras preservam legibilidade e o estilo.

Desejo: criar uma vida própria. Conflito: encontrar equilíbrio entre produzir, conhecer as pessoas e descansar. Sua voz oferece escolhas curtas e naturais. Não supor abandono familiar, luto ou profissão anterior. O protagonista nunca é obrigado a paquerar para progredir.

### Rainara — 26 anos — viveirista e coprotagonista

Visual canônico: cabelos castanhos longos e ondulados, olhos castanhos grandes, pele morena, blusa coral, saia terracota, bolsa verde-oliva, botas e presilha de folha. Nas tarefas, usa avental e luvas sobre esse conjunto; não perde sua identidade visual. Silhueta marcada pelo cabelo e pela bolsa.

Desejo: recuperar o viveiro e ficar no vale por escolha, não por obrigação. Medo: que aceitar ajuda signifique dever sua vida aos outros. Defeito: trabalha além do combinado e decide por quem acha estar protegendo. Qualidades: observação, persistência, humor rápido, habilidade com mudas. Mania: desenha uma pequena folha ao encerrar anotações. Não gosta de desperdício de sementes; gosta de sopa, morangos e presentes feitos com intenção.

Arco: começa organizando tudo; aprende a negociar, confiar e descansar. Relações: filha de Helena; afeto franco com Marta; admiração impaciente por Tião; amizade com Luna; confiança profissional em Celina. Sua relação com o jogador nunca substitui as demais.

Rotina base: 7h varanda; 8h–11h viveiro; 11h–12h praça; 12h refeição; 13h–17h tarefas próprias ou combinadas; 18h retorno; 19h varanda; 21h descanso. Em acompanhamento, reserva uma tarefa própria para outro horário sem desaparecer nem bloquear missões.

Falas de voz: “Essa muda parece parada. Está criando raiz.” / “Você pode dizer que não sabe. Eu também estou aprendendo.” / “O Bento enterrou minha luva. Tecnicamente, ele começou a plantação.”

Romance opcional: adultos, desbloqueado por conversa explícita após confiança suficiente. Opção “Quero nossa parceria como ela é” preserva todas as funções e cenas centrais. Não usar ciúme punitivo, casamento obrigatório ou abandono. Rainara permanece depois dos créditos.

### Dona Marta — 58 anos — comerciante

Visual: coque grisalho, óculos pequenos, blusa coral e avental vinho com bolsos. Corpo arredondado e postura firme. Mora sobre o armazém. Desejo: manter o lugar onde todos se encontram. Medo: admitir que já não consegue sustentar o armazém sozinha. Guarda cadernetas de crédito e receitas, não segredos malignos.

Arco: transforma favores silenciosos em acordos claros da comunidade. Voz: objetiva, carinhosa sem infantilizar. “Desconto eu calculo. Amizade a gente conversa.” / “Sopa boa precisa de tempo. Gente também.” Prefere nabo, sopa e morango; não aprecia pedra como presente. 8h–18h loja; intervalo 12h–13h com caixa de retirada funcional; 19h jantar; 21h casa. Missão pessoal: Livro de fiados; recompensa: receita de pão de milho e prateleira decorativa.

### Tião — 63 anos — pescador e conhecedor da água

Visual: pele morena, bigode grisalho, chapéu de palha, camisa azul, calça oliva, vara. Desejo: voltar a ser útil sem precisar explicar o que fez. Defeito: responde com provérbios quando deveria responder diretamente. Medo: que reconhecer um erro apague tudo o que ajudou a construir.

Arco: relata a emergência inteira e participa da reparação. “Água não esquece o caminho. A gente é que tapa.” / “Hoje eu vim conversar. Os peixes podem esperar.” Gosta de peixe assado; desgosta de abóbora crua como presente. 7h–11h lago grande; 12h refeição; 14h canal; 17h ponte; 20h casa. Na chuva forte, prepara linhas na varanda. Missão pessoal: Banco da margem; recompensa: receita de isca simples e banco.

### Luna — 23 anos — desenhista e cronista

Visual: pele negra, cabelo curto cacheado, jardineira lavanda, blusa creme, caderno e pequena flor amarela. Desejo: estudar ilustração e mostrar o vale ao mundo. Medo: ser acusada de abandonar quem ama. Defeito: transforma conversas em projetos antes de perguntar se pode registrá-las.

Arco: prepara uma exposição com consentimento dos moradores e escolhe uma temporada de estudo com retornos regulares. Isso não a remove permanentemente do jogo. “Posso desenhar? Tem coisa que só aparece quando a gente para.” / “Ir embora por um tempo não é apagar o caminho de volta.” Gosta de torta e abóbora. 9h praça; 11h bosque; 14h atelier; 17h ponte; 21h casa. Missão pessoal: Retratos com licença; recompensa: retratos decorativos e página ilustrada do diário.

### Celina — 37 anos — veterinária

Visual: pele negra, tranças presas, colete verde-petróleo, bolsa de cuidados, camisa creme e calça castanha. Desejo: estabelecer uma pequena estação permanente de cuidado animal. Defeito: tenta resolver inseguranças com instruções. Medo: chegar tarde quando alguém precisa de ajuda.

Arco: aprende a ensinar, compartilhar trabalho e aceitar que afeto tem muitas formas. “Primeiro observe. Nem todo silêncio é descanso.” / “Ela já conhece sua voz. Agora aprenda os sinais dela.” Prefere omelete e leite; presentes não substituem cuidados reais. 8h–11h abrigos; 12h praça; 14h–18h estação; 20h casa. Torna-se residente após o abrigo comunitário. Missão pessoal: Plantão dividido; recompensa: escova, cuidados preventivos e espaço de adoção.

### Augusto — 56 anos — carpinteiro

Visual: barba sal e pimenta, camisa xadrez ferrugem, avental cinza, ferramenta no cinto. Desejo: construir algo que os outros possam manter sem depender dele. Defeito: esconde informações quando acha que só ele entende o risco. Medo: um reparo seu falhar.

Arco: entrega a peça guardada e explica a técnica para os demais. “Se só eu consigo consertar, ainda não terminei o serviço.” / “Essa marca torta fui eu. Funciona há vinte anos.” Gosta de pão e queijo; madeira pode ser presente comum, não item amado infinito. 8h–12h oficina; 14h–17h encomendas; 18h praça; 21h casa. Missão pessoal: A cadeira que balança; recompensa: móveis e projeto de ponte.

### Iara — 41 anos — apicultora e cozinheira

Visual: trança longa, blusa mostarda, saia verde, avental creme e véu de apicultura dobrado. Desejo: recuperar a variedade de flores e abrir uma cozinha de encontros. Defeito: faz piada para evitar discussões. Medo: investir de novo onde já perdeu trabalho.

Arco: planta primeiro um canteiro pequeno e volta a confiar no lugar. “Mel de uma flor só conta uma história curta.” / “Prove antes de dizer que não gosta. Vale para conversa também.” Prefere mel e frutas; não gosta de peixe cru. 7h–10h colmeias; 11h–14h cozinha; 16h horta; 19h praça; 21h casa. Missão pessoal: Receita sem medida; recompensa: pão com mel e colmeia.

### Bento, Amora e Helena

Bento: cachorro caramelo, uma orelha caída, lenço azul; curioso e afetuoso, teme trovões. Brinca, dorme, acompanha, encontra objetos já existentes e reage à chegada de Rainara. Não gera itens infinitos. O vínculo abre uma animação de oferecer a pata e uma cena sob a mesa na tempestade.

Amora: gata preta e branca, patas claras; passa a visitar a fazenda após a cozinha ser construída. O jogador pode adotá-la preparando cama, água e alimento. Gosta da janela quente e respeita abrigos dos bichos menores. Não caça os animais do jogador.

Helena: mãe de Rainara, 52 anos, vive fora do vale cuidando da irmã. Participa por cartas em pontos definidos da campanha; não exige arte animada na primeira versão. Seu caderno é técnico e afetivo. Sua voz é franca: “Eu anotei o que soube. O que vocês descobrirem agora também merece uma página.”

## 5. Rainara como sistema jogável

Estados: rotina, acompanhar, esperar, executar tarefa, conversar, participar de cena, descansar. O comando “Vamos juntos?” aparece em interação direta e no caderno depois da abertura. “Pode seguir sua rotina” encerra acompanhamento com confirmação visual, sem punição afetiva. Ela se mantém a 1–2 tiles, contorna obstáculos e não empurra o jogador. Após 3 segundos sem caminho, recalcula; se continuar presa e fora de cena, reposiciona-se em um tile válido próximo, discretamente, sem atravessar uma porta bloqueada.

Tarefas iniciais: regar até 8 tiles acessíveis; alimentar até 3 animais; coletar até 6 produtos prontos; colher até 6 cultivos maduros. Uma tarefa combinada por dia, duas após o evento R03. Usa água/ração da reserva compartilhada visível e deposita produtos num cesto acessível. Se não houver recurso, ela informa e para. Nunca usa itens marcados como reservados para missão, vende produtos ou altera plantações sem autorização.

Tarefas duram no mínimo uma ação animada por alvo; o mesmo alvo fica reservado durante a operação. Jogador pode cancelar. A conclusão gera um recibo no diário: feitos, insumos e pendências. O save guarda tarefa, alvos restantes e itens já transferidos. O efeito de uma ação não pode repetir ao recarregar.

Confiança: 0–100; conversa significativa +2 uma vez ao dia; tarefa compartilhada +3 uma vez ao dia; evento pessoal +8; presente apreciado +2, máximo um por dia. Sem decadência por ausência. Eventos R01/R02/R03/R04/R05 em 10/25/40/60/80, com condições de história descritas no conteúdo. Não exigir esperar vários anos para chegar ao final: campanha concede confiança suficiente. Romance usa uma flag explícita, independente da pontuação.

## 6. Animais e manejo

Os animais são indivíduos. Nome pode ser editado com até 20 caracteres, inserido na UI com textContent. Cada animal tem ID, espécie, variante de cor, temperamento, idade em dias, abrigo, vínculo, saciedade do dia, água, higiene, conforto, estado e produtos armazenados. Limite inicial de 24 animais de criação no mundo ativo, ampliável só após medir desempenho. Pets e colmeias têm contagem separada.

Três temperamentos: tranquilo (aproximação lenta), curioso (investiga objetos seguros) e reservado (demora mais a aceitar carinho). Nenhum reduz permanentemente a rentabilidade; diferenças são de comportamento. Os nomes sugeridos das pranchas são os primeiros indivíduos, renomeáveis.

| Espécie | Primeiro nome | Abrigo | Maturidade de filhote | Produto ou função | Ciclo em dias bem cuidados |
| --- | --- | --- | --- | --- | --- |
| Galinha | Pipoca | Galinheiro | 3 | Ovo | 1 |
| Vaca | Mimosa | Estábulo | 7 | Leite | 1 |
| Cabra | Jujuba | Estábulo | 5 | Leite de cabra | 1 |
| Ovelha | Brisa | Estábulo | 5 | Lã por tosquia | 3 |
| Pato | Pingo | Galinheiro com lago | 4 | Ovo de pato | 2 |
| Porco | Torresmo | Pocilga sombreada | 6 | Composto e raízes comuns | 2; uma busca diária opcional |
| Cavalo | Castanha | Baia | 8 | Montaria | Sem produto periódico |
| Burro | Zé | Baia | 8 | Transporte de carga entre pontos | Sem produto periódico |
| Coelho | Flocos | Coelheira | 3 | Companhia e pelo escovado | 3; sem pés de coelho |
| Abelhas | Colmeia | Apiário | 3 de instalação | Mel | 3, com flores; suspenso no inverno |

Regras são abstrações de jogo, não instruções de criação real. Não há abate, doença fatal ou morte por ausência. Negligência reduz conforto e suspende produção; o jogador recupera a rotina com comida, água, limpeza e descanso. Ausência fora do jogo não avança o calendário.

### Produção e qualidade

Na passagem de dia, avalie o dia encerrado antes de zerar indicadores. Adulto alimentado, com água e abrigo válido acumula 1 dia de ciclo. Carinho melhora vínculo, mas não é requisito absoluto de sobrevivência nem de produção básica. Conforto 0–100: alimentação +40, água +30, abrigo limpo +20, interação respeitada +10. Qualidade boa a partir de 80 e vínculo 30; excelente a partir de 95 e vínculo 70. Preço: base ×1 / ×1,25 / ×1,5, arredondado para baixo.

Cada produção recebe ID composto por animal, dia e sequência. Produtos podem acumular até 3 ciclos; aviso de coleta ao atingir o limite. Nunca apague produtos existentes em migração. Filhotes não produzem. Chuva e frio fazem os bichos buscar abrigo; patos podem nadar quando seguro. A saída do abrigo não requer animação de porta perfeita para calcular cuidado: a simulação deve ser coerente mesmo fora da câmera.

Água de bebedouro tem capacidade por abrigo, consumo diário visível e reposição simples. Ração é comprada ou preparada de milho/trigo; pasto pode cobrir a necessidade dos herbívoros em dia seco, com área suficiente e acesso. Não exigir que jogador alimente dezenas de indivíduos por menus repetidos: cochos e um resumo do abrigo permitem cuidar em grupo.

### Novos bichos e reprodução

Os primeiros exemplares comprados são adultos. Filhotes são opcionais, desbloqueados por Celina depois de um abrigo melhorado. Galinhas/patos: incubação de ovos férteis comprados, 3 dias. Mamíferos: serviço de reprodução solicitado a Celina para adulto com vínculo 50, abrigo limpo e vaga reservada; 5 dias para o nascimento. Modelo abstrato sem genética ou sexo obrigatório na UI. Um pedido por abrigo por vez. Cancelar devolve apenas recursos não consumidos, conforme aviso prévio. A espécie do filhote é fixa e não há sorteio frustrante.

### Primeiras histórias animais

Pipoca prefere o canto da cerca; construir o ninho resolve ovos fora do lugar e abre uma cena engraçada com Rainara. Mimosa se assusta com o martelo de Augusto; combinar o horário do reparo cria confiança. Jujuba sobe num caixote; oferecer um ponto seguro para escalar encerra a fuga. Brisa reconhece o som da escova; escovar três dias diferentes libera uma pose de aproximação. Pingo segue Bento até a água; uma rampa permite retornar. Amora escolhe a cadeira do jogador; a cama junto à janela oferece uma alternativa. Nenhuma dessas cenas destrói itens ou pune afeto.

## 7. Economia, construções e receitas

Preserve preços existentes na migração; estes valores são ponto inicial para itens novos e precisam de playtest. A primeira galinha e um pacote de ração são recompensa da campanha após construir abrigo, sem exigir compra de outro animal para avançar. Missões principais aceitam peixes de qualquer espécie quando a identidade não importa.

| Produto novo | Venda base G | Destino |
| --- | --- | --- |
| Leite de cabra | 42 | Queijo e cozinha |
| Lã | 65 | Tecelagem e venda |
| Ovo de pato | 45 | Cozinha |
| Composto | 18 | Solo ou venda |
| Pelo escovado | 35 | Almofada e artesanato |
| Mel | 70 | Pão com mel e presentes |
| Queijo | 95 | Mesa compartilhada e venda |
| Queijo de cabra | 110 | Receitas e presentes |

| Construção nova | Custo inicial | Capacidade e condição |
| --- | --- | --- |
| Ampliação do galinheiro | 240 G, 20 madeira, 12 pedra | 6 aves; mantém as existentes |
| Ampliação do estábulo | 500 G, 35 madeira, 25 pedra | 6 animais; mantém os existentes |
| Lago de patos | 120 G, 10 pedra | Ligado ao galinheiro; saída caminhável |
| Pocilga | 350 G, 25 madeira, 15 pedra | 3 porcos; sombra e lama |
| Baia | 600 G, 40 madeira, 20 pedra | 2 montarias |
| Coelheira | 180 G, 15 madeira, 5 pedra | 4 coelhos |
| Apiário | 200 G, 12 madeira | 2 caixas; exige flores próximas |
| Queijeira | 180 G, 12 madeira, 8 pedra | Uma unidade por ciclo |
| Tear | 220 G, 20 madeira | 2 lãs para 1 tecido |

Receitas novas: queijo = 2 leites, 1 dia; queijo de cabra = 2 leites de cabra, 1 dia; pão de milho = 2 milhos + 1 trigo, instantâneo; pão com mel = 1 pão de milho + 1 mel; ensopado da serra = 1 cenoura + 1 abóbora + 1 queijo; chá do viveiro = 2 ervas coletadas. Preservar sopa, peixe assado, torta e omelete existentes.

Benefícios: chá reduz pela metade o tempo de recuperação das ferramentas durante 120 minutos de jogo, sem dobrar produção animal; pão com mel amplia janela de pesca como o benefício existente; ensopado prolonga corrida, sem empilhar multiplicadores. Efeitos do mesmo tipo renovam duração até um teto; não acumulam potência.

Itens narrativos ficam numa bolsa de história não vendável e não ocupam espaço de inventário. Materiais de reparo são comuns; sempre existe alternativa de compra ou coleta renovável. Recursos de missão não dependem de sorte rara. Culturas fora de época podem ser substituídas nas missões principais por produto comum equivalente, explicitado antes de aceitar.

## 8. Mapa, regiões e desbloqueios

Fazenda: preservar layout inicial; casa, viveiro, abrigos, pomar opcional e varanda. Praça: armazém, oficina, estação de Celina, cozinha de Iara, atelier de Luna e quadro comunitário. Bosque: ervas, flores, ponte antiga e caminho de Bento. Alto: fonte, comporta, zona úmida e mirante. Interiores compactos: casa do jogador e estabelecimentos necessários; casas secundárias podem inicialmente usar transição de dormir e diálogos na porta sem fingir interior acessível.

Cada acesso mostra nome e destino. Ao voltar, há tile de chegada livre e posição segura de Rainara. Missões não podem colocar cercas em portais. Mudanças de história alteram objetos de regiões sem destruir construções do jogador. Novos terrenos são adicionados em bordas reservadas ou regiões novas; nunca reconstruir o mapa antigo por um novo gerador sobre o save.

## 9. Festivais e pós-jogo

Calendário recorrente: dia 10 da primavera, Feira das Mudas; dia 10 do verão, Noite das Lanternas; dia 10 do outono, Mesa da Colheita; dia 10 do inverno, Varanda Acesa. Aviso com 2 dias de antecedência. A participação pode ser adiada para o ano seguinte sem perder história. O Festival das Duas Águas é a conclusão principal, acionada separadamente quando o jogador confirma.

Feira: trocar uma muda comum por uma cor decorativa, mostrar o viveiro e conversar com Rainara. Lanternas: passeio com percurso acessível e música, sem soltar objetos poluentes no mundo. Colheita: mesa com contribuição de qualquer alimento cultivado ou comprado, avaliação por variedade sem humilhar o jogador. Inverno: troca opcional de presentes com lista de preferências conhecida, leitura de cartas e bebida quente.

Pós-jogo: construir o projeto não escolhido no final; completar coleção de peixes; desenvolver todas as espécies; decorar casa; exposição de Luna; feira semanal e cenas da varanda. Rainara mantém rotina e acompanhamento. A água restaurada não pode voltar a secar por um relógio oculto. A manutenção recorrente é opcional e recompensa decoração, não ameaça desfazer o final.

## 10. Interface, acessibilidade e som

Diário com abas Hoje, História, Pessoas, Animais, Coleções e Configurações. A aba Hoje mostra no máximo três objetivos acompanhados, próximo passo e local. Evitar lista de todos os personagens sobre o mapa. Interações têm verbo e alvo; a proximidade não pode escolher o NPC errado atrás de um animal.

Texto configurável, contraste alto opcional, ritmo de texto ajustável, avanço e histórico de falas, pausa em menus/cenas, volume de música/efeitos, vibração opcional somente se suportada, sem depender de áudio ou cor para objetivos. Modo tranquilo: relógio em 50%, 75% ou 100% da velocidade base; pesca 0,9/1,3/1,8 segundos. Tutorial demonstra e deixa repetir.

Som original: tema da varanda com notas espaçadas, tema do viveiro com motivo ascendente de três notas, praça com percussão discreta, fonte com água e textura suave. Criar motivos próprios; não reproduzir melodias de referências. Se tudo continuar procedural, usar WebAudio com envelopes suaves e limite de vozes. Áudio inicia após gesto do usuário, pausa ao ocultar página e respeita mute.

## 11. Escopo e término

Este pacote contém conteúdo narrativo e direção visual completos para a campanha proposta. As pranchas anexas são arte conceitual; o desenvolvimento ainda precisa preparar sprites e implementar, integrar e testar os sistemas. A campanha não está implementada por existir este documento.

O jogo estará concluído para esta versão quando for possível começar em save novo, conhecer Rainara, completar os cinco movimentos da história, jogar o epílogo e continuar a fazenda; migrar um save existente sem perda; usar cada espécie, receita, personagem, cena e interação exigida; manter teclado/toque e ausência de erros bloqueadores. Desempenho deve ser medido, não presumido.

Não entram nesta versão: multiplayer, APK, loja de dinheiro real, servidor, mapa infinito, combate complexo, geração de diálogos por API ou dezenas de NPCs adicionais. A identidade vem da profundidade do elenco e da resposta do mundo.

## 12. Referências consultadas e autoria

Consulta em 12/10/2026: https://www.stardewvalley.net/about/ — integração entre fazenda, progressão e comunidade; https://thunderlotusgames.com/games/spiritfarer/ — cuidado e convivência como narrativa; https://rootsofpacha.com/ — descobertas e construção comunitária. São referências de princípios de design. Não usar nomes, diálogos, música, sprites ou mapas desses jogos.

A direção visual segue as duas referências de pixel art enviadas pelo usuário e a proposta gerada para protagonista/Rainara. Este pacote contém novas artes conceituais, não os screenshots de plataformas externas. O enredo das Duas Águas, suas falas e missões foram escritos para Vale a Dois. Não atribuir às fontes a autoria dessas criações.
