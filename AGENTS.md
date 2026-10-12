# VALE-2 — instruções para agentes

Leia este arquivo, `README.md`, `project.godot` e os arquivos envolvidos antes de editar. Confira branch, alterações locais e a versão real do projeto. Preserve mudanças do usuário e não reescreva funcionalidades existentes para resolver uma tarefa pequena.

## Contrato do produto

- Jogo próprio de fazenda cooperativa para **exatamente duas pessoas** em dois celulares Android na **mesma rede Wi-Fi local**.
- Godot 4, GDScript, ENet/UDP. Celular host é autoridade do mundo e salva o progresso; um único cliente envia intenções. Sem backend online para a partida.
- Mantenha nome e interface em português: **Vale a Dois**. Inspire-se em profundidade de sistemas, sem copiar código, personagens, mapas, textos, identidade ou assets de Stardew Valley ou terceiros.
- O HTML anterior era uma prévia de mecânicas, não a fonte do multiplayer. Estado operacional deve vir do repositório.
- Não acrescente novos sistemas grandes sem uma fatia jogável, critérios de aceite e verificação em dois dispositivos.

## Especialistas e skills

Os cinco agentes em `.github/agents/` podem ser escolhidos no Copilot/VS Code. Cada um referencia sua skill em `.agents/skills/`:

1. `vale2-arquiteto` → `vale2-arquitetura`: organização de cenas, dados e persistência.
2. `vale2-rede` → `vale2-rede-lan`: autoridade, sincronização e reconexão.
3. `vale2-gameplay` → `vale2-gameplay`: agricultura, economia e cooperação.
4. `vale2-arte` → `vale2-direcao-visual`: pixel art, identidade e interface.
5. `vale2-android` → `vale2-android-qualidade`: toque, desempenho, exportação e testes.

Ao trabalhar com Codex, leia a skill correspondente antes da alteração. Um agente no GitHub é uma configuração reutilizável; nenhum deles executa em segundo plano apenas por estar no repositório.

## Critérios para aceitar uma mudança

Descreva o comportamento antes e depois, os arquivos alterados e a prova disponível. Para rede ou save, teste host e cliente em processos distintos e depois em dois Android quando houver build. Para visual, confira paisagem ampla e tela estreita; para arte de terceiros, registre licença e atribuição exigida antes de incorporar. Se Godot ou aparelhos não estiverem disponíveis, informe explicitamente o que ainda não foi verificado.
