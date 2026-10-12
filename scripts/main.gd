extends Node2D
## Primeiro marco: mundo autoritativo para duas pessoas na mesma rede local.

const PORT := 24562
const SPEED := 175.0
const UPDATE_INTERVAL := 1.0 / 15.0
const SAVE_PATH := "user://vale2_save.json"
const FARM_ORIGIN := Vector2(465, 295)
const FARM_STEP := Vector2(65, 62)
const PLAYER_RADIUS := 14.0
const ACTION_RANGE := 58.0
const TOOLS := ["Enxada", "Semente", "Regador", "Colher"]
const COLORS := [Color("8765ac"), Color("e7bb69")]

var peer: ENetMultiplayerPeer
var positions := {1: Vector2(330, 390), 2: Vector2(385, 390)}
var inputs := {1: Vector2.ZERO, 2: Vector2.ZERO}
var plots: Array[Dictionary] = []
var seeds := 8
var gold := 25
var selected_tool := 0
var world_time := 0.0
var net_timer := 0.0
var save_timer := 0.0
var hosted := false
var connected := false
var guest_peer_id := 0
var touch_dirs := {"left": false, "right": false, "up": false, "down": false}

var hud: Control
var lobby: Control
var status_label: Label
var room_label: Label
var inventory_label: Label
var tool_label: Label
var ip_edit: LineEdit
var tool_buttons: Array[Button] = []

func _ready() -> void:
	multiplayer.peer_connected.connect(_on_peer_connected)
	multiplayer.peer_disconnected.connect(_on_peer_disconnected)
	multiplayer.connected_to_server.connect(_on_connected_to_server)
	multiplayer.connection_failed.connect(_on_connection_failed)
	multiplayer.server_disconnected.connect(_on_server_disconnected)
	_reset_world()
	_build_ui()
	_update_ui()
	queue_redraw()

func _reset_world() -> void:
	positions = {1: Vector2(330, 390), 2: Vector2(385, 390)}
	inputs = {1: Vector2.ZERO, 2: Vector2.ZERO}
	plots.clear()
	for i in 12:
		plots.append({"stage": 0, "ready_at": 0.0})
	seeds = 8
	gold = 25
	world_time = 0.0

func _start_host() -> void:
	_close_peer()
	_reset_world()
	_load_world()
	peer = ENetMultiplayerPeer.new()
	var result := peer.create_server(PORT, 1)
	if result != OK:
		peer = null
		status_label.text = "Não foi possível abrir UDP %d (erro %d)." % [PORT, result]
		return
	multiplayer.multiplayer_peer = peer
	hosted = true
	connected = true
	lobby.visible = false
	hud.visible = true
	room_label.text = "HOST • IP %s • UDP %d" % [_local_ip(), PORT]
	_update_ui()

func _start_client() -> void:
	var address := ip_edit.text.strip_edges()
	if not _valid_ipv4(address):
		status_label.text = "Digite o IPv4 local do host, por exemplo 192.168.1.10."
		return
	_close_peer()
	peer = ENetMultiplayerPeer.new()
	var result := peer.create_client(address, PORT)
	if result != OK:
		peer = null
		status_label.text = "Não foi possível iniciar a conexão (erro %d)." % result
		return
	multiplayer.multiplayer_peer = peer
	status_label.text = "Conectando a %s..." % address

func _valid_ipv4(address: String) -> bool:
	var parts := address.split(".")
	if parts.size() != 4:
		return false
	for part in parts:
		if part.is_empty() or not part.is_valid_int() or part.length() > 3:
			return false
		if str(int(part)) != part or int(part) < 0 or int(part) > 255:
			return false
	return true

func _local_ip() -> String:
	for address in IP.get_local_addresses():
		if _valid_ipv4(address) and not address.begins_with("127.") and not address.begins_with("169.254."):
			return address
	return "consulte o Wi-Fi"

func _close_peer() -> void:
	if hosted:
		_save_world()
	if peer != null:
		peer.close()
		peer = null
	multiplayer.multiplayer_peer = OfflineMultiplayerPeer.new()
	hosted = false
	connected = false
	inputs[2] = Vector2.ZERO
	guest_peer_id = 0

