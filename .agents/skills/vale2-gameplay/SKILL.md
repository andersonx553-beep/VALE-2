---
name: vale2-gameplay
description: Desenha e implementa sistemas de agricultura, inventário, progressão, economia e cooperação do VALE-2. Use quando adicionar ferramentas, cultivo, colheita, loja, atividades e ritmo de jogo.
---

# Gameplay VALE-2

1. Descreva loop de 30 segundos, progressão e motivo de colaboração antes de adicionar uma mecânica. Preserve a sequência enxada → semente → água → crescimento → colheita.
2. Para cada interação, especifique pré-condição, custo, duração, recompensa, feedback e comportamento quando duas pessoas agem ao mesmo tempo.
3. Faça transições determinísticas no host; consumo de semente e ganho de ouro devem ser atômicos. Estado inválido não deve conceder item ou recompensa.
4. Balanceie com uma tabela de entradas e saídas verificáveis; os números do protótipo são 8 sementes, 25 G, pacote de 3 por 5 G, colheita por 10 G e 15 s de crescimento enquanto a sessão está ativa. Trate-os como ponto inicial a testar, não como economia final.
5. Entregue interação jogável e feedback de erro/sucesso. Verifique com dois jogadores, incluindo disputa pelo último recurso e encerramento do host.

Não copie sistemas, escrita ou arte de outro jogo; derive uma proposta própria para Vale a Dois.
