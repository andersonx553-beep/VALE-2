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