func _leave() -> void:
	_close_peer()
	hud.visible = false
	lobby.visible = true
	status_label.text = "Escolha host ou entre pelo IP local."
	queue_redraw()

func _on_peer_connected(id: int) -> void:
	if not hosted:
		return
	if guest_peer_id != 0:
		peer.disconnect_peer(id)
		return
	guest_peer_id = id
	inputs[2] = Vector2.ZERO
	positions[2] = Vector2(385, 390)
	_send_full_state(id)
	room_label.text = "HOST • DUPLA CONECTADA"
	queue_redraw()

func _on_peer_disconnected(id: int) -> void:
	if id != guest_peer_id:
		return
	guest_peer_id = 0
	inputs[2] = Vector2.ZERO
	positions[2] = Vector2(385, 390)
	if hosted:
		room_label.text = "HOST • aguardando segunda pessoa"
		_save_world()
	queue_redraw()

func _on_connected_to_server() -> void:
	connected = true
	lobby.visible = false
	hud.visible = true
	room_label.text = "CLIENTE • conectado ao host"
	_update_ui()

func _on_connection_failed() -> void:
	_close_peer()
	status_label.text = "Conexão falhou. Confira IP, Wi-Fi e UDP %d." % PORT

func _on_server_disconnected() -> void:
	_close_peer()
	hud.visible = false
	lobby.visible = true
	status_label.text = "O host saiu. O progresso fica no aparelho dele."
	queue_redraw()

func _physics_process(delta: float) -> void:
	if not connected:
		return
	var direction := _movement_direction()
	if hosted:
		inputs[1] = direction
		for id in inputs.keys():
			if positions.has(id) and (id == 1 or guest_peer_id != 0):
				positions[id] = _clamp_position(positions[id] + inputs[id] * SPEED * delta)
		world_time += delta
		for plot in plots:
			if plot.stage == 3 and world_time >= plot.ready_at:
				plot.stage = 4
				_broadcast_state()
		save_timer += delta
		if save_timer >= 10.0:
			save_timer = 0.0
			_save_world()
	else:
		inputs[2] = direction
		# O cliente não move o estado do mundo: envia somente a intenção.
		net_timer += delta
		if net_timer >= UPDATE_INTERVAL:
			net_timer = 0.0
			_submit_direction.rpc_id(1, direction)
	if hosted:
		net_timer += delta
		if net_timer >= UPDATE_INTERVAL:
			net_timer = 0.0
			_send_positions.rpc(positions.get(1, Vector2.ZERO), positions.get(2, Vector2.ZERO))
	queue_redraw()

func _movement_direction() -> Vector2:
	var v := Vector2.ZERO
	if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT) or touch_dirs.left:
		v.x -= 1
	if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT) or touch_dirs.right:
		v.x += 1
	if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP) or touch_dirs.up:
		v.y -= 1
	if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN) or touch_dirs.down:
		v.y += 1
	return v.normalized()

func _clamp_position(p: Vector2) -> Vector2:
	return Vector2(clampf(p.x, 150, 1130), clampf(p.y, 185, 610))

@rpc("any_peer", "call_remote", "unreliable")
func _submit_direction(direction: Vector2) -> void:
	if not hosted or guest_peer_id == 0 or multiplayer.get_remote_sender_id() != guest_peer_id:
		return
	if not is_finite(direction.x) or not is_finite(direction.y):
		return
	inputs[2] = direction.limit_length(1.0)

@rpc("authority", "call_remote", "unreliable")
func _send_positions(host_position: Vector2, guest_position: Vector2) -> void:
	positions[1] = host_position
	positions[2] = guest_position

func _interact() -> void:
	if not connected:
		return
	if hosted:
		_apply_action(1, selected_tool)
	else:
		_request_action.rpc_id(1, selected_tool)

@rpc("any_peer", "call_remote", "reliable")
func _request_action(tool: int) -> void:
	if hosted and multiplayer.get_remote_sender_id() == guest_peer_id and guest_peer_id != 0:
		_apply_action(2, tool)

