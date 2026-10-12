# Direção de arte e animação

## Hierarquia visual

1. A dupla em `arte/01_dupla.png` define rosto, proporção, cores e contorno do protagonista e de Rainara.
2. `arte/02_moradores.png` define a individualidade do elenco restante.
3. `arte/03_animais.png` define aparência e temperamento visual das espécies e pets.
4. `arte/04_mundo.png` define materiais, vegetação, arquitetura e atmosfera. É referência de ambiente, não um mapa ou tileset pronto. Seus enquadramentos variam; os assets finais devem usar a câmera top-down do jogo atual. Elementos decorativos incidentais, como edifícios ao fundo, não criam novos lugares ou obrigações de história.
5. `arte/05_rainara.png` detalha expressões e vistas de Rainara. Pequenas diferenças entre vistas devem ser regularizadas nos sprites finais: manter a bolsa sobre o mesmo ombro e a presilha no lado esquerdo da personagem. Não espelhar acessórios assimétricos inadvertidamente.

As cinco pranchas são imagens raster geradas como arte conceitual. Não têm transparência nem grade de animação certificada. O Codex deve produzir os atlases finais a partir desta direção, e validar cada célula. O documento não os apresenta como sprites prontos.

## Linguagem visual obrigatória

Pixel art chibi expressiva: aproximadamente 2,5 cabeças por corpo, olhos grandes com pequenos brilhos quadrados, contorno escuro em degraus, cabelo em massas legíveis, rosto com poucos tons e roupas que identificam a pessoa. Adultos continuam adultos em voz, história e postura. Os bichos seguem a mesma família visual, com formas arredondadas e expressões reconhecíveis.

Paleta base: contorno #251B17; creme #F5E8CF; pele clara #E9B88B, média #B87548 e escura #74442E; castanho #68462A; coral #CC7060; terracota #A94F3C; oliva #687044; lavanda #9270A1; azul #527D9B; verde-petróleo #356F69; mostarda #C79B48. Esses valores orientam, não obrigam todos os objetos à mesma cor. Usar 3–5 tons por material e no máximo aproximadamente 24 cores por personagem, sem contar transparência. Evitar excesso de dithering nos rostos.

Iluminação convencional do alto à esquerda; sombras compactas, separadas do sprite quando possível. Água, luz e partículas podem usar transparência, mas manter bordas dos personagens nítidas. Nenhum blur sobre pixel art. Elementos de interface e fontes HTML podem ser lisos para leitura; o mundo mantém amostragem nearest-neighbor.

## Compatibilidade com o mapa existente

Manter tile lógico de 16 px e mundo de 80 × 60 na fazenda. Um personagem pode ocupar uma célula de sprite de 32 × 48 px sem ocupar três tiles de colisão. A âncora fica no centro dos pés; a colisão é uma área pequena, aproximadamente 10 × 6 px, independente do cabelo. Desenhar os pés na posição lógica existente. Nunca multiplicar coordenadas de árvores, solo ou personagem por causa da arte nova.

Protótipo visual obrigatório: testar protagonista e Rainara junto a uma porta, uma vaca e um canteiro. Se o personagem parecer grande demais, reduzir a área desenhada dentro da célula ou adaptar a altura visual das fachadas mantendo a colisão. Não resolver aumentando silenciosamente o tile lógico em saves existentes.

## Especificação dos atlases finais

| Família | Célula sugerida | Direções | Estados mínimos |
| --- | --- | --- | --- |
| Humanos | 32 × 48 | baixo, esquerda, direita, cima | parado 2, andar 6, falar 2 por direção |
| Protagonista extra | 32 × 48; ferramenta em camada | mesmas 4 | correr 6; enxada, rega, machado, pesca, plantar, colher: 6 cada; carinho 4 |
| Rainara extra | 32 × 48 | mesmas 4 | regar 6, plantar 6, alimentar 6, colher 6, anotar 4, acenar 4 |
| Sentados | 32 × 40 | frente e lado | 2 frames de descanso por direção |
| Retratos | 96 × 96 | frente ou três quartos | calma, alegria, curiosidade, preocupação, determinação, carinho |
| Cão e gato | 32 × 32 | mesmas 4 | parado 2, andar 6, comer 4, dormir 2, carinho 4; cão abana rabo e brinca |
| Aves e coelho | 24 × 24 | mesmas 4 | parado 2, andar/pular 4, comer 4, dormir 2, reagir 2 |
| Vaca, cavalo, burro | 48 × 40 | mesmas 4 | parado 2, andar 6, pastar 4, dormir 2, carinho 2 |
| Cabra, ovelha, porco | 40 × 32 | mesmas 4 | parado 2, andar 4, comer 4, dormir 2, espécie 4 |
| Filhotes | 16 × 20 ou 24 × 24 | mesmas 4 | parado 2, andar 4, dormir 2 |
| Ícones | 24 × 24 | frente | 1, com margem transparente uniforme |
| Terreno | 16 × 16 | tile top-down | centro, bordas, cantos; água 4 frames |
| Efeitos | 16 × 16 ou 32 × 32 | variável | 4–6 frames por efeito |

