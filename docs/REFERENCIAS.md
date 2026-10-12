# Fontes e decisões

Consultadas em 12 de outubro de 2026. Priorize a documentação da versão Godot instalada ao atualizar o jogo.

| Tema | Fonte primária | Aplicação no VALE-2 |
| --- | --- | --- |
| ENet, LAN e RPC | [Godot: multiplayer de alto nível](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html) | Host em IP privado, RPC na mesma cena e UDP. |
| Capacidade do host | [Godot: ENetMultiplayerPeer](https://docs.godotengine.org/en/stable/classes/class_enetmultiplayerpeer.html) | `create_server(PORT, 1)` aceita um cliente. |
| Estilo GDScript | [Godot: GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) | Nomes e organização das cenas/scripts. |
| Mapa/arte futura | [Godot: TileSets](https://docs.godotengine.org/en/stable/tutorials/2d/using_tilesets.html) e [TileMaps](https://docs.godotengine.org/en/stable/tutorials/2d/using_tilemaps.html) | Atlas/terrenos quando houver arte original final. |
| Telas | [Godot: múltiplas resoluções](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html) | Revisar layout landscape em proporções distintas. |
| Android | [Godot: exportação Android](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html) | SDK/JDK, templates e preset. |
| Toque | [Google: design de jogos para touch](https://developers.google.com/youtube/gaming/playables/certification/best_practices_design) | Dimensionar alvos e espaço entre controles. |
| Agentes de repositório | [GitHub: custom agents](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/use-copilot-agents/use-custom-agents) | Perfis `.github/agents/*.agent.md`. |
| Skills de projeto | [GitHub: agent skills](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) | Pastas `.agents/skills/*/SKILL.md`. |

Repositórios citados na conversa anterior servem como referência conceitual; nenhum código ou asset deles foi copiado. A licença de Bloomrise não foi identificada, então não use seus arquivos. Profundidade de Stardew Valley é referência de ambição, não autorização para copiar sua expressão criativa.