func _apply_action(id: int, tool: int) -> void:
	if not positions.has(id) or tool < 0 or tool >= TOOLS.size():
		return
	var nearest := -1
	var distance := ACTION_RANGE
	for i in plots.size():
		var d: float = (positions[id] as Vector2).distance_to(_plot_center(i))
		if d < distance:
			distance = d
			nearest = i
	if nearest == -1:
		return
	var plot := plots[nearest]
	match tool:
		0:
			if plot.stage == 0:
				plot.stage = 1
		1:
			if plot.stage == 1 and seeds > 0:
				seeds -= 1
				plot.stage = 2
		2:
			if plot.stage == 2:
				plot.stage = 3
				plot.ready_at = world_time + 15.0
		3:
			if plot.stage == 4:
				plot.stage = 1
				plot.ready_at = 0.0
				gold += 10
	_broadcast_state()

func _buy_seeds() -> void:
	if not connected:
		return
	if hosted:
		_apply_buy()
	else:
		_request_buy.rpc_id(1)

@rpc("any_peer", "call_remote", "reliable")
func _request_buy() -> void:
	if hosted and multiplayer.get_remote_sender_id() == guest_peer_id and guest_peer_id != 0:
		_apply_buy()

func _apply_buy() -> void:
	if gold < 5:
		return
	gold -= 5
	seeds += 3
	_broadcast_state()

func _broadcast_state() -> void:
	_update_ui()
	queue_redraw()
	if hosted:
		_save_world()
		if guest_peer_id != 0:
			_receive_state.rpc_id(guest_peer_id, plots, seeds, gold, world_time)

func _send_full_state(id: int) -> void:
	_receive_state.rpc_id(id, plots, seeds, gold, world_time)
	_send_positions.rpc_id(id, positions[1], positions[2])

@rpc("authority", "call_remote", "reliable")
func _receive_state(new_plots: Array, new_seeds: int, new_gold: int, new_time: float) -> void:
	if hosted:
		return
	plots.clear()
	for plot in new_plots:
		plots.append(plot)
	seeds = new_seeds
	gold = new_gold
	world_time = new_time
	_update_ui()
	queue_redraw()

func _save_world() -> void:
	if not hosted:
		return
	var data := {"version": 1, "plots": plots, "seeds": seeds, "gold": gold, "world_time": world_time}
	var file := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if file != null:
		file.store_string(JSON.stringify(data))

func _load_world() -> void:
	if not FileAccess.file_exists(SAVE_PATH):
		return
	var file := FileAccess.open(SAVE_PATH, FileAccess.READ)
	if file == null:
		return
	var data = JSON.parse_string(file.get_as_text())
	if not (data is Dictionary) or data.get("version") != 1:
		return
	var saved_plots = data.get("plots", [])
	if not (saved_plots is Array) or saved_plots.size() != 12:
		return
	for i in 12:
		if not (saved_plots[i] is Dictionary):
			return
		var stage := int(saved_plots[i].get("stage", 0))
		if stage < 0 or stage > 4:
			return
		plots[i] = {"stage": stage, "ready_at": maxf(0.0, float(saved_plots[i].get("ready_at", 0.0)))}
	seeds = clampi(int(data.get("seeds", 8)), 0, 99999)
	gold = clampi(int(data.get("gold", 25)), 0, 999999)
	world_time = maxf(0.0, float(data.get("world_time", 0.0)))

func _notification(what: int) -> void:
	if what == NOTIFICATION_WM_CLOSE_REQUEST and hosted:
		_save_world()

func _plot_center(i: int) -> Vector2:
	return FARM_ORIGIN + Vector2(i % 4, floori(float(i) / 4.0)) * FARM_STEP

func _unhandled_key_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and connected:
		if event.keycode == KEY_E or event.keycode == KEY_SPACE:
			_interact()
		elif event.keycode >= KEY_1 and event.keycode <= KEY_4:
			_select_tool(event.keycode - KEY_1)

func _select_tool(index: int) -> void:
	selected_tool = index
	_update_ui()