Números em estados indicam frames, não segundos. Cadência inicial: parado 2 fps, andar 8 fps, correr 12 fps, ferramentas 10 fps, dormir 1 fps. Ajustar pelo movimento real; a animação não continua andando quando o personagem está bloqueado. Ferramenta causa efeito no frame de contato uma única vez, nunca em todos os frames.

Atlases possuem gutters de 1–2 px e mapa JSON de coordenadas explícitas. Ordem de direções armazenada por nome; não depender de índice implícito, pois o jogo atual usa 0=baixo, 1=cima, 2=esquerda, 3=direita. Alpha real no fundo. Sem nome, legenda, chão bege, sombras de prancha ou moldura dentro das células.

Se for necessário preparar arte por código, usar grids autorais de pixels e rasterização determinística seguindo as silhuetas; não voltar à função genérica person() com apenas outra cor de camiseta. Ferramenta de geração de imagens pode auxiliar conceitos e frames, mas exige revisão de contorno, escala, identidade, grade e anatomia.

## Catálogo obrigatório

### Humanos e pets

CHR_PLAYER, CHR_RAINARA, CHR_MARTA, CHR_TIAO, CHR_LUNA, CHR_CELINA, CHR_AUGUSTO, CHR_IARA. PET_BENTO e PET_AMORA. Helena usa carta e um retrato opcional futuro, sem animação obrigatória.

Retratos: pelo menos seis expressões para Rainara e quatro para cada outro morador (neutro, alegria, preocupação, determinação). Protagonista pode usar retrato configurável neutro e reação contextual. Nenhum retrato de Rainara usa a aparência de Luna ou troca presilha/bolsa de lado entre falas.

### Criação

ANM_CHICKEN, ANM_COW, ANM_GOAT, ANM_SHEEP, ANM_DUCK, ANM_PIG, ANM_HORSE, ANM_DONKEY, ANM_RABBIT, ANM_BEE. Adultos e filhotes das nove espécies vertebradas; abelhas são um efeito de grupo do apiário, sem indivíduo com inventário.

Variações de cor são paletas controladas e não espécies novas. Vaca: creme com manchas chocolate; galinha: buff; cabra: canela; ovelha: lã marfim e focinho cinza; pato: branco com detalhe verde; porco: rosa pêssego e lama; cavalo: castanho com estrela clara; burro: cinza; coelho: creme com pontas castanhas. Cada espécie recebe som próprio opcional de volume baixo e cooldown.

### Edifícios e objetos

BLD_HOME_0/1, BLD_NURSERY_0/1/2, BLD_SHOP, BLD_WORKSHOP, BLD_CLINIC, BLD_KITCHEN, BLD_ATELIER, BLD_COOP_0/1, BLD_BARN_0/1, BLD_PIGPEN, BLD_STALL, BLD_RABBIT_HUTCH, BLD_APIARY. Dimensões visuais registradas separadamente do footprint lógico.

OBJ_CHEST, OBJ_BED, OBJ_STOVE, OBJ_CHAIR, OBJ_PORCH_TABLE, OBJ_NOTICEBOARD, OBJ_FEEDER, OBJ_TROUGH, OBJ_NEST, OBJ_BRUSH, OBJ_SHEARS, OBJ_FENCE, OBJ_GATE_OPEN/CLOSED, OBJ_DUCK_RAMP, OBJ_GOAT_PLATFORM, OBJ_BEEBOX, OBJ_CHEESEMAKER, OBJ_LOOM, OBJ_SEED_BENCH, OBJ_MAILBOX, OBJ_BRIDGE_BROKEN/FIXED, OBJ_SLUICE_CLOSED/PARTIAL/OPEN, OBJ_FILTER_DIRTY/CLEAN, OBJ_WATER_GAUGE, OBJ_PICNIC_BLANKET. Cercas têm conexões horizontais, verticais e cantos.

### Solo e natureza

