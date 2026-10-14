# Progresso — Vale a Dois / Duas Águas

Base: main 0fd172d, index.html de 68.934 bytes; sem alterações locais. Branch: feature/duas-aguas.

## Direção adotada

Pedido atual e pacote ZIP orientam implementação e arte. DOCX complementa a referência visual; sugestões antigas de engine, coop online, nomes de pets e lore mágico não substituem a campanha canônica das Duas Águas. As cinco pranchas são conceitos, não sprites ou animações prontas.

## Marcos

- M0 em execução: preservar mapa de 80×60/tiles de 16, inventário, saves, recursos, construções, animais e missões locais. Fontes HTML separadas e build Python geram distribuição autocontida.
- M1–M7 pendentes. A implementação existente de fazenda continua sendo a base.

## Reprodução

`python3 tools/build.py` gera index.html de src/game.html e assets/dados locais. Servir com `python3 -m http.server 8000 --bind 127.0.0.1`.

## Próximo passo

Adicionar migração versionada com IDs de moradores e backup, exportação/importação validada e teste de regressão antes de iniciar Q01–Q05.

## M0 concluído

- Pacote lido integralmente, cinco pranchas inspecionadas e base atual comparada com o SHA remoto.
- Chave vale-a-dois-v2 e migração de vale-a-dois-v1/vd2; backup recuperável antes da migração. Moradores persistem por marta/tiao/luna. Nomes de animais são preservados e tratados como texto literal.
- Exportação JSON e importação com validação, prévia do dia/nome, confirmação e backup. Armazenamento indisponível e saves inválidos não são sobrescritos.
- Teste real: `node tests/m0.cjs` no Chromium headless, aprovado para legado com galinha/vaca, recursos removidos/cultivos, estoque, missões, amizade, backup, exportação, importação inválida, nome com HTML e falhas de leitura/gravação.
- Fonte: src/game.html. Distribuição: index.html, gerada por `python3 tools/build.py`.
- Próximo passo: preparar atlases da dupla e implementar Q01–Q05, companhia e ritual da varanda.

## M1 concluído

- Atlases raster autorais: células humanas 32×48 com gutters, quatro direções, estados de movimento/ações; retratos 96×96 com seis expressões. Pixel art feita por autoria de pixels em tools/make_art.py, sem recortar as pranchas. PNGs e coordenadas explícitas ficam em assets; o build incorpora apenas assets finais.
- Dupla e moradores originais usam sprites novos. Rainara: cabelo ondulado longo, coral/terracota, bolsa oliva e folha assimétrica. Protagonista: cabelo preto, jaqueta creme, calça grafite. Olhos e silhuetas adaptados à resolução do mapa.
- Q01–Q05 jogáveis: nome/motivo, mala, três plantios regados, entrega sazonal com equivalência de legado, galinheiro/bebedouro/Pipoca e três ações na marca do canal. Falas canônicas, escolhas reais, retomada e releitura sem recompensas duplicadas.
- Rainara acompanha/espera/segue rotina, entra/sai da casa e contorna ocupação temporária do jogador. Tarefas de rega/alimentação/coleta/colheita têm reserva, insumos reais, cancelamento, pausa e cesto. Varanda funciona com conversa gratuita ou consumo real de refeição.
- Ferramentas aplicam efeitos no frame de contato. Colheita também é animada e respeita reservas.
- Testes: `node tests/m1.cjs` aprovado em desktop 1280×720 e toque 360×800. Verificados Q01–Q05, cena interrompida, pagamento único, replay, tarefa sem água, retomada após reload, colheita e cesto sem duplicação.
- Arte já funcional, ainda a aprimorar no M6: pets/animais/ambientes e cobertura visual das cenas. O pacote inteiro não está concluído.
- Próximo passo: M2 — Praça e estabelecimentos, Celina/Augusto/Iara, Q06–Q13, viveiro e diário ampliado.

## M2 concluído

- Praça, Bosque e acesso ao Alto têm regiões próprias com grids, portais, caches de terreno e spawns seguros; fazenda antiga permanece intacta. Mudanças de estação/ponte invalidam só caches relevantes.
- Celina, Augusto e Iara têm sprites, retratos, rotina, interações e IDs persistentes. Moradores originais seguem acessíveis e mantêm amizade e tarefas locais. Armazém da fazenda funciona como retirada.
- Q06–Q13 implementadas com condições tipadas: marcas do lago, conversa com Tião, materiais/ponte realmente transitável, água/escova da vaca comunitária, relatos autorizados, três mudas, peça na bolsa de história, bancada construída/rega compartilhada e carta de Helena.
- Diário organiza objetivos, pessoas, história relida e coleções. Fontes renováveis de materiais e compra de vegetais/comidas mantêm a progressão disponível.
- Teste `node tests/m2.cjs` passou em desktop e toque: encadeamento Q06–Q13, região/companhia após reload, ponte, viveiro, objetos narrativos, diálogo correto e preservação do solo da fazenda.
- Próximo: M3 — três marcos no Alto, habitat, reunião, escolhas e quadro de tarefas (Q14–Q18).

