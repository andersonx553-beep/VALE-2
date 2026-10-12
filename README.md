# Vale a Dois / VALE-2

Protótipo inicial de fazenda cooperativa para **duas pessoas** em **dois Android na mesma rede Wi-Fi local**. Projeto Godot 4.4+ em GDScript, com host autoritativo e ENet/UDP. Arte e código deste marco são originais; o desenho por formas é provisório e ainda não representa a direção final de pixel art detalhada.

## Rodar

1. Abra esta pasta no Godot 4.4 ou superior e execute `scenes/main.tscn` (F6) ou o projeto (F5).
2. Na primeira instância, selecione **Criar mundo (host)**. O IP local aparece na faixa superior.
3. Na segunda instância, no mesmo Wi-Fi, digite esse IP e selecione **Entrar**. O host usa UDP 24562; roteadores com isolamento de clientes impedem a conexão.
4. No desktop, mova-se com WASD ou setas, use E/Espaço e selecione ferramentas com 1–4. No Android, use direção e ação na tela.
5. Aproxime-se de um canteiro e aplique enxada, semente, água e colheita, cada qual com sua ferramenta. O crescimento leva 15 s de sessão ativa. Compre 3 sementes por 5 G; cada colheita rende 10 G.

O host é o único que altera canteiros, sementes e ouro. O cliente envia movimento e pedidos; o host verifica remetente, alcance, custo e transições. O save `user://vale2_save.json` pertence ao aparelho host. Sair da sessão não apaga o save. Reconectar restaura o mundo do host, mas a posição dos jogadores volta ao início.

## Android

Crie um preset Android no editor Godot, configure JDK/SDK e templates de exportação conforme a [documentação oficial](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html). Marque a permissão **INTERNET** no preset para o tráfego ENet local. Configure o identificador Android e assinatura conforme seu ambiente. O repositório não contém APK, preset assinado ou chave. Teste em dois aparelhos físicos antes de classificar a versão como pronta para Android.

## Estado e próximos marcos

Este marco inclui lobby por IP, limite de um cliente, movimentação compartilhada, 12 canteiros, inventário/ouro compartilhados e save local no host. Ainda faltam arte final, animação, colisões, controles responsivos para diferentes proporções, feedback contextual das ações, reconexão robusta e teste em celulares. O segundo jogador não é simulado: a arquitetura usa ENet real, mas a conexão e a exportação Android ainda não foram verificadas nesta entrega por ausência do Godot e de aparelhos no ambiente de execução.

Para desenvolvimento assistido, leia `AGENTS.md`. Há cinco agentes em `.github/agents/` e cinco skills em `.agents/skills/`. As [fontes e decisões](docs/REFERENCIAS.md) indicam documentação consultada e critérios de licenças.
