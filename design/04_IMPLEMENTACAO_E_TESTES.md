# Implementação incremental e critérios de conclusão

## Base observada

Em 12/10/2026 foi consultada a main do repositório VALE-2 no commit `0fd172de6262c45062bc81babc3c1940ae42fb04`. A árvore continha `index.html` com 68.934 bytes. A inspeção do código encontrou estações de 14 dias, oito culturas, sete peixes, casa, receitas, baú, construções, animais de dois tipos, presentes, rotinas e salvamento. Essa observação não certifica que todos os recursos passaram por teste de navegador. Inspecionar a versão atual antes de implementar; não fazer reset para esse commit.

## Arquitetura compatível

Distribuição final: um HTML autocontido. Na árvore de desenvolvimento podem existir documentação, fontes PNG, dados JSON e scripts de empacotamento. O build incorpora dados e atlases no HTML, sem fetch, CDN, módulos externos ou serviços de tempo de execução. Manter uma cópia reprodutível das fontes é preferível a editar strings base64 manualmente.

Manter o estilo do jogo: estado global pequeno, funções explícitas, render pelo Canvas, mapas offscreen e y-sort. Acrescentar seções: CONTENT, STORY, COMPANION, REGIONS, ANIMALS, ASSETS, SAVE e UI. Não introduzir ECS, engine nova, framework ou backend para atender esta especificação.

Dados do pacote são especificações. Não despejar os diálogos JSON no HTML sem implementar o encadeamento. Traduzir objetivos em tipos permitidos: inspect, talk, deliver, build, plant, water, care, visit, choose e sceneComplete. Implementar validadores por tipo; nunca eval. Condições compostas usam all/any explícitos.

Cada evento do jogo emite um fato com identificador único: harvest, careAnimal, build, enterRegion, inspect, choose, deliver. O sistema de missão atualiza contadores relevantes. Distinguir objetivos que verificam estado atual (ter galinheiro), histórico (cuidou 3 dias) e entrega (consumir itens). Não concluir entrega só porque um item esteve na bolsa em algum momento.

Campos novos sugeridos:

```
story = { completed: [], active: [], counters: {}, choices: {}, flags: {},
          storyItems: [], rewarded: [], scene: null, memories: [] }
companion = { id: 'rainara', state: 'routine', trust: 0,
              relationship: 'friendship', task: null, daily: {} }
world = { region: 'farm', regions: {}, projects: {}, festivalEditions: [] }
```

Os nomes são proposta de implementação, não formato já presente no save. Agrupar todas as mutações relacionadas em uma operação antes de salvar: debitar, conceder, registrar recompensa e concluir objetivo. Q20 pode retomar no último checkpoint seguro com comporta fechada. Recompensas não se repetem após load, reler cena ou entrar novamente na região.

## Migração e persistência

Ler o código atual para descobrir chave e versão reais. A origem histórica é `vd2`, mas não assumir que a versão atual ainda usa exatamente esse formato. Guardar backup recuperável antes da migração; preservar inventário, árvores removidas, pedras, solo, cultivos, estações, horários, receitas, casa, construções, animais e relações. Tratar indisponibilidade de armazenamento com aviso persistente discreto e permitir jogar sem afirmar sucesso de save.

Converter NPCs de índices para IDs estáveis (`marta`, `tiao`, `luna`) sem trocar amizade entre pessoas. Novos personagens recebem valores iniciais; Rainara não ocupa um índice antes usado por Tião. Espécies legadas `chicken` e `cow` preservam abrigo, nome, cuidados e estoque; o formato observado reconstruía nomes padrão no load, portanto a migração deve tornar nomes personalizados persistentes.

Legado de missões: ao reconhecer a primeira entrega de Marta já concluída, permitir Q03 sem novo consumo nem novo pagamento. As outras missões antigas continuam como tarefas locais ou ganham equivalência explícita; não zerar `questStage`. Introdução em save avançado não remove recursos para recriar sensação de começo. Mostrar “Uma nova história chegou ao vale” e oferecer a cena Q01 em posição segura.

