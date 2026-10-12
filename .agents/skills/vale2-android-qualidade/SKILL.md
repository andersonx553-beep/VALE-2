---
name: vale2-android-qualidade
description: Verifica exportação Android, controles de toque, desempenho, acessibilidade e qualidade do VALE-2. Use para APK, preset, testes de dispositivos, bugs de interação e critérios de entrega.
---

# Android e qualidade VALE-2

1. Confira versão Godot, templates de exportação, Android SDK/JDK, orientação paisagem, permissão INTERNET e pacote antes de gerar APK. Não inclua chave de assinatura no Git.
2. Teste dois dispositivos reais no mesmo Wi-Fi: host abre mundo, cliente entra por IP, ambos movem e cultivam, inventário bate, host salva, reinicia e carrega. Teste rede interrompida e terceiro cliente.
3. Avalie toque em telas diferentes: comandos alcançáveis, estado pressionado e zona de toque clara; mantenha teclado funcional no desktop para depuração.
4. Registre FPS, frame time, memória e tamanho do build em aparelhos representativos antes de otimizar. Compare antes/depois no mesmo cenário; não substitua medição por aparência.
5. Rode importação Godot headless e revisão visual quando possível. Relate separadamente testes locais, testes Android e lacunas.

Referências: [exportação Android](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html), [resoluções](https://docs.godotengine.org/en/stable/tutorials/rendering/multiple_resolutions.html) e [alvos de toque](https://developers.google.com/youtube/gaming/playables/certification/best_practices_design).