func _draw() -> void:
	# Formas e paleta próprias, sem assets externos. Área de jogo 1280 × 720.
	draw_rect(Rect2(0, 0, 1280, 720), Color("172d2b"))
	for y in range(135, 705, 32):
		for x in range(0, 1280, 32):
			var tint := Color("497753") if ((x / 32 + y / 32) % 3 == 0) else Color("426e4d")
			draw_rect(Rect2(x, y, 31, 31), tint)
	# trilha, lago e casa em blocos com leitura pixel art
	draw_rect(Rect2(230, 374, 800, 58), Color("a18b62"))
	draw_rect(Rect2(210, 432, 58, 220), Color("a18b62"))
	draw_rect(Rect2(900, 175, 228, 150), Color("2d6274"))
	draw_rect(Rect2(913, 187, 204, 126), Color("41859a"))
	draw_rect(Rect2(932, 205, 71, 8), Color("6bb4b0"))
	draw_rect(Rect2(1050, 272, 46, 7), Color("6bb4b0"))
	draw_rect(Rect2(171, 203, 184, 129), Color("302e32"))
	draw_rect(Rect2(181, 166, 164, 48), Color("a75d55"))
	draw_rect(Rect2(197, 211, 131, 112), Color("d7b681"))
	draw_rect(Rect2(246, 267, 38, 56), Color("564540"))
	draw_rect(Rect2(209, 232, 23, 21), Color("75b5b7"))
	for i in 12:
		var center := _plot_center(i)
		var stage: int = plots[i].stage
		draw_rect(Rect2(center - Vector2(26, 23), Vector2(52, 46)), Color("392f27"))
		draw_rect(Rect2(center - Vector2(23, 20), Vector2(46, 40)), Color("715338"))
		if stage >= 1:
			draw_rect(Rect2(center - Vector2(19, 12), Vector2(38, 3)), Color("987350"))
			draw_rect(Rect2(center - Vector2(19, 3), Vector2(38, 3)), Color("987350"))
		if stage >= 2:
			var leaf := Color("a0b77b") if stage < 4 else Color("e4bd68")
			draw_rect(Rect2(center + Vector2(-3, -15), Vector2(6, 25)), Color("315941"))
			draw_rect(Rect2(center + Vector2(-13, -12), Vector2(12, 7)), leaf)
			draw_rect(Rect2(center + Vector2(2, -17), Vector2(13, 7)), leaf)
		if stage == 3:
			draw_rect(Rect2(center + Vector2(16, 9), Vector2(5, 7)), Color("69a9c1"))
	for spot in [Vector2(70, 215), Vector2(89, 531), Vector2(1135, 490), Vector2(1190, 254)]:
		draw_rect(Rect2(spot + Vector2(-5, 14), Vector2(11, 37)), Color("614634"))
		draw_rect(Rect2(spot + Vector2(-25, -12), Vector2(50, 43)), Color("254e40"))
		draw_rect(Rect2(spot + Vector2(-16, -27), Vector2(32, 42)), Color("38735a"))
	for id in positions.keys():
		if id == 2 and not (connected and (not hosted or guest_peer_id != 0)):
			continue
		var p: Vector2 = positions[id]
		draw_rect(Rect2(p + Vector2(-14, 12), Vector2(28, 7)), Color(0.12, 0.17, 0.15, 0.5))
		draw_rect(Rect2(p + Vector2(-10, -5), Vector2(20, 23)), COLORS[id - 1])
		draw_rect(Rect2(p + Vector2(-8, -17), Vector2(16, 15)), Color("e4b992"))
		draw_rect(Rect2(p + Vector2(-10, -20), Vector2(20, 6)), Color("3c3038"))
		draw_rect(Rect2(p + Vector2(-5, -10), Vector2(3, 3)), Color("292a2d"))
		draw_rect(Rect2(p + Vector2(4, -10), Vector2(3, 3)), Color("292a2d"))

func _label(parent: Control, content: String, pos: Vector2, size: Vector2, font_size: int, color: Color) -> Label:
	var label := Label.new()
	label.text = content
	label.position = pos
	label.size = size
	label.add_theme_font_size_override("font_size", font_size)
	label.add_theme_color_override("font_color", color)
	parent.add_child(label)
	return label

func _button(parent: Control, title: String, pos: Vector2, size: Vector2, callback: Callable) -> Button:
	var button := Button.new()
	button.text = title
	button.position = pos
	button.size = size
	button.add_theme_font_size_override("font_size", 22)
	button.pressed.connect(callback)
	parent.add_child(button)
	return button