Saves só avançam dias quando o jogo avança, nunca pelo relógio real. Um dia passa exatamente uma vez ao dormir, desmaiar ou terminar festival conforme regra. Avaliar produção com os cuidados do dia encerrado, criar IDs de produto, então limpar flags diárias e incrementar o dia. Evitar avaliar o dia novo e perder alimentação feita na véspera.

Adicionar exportação/importação de save em JSON como proteção útil: validar versão, limites e chaves; pedir confirmação para substituir o save atual após mostrar data/ano; manter backup. Não executar conteúdo importado, não permitir HTML em nome de animal e limitar tamanhos para evitar travamento.

## Regiões, companheira e animais

Mapa da fazenda atual permanece. Novas regiões usam IDs, portais e spawn seguro. Navegação separa terreno transitável, obstáculos fixos, construções e ocupação temporária. Caminhos recalculam quando portão muda ou uma construção surge; planejar só quando necessário, com orçamento por frame. Entidades fora da tela usam atualização reduzida. NPCs podem simular rotina por destinos e horários sem calcular centenas de passos invisíveis.

Rainara observa o mesmo mapa de colisão. Comandos possuem feedback e cancelamento. Ao iniciar cena, guardar estados e locais de retorno. Ao sair, devolver entidades à rotina sem sobrepor ao jogador. Tarefas usam reserva de alvo, validação dos insumos e efeito no frame de contato. Cancelar ou mudar de região não duplica itens.

Cavalo: montar apenas no exterior, velocidade máxima 1,4 vezes corrida sem buff, mesma malha de navegação e acesso bloqueado a interiores. Desmontar exige tile livre; salvar montaria e estado de montagem. Burro: primeiro implementar transporte entre baia e cesto da fazenda com capacidade fixa de 12 unidades, sem inventário perdido ao interromper. Expansão de inventário genérica não substitui essa função sem informar o ajuste.

## Desempenho e limites de conteúdo

Metas de desenvolvimento, a medir: 60 fps em desktop de teste; pelo menos 30 fps sustentados no celular alvo, quando houver aparelho para testar. Relatar resultados reais, viewport e ambiente. Simulação não deve depender da taxa de frames. Usar requestAnimationFrame, dt limitado e pausa em document.hidden.

Carregar e decodificar cada atlas uma vez. Não desenhar imagens gigantes redimensionadas por entidade a cada frame. HTML final alvo de até aproximadamente 15 MB; soma aproximada de buffers de imagem alvo de 64 MiB. Esses valores são orçamentos propostos, não características garantidas. Medir dimensões × 4 bytes, incluindo caches, e reduzir atlas ou variar carregamento antes de aumentar limites. Base64 adiciona tamanho ao arquivo; pranchas conceituais não entram no runtime.

Cache de terreno por região/estação; mudanças localizadas invalidam apenas o necessário. Limites iniciais: 24 animais de criação ativos, 2 pets, 120 partículas simultâneas e 8 vozes de som. Não usar efeitos de sombra pesada em toda entidade. Menus só atualizam ao mudar dados. UI não deve reconstruir strings enormes todo frame.

## Marcos de produção

| Marco | Entrega funcional | Aceite |
| --- | --- | --- |
| M0 Base e segurança de evolução | Inspeção, branch, inventário do que existe, migração testável, save de regressão | Jogo antigo continua iniciando; dados existentes preservados |
| M1 Abertura completa | Rainara/protagonista em arte nova, Q01–Q05, acompanhamento, varanda, Pipoca | Novo jogador entende controles e conclui abertura; reload preserva tudo |
| M2 Comunidade | Praça, três novos moradores, Q06–Q13, retratos, diário e viveiro | Missões encadeadas com rotina e diálogo; nenhum portão inacessível |
| M3 Revelação | Bosque/Alto, Q14–Q18, decisões, confiança e eventos de Rainara | Nenhuma escolha trava a campanha; companheira acompanha regiões |
| M4 Final da campanha | Q19–Q24, comporta, festival e pós-jogo | Final completo testado; Rainara permanece; história pode ser relida |
| M5 Criação ampliada | Todas as dez espécies, pets, filhotes, receitas e construções definidas | Cada espécie tem função e ciclo testados; sem duplicação de produto |
| M6 Arte e animação completas | Elenco, bichos, ambientes, objetos, estados e efeitos do catálogo | Silhuetas próprias, atlas válidos, escala e colisão coerentes |
| M7 Acabamento | Eventos pessoais, festivais, acessibilidade, áudio, ajustes econômicos | Checklist completo, console limpo, desempenho medido |

