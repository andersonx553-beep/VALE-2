---
name: vale2-rede-lan
description: Implementa e audita multiplayer local ENet/UDP do VALE-2 em Godot 4. Use para lobby host/cliente, sincronização, RPC, validação, queda de conexão e testes LAN entre dois Android.
---

# Rede local VALE-2

1. Mapeie autoridade de cada campo e método RPC antes de alterar. `create_server(PORT, 1)` limita a um cliente; IDs dos clientes são dinâmicos, não assuma que o segundo jogador tem peer ID 2.
2. Cliente envia intenção de movimento ou ação. Host valida peer remetente, faixa dos valores, alcance, recursos e transição de estado; somente ele altera mundo, economia e save.
3. Envie movimentos em cadência limitada com modo não confiável; ações e estado persistente com modo confiável. Após conexão, envie snapshot completo antes de aceitar a visão como pronta. Não replique todo o mapa a cada frame.
4. Cubra recusa de terceiro cliente, IP incorreto, timeout, host que sai, troca de rede, segundo jogador que reconecta e ações simultâneas no mesmo canteiro.
5. Teste dois processos isolados e depois dois Android no mesmo SSID com UDP liberado e permissão INTERNET no preset Android. Anote latência, perda e divergências observadas; não alegue teste físico sem os dispositivos.

Referências: [multiplayer de alto nível](https://docs.godotengine.org/en/stable/tutorials/networking/high_level_multiplayer.html) e [ENetMultiplayerPeer](https://docs.godotengine.org/en/stable/classes/class_enetmultiplayerpeer.html).
