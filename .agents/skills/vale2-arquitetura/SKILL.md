---
name: vale2-arquitetura
description: Organiza ou refatora cenas, GDScript, dados e persistência do projeto Godot 4 VALE-2. Use para arquitetura, criação de sistemas, separação de responsabilidades, migração de save e revisão de código do jogo.
---

# Arquitetura VALE-2

1. Inspecione `AGENTS.md`, `project.godot`, cenas, scripts, save e alterações locais. Registre o fluxo atual antes de editar.
2. Modele cada mudança como uma fatia jogável. Separe dados do mundo, regras e apresentação quando o código crescer; mantenha o host como única fonte de verdade.
3. Defina invariantes e contratos de dados: duas pessoas no máximo, 12 canteiros no protótipo, inventário e ouro compartilhados, save apenas no host. Versione o formato de save e defina migração antes de mudar esquema.
4. Prefira cenas reutilizáveis e sinais explícitos. Tipagem em GDScript, nomes coerentes e ausência de dependência cíclica. Não crie autoloads sem necessidade real.
5. Execute importação headless e teste a cena inicial se houver Godot; relate erros exatos. Revise o diff para preservar conteúdo e comportamento.

Referência: [guia oficial de estilo GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html).