## M3 concluído

- Q14–Q18: Rainara acompanha o Alto, três marcos e três observações do habitat ficam registrados, Tião/Augusto se reúnem na ponte e retornam às rotinas, Q17 oferece três escolhas e Q18 confirma as frentes do plano.
- Pontos narrativos e tarefas públicas não afetam solo/inventário da fazenda por coincidência de coordenadas. Pets/portas/animais e cercas de outra região não podem ser acionados invisivelmente.
- Testes `node tests/m3.cjs`: measure/group/listen em viewport 800×360 com toque; todas as escolhas preservam parceria, abrem Q18 e persistem após reload. Companheira atravessa portais, habitat não é removido, NPCs deixam a cena e volta ao controle é segura.
- Próximo: M4 — doações parciais, teste gradual da comporta, projeto escolhido, restauro, festival, epílogo/créditos e pós-jogo.

## M4 concluído

- Q19–Q24 jogáveis: materiais e comidas doados parcialmente, três mudas, abertura em 1/3, observação/fechamento/filtro, projeto único, fluxo gradual definitivo e visita à confluência.
- Q21 exige escolha real mesmo ao pular falas. Só um projeto é gratuito; P01 cobra pelo outro. Pomar tem colheita diária e sombra é um projeto permanente para os cuidados.
- Festival acionado pelo jogador, com alimento consumido; epílogo com parceria/amizade, créditos puláveis, um único avanço de dia e Rainara permanente. Falas podem ser relidas sem pagar de novo.
- Pós-jogo P01–P04 possui construção, exposição condicionada ao consentimento, contribuições de três categorias/feira semanal e passeio condicionado ao evento R05 (eventos completos entram no M7).
- `node tests/m4.cjs`: orchard e shade aprovados em toque 360×800, incluindo doação parcial/reload, checkpoint seguro, escolha obrigatória, único projeto grátis, final, créditos e pós-jogo sem duplicação.
- Visual/áudio final do canal, cenas e retratos decorativos serão completados no acabamento M6/M7; não são substituídos por afirmações de prontidão total.
- Próximo: M5 — dez espécies, água/limpeza/conforto, qualidade e IDs de produção, filhotes, montaria, transporte, pets, processamento e receitas.

### M5 — criação ampliada
Implementadas dez espécies com indivíduos persistentes, cuidados em grupo, estoques com IDs únicos, conforto/qualidade, ferramentas, filhotes e vagas reservadas. Cavalo usa colisão exterior e desmontagem segura; burro move até 12 itens entre baia/cesto, com entrega única após reload. Queijeira, tear, composto, flores e novas receitas funcionam com consumo real. Save legado mantém estoques acima do limite novo sem apagá-los.
Verificação: `node tests/m5.cjs` passou: dez funções/ciclos, qualidade, reload, filhote, montaria, transporte e processamento. Regressões M0–M4 passaram, incluindo nomes literais e backup. A adoção de Amora se conclui no evento B06, implementado no M7.

### M6 — cobertura visual
Atlas próprios para oito humanos, retratos/expressões, dez espécies/filhotes, Bento/Amora, prédios, móveis, plantas e objetos. Autoria de pixels em scripts reproduzíveis, sem recortes das pranchas conceituais. Cabelo, roupas e acessórios por direção; ações com contato, boca nas falas e caminhada ligada ao deslocamento real. Ambientes da praça/bosque/alto, canal seco/turvo/restaurado e habitat preservado. Sprites raster embutidos no HTML; nenhuma solicitação externa em execução.
Verificação: `node tests/m6.cjs` passou com 4.289 frames válidos, 42,52 MiB estimados de atlas/caches/canvases; capturas das quatro regiões e interior revisadas em Chromium desktop. HTML 1,24 MB, abaixo do orçamento. Regressões M0–M5 passaram após integração visual. Acabamento de áudio, interface, eventos e festivais segue no M7.

## M7 concluído — narrativa pessoal, festivais e acabamento

- Os 17 eventos R01–R05, M01, T01, L01, C01, A01, I01 e B01–B06 são disparados por condições verificáveis e consumos/ações reais; progresso e recompensas são salvos uma única vez. Amizade e romance permanecem escolhas distintas, com consentimento explícito; o diário relê eventos sem repetir recompensas. B06 conclui a adoção de Amora.
- F01–F04 agora são festivais anuais funcionais, com troca de sementes, trajeto de lanternas, concurso culinário e janela de cartas. A progressão da ponte, gastos, horários e reload são respeitados.
- Opções persistentes de relógio, janela de pesca, escala de texto, ritmo de diálogo, alto contraste, volume e mudo; pausa quando a aba fica oculta, navegação de menu por teclado, caminho acessível, retratos, transições e efeitos/sons procedurais sem downloads externos.
- Integridade adicional: limite global de 24 animais novos, espaços para bichos grandes, recibos limitados e entregas de carga protegidas contra repetição; pontos públicos, cenas e habitat não permitem alterar a fazenda por coordenadas sobrepostas. Telhas raster autorais cobrem quatro estações, caminhos, solos, água animada e interiores; efeitos de chuva, neve, folhas, passos, colheita, água e corações usam o atlas pixelado.
- Build atual: `python3 tools/build.py`; `index.html` autocontido com 2.058.687 bytes. Atlas e caches estimados pelo teste visual: 59,07 MiB, 7.686 frames. Os PNGs são fontes locais reproduzíveis via `python3 tools/build_art.py`.