TIL_GRASS por estação; TIL_PATH; TIL_SAND; TIL_WATER; TIL_SOIL_DRY/WET; TIL_SNOW; TIL_STONE; TIL_WOOD_FLOOR. Árvores, pedras, arbustos, flores, ervas, ipê e caniços com variações visuais. Canal seco, turvo e restaurado; zona úmida sempre preservada após Q15. Flores não usam a mesma cor de culturas maduras se isso confundir interação.

Culturas existentes: nabo, cenoura, abóbora, morango, tomate, milho, trigo e espinafre. Cada uma: semente, broto, crescimento, maturidade e dormência; culturas recorrentes têm estado pós-colheita. Silhuetas distinguíveis sem depender de emoji.

### Inventário e interface

Ícones de todas as ferramentas, sementes, culturas, sete espécies de peixe existentes, madeira, pedra, ração, água, ovo, leite, leite de cabra, lã, ovo de pato, composto, raiz, pelo escovado, mel, queijo, queijo de cabra, tecido, erva, sopa, peixe assado, torta, omelete, pão de milho, pão com mel, ensopado e chá. Ícones das moedas, calendário, clima, diálogo, coração, tarefa, diário, comida, água e limpeza. Em dados, usar IDs existentes sempre que possível e mapear novos rótulos sem quebrar saves.

Molduras: diálogo, ficha de animal, caderno, loja e tooltip com aparência de madeira clara e papel, mantendo contraste. Ícone sempre acompanhado de nome acessível ou tooltip. Não substituir toda a UI por texto em imagem.

### Efeitos e cenas

FX_WATER_SPLASH, FX_SOIL, FX_LEAF, FX_HARVEST, FX_HEART, FX_FOOTSTEP, FX_RAIN, FX_SNOW, FX_FIREFLY, FX_SMOKE, FX_FLOW_TURBID/CLEAR. Aplicar limite de partículas e desenhar apenas regiões visíveis. Cena de varanda usa os mesmos sprites do jogo, sem exigir uma ilustração nova para cada diálogo.

## Prompts reutilizáveis para produção de arte

Prompt base de estilo: “Original cozy Brazilian mountain farming RPG pixel art. Chibi adult proportions, large expressive eyes, compact body, dark stepped outlines, crisp square pixel clusters, warm limited palette, consistent top-left lighting, no blur, no vector smoothing, no 3D. Match the attached Vale a Dois character reference. Preserve character identity, clothing and accessories. Production sprite with real transparent background, exact equal cells, no text, no frame, no floor or labels.”

Rainara: adicionar “long wavy dark brown hair, tan complexion, coral blouse, terracotta skirt, olive utility bag, brown boots, green leaf hairclip on character left; kind, alert expression”. Protagonista: adicionar “tousled black hair, tan complexion, cream work jacket, white shirt, charcoal trousers, brown sturdy shoes”. Usar as fichas para o elenco restante; não criar cópias com roupas recoloridas.

Animal: adicionar espécie, paleta e comportamento do catálogo; “farm animal in the same cozy pixel language as the humans; anatomically coherent silhouette, readable face, no clothing except Bento's blue kerchief and cow bell; idle, walk, eat, rest states; keep identical size and markings across frames”.

Edifício: “top-down orthographic RPG asset, roof and front wall visible, parallel perspective, tile grid compatible with a 16 px logical map, no isometric diamond grid, entrance clearly readable, exterior footprint and visual roof distinct”. Usar `04_mundo.png` para materiais e cores, não copiar sua câmera de apresentação.

Cada chamada deve ter um sujeito ou atlas claramente definido. Não pedir ao gerador todos os sprites, cenários e ícones de uma vez. Conferir resultados antes de incorporá-los. Os prompts ajudam a produzir; não substituem as imagens que acompanham este pacote.

## Aceite visual

- A 100% da escala do jogo, cada morador é reconhecível sem legenda.
- Rainara e protagonista mantêm proporções das referências; olhos, cabelo e roupa não mudam entre frames.
- Mesmo tamanho de pixel aparente em personagens e animais; ambientes podem ter mais detalhe sem parecer outro jogo.
- Nenhum sprite flutua, treme ou muda de escala ao virar; pés ficam ancorados.
- Transparência sem retângulo bege ou halo branco; contornos visíveis à noite.
- Colisão não acompanha o volume inteiro do cabelo; y-sort permite passar atrás de árvores e na frente das portas.
- Caminhada sincronizada com deslocamento; ferramenta toca o alvo; partícula sai do alvo.
- Diálogos legíveis em 360 × 800 e 800 × 360, botões de pelo menos 44 px CSS, áreas seguras respeitadas.
- Artes conceituais não são consideradas implementação visual concluída até esses itens passarem no jogo.
