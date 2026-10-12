# Vale a Dois / VALE-2

Protótipo inicial de fazenda cooperativa para **duas pessoas** em **dois Android na mesma rede Wi-Fi local**. Projeto Godot 4.4+ em GDScript, com host autoritativo e ENet/UDP. Arte e código deste marco são originais; o desenho por formas é provisório e ainda não representa a direção final de pixel art detalhada.

## Rodar

1. Abra esta pasta no Godot 4.4 ou superior e execute `scenes/main.tscn` (F6) ou o projeto (F5).
2. Na primeira instância, selecione **Criar mundo (host)**. O IP local aparece na faixa superior.
3. Na segunda instância, no mesmo Wi-Fi, digite esse IP e selecione **Entrar**. O host usa UDP 24562; roteadores com isolamento de clientes impedem a conexão.
4. No desktop, mova-se com WASD ou setas, use E/Espaço e selecione ferramentas com 1–4. No Android, use direção e ação na tela.
5. Aproxime-se de um canteiro e aplique enxada, semente, água e colheita, cada qual com sua ferramenta. O crescimento leva 15 s de sessão ativa. Compre 3 sementes por 5 G; cada colheita rende 10 G.

O host é o único que altera canteiros, sementes e ouro. O cliente envia movimento e pedidos; o host verifica remetente, alcance, custo e transições. O save `user://vale2_save.json` pertence ao aparelho host. Sair da sessão não apaga o save. Reconectar restaura o mundo do host, mas a posição dos jogadores volta ao início.

## Baixar e instalar o APK

A [aba Releases](https://github.com/andersonx553-beep/VALE-2/releases) contém o APK de teste mais recente quando a compilação da `main` conclui. Escolha a versão **Preview** mais recente e baixe `VALE-2-preview.apk` em **Assets**. Instale o mesmo arquivo nos dois celulares Android. O [workflow Android APK](https://github.com/andersonx553-beep/VALE-2/actions/workflows/android-apk.yml) também oferece o artefato `VALE-2-Android-APK` em cada execução bem-sucedida por 90 dias (o download de Actions pode exigir login no GitHub).

O APK é um **build de depuração**, assinado pela chave de teste gerada no GitHub Actions para aquela execução. Atualizações geradas em outra execução podem usar outra chave e exigir desinstalação antes da instalação; isso apaga o save local do host. Antes de desinstalar, preserve o aparelho/save se o progresso importar. Para distribuição estável, será necessária uma chave de assinatura de lançamento persistente, armazenada como secret do repositório, jamais em código.

No primeiro celular, crie o mundo. No segundo, conectado ao mesmo Wi-Fi, informe o IP local mostrado no host. O roteador deve permitir comunicação entre clientes e UDP 24562. O preset `export_presets.cfg` inclui a permissão Android `INTERNET`. O build automatizado não substitui a prova de conexão real em dois aparelhos.

## Estado e próximos marcos

Este marco inclui lobby por IP, limite de um cliente, movimentação compartilhada, 12 canteiros, inventário/ouro compartilhados e save local no host. Ainda faltam arte final, animação, colisões, controles responsivos para diferentes proporções, feedback contextual das ações, reconexão robusta e teste em celulares. O segundo jogador não é simulado: a arquitetura usa ENet real, mas a conexão em dois Android permanece pendente de prova física. O GitHub Actions verifica importação e exportação do projeto antes de publicar cada APK.

Para desenvolvimento assistido, leia `AGENTS.md`. Há cinco agentes em `.github/agents/` e cinco skills em `.agents/skills/`. As [fontes e decisões](docs/REFERENCIAS.md) indicam documentação consultada e critérios de licenças.