Arte entra desde M1; M6 completa a cobertura, não é a primeira vez que personagens deixam de ser placeholders. M5 pode ocorrer depois de M2 se facilitar recursos de eventos, mas a campanha não fica bloqueada por uma espécie ainda não liberada. M4 inclui o pós-jogo narrativo; equipamentos de produção são finalizados até M7.

## Casos de teste necessários

| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| T01 | Abrir save novo | Introdução funcional, controles, recursos e Rainara disponíveis |
| T02 | Abrir save legado com galinhas/vacas | Nenhum item/animal/edifício perdido, novas flags inicializadas |
| T03 | Salvar durante entrega | Consumo e recompensa ocorrem uma única vez |
| T04 | Recarregar em cena | Retomada segura; escolhas respondidas não mudam |
| T05 | Pular Q24 | Final registrado, manhã seguinte jogável, sem repetir créditos |
| T06 | Escolher amizade em R04 | Final completo e Rainara permanente |
| T07 | Romance explícito | Falas opcionais corretas, sem vantagens obrigatórias |
| T08 | Cercar caminho de Rainara | Replanejamento ou reposicionamento seguro; sem bloqueio permanente |
| T09 | Acabar ração em tarefa | Trabalho pausa, recibo correto, sem recurso negativo |
| T10 | Jogador colhe alvo reservado | Um único beneficiário recebe item; tarefa se ajusta |
| T11 | Virar dia com produção pronta | Um ciclo máximo por passagem; produtos antigos preservados |
| T12 | Recarregar após coleta | Produto não reaparece; inventário preservado |
| T13 | Trocar estação no meio da missão | Alternativas mantêm campanha possível; dormência preservada |
| T14 | Sair do jogo por vários dias reais | Animais e cultivos não degradam offline |
| T15 | Novo filhote com abrigo cheio | Vaga reservada impede exceder capacidade |
| T16 | Montar/desmontar perto de obstáculo | Sem atravessar parede ou ficar preso |
| T17 | Entrar/sair de interior com Rainara | Posições e estados válidos; sem teleporte para dentro da parede |
| T18 | Falha/quota de localStorage | Aviso verdadeiro, jogo continua; exportação oferecida |
| T19 | Save inválido importado | Rejeição explicada, save válido preservado |
| T20 | Nome com caracteres HTML | Texto literal; nenhuma execução ou alteração de UI |
| T21 | Celular retrato e paisagem | Toque, safe areas, menus e botões utilizáveis |
| T22 | Mudar aba durante pesca/cena | Pausa; sem perder peixe por tempo fora da tela |
| T23 | Fazer Q21 duas vezes | Só um projeto inicial gratuito; outro desbloqueável |
| T24 | Festival sobre evento pessoal | Prioridade previsível; nenhum evento perdido |
| T25 | Construir em saída/portal | Ação impedida com motivo, recursos não consumidos |
| T26 | Desempenho com limite de bichos | Medição e ausência de alocação crescente por frame |
| T27 | Mute e modo tranquilo | Persistem e funcionam sem prejudicar progressão |
| T28 | Completar todas as missões | Todas as recompensas existem; nenhum placeholder ou ID órfão |

Verificação visual: revisar cada direção de cada personagem, alpha, âncora dos pés, frames, expressão, fonte e z-order. Verificação econômica: simular três perfis — plantar, pescar, criar — por 14 dias de jogo e conferir acesso à primeira construção; ajustar números com justificativa. Não prometer uma duração de campanha em horas antes de playtest.

## Entrega do Codex

Entregar HTML funcional, fontes organizadas, changelog, comandos executados, testes reais e pendências. Abrir PR se a sessão autorizar e fornecer identificação dos commits. Nunca declarar “pronto” com sprites ausentes, final inacessível ou sistemas apenas descritos em texto. Se uma sessão acabar, deixar progresso persistente para continuação; a existência de um plano não satisfaz implementação.
