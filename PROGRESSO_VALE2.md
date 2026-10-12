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
