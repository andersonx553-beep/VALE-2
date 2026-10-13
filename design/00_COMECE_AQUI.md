# Vale a Dois — instrução para o Codex

Você é responsável por implementar a evolução narrativa, visual e mecânica de Vale a Dois no repositório https://github.com/andersonx553-beep/VALE-2. Leia `VALE_A_DOIS_DOCUMENTO_MESTRE.md` inteiro e os dados em `conteudo/` antes de editar. As imagens em `arte/` são referências conceituais originais produzidas para este pacote, não atlases de animação prontos.

## Objetivo autorizado

Continue o jogo existente. Implemente a história completa das Duas Águas, Rainara como coprotagonista permanente, o elenco, as espécies, os eventos, as melhorias de interface e a direção visual deste documento. A prioridade é um jogo individual consistente, com todas as funcionalidades realmente utilizáveis. Multiplayer e APK ficam fora desta entrega.

## Antes de começar

1. Confirme repositório, branch, alterações locais e instruções existentes. Leia o `index.html` completo. Não sobrescreva trabalho mais recente.
2. Compare a implementação com esta especificação. Na inspeção de 12/10/2026, a main estava em `0fd172de6262c45062bc81babc3c1940ae42fb04`, com um index.html de 68.934 bytes. Esse SHA é apenas referência histórica, não uma ordem de reset.
3. Reconheça o que já funciona: estações de 14 dias, culturas, pesca, casa, culinária, construções, vacas/galinhas, rotinas, presentes, missões e save. Preserve e amplie esses sistemas.
4. Crie uma branch própria. Faça um plano de implementação por marcos, com critérios de aceite. Prossiga sem pedir aprovação para cada pequeno detalhe já especificado.

## Regras de implementação

- Mantenha a distribuição do jogo em um HTML autocontido, CSS/JS inline, sem bibliotecas ou pedidos de rede em tempo de execução. Imagens finais podem ser incorporadas como data URLs; o código de construção e as fontes artísticas podem existir fora do HTML no repositório.
- Não reescreva do zero. Preserve Canvas, cache do terreno, câmera, estado simples e y-sort; introduza apenas as estruturas necessárias para conteúdo, cenas, companheira e espécies.
- A aparência obrigatória é pixel art chibi expressiva das pranchas, com cabeça grande, olhos grandes e contornos marcados. Não substituir por desenho vetorial liso, 3D ou bonecos genéricos de retângulos.
- Prepare sprites reais com grade consistente. Não use a prancha inteira como sprite, nem recorte retratos arbitrariamente e os declare animação. Se não houver ferramenta de imagem, produza atlases raster com autoria de pixels e Canvas, guiados pelas referências; mantenha uma lista honesta do que falta atingir visualmente.
- Rainara permanece no pós-jogo e não exige romance. Relação, tarefas e cenas têm estado persistente, sem eventos duplicados.
- Use IDs estáveis; salve com versionamento e migração. Preserve saves existentes, inventário, animais, construções e missões já concluídas. Nunca apague progresso silenciosamente.
- Recursos de toque, teclado, áreas seguras, legibilidade e acessibilidade fazem parte da conclusão de cada marco.
- Trabalhe pelos marcos do documento. Primeiro entregue uma abertura completa com Rainara, arte representativa, uma missão e persistência. Depois complete campanha, elenco, criação e pós-jogo.
- Toda ação relevante deve gerar retorno visual e uma consequência real. Não deixe placeholders, botões vazios, texto prometendo recursos ausentes ou recompensas que não existem.

## Validação e continuidade

Faça checagem de sintaxe e teste em navegador quando disponível. Verifique console, toque, colisões, transições, save antigo/novo, perda de foco, eventos interrompidos e objetivos já cumpridos. Valide progressão até o final com um save de teste, sem deixar atalhos de depuração na versão final. Meça carregamento e desempenho no ambiente disponível e descreva o aparelho/viewport usado; não alegue testes em dispositivo físico sem realizá-los.

Se precisar dividir o trabalho em sessões, grave `PROGRESSO_VALE2.md` com o marco concluído, os testes reais, os arquivos alterados e o próximo passo exato. Não declare o projeto inteiro pronto ao concluir apenas a primeira parte.

Ao concluir: entregue mudanças, controles, roteiro de teste, pendências reais, commits e PR. Não faça merge nem publique por causa deste documento sozinho: siga a autorização existente na sessão de implementação. Não gere APK.

Comece inspecionando os arquivos e implementando o marco M0. O documento e o conteúdo canônico abaixo já definem a direção criativa; a tarefa é transformá-los em jogo.