func _build_ui() -> void:
	var layer := CanvasLayer.new()
	add_child(layer)
	hud = Control.new()
	hud.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	layer.add_child(hud)
	var bar := ColorRect.new()
	bar.color = Color("192b2b")
	bar.position = Vector2.ZERO
	bar.size = Vector2(1280, 126)
	bar.mouse_filter = Control.MOUSE_FILTER_IGNORE
	hud.add_child(bar)
	_label(hud, "VALE A DOIS", Vector2(35, 14), Vector2(300, 39), 30, Color("f2ddb2"))
	room_label = _label(hud, "", Vector2(35, 54), Vector2(570, 35), 19, Color("b9d5c5"))
	inventory_label = _label(hud, "", Vector2(810, 26), Vector2(390, 48), 24, Color("f4dfb4"))
	tool_label = _label(hud, "", Vector2(35, 654), Vector2(550, 45), 22, Color("fff1c6"))
	for i in TOOLS.size():
		var b := _button(hud, TOOLS[i], Vector2(320 + i * 142, 655), Vector2(132, 53), _select_tool.bind(i))
		tool_buttons.append(b)
	_button(hud, "AÇÃO", Vector2(1110, 615), Vector2(148, 91), _interact)
	_button(hud, "+3 sementes · 5 G", Vector2(814, 140), Vector2(259, 48), _buy_seeds)
	_button(hud, "Sair", Vector2(1160, 18), Vector2(95, 42), _leave)
	for spec in [["up", "▲", 77, 534], ["left", "◀", 12, 593], ["down", "▼", 77, 593], ["right", "▶", 142, 593]]:
		var name: String = spec[0]
		var b := _button(hud, spec[1], Vector2(spec[2], spec[3]), Vector2(58, 55), func() -> void: pass)
		b.button_down.connect(func() -> void: touch_dirs[name] = true)
		b.button_up.connect(func() -> void: touch_dirs[name] = false)
	hud.visible = false
	lobby = Control.new()
	lobby.set_anchors_and_offsets_preset(Control.PRESET_FULL_RECT)
	layer.add_child(lobby)
	var shade := ColorRect.new()
	shade.color = Color("132522")
	shade.size = Vector2(1280, 720)
	lobby.add_child(shade)
	_label(lobby, "VALE A DOIS", Vector2(90, 65), Vector2(780, 70), 54, Color("f4dbac"))
	_label(lobby, "UM MUNDO PARA DOIS • FAZENDA COOPERATIVA LOCAL", Vector2(92, 143), Vector2(850, 42), 23, Color("a9c7b5"))
	_label(lobby, "1. Conecte os dois celulares ao mesmo Wi-Fi.", Vector2(92, 239), Vector2(860, 38), 23, Color("e4e6d7"))
	_label(lobby, "2. Abra o mundo no primeiro celular e anote o IP exibido.", Vector2(92, 281), Vector2(1000, 38), 23, Color("e4e6d7"))
	_label(lobby, "3. No segundo celular, digite o IP e entre.", Vector2(92, 323), Vector2(860, 38), 23, Color("e4e6d7"))
	_button(lobby, "CRIAR MUNDO (HOST)", Vector2(92, 416), Vector2(365, 68), _start_host)
	ip_edit = LineEdit.new()
	ip_edit.placeholder_text = "IP do host: 192.168.1.10"
	ip_edit.position = Vector2(495, 416)
	ip_edit.size = Vector2(351, 68)
	ip_edit.add_theme_font_size_override("font_size", 23)
	ip_edit.text_submitted.connect(func(_value: String) -> void: _start_client())
	lobby.add_child(ip_edit)
	_button(lobby, "ENTRAR", Vector2(860, 416), Vector2(203, 68), _start_client)
	status_label = _label(lobby, "Escolha host ou entre pelo IP local.", Vector2(92, 514), Vector2(1080, 70), 22, Color("f3cea0"))
	_label(lobby, "Protótipo jogável • 2 jogadores • UDP 24562 • progresso salvo no host", Vector2(92, 647), Vector2(1090, 36), 18, Color("9eb5a8"))

func _update_ui() -> void:
	if inventory_label == null:
		return
	inventory_label.text = "SEMENTES  %d     OURO  %d G" % [seeds, gold]
	tool_label.text = "Ferramenta: %s" % TOOLS[selected_tool]
	for i in tool_buttons.size():
		tool_buttons[i].disabled = i == selected_tool
