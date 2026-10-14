# Auditoria do HTML aprovado e do documento de gaps

O HTML entregue contém o jogo M7 como prefixo idêntico ao `index.html` de M7 e acrescenta uma camada visual de 52 linhas. A `main` já tinha recebido M8 (controles) depois daquela cópia. O build atual gera o HTML aprovado, as funções M8 e as melhorias abaixo a partir de `src/`; `index.html` continua sendo a distribuição autocontida.

| Tema do MD | Situação nesta branch | Evidência |
|---|---|---|
| Sombras, profundidade, lagos e partículas | Camada visual canônica integrada; nuvens leves em paralaxe; telhas de água e efeitos sazonais anteriores preservados | `src/95-canonical-visual.js`, `src/98-clouds.js`, `src/82-raster-effects.js` |
| Ícones e retratos | Já havia atlas de ícones e retratos narrativos; retratos também aparecem em diálogos comuns | `src/75-icons.js`, `src/85-gap-features.js` |
| Presentes, gostos e aniversários | Presentes e preferências já existiam; calendário, bônus anual e reações adicionados | `src/85-gap-features.js`, `tests/gaps.cjs` |
| Falas contextuais e avatar | Falas variam com clima/hora/campanha; três aparências completas do protagonista são selecionáveis e salvas | `src/85-gap-features.js`, `tools/make_art.py` |
| Campanha e pós-jogo | 24 missões e quatro arcos já existiam; arquivo de relíquias acrescenta meta posterior | `src/10-story.js`, `src/30-campaign-end.js`, `tests/campaign.cjs` |
| Festivais | Quatro eventos anuais já existiam e continuam jogáveis | `src/65-festivals.js`, `tests/m7.cjs` |
| Eventos surpresa, relíquias e coleções | Cartas, visitas/orvalho, três relíquias e exposição registrável adicionadas ao diário | `src/85-gap-features.js`, `tests/gaps.cjs` |
| Animais, carinho, nomes, filhotes e qualidade | Dez espécies, felicidade, nomeação, crescimento e qualidade já existiam; mantidos | `src/40-husbandry.js`, `tests/m5.cjs` |
| Ferramentas, colheita, sorte e feno | Níveis 0–2, prata/ouro com preço maior, sorte diária e estoque de feno adicionados | `src/85-gap-features.js`, `tests/gaps.cjs` |
| Máquinas | Queijeira, tear e apiário com insumos e tempo já existiam; mantidos | `src/40-husbandry.js`, `tests/m5.cjs` |
| Casa, abrigos e Augusto | Primeira expansão e upgrades de capacidade já existiam; segunda reforma e melhorias de conforto levam dois dias | `src/85-gap-features.js`, `tests/gaps.cjs` |
| Exploração livre | Clareira e pedreira opcionais com portais, recursos renováveis, arte e marcação de visita no diário | `src/87-exploration.js`, `tests/gaps.cjs` |

O mapa é visto de cima; a paralaxe usa sombra de nuvens em vez de criar um horizonte de montanhas que encobriria trilhas e personagens. O pós-processamento integral do HTML aprovado fica ativo em telas amplas. Em telas horizontais compactas ele é reduzido; casas, fonte, nuvens, telhas, sprites e efeitos sazonais seguem presentes para manter a resposta dos controles.

## Rede e Android

`src/92-lan.js` usa o host como único simulador e dono do save. O segundo jogador tem posição, direção, aparência, ferramenta, regador e inventário próprios; o dinheiro é compartilhado. O host valida movimento, cultivo, compra/venda e cuidados com animais. Há handshake versionado, sequência, heartbeat, rejeição de terceiro, snapshot inicial, mudanças discretas e reconexão. O aplicativo Android hospeda WebSocket no aparelho e oferece busca NSD e entrada por IP. `lan/dev-server.cjs` reproduz o transporte para testes de duas instâncias no navegador sem serviço externo.

**Limite atual:** no cooperativo, o jogador convidado controla o cultivo, negociações e cuidados básicos; diálogos de missão, festivais, construção e operação de máquinas continuam sob o jogador host. O modo solo mantém todas as funções. O teste automatizado cobre convergência em duas instâncias; não representa dois aparelhos Android físicos.

Capacitor empacota o mesmo HTML. O workflow `.github/workflows/android-debug.yml` monta um APK debug instalável e publica o artifact `VALE-2-Android-debug-APK`. Assinatura release/AAB e teste em dois aparelhos físicos dependem de recursos externos e não são declarados como feitos.