### Verificação final

- `node tests/m0.cjs` a `node tests/m7.cjs`, `node tests/campaign.cjs`, `node tests/economy.cjs` e `node tests/performance.cjs`: aprovados. A campanha completa foi iniciada sem progresso injetado, concluiu as 24 missões, eventos de Rainara/Luna e os quatro arcos pós-jogo. Testes exercitam amizade/romance, pausa, configurações, recarga e os festivais anuais.
- Chromium headless, sem solicitações remotas: 1280×720 a 59,998 FPS (p95 16,7 ms), 360×800 a 60,318 FPS (p95 16,8 ms, simulação CPU ×4) e 800×360 a 60,183 FPS (p95 16,7 ms, CPU ×4), com 24 animais e pico de 8 vozes. Isso mede o navegador simulado; não substitui teste em aparelho físico.
- Cenários econômicos de 14 dias construíram o primeiro abrigo nos três perfis: cultivo no dia 4, pesca e criação no dia 1. O cenário maximiza uma atividade de cada vez; os saldos não são comparação de esforço equivalente.
- Servidor local de teste continuou ativo em `127.0.0.1:8000`.


## M8 implementado — controles profissionais desktop/mobile

- Criado `GameInput`, uma camada única de entrada que desacopla gameplay de teclado e touchscreen e já expõe pacote futuro `{moveX, moveY, run, action, tool}` para o multiplayer LAN.
- Desktop: WASD + setas preservados, ação/ferramenta separadas, inventário, caderno e mapa por teclado, corrida em modo segurar/alternar, remapeamento com detecção de conflito e restauração dos padrões.
- Mobile: joystick analógico 360° como padrão, D-pad opcional, joystick fixo/flutuante, zona morta, sensibilidade, tamanhos, opacidade, modo canhoto, feedback visual, vibração opcional e multitouch para andar + correr/ação/ferramenta.
- Layout mobile respeita safe areas e prioriza paisagem com aviso em retrato; a barra de itens original e todo o visual M0–M7 foram preservados.
- Preferências de controle usam `vale-a-dois-controls-v1` no `localStorage`, separadas do save da fazenda.
- Adicionado `tests/m8.cjs` para regressão de remapeamento, velocidade diagonal, joystick, multitouch, corrida, reset após perda de foco e formato do pacote de input.
- Limitação desta execução: o código e o teste tiveram sintaxe validada, mas não houve teste em aparelho Android físico. O teste Playwright deve ser executado no ambiente do projeto com Chromium/Playwright disponíveis.


## M9 em andamento — HTML canônico, lacunas, LAN e Android

- O HTML anexado tem o jogo M7 como prefixo idêntico e mais 52 linhas de apresentação. A `main` também já continha M8. A camada nova está em `src/95-canonical-visual.js` e o build a incorpora depois de M8, preservando a versão oficial mais recente. Em tela horizontal compacta, pós-processamento de tela inteira é reduzido para manter o controle responsivo; casas, fonte, sprites, partículas sazonais e mapas continuam renderizados.
- Gaps já existentes: retratos de cenas, ícones, festivais F01–F04, pós-jogo P01–P04, dez espécies, crescimento, qualidade animal, queijeira/tear/apiário, upgrades básicos. Novo módulo `src/85-gap-features.js`: calendário/aniversários, presentes com reação, avatar visível em três aparências, qualidade prata/ouro de colheita, ferramentas níveis 0–2, sorte diária, relíquias/arquivo, eventos de surpresa, feno e segunda reforma da casa/abrigo com prazo.
- Coop LAN em `src/92-lan.js`: dois jogadores, host único de save, inventários separados e dinheiro conjunto; WebSocket local, entrada por IP, descoberta Android por NSD, heartbeat e reconexão. Dev relay permite testes de duas instâncias no navegador. O plugin nativo Android hospeda o WebSocket sem serviço externo.
- Projeto Capacitor Android criado com package `com.valeadois.app`, orientação horizontal, fullscreen, ícone autoral da dupla e workflow para APK debug. Teste físico em dois aparelhos ainda necessário.

- Duas áreas opcionais de exploração foram adicionadas: Clareira das Flores e Pedreira Antiga. Auditoria detalhada: `AUDITORIA_GAPS.md`.
- Regressões locais M0–M8, campaign, economy, gaps e LAN passaram. Chromium headless com 24 animais mediu ~60 FPS desktop e retrato, ~59 FPS horizontal com CPU ×4 antes dos últimos efeitos leves; não substitui aparelho físico.
