import json
import math
import random
from datetime import date
from pathlib import Path
import pygame

PRIMARY_GREEN = (53, 199, 89)
SKY_BLUE = (56, 189, 248)
SUNNY_YELLOW = (255, 213, 74)
CORAL = (255, 122, 89)
CREAM = (255, 249, 236)
SOFT_MINT = (233, 249, 238)
SOFT_BLUE = (234, 247, 255)
CHARCOAL = (24, 33, 43)
MUTED_TEXT = (86, 105, 116)
CARD_WHITE = (255, 255, 255)
SHADOW = (193, 211, 205)

scores_file = "high_scores.json"
player_file = "player_data.json"
try:
    with open(scores_file, "r") as file:
        high_scores = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    high_scores = []

try:
    with open(player_file, "r") as file:
        player_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    player_data = {"coins": 0, "coin_multiplier": 1}

coins = player_data.get("coins", 0)
coin_multiplier = player_data.get("coin_multiplier", 1)
control_mode = player_data.get("control_mode", "wasd")
if control_mode not in ("wasd", "touch", "mouse"):
    control_mode = "wasd"
new_high_score = False

MISSIONS = {
    "first_bite": ("First Bite", "Eat your first food", "foods", 1, 10),
    "food_20": ("Hungry Snake", "Eat 20 food", "foods", 20, 25),
    "score_50": ("Rising Star", "Reach score 50", "score", 50, 40),
    "coins_100": ("Collector", "Collect 100 coins", "coins", 100, 50),
    "games_5": ("Regular", "Play 5 games", "games", 5, 35),
    "combo_10": ("Combo Master", "Achieve a 10x combo", "combo", 10, 60),
    "powerups_3": ("Power User", "Collect 3 power-ups", "powerups", 3, 45),
}
ACHIEVEMENTS = {
    "first_bite": ("First Bite", "Eat your first food", "foods", 1, 10),
    "speed_demon": ("Speed Demon", "Reach level 5", "level", 5, 40),
    "combo_master": ("Combo Master", "Reach a 10x combo", "combo", 10, 60),
    "collector": ("Collector", "Collect 250 coins", "coins", 250, 75),
    "power_user": ("Power User", "Collect 5 power-ups", "powerups", 5, 50),
    "snake_legend": ("Snake Legend", "Reach a lifetime score of 500", "lifetime_score", 500, 100),
}
MAPS = {
    "jungle": ("Jungle", 0, (9, 24, 30), (20, 61, 49)),
    "desert": ("Desert", 120, (39, 28, 22), (116, 75, 42)),
    "arctic": ("Arctic", 160, (18, 35, 48), (57, 104, 126)),
    "cyber": ("Cyber City", 220, (17, 19, 38), (40, 54, 103)),
    "volcano": ("Volcano", 260, (40, 16, 18), (112, 45, 30)),
    "space": ("Space", 320, (10, 10, 27), (35, 34, 78)),
}
default_missions = {mission_id: {"progress": 0, "completed": False} for mission_id in MISSIONS}
default_achievements = {achievement_id: {"progress": 0, "unlocked": False} for achievement_id in ACHIEVEMENTS}
mission_progress = player_data.get("missions", default_missions)
achievement_progress = player_data.get("achievements", default_achievements)
daily_state = player_data.get("daily_challenge", {"date": "", "progress": 0, "completed": False})
unlocked_maps = player_data.get("unlocked_maps", ["jungle"])
selected_map = player_data.get("selected_map", "jungle")
lifetime_stats = player_data.get("lifetime_stats", {"foods": 0, "score": 0, "coins": 0, "games": 0, "powerups": 0, "golden_food": 0, "best_combo": 0})
for mission_id, defaults in default_missions.items():
    mission_progress.setdefault(mission_id, defaults.copy())
for achievement_id, defaults in default_achievements.items():
    achievement_progress.setdefault(achievement_id, defaults.copy())
if selected_map not in unlocked_maps:
    selected_map = "jungle"

def daily_target():
    day_number = date.today().toordinal()
    challenges = [("score", "Score target", 25 + day_number % 26, 30), ("foods", "Food target", 10 + day_number % 11, 25), ("combo", "Combo target", 5 + day_number % 6, 35)]
    return challenges[day_number % len(challenges)]

def ensure_daily_challenge():
    global daily_state
    today = date.today().isoformat()
    if daily_state.get("date") != today:
        daily_state = {"date": today, "progress": 0, "completed": False}

def grant_progress(kind, amount=1):
    global coins, daily_state
    ensure_daily_challenge()
    lifetime_stats[kind] = lifetime_stats.get(kind, 0) + amount
    daily_kind, _, daily_target_value, _ = daily_target()
    if daily_kind == kind and not daily_state["completed"]:
        daily_state["progress"] = min(daily_target_value, daily_state["progress"] + amount)
        if daily_state["progress"] >= daily_target_value:
            daily_state["completed"] = True
            coins += 30
    for mission_id, mission in MISSIONS.items():
        if mission[2] == kind and not mission_progress[mission_id]["completed"]:
            mission_progress[mission_id]["progress"] = min(mission[3], mission_progress[mission_id]["progress"] + amount)
            if mission_progress[mission_id]["progress"] >= mission[3]:
                mission_progress[mission_id]["completed"] = True
                coins += mission[4]
    for achievement_id, achievement in ACHIEVEMENTS.items():
        if achievement[2] == kind and not achievement_progress[achievement_id]["unlocked"]:
            achievement_progress[achievement_id]["progress"] = min(achievement[3], achievement_progress[achievement_id]["progress"] + amount)
            if achievement_progress[achievement_id]["progress"] >= achievement[3]:
                achievement_progress[achievement_id]["unlocked"] = True
                coins += achievement[4]
    save_player_data()

SHOP_CATEGORIES = {
    "colors": "Snake Colors",
    "skins": "Snake Skins",
    "outfits": "Snake Outfits",
    "foods": "Food / Fruits",
}
SHOP_ITEMS = {
    "colors": [
        ("classic_green", "Classic Green", "Common", 0, (58, 177, 120)),
        ("blue", "Blue", "Common", 15, (72, 155, 220)),
        ("red", "Red", "Common", 20, (220, 75, 85)),
        ("orange", "Orange", "Uncommon", 30, (238, 135, 58)),
        ("neon", "Neon", "Rare", 45, (90, 240, 185)),
        ("black", "Black", "Rare", 55, (42, 48, 58)),
        ("gold", "Gold", "Epic", 80, (238, 190, 70)),
        ("rainbow", "Rainbow", "Legendary", 120, (220, 95, 190)),
    ],
    "skins": [
        ("classic", "Classic", "Common", 0, "classic"),
        ("fire", "Fire", "Uncommon", 35, "fire"),
        ("ice", "Ice", "Rare", 50, "ice"),
        ("galaxy", "Galaxy", "Epic", 75, "galaxy"),
        ("toxic", "Toxic", "Rare", 60, "toxic"),
        ("lava", "Lava", "Epic", 85, "lava"),
        ("cyber", "Cyber", "Epic", 90, "cyber"),
        ("shadow", "Shadow", "Legendary", 110, "shadow"),
        ("golden", "Golden", "Legendary", 140, "golden"),
    ],
    "outfits": [
        ("none", "No Outfit", "Common", 0, "none"),
        ("crown", "Crown", "Rare", 45, "crown"),
        ("cowboy_hat", "Cowboy Hat", "Uncommon", 30, "cowboy_hat"),
        ("pirate_hat", "Pirate Hat", "Rare", 55, "pirate_hat"),
        ("wizard_hat", "Wizard Hat", "Epic", 75, "wizard_hat"),
        ("samurai_helmet", "Samurai Helmet", "Epic", 90, "samurai_helmet"),
        ("sunglasses", "Sunglasses", "Uncommon", 25, "sunglasses"),
        ("headband", "Headband", "Common", 15, "headband"),
        ("bow_tie", "Bow Tie", "Uncommon", 25, "bow_tie"),
        ("backpack", "Small Backpack", "Rare", 60, "backpack"),
        ("royal_outfit", "Royal Outfit", "Legendary", 130, "royal_outfit"),
    ],
    "foods": [
        ("apple", "Apple", "Common", 0, "apple"),
        ("orange", "Orange", "Common", 15, "orange"),
        ("strawberry", "Strawberry", "Uncommon", 25, "strawberry"),
        ("cherry", "Cherry", "Uncommon", 25, "cherry"),
        ("banana", "Banana", "Rare", 40, "banana"),
        ("watermelon", "Watermelon", "Rare", 50, "watermelon"),
        ("pineapple", "Pineapple", "Epic", 70, "pineapple"),
        ("grapes", "Grapes", "Epic", 75, "grapes"),
        ("golden_apple", "Golden Apple", "Legendary", 110, "golden_apple"),
        ("energy_orb", "Energy Orb", "Legendary", 125, "energy_orb"),
    ],
}
default_owned = {
    "colors": ["classic_green"],
    "skins": ["classic"],
    "outfits": ["none"],
    "foods": ["apple"],
}
owned_cosmetics = player_data.get("owned_cosmetics", default_owned)
equipped_cosmetics = player_data.get(
    "equipped_cosmetics",
    {"colors": "classic_green", "skins": "classic", "outfits": "none", "foods": "apple"},
)
for category, defaults in default_owned.items():
    owned_cosmetics.setdefault(category, list(defaults))
equipped_cosmetics.setdefault(category, defaults[0])

def save_player_data():
    with open(player_file, "w") as file:
        json.dump(
            {
                "coins": coins,
                "coin_multiplier": coin_multiplier,
                "owned_cosmetics": owned_cosmetics,
                "equipped_cosmetics": equipped_cosmetics,
                "missions": mission_progress,
                "achievements": achievement_progress,
                "daily_challenge": daily_state,
                "unlocked_maps": unlocked_maps,
                "selected_map": selected_map,
                "lifetime_stats": lifetime_stats,
                "control_mode": control_mode,
            },
            file,
        )

def draw_gear(surface, center, radius, color):
    for angle in range(0, 360, 45):
        radians = math.radians(angle)
        start = (
            center[0] + int(math.cos(radians) * radius * 0.55),
            center[1] + int(math.sin(radians) * radius * 0.55),
        )
        end = (
            center[0] + int(math.cos(radians) * radius),
            center[1] + int(math.sin(radians) * radius),
        )
        pygame.draw.line(surface, color, start, end, 6)
    pygame.draw.circle(surface, color, center, int(radius * 0.65))
    pygame.draw.circle(surface, (60, 90, 120), center, int(radius * 0.28))

def record_score(score):
    global new_high_score
    new_high_score = score > max(high_scores, default=0)
    high_scores.append(score)
    high_scores.sort(reverse=True)
    del high_scores[5:]
    with open(scores_file, "w") as file:
        json.dump(high_scores, file)

def spawn_food():
    while True:
        position = (
            random.randrange(0, W, 20),
            random.randrange(TOP_BAR_HEIGHT, SCREEN_HEIGHT, 20),
        )
        if position not in snake:
            return position

def respawn():
    global snake, direction, food, speed, score, round_coins, score_saved
    global screen_mode, particles, new_high_score, powerup, special_food, trap
    global active_effects, shield_charges, combo, combo_deadline, round_start_time
    if "lifetime_stats" in globals() and "mission_progress" in globals():
        grant_progress("games")
    snake = [(200, 200)]
    direction = (20, 0)
    food = spawn_food()
    speed = 3
    score = 0
    round_coins = 0
    particles = []
    powerup = None
    special_food = None
    trap = None
    active_effects = {}
    shield_charges = 0
    combo = 0
    combo_deadline = 0
    round_start_time = pygame.time.get_ticks()
    new_high_score = False
    score_saved = False
    screen_mode = "game"

pygame.init()
TOP_BAR_HEIGHT = 80
SCREEN_HEIGHT = 720
W = SCREEN_HEIGHT
PLAY_HEIGHT = SCREEN_HEIGHT - TOP_BAR_HEIGHT
screen = pygame.display.set_mode((W, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

def outline_button(button):
    pygame.draw.rect(screen, (255, 255, 255), button, 2, border_radius=10)

def draw_button(button, label):
    hovered = button.collidepoint(pygame.mouse.get_pos())
    important = label in ("Start", "Respawn", "Resume")
    fill = PRIMARY_GREEN if important else SKY_BLUE
    if hovered:
        fill = tuple(min(255, channel + 15) for channel in fill)
    shadow_rect = button.move(0, 4)
    pygame.draw.rect(screen, SHADOW, shadow_rect, border_radius=10)
    pygame.draw.rect(screen, fill, button, border_radius=10)
    outline_button(button)
    text_font = font
    if font.size(label)[0] > button.width - 24:
        text_font = pygame.font.SysFont("trebuchet ms", max(14, min(font.get_height() - 2, button.width // 9)), bold=True)
    text = text_font.render(label, True, CARD_WHITE)
    icon = icon_images.get(label)
    if icon:
        icon_size = max(18, min(26, button.height - 12))
        icon_surface = pygame.transform.smoothscale(icon, (icon_size, icon_size))
        group_width = icon_size + 10 + text.width
        group_left = button.centerx - group_width // 2
        screen.blit(icon_surface, (group_left, button.centery - icon_size // 2))
        text_position = text.get_rect(midleft=(group_left + icon_size + 10, button.centery))
    else:
        text_position = text.get_rect(center=button.center)
    screen.blit(text, text_position)

def draw_map_ambience(map_id):
    ambience = pygame.Surface((W, SCREEN_HEIGHT), pygame.SRCALPHA)
    accent = MAPS.get(map_id, MAPS["jungle"])[3]
    if map_id == "jungle":
        for x in range(36, W, 120):
            pygame.draw.line(ambience, (*accent, 55), (x, TOP_BAR_HEIGHT + 20), (x + 24, TOP_BAR_HEIGHT + 8), 5)
            pygame.draw.line(ambience, (*accent, 45), (x + 16, TOP_BAR_HEIGHT + 22), (x + 2, TOP_BAR_HEIGHT + 38), 4)
    elif map_id == "desert":
        for x in range(50, W, 140):
            pygame.draw.arc(ambience, (*accent, 50), (x, SCREEN_HEIGHT - 100, 90, 48), math.pi, math.tau, 3)
            pygame.draw.circle(ambience, (255, 214, 124, 55), (x + 20, TOP_BAR_HEIGHT + 54), 3)
    elif map_id == "arctic":
        for x in range(25, W, 105):
            pygame.draw.polygon(ambience, (255, 255, 255, 80), [(x, TOP_BAR_HEIGHT + 8), (x + 18, TOP_BAR_HEIGHT + 8), (x + 9, TOP_BAR_HEIGHT + 28)])
    elif map_id == "cyber":
        for x in range(30, W, 90):
            pygame.draw.line(ambience, (*accent, 70), (x, TOP_BAR_HEIGHT + 10), (x, SCREEN_HEIGHT - 10), 2)
        for y in range(TOP_BAR_HEIGHT + 20, SCREEN_HEIGHT, 90):
            pygame.draw.line(ambience, (*accent, 45), (0, y), (W, y), 2)
    elif map_id == "volcano":
        for x in range(30, W, 150):
            pygame.draw.polygon(ambience, (255, 133, 74, 65), [(x, SCREEN_HEIGHT - 12), (x + 24, SCREEN_HEIGHT - 52), (x + 48, SCREEN_HEIGHT - 12)])
    else:
        for index in range(12):
            x = (index * 97 + 32) % max(1, W)
            y = TOP_BAR_HEIGHT + 18 + (index * 61) % max(1, PLAY_HEIGHT - 30)
            pygame.draw.circle(ambience, (255, 255, 255, 85), (x, y), 2 + index % 2)
    screen.blit(ambience, (0, 0))

def draw_grid():
    map_data = MAPS.get(selected_map, MAPS["jungle"])
    background, accent = map_data[2], map_data[3]
    # Use the selected map palette for the full play area, not only its ambience.
    grid_color = tuple((base * 2 + detail) // 3 for base, detail in zip(background, accent))
    screen.fill(background)
    pygame.draw.rect(screen, background, (0, TOP_BAR_HEIGHT, W, SCREEN_HEIGHT - TOP_BAR_HEIGHT))
    for x in range(0, W + 1, 20):
        pygame.draw.line(screen, grid_color, (x, TOP_BAR_HEIGHT), (x, SCREEN_HEIGHT))
    for y in range(TOP_BAR_HEIGHT, SCREEN_HEIGHT + 1, 20):
        pygame.draw.line(screen, grid_color, (0, y), (W, y))
    for x in range(20, W, 80):
        pygame.draw.line(screen, map_data[3], (x, SCREEN_HEIGHT - 8), (x + 5, SCREEN_HEIGHT - 22), 2)
    draw_map_ambience(selected_map)

def get_shop_item(category, item_id):
    for item in SHOP_ITEMS[category]:
        if item[0] == item_id:
            return item
    return SHOP_ITEMS[category][0]

def snake_palette(index):
    color_item = get_shop_item("colors", equipped_cosmetics["colors"])
    base = color_item[4]
    skin = equipped_cosmetics["skins"]
    if skin == "fire":
        base = (235, 75 + (index * 9) % 55, 45)
    elif skin == "ice":
        base = (75, 170 + (index * 7) % 55, 235)
    elif skin == "galaxy":
        base = (75 + (index * 8) % 45, 52, 135 + (index * 5) % 55)
    elif skin == "toxic":
        base = (74, 210, 75 + (index * 8) % 75)
    elif skin == "lava":
        base = (180 + (index * 7) % 70, 42, 30)
    elif skin == "cyber":
        base = (35, 180 + (index * 6) % 60, 210)
    elif skin == "shadow":
        base = (38 + index * 3 % 28, 45 + index * 3 % 30, 60 + index * 4 % 35)
    elif skin == "golden":
        base = (220, 155 + (index * 7) % 55, 42)
    if equipped_cosmetics["colors"] == "rainbow":
        hue = (index * 0.08 + pygame.time.get_ticks() / 3000) % 1
        color = pygame.Color(0)
        color.hsva = (hue * 360, 72, 96, 100)
        base = color[:3]
    if index == 0:
        return tuple(min(255, value + 35) for value in base)
    return base

def draw_food():
    pulse = 1 + 0.12 * math.sin(pygame.time.get_ticks() / 150)
    center = (food[0] + 10, food[1] + 10)
    food_type = equipped_cosmetics["foods"]
    glow = pygame.Surface((44, 44), pygame.SRCALPHA)
    pygame.draw.circle(glow, (255, 196, 91, 45), (22, 22), int(16 * pulse))
    screen.blit(glow, (center[0] - 22, center[1] - 22))
    if food_type in ("apple", "golden_apple"):
        color = (238, 190, 70) if food_type == "golden_apple" else (255, 75, 83)
        pygame.draw.circle(screen, color, center, int(8 * pulse))
        pygame.draw.line(screen, (84, 166, 87), (center[0], center[1] - 7), (center[0] + 4, center[1] - 13), 2)
    elif food_type == "orange":
        pygame.draw.circle(screen, (243, 143, 45), center, int(8 * pulse))
        pygame.draw.arc(screen, (255, 205, 92), (center[0] - 5, center[1] - 5, 10, 10), 0.4, 2.5, 2)
    elif food_type == "strawberry":
        pygame.draw.polygon(screen, (232, 60, 76), [(center[0], center[1] + 9), (center[0] - 9, center[1] - 5), (center[0] + 9, center[1] - 5)])
        pygame.draw.circle(screen, (90, 204, 102), (center[0], center[1] - 7), 4)
    elif food_type == "cherry":
        pygame.draw.circle(screen, (230, 52, 72), (center[0] - 5, center[1] + 2), 6)
        pygame.draw.circle(screen, (230, 52, 72), (center[0] + 6, center[1] + 2), 6)
        pygame.draw.line(screen, (90, 204, 102), center, (center[0] + 4, center[1] - 10), 2)
    elif food_type == "banana":
        pygame.draw.arc(screen, (249, 210, 61), (center[0] - 10, center[1] - 7, 20, 18), 0.3, 2.6, 5)
    elif food_type == "watermelon":
        pygame.draw.arc(screen, (74, 195, 103), (center[0] - 10, center[1] - 7, 20, 18), 0, math.pi, 6)
        pygame.draw.arc(screen, (239, 83, 94), (center[0] - 7, center[1] - 4, 14, 13), 0, math.pi, 4)
    elif food_type == "pineapple":
        pygame.draw.polygon(screen, (241, 183, 61), [(center[0], center[1] - 9), (center[0] + 8, center[1] + 7), (center[0], center[1] + 10), (center[0] - 8, center[1] + 7)])
        pygame.draw.polygon(screen, (88, 193, 105), [(center[0], center[1] - 10), (center[0] - 7, center[1] - 15), (center[0], center[1] - 13), (center[0] + 6, center[1] - 16)])
    elif food_type == "grapes":
        for offset in ((-5, -2), (5, -2), (-5, 6), (5, 6), (0, 13)):
            pygame.draw.circle(screen, (143, 83, 205), (center[0] + offset[0], center[1] + offset[1]), 5)
    elif food_type == "energy_orb":
        pygame.draw.circle(screen, (75, 220, 255), center, int(8 * pulse))
        pygame.draw.circle(screen, (210, 250, 255), (center[0] - 3, center[1] - 3), 2)
    else:
        pygame.draw.circle(screen, (255, 93, 91), center, int(8 * pulse))
    pygame.draw.circle(screen, (255, 220, 172), (center[0] - 3, center[1] - 3), 2)
    sparkle = int(2 + 2 * math.sin(pygame.time.get_ticks() / 190))
    pygame.draw.line(screen, CARD_WHITE, (center[0] + 9, center[1] - 9 - sparkle), (center[0] + 9, center[1] - 5 + sparkle), 1)
    pygame.draw.line(screen, CARD_WHITE, (center[0] + 7, center[1] - 7), (center[0] + 11, center[1] - 7), 1)

def draw_special_food():
    if not special_food:
        return
    position, food_type = special_food
    center = (position[0] + 10, position[1] + 10)
    colors = {"golden": (247, 204, 70), "crystal": (117, 225, 255), "ice": (176, 241, 255), "energy": (222, 91, 255), "fire": (255, 101, 54)}
    color = colors[food_type]
    pulse = 12 + int(3 * math.sin(pygame.time.get_ticks() / 120))
    pygame.draw.circle(screen, tuple(max(0, value // 3) for value in color), center, pulse + 7)
    pygame.draw.polygon(screen, color, [(center[0], center[1] - pulse), (center[0] + pulse, center[1]), (center[0], center[1] + pulse), (center[0] - pulse, center[1])])
    label = font.render(food_type.upper(), True, color)
    screen.blit(label, label.get_rect(center=(center[0], center[1] - 22)))

def draw_powerup():
    if not powerup:
        return
    position, powerup_type, _ = powerup
    center = (position[0] + 10, position[1] + 10)
    colors = {"magnet": (255, 91, 139), "slow": (92, 181, 255), "coin": (247, 204, 70), "shield": (112, 224, 210), "ghost": (192, 157, 255), "double": (255, 145, 74)}
    color = colors[powerup_type]
    pygame.draw.circle(screen, tuple(max(0, value // 3) for value in color), center, 17)
    pygame.draw.circle(screen, color, center, 10, 3)
    if powerup_type == "magnet":
        pygame.draw.arc(screen, CARD_WHITE, (center[0] - 6, center[1] - 7, 12, 14), 0, math.pi, 2)
        pygame.draw.line(screen, CARD_WHITE, (center[0] - 6, center[1]), (center[0] - 6, center[1] + 5), 2)
        pygame.draw.line(screen, CARD_WHITE, (center[0] + 6, center[1]), (center[0] + 6, center[1] + 5), 2)
    elif powerup_type == "shield":
        pygame.draw.polygon(screen, CARD_WHITE, [(center[0], center[1] - 7), (center[0] + 7, center[1] - 3), (center[0] + 5, center[1] + 6), (center[0], center[1] + 10), (center[0] - 5, center[1] + 6), (center[0] - 7, center[1] - 3)], 2)
    elif powerup_type == "slow":
        pygame.draw.circle(screen, CARD_WHITE, center, 7, 2)
        pygame.draw.line(screen, CARD_WHITE, center, (center[0], center[1] - 5), 2)
        pygame.draw.line(screen, CARD_WHITE, center, (center[0] + 4, center[1] + 3), 2)
    elif powerup_type == "ghost":
        pygame.draw.arc(screen, CARD_WHITE, (center[0] - 7, center[1] - 8, 14, 16), math.pi, math.tau, 2)
        pygame.draw.circle(screen, CARD_WHITE, (center[0] - 3, center[1] - 1), 1)
        pygame.draw.circle(screen, CARD_WHITE, (center[0] + 3, center[1] - 1), 1)
    elif powerup_type in ("coin", "double"):
        pygame.draw.circle(screen, CARD_WHITE, center, 6, 2)
        pygame.draw.line(screen, CARD_WHITE, (center[0] - 2, center[1] + 9), (center[0] + 5, center[1] + 2), 2)
        pygame.draw.line(screen, CARD_WHITE, (center[0] + 5, center[1] + 2), (center[0] + 3, center[1] + 2), 2)
        pygame.draw.line(screen, CARD_WHITE, (center[0] + 5, center[1] + 2), (center[0] + 5, center[1] + 5), 2)

def activate_powerup(powerup_type):
    global shield_charges
    now = pygame.time.get_ticks()
    durations = {"magnet": 10000, "slow": 10000, "coin": 10000, "ghost": 10000, "double": 10000}
    if powerup_type == "shield":
        shield_charges = 1
        active_effects["shield"] = now + 10000
    else:
        active_effects[powerup_type] = now + durations[powerup_type]
    spawn_particles(snake[0])
    grant_progress("powerups")

def effect_active(effect_type):
    return active_effects.get(effect_type, 0) > pygame.time.get_ticks()

def maybe_spawn_pickups():
    global powerup, special_food, trap, shield_charges
    now = pygame.time.get_ticks()
    if powerup and now - powerup[2] >= 5000:
        powerup = None
    if trap and now - trap[1] >= 5000:
        trap = None
    if active_effects.get("shield", 0) <= now:
        shield_charges = 0
    if powerup is None and random.random() < 0.004:
        powerup = (spawn_food(), random.choice(("magnet", "slow", "coin", "shield", "ghost", "double")), now)
    if special_food is None and random.random() < 0.003:
        special_food = (spawn_food(), random.choice(("golden", "crystal", "ice", "energy", "fire")))
    if trap is None and random.random() < 0.002:
        trap = (spawn_food(), now)

def draw_trap():
    if not trap:
        return
    position, _ = trap
    x, y = position
    pygame.draw.rect(screen, (79, 25, 31), (x + 2, y + 13, 16, 6), border_radius=2)
    for offset in (1, 7, 13):
        pygame.draw.polygon(screen, (232, 79, 63), [(x + offset, y + 14), (x + offset + 3, y + 3), (x + offset + 6, y + 14)])

def draw_snake():
    if shield_charges or effect_active("ghost") or effect_active("magnet"):
        aura_color = (112, 224, 210) if shield_charges else (192, 157, 255) if effect_active("ghost") else (255, 91, 139)
        pygame.draw.circle(screen, aura_color, (snake[0][0] + 10, snake[0][1] + 10), 17, 2)
    for index, segment in enumerate(snake):
        shadow = pygame.Rect(segment[0] + 3, segment[1] + 4, 20, 20)
        pygame.draw.rect(screen, (121, 172, 166), shadow, border_radius=8)
        color = snake_palette(index)
        pygame.draw.rect(screen, color, (*segment, 20, 20), border_radius=8)
        pygame.draw.line(screen, tuple(min(255, value + 45) for value in color), (segment[0] + 5, segment[1] + 4), (segment[0] + 14, segment[1] + 4), 2)
        skin = equipped_cosmetics["skins"]
        if skin in ("galaxy", "cyber") and index % 3 == 0:
            pygame.draw.circle(screen, (200, 240, 255), (segment[0] + 7, segment[1] + 6), 2)
        elif skin in ("fire", "lava") and index % 2 == 0:
            pygame.draw.line(screen, (255, 190, 65), (segment[0] + 5, segment[1] + 15), (segment[0] + 15, segment[1] + 5), 2)
        elif skin == "ice":
            pygame.draw.line(screen, (185, 245, 255), (segment[0] + 5, segment[1] + 5), (segment[0] + 15, segment[1] + 15), 2)
    draw_snake_outfit()

    head = snake[0]
    center = (head[0] + 10, head[1] + 10)
    if direction[0] > 0:
        eyes = [(center[0] + 5, center[1] - 4), (center[0] + 5, center[1] + 4)]
    elif direction[0] < 0:
        eyes = [(center[0] - 5, center[1] - 4), (center[0] - 5, center[1] + 4)]
    elif direction[1] < 0:
        eyes = [(center[0] - 4, center[1] - 5), (center[0] + 4, center[1] - 5)]
    else:
        eyes = [(center[0] - 4, center[1] + 5), (center[0] + 4, center[1] + 5)]
    for eye in eyes:
        pygame.draw.circle(screen, (245, 255, 240), eye, 3)
        pygame.draw.circle(screen, (12, 25, 25), eye, 1)
    cheek = (center[0] + 7, center[1] + 7) if direction[0] >= 0 else (center[0] - 7, center[1] + 7)
    pygame.draw.circle(screen, (255, 157, 145), cheek, 2)

def draw_snake_outfit():
    outfit = equipped_cosmetics["outfits"]
    head = snake[0]
    center = (head[0] + 10, head[1] + 10)
    if outfit == "crown":
        pygame.draw.polygon(screen, (247, 204, 70), [(center[0] - 10, center[1] - 8), (center[0] - 6, center[1] - 18), (center[0], center[1] - 10), (center[0] + 6, center[1] - 18), (center[0] + 11, center[1] - 8)])
    elif outfit == "cowboy_hat":
        pygame.draw.ellipse(screen, (126, 76, 40), (center[0] - 16, center[1] - 13, 32, 9))
        pygame.draw.rect(screen, (157, 95, 48), (center[0] - 9, center[1] - 22, 18, 13), border_radius=4)
    elif outfit == "pirate_hat":
        pygame.draw.ellipse(screen, (28, 28, 38), (center[0] - 16, center[1] - 13, 32, 9))
        pygame.draw.rect(screen, (39, 39, 53), (center[0] - 10, center[1] - 23, 20, 13), border_radius=4)
        pygame.draw.circle(screen, (240, 220, 172), center, 3)
    elif outfit == "wizard_hat":
        pygame.draw.polygon(screen, (92, 64, 176), [(center[0] - 13, center[1] - 8), (center[0], center[1] - 28), (center[0] + 13, center[1] - 8)])
        pygame.draw.ellipse(screen, (113, 81, 203), (center[0] - 16, center[1] - 11, 32, 9))
    elif outfit == "samurai_helmet":
        pygame.draw.arc(screen, (178, 184, 199), (center[0] - 14, center[1] - 19, 28, 22), math.pi, math.tau, 5)
        pygame.draw.line(screen, (220, 75, 88), (center[0], center[1] - 22), (center[0], center[1] - 7), 3)
    elif outfit == "sunglasses":
        pygame.draw.line(screen, (18, 22, 29), (center[0] - 9, center[1] - 3), (center[0] + 9, center[1] - 3), 3)
        pygame.draw.circle(screen, (24, 30, 40), (center[0] - 5, center[1] - 3), 5)
        pygame.draw.circle(screen, (24, 30, 40), (center[0] + 5, center[1] - 3), 5)
    elif outfit == "headband":
        pygame.draw.line(screen, (224, 61, 74), (center[0] - 12, center[1] - 8), (center[0] + 12, center[1] - 8), 4)
    elif outfit == "bow_tie":
        pygame.draw.polygon(screen, (224, 61, 74), [(center[0] - 10, center[1] + 9), (center[0] - 1, center[1] + 5), (center[0] - 1, center[1] + 14)])
        pygame.draw.polygon(screen, (224, 61, 74), [(center[0] + 10, center[1] + 9), (center[0] + 1, center[1] + 5), (center[0] + 1, center[1] + 14)])
    elif outfit == "backpack" and len(snake) > 2:
        pygame.draw.rect(screen, (171, 92, 56), (snake[-1][0] - 2, snake[-1][1] + 2, 14, 16), border_radius=4)
    elif outfit == "royal_outfit":
        pygame.draw.circle(screen, (247, 204, 70), (head[0] + 10, head[1] - 8), 5)
        pygame.draw.line(screen, (247, 204, 70), (head[0] + 4, head[1] - 7), (head[0] + 16, head[1] - 7), 3)

def spawn_particles(position):
    for _ in range(12):
        angle = random.random() * math.tau
        velocity = random.uniform(1.0, 2.8)
        particles.append([
            position[0] + 10,
            position[1] + 10,
            math.cos(angle) * velocity,
            math.sin(angle) * velocity,
            24,
        ])

def update_particles():
    for particle in particles[:]:
        particle[0] += particle[2]
        particle[1] += particle[3]
        particle[4] -= 1
        if particle[4] <= 0:
            particles.remove(particle)
        else:
            pygame.draw.circle(
                screen,
                (255, 196, 91),
                (int(particle[0]), int(particle[1])),
                max(1, particle[4] // 8),
            )

def draw_high_score_effect():
    if new_high_score and pygame.time.get_ticks() % 900 < 450:
        overlay = pygame.Surface((W, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 215, 100, 24))
        screen.blit(overlay, (0, 0))
        message = big_font.render("NEW HIGH SCORE", True, (255, 220, 110))
        screen.blit(message, message.get_rect(center=(W // 2, TOP_BAR_HEIGHT + 55)))

def draw_home_scene():
    scale = min(W, SCREEN_HEIGHT) / 720
    now = pygame.time.get_ticks()
    screen.fill(CREAM)
    pygame.draw.rect(screen, SOFT_BLUE, (0, TOP_BAR_HEIGHT, W, SCREEN_HEIGHT - TOP_BAR_HEIGHT))
    pygame.draw.circle(screen, (193, 235, 255), (int(W * 0.52), int(SCREEN_HEIGHT * 0.16)), int(150 * scale))
    pygame.draw.circle(screen, (220, 245, 255), (int(W * 0.52), int(SCREEN_HEIGHT * 0.16)), int(112 * scale))

    # Slow fireflies and layered leaves add atmosphere without heavy effects.
    for index in range(10):
        firefly_x = int(W * (0.10 + (index * 0.083) % 0.82))
        firefly_y = int(SCREEN_HEIGHT * (0.12 + ((index * 0.071) % 0.20)))
        glow = 2 + int(2 * math.sin(now / 500 + index))
        pygame.draw.circle(screen, SUNNY_YELLOW, (firefly_x, firefly_y), max(1, glow))

    foliage_color = (113, 211, 133)
    pygame.draw.polygon(screen, foliage_color, [(0, 60), (80, 42), (46, 78), (132, 66), (54, 103), (0, 92)])
    pygame.draw.polygon(screen, (83, 190, 112), [(W, 54), (W - 86, 38), (W - 52, 78), (W - 150, 66), (W - 60, 106), (W, 94)])
    pygame.draw.line(screen, (53, 160, 91), (0, 68), (76, 48), 2)
    pygame.draw.line(screen, (53, 160, 91), (W, 64), (W - 72, 45), 2)
    pygame.draw.ellipse(
        screen,
        (207, 239, 247),
        (int(W * 0.08), int(SCREEN_HEIGHT * 0.12), int(W * 0.84), int(SCREEN_HEIGHT * 0.34)),
    )

    # Small environmental details keep the scene grounded without competing with the menu.
    ground_y = int(SCREEN_HEIGHT * 0.28)
    pygame.draw.ellipse(screen, (180, 232, 184), (int(W * 0.08), ground_y, int(W * 0.84), int(55 * scale)))
    for x in range(int(W * 0.12), int(W * 0.9), max(18, int(28 * scale))):
        pygame.draw.line(screen, (53, 160, 91), (x, ground_y + 34), (x - 5, ground_y + 18), 2)
        pygame.draw.line(screen, (53, 160, 91), (x, ground_y + 34), (x + 7, ground_y + 20), 2)

    for rock_x, rock_y, rock_size in ((0.16, 0.30, 18), (0.82, 0.31, 14)):
        rock = pygame.Rect(
            int(W * rock_x),
            int(SCREEN_HEIGHT * rock_y),
            int(rock_size * scale),
            int(rock_size * 0.7 * scale),
        )
        pygame.draw.ellipse(screen, (143, 180, 187), rock)
        pygame.draw.arc(screen, (94, 137, 145), rock, math.pi, math.tau, 2)

    apple = (
        int(W * 0.73 + math.sin(now / 850) * 5 * scale),
        int(SCREEN_HEIGHT * 0.19 + math.sin(now / 650) * 4 * scale),
    )
    pygame.draw.circle(screen, (255, 191, 87), apple, int(24 * scale))
    pygame.draw.circle(screen, CORAL, apple, int(12 * scale))
    pygame.draw.circle(screen, (255, 174, 126), (apple[0] - 4, apple[1] - 4), max(2, int(3 * scale)))
    pygame.draw.line(screen, (53, 160, 91), (apple[0], apple[1] - 11), (apple[0] + 5, apple[1] - 19), 3)
    pygame.draw.ellipse(screen, (83, 190, 112), (apple[0] + 3, apple[1] - 20, int(12 * scale), int(6 * scale)))

    # Each segment has its own shadow, body tone, and highlight to suggest volume.
    phase = now / 2600
    center_x = W * 0.46
    center_y = SCREEN_HEIGHT * 0.20
    radius_x = min(W * 0.25, 185 * scale)
    radius_y = min(SCREEN_HEIGHT * 0.075, 52 * scale)
    segments = []
    for index in range(15):
        angle = phase * math.tau - index * 0.22
        x = center_x + math.cos(angle) * radius_x + math.sin(angle * 2) * 18 * scale
        y = center_y + math.sin(angle * 1.7) * radius_y
        depth = 0.82 + 0.18 * math.sin(angle + 0.8)
        segments.append((int(x), int(y), max(8, int(15 * scale * depth))))

    for (x1, y1, radius1), (x2, y2, radius2) in zip(segments, segments[1:]):
        pygame.draw.line(screen, (125, 174, 178), (x1 + 4, y1 + 5), (x2 + 4, y2 + 5), radius1 * 2 + 7)
        pygame.draw.line(screen, PRIMARY_GREEN, (x1, y1), (x2, y2), radius1 * 2)

    for index, (x, y, radius) in enumerate(reversed(segments)):
        color = snake_palette(index)
        highlight = tuple(min(255, value + 42) for value in color)
        pygame.draw.circle(screen, (125, 174, 178), (x + 4, y + 6), radius + 3)
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.draw.circle(screen, highlight, (x - radius // 3, y - radius // 3), max(2, radius // 3))
        if index % 3 == 0:
            pygame.draw.arc(screen, (24, 150, 73), (x - radius, y - radius, radius * 2, radius * 2), 0.5, 2.5, 2)

    head_x, head_y, head_radius = segments[0]
    pygame.draw.circle(screen, (97, 220, 119), (head_x, head_y), head_radius + 2)
    head_dx = segments[0][0] - segments[1][0]
    head_dy = segments[0][1] - segments[1][1]
    if abs(head_dx) >= abs(head_dy):
        eye_x = 5 if head_dx >= 0 else -5
        eyes = [(head_x + eye_x, head_y - 4), (head_x + eye_x, head_y + 4)]
        tongue_start = (head_x + eye_x * 2, head_y)
        tongue_end = (tongue_start[0] + (9 if head_dx >= 0 else -9), head_y - 3)
    else:
        eye_y = 5 if head_dy >= 0 else -5
        eyes = [(head_x - 4, head_y + eye_y), (head_x + 4, head_y + eye_y)]
        tongue_start = (head_x, head_y + eye_y * 2)
        tongue_end = (head_x + 3, tongue_start[1] + (9 if head_dy >= 0 else -9))
    for eye in eyes:
        pygame.draw.circle(screen, (245, 255, 235), eye, max(2, int(4 * scale)))
        pygame.draw.circle(screen, (12, 26, 25), eye, max(1, int(2 * scale)))
    pygame.draw.line(screen, CORAL, tongue_start, tongue_end, 2)

def draw_game_header():
    pygame.draw.rect(screen, CREAM, (0, 0, W, TOP_BAR_HEIGHT))
    pygame.draw.line(screen, (198, 226, 213), (0, TOP_BAR_HEIGHT - 1), (W, TOP_BAR_HEIGHT - 1), 2)
    high_score = max(high_scores, default=0)
    level = 1 + int((speed - BASE_SPEED) // 2.5)
    stats = [(f"SCORE  {score}", PRIMARY_GREEN), (f"BEST  {high_score}", SKY_BLUE), (f"LEVEL  {level}", CORAL), (f"COINS  {round_coins}", SUNNY_YELLOW)]
    panel_width = max(84, W // 5)
    header_font = pygame.font.SysFont("trebuchet ms", max(12, min(18, panel_width // 6)), bold=True)
    for index, (label, color) in enumerate(stats):
        panel = pygame.Rect(8 + index * panel_width, 5, panel_width - 8, 30)
        pygame.draw.rect(screen, CARD_WHITE, panel, border_radius=8)
        pygame.draw.rect(screen, color, panel, 2, border_radius=8)
        label_surface = header_font.render(label, True, CHARCOAL)
        screen.blit(label_surface, label_surface.get_rect(center=panel.center))
    if combo > 1 and pygame.time.get_ticks() <= combo_deadline:
        combo_text = font.render(f"COMBO x{combo}", True, CORAL)
        screen.blit(combo_text, combo_text.get_rect(center=(W // 2, TOP_BAR_HEIGHT + 22)))

def change_direction(new_direction):
    global direction
    if new_direction != (-direction[0], -direction[1]):
        direction = new_direction

def pointer_direction(start, end):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]
    if max(abs(delta_x), abs(delta_y)) < 18:
        return
    if abs(delta_x) > abs(delta_y):
        change_direction((20 if delta_x > 0 else -20, 0))
    else:
        change_direction((0, 20 if delta_y > 0 else -20))

def follow_mouse():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    head_center = (snake[0][0] + 10, snake[0][1] + 10)
    delta_x = mouse_x - head_center[0]
    delta_y = mouse_y - head_center[1]
    if max(abs(delta_x), abs(delta_y)) < 24:
        return
    if abs(delta_x) > abs(delta_y):
        change_direction((20 if delta_x > 0 else -20, 0))
    else:
        change_direction((0, 20 if delta_y > 0 else -20))

snake =[(200,200)]
direction =(20,0)
food = spawn_food()
speed = 3
score = 0
round_coins = 0
particles = []
powerup = None
special_food = None
trap = None
active_effects = {}
shield_charges = 0
combo = 0
combo_deadline = 0
round_start_time = 0
BASE_SPEED = 3
font = pygame.font.SysFont("trebuchet ms", 28, bold=True)
big_font = pygame.font.SysFont("trebuchet ms", 42, bold=True)
ICON_DIR = Path(__file__).with_name("assets") / "icons"
icon_images = {}
for icon_label, icon_file in {
    "Start": "start.png",
    "Pause": "pause.png",
    "Restart": "restart.png",
    "Settings": "settings.png",
    "Shop": "shop.png",
    "High Score": "high_score.png",
    "Quit": "quit.png",
}.items():
    icon_path = ICON_DIR / icon_file
    if icon_path.exists():
        icon_images[icon_label] = pygame.image.load(str(icon_path)).convert_alpha()
pause_button = pygame.Rect(575, 5, 85, 30)
restart_button = pygame.Rect(480, 5, 85, 30)
settings_button = pygame.Rect(675, 5, 45, 30)
start_button = pygame.Rect(210, 150, 300, 45)
menu_high_score_button = pygame.Rect(210, 205, 300, 45)
shop_button = pygame.Rect(210, 260, 300, 45)
menu_settings_button = pygame.Rect(210, 315, 300, 45)
quit_button = pygame.Rect(210, 370, 300, 45)
classic_button = pygame.Rect(210, 220, 300, 45)
endless_button = pygame.Rect(210, 285, 300, 45)
resume_button = pygame.Rect(210, 220, 300, 45)
pause_menu_button = pygame.Rect(210, 285, 300, 45)
respawn_button = pygame.Rect(210, 220, 300, 45)
high_score_button = pygame.Rect(210, 285, 300, 45)
shop_booster_button = pygame.Rect(160, 220, 400, 50)
profile_button = pygame.Rect(14, 12, 190, 38)
shop_category = "colors"
shop_message = ""
shop_message_until = 0
map_buttons = {}

def update_layout():
    global W, SCREEN_HEIGHT, PLAY_HEIGHT, font, big_font
    global pause_button, restart_button, settings_button, start_button
    global menu_high_score_button, shop_button, menu_settings_button, quit_button
    global missions_button, daily_button, achievements_button, maps_button
    global classic_button, endless_button, resume_button, pause_menu_button
    global respawn_button, high_score_button, shop_booster_button, profile_button

    W, SCREEN_HEIGHT = screen.get_size()
    PLAY_HEIGHT = max(40, SCREEN_HEIGHT - TOP_BAR_HEIGHT)
    scale = min(W, SCREEN_HEIGHT) / 720
    font = pygame.font.SysFont("trebuchet ms", max(18, int(28 * scale)), bold=True)
    big_font = pygame.font.SysFont("trebuchet ms", max(28, int(42 * scale)), bold=True)

    narrow_layout = W < 600
    button_width = min(300, max(130, W - 30 if narrow_layout else (W - 30) // 2))
    button_height = max(34, min(50, int(SCREEN_HEIGHT * 0.06)))
    button_x = (W - button_width) // 2
    button_gap = max(10, int(button_height * 0.35))

    menu_start_y = max(150 if narrow_layout else 170, int(SCREEN_HEIGHT * 0.43))
    column_gap = max(10, W - button_width * 2 - 20)
    left_x = max(10, (W - button_width * 2 - column_gap) // 2)
    right_x = left_x + button_width + column_gap
    if narrow_layout:
        menu_rects = [
            pygame.Rect(button_x, menu_start_y + index * (button_height + button_gap), button_width, button_height)
            for index in range(9)
        ]
    else:
        positions = [
            (left_x, menu_start_y), (right_x, menu_start_y),
            (left_x, menu_start_y + button_height + button_gap),
            (right_x, menu_start_y + button_height + button_gap),
            (left_x, menu_start_y + 2 * (button_height + button_gap)),
            (right_x, menu_start_y + 2 * (button_height + button_gap)),
            (left_x, menu_start_y + 3 * (button_height + button_gap)),
            (right_x, menu_start_y + 3 * (button_height + button_gap)),
            (left_x, menu_start_y + 4 * (button_height + button_gap)),
        ]
        menu_rects = [pygame.Rect(x, y, button_width, button_height) for x, y in positions]
    (
        start_button, menu_high_score_button, shop_button, menu_settings_button,
        quit_button, missions_button, daily_button, achievements_button, maps_button,
    ) = menu_rects

    classic_button = pygame.Rect(button_x, int(SCREEN_HEIGHT * 0.31), button_width, button_height)
    endless_button = classic_button.move(0, button_height + button_gap)
    resume_button = classic_button.copy()
    pause_menu_button = endless_button.copy()
    respawn_button = classic_button.copy()
    high_score_button = endless_button.copy()
    shop_booster_button = pygame.Rect(
        max(20, (W - min(400, W - 40)) // 2),
        int(SCREEN_HEIGHT * 0.31),
        min(400, W - 40),
        button_height,
    )
    profile_button = pygame.Rect(14, 12, min(190, max(120, W // 3)), 38)

    controls_y = TOP_BAR_HEIGHT // 2 + 4
    settings_width = min(40, max(32, W // 8))
    control_width = max(48, min(85, (W - settings_width - 28) // 2))
    settings_button = pygame.Rect(max(5, W - settings_width - 5), controls_y, settings_width, 30)
    pause_button = pygame.Rect(max(5, settings_button.left - control_width - 6), controls_y, control_width, 30)
    restart_button = pygame.Rect(max(5, pause_button.left - control_width - 6), controls_y, control_width, 30)

update_layout()

def shop_layout():
    global shop_booster_button
    tab_rows = 2 if W < 600 else 1
    tab_columns = 2 if tab_rows == 2 else 4
    tab_gap = 8
    tab_width = (W - 20 - tab_gap * (tab_columns - 1)) // tab_columns
    tabs = {}
    for index, category in enumerate(SHOP_CATEGORIES):
        row, column = divmod(index, tab_columns)
        tabs[category] = pygame.Rect(10 + column * (tab_width + tab_gap), 50 + row * 38, tab_width, 32)
    columns = 3 if W >= 650 else 2 if W >= 430 else 1
    gap = 10
    card_width = max(1, (W - 20 - (columns - 1) * gap) // columns)
    card_height = max(94, min(116, int(SCREEN_HEIGHT * 0.15)))
    cards = []
    for index, item in enumerate(SHOP_ITEMS[shop_category]):
        row, column = divmod(index, columns)
        x = 10 + column * (card_width + gap)
        cards_start_y = 94 + (38 if tab_rows == 2 else 0)
        y = cards_start_y + row * (card_height + gap)
        card = pygame.Rect(x, y, card_width, card_height)
        action = pygame.Rect(card.right - min(105, card.width - 12), card.bottom - 32, min(105, card.width - 12), 24)
        cards.append((item, card, action))
    return tabs, cards

def draw_shop_preview(category, item, center):
    item_id = item[0]
    if category == "colors":
        color = item[4]
        pygame.draw.circle(screen, color, center, 19)
        pygame.draw.circle(screen, (225, 244, 224), (center[0] - 6, center[1] - 7), 4)
    elif category == "skins":
        for offset, color in enumerate(((45, 145, 101), (112, 224, 153), (45, 145, 101))):
            pygame.draw.circle(screen, color, (center[0] - 20 + offset * 20, center[1]), 14)
        if item_id in ("fire", "lava"):
            pygame.draw.line(screen, (255, 190, 65), (center[0] - 12, center[1] + 7), (center[0] + 12, center[1] - 7), 3)
        elif item_id == "ice":
            pygame.draw.line(screen, (190, 250, 255), (center[0] - 12, center[1] - 7), (center[0] + 12, center[1] + 7), 3)
        elif item_id == "galaxy":
            pygame.draw.circle(screen, (215, 240, 255), center, 3)
    elif category == "outfits":
        pygame.draw.circle(screen, (67, 178, 120), center, 16)
        if item_id == "crown":
            pygame.draw.polygon(screen, (247, 204, 70), [(center[0] - 13, center[1] - 10), (center[0] - 6, center[1] - 22), (center[0], center[1] - 12), (center[0] + 7, center[1] - 22), (center[0] + 13, center[1] - 10)])
        elif item_id in ("wizard_hat", "cowboy_hat", "pirate_hat"):
            hat_color = (92, 64, 176) if item_id == "wizard_hat" else (126, 76, 40)
            pygame.draw.polygon(screen, hat_color, [(center[0] - 15, center[1] - 7), (center[0], center[1] - 27), (center[0] + 15, center[1] - 7)])
        elif item_id == "sunglasses":
            pygame.draw.line(screen, (18, 22, 29), (center[0] - 12, center[1] - 2), (center[0] + 12, center[1] - 2), 4)
        else:
            pygame.draw.circle(screen, (247, 204, 70), (center[0], center[1] - 15), 5)
    else:
        colors = {"orange": (243, 143, 45), "strawberry": (232, 60, 76), "cherry": (230, 52, 72), "banana": (249, 210, 61), "golden_apple": (238, 190, 70), "energy_orb": (75, 220, 255)}
        color = colors.get(item_id, (238, 75, 83))
        pygame.draw.circle(screen, color, center, 16)
        if item_id == "grapes":
            for offset in ((-6, -3), (6, -3), (-5, 6), (5, 6), (0, 13)):
                pygame.draw.circle(screen, (143, 83, 205), (center[0] + offset[0], center[1] + offset[1]), 5)
        elif item_id == "pineapple":
            pygame.draw.polygon(screen, (241, 183, 61), [(center[0], center[1] - 14), (center[0] + 10, center[1] + 10), (center[0] - 10, center[1] + 10)])
        else:
            pygame.draw.circle(screen, (255, 220, 172), (center[0] - 5, center[1] - 5), 3)

def handle_shop_click(position):
    global shop_category, shop_message, shop_message_until, coins, coin_multiplier
    tabs, cards = shop_layout()
    if shop_booster_button.collidepoint(position):
        if coin_multiplier == 1 and coins >= 20:
            coins -= 20
            coin_multiplier = 2
            save_player_data()
            shop_message = "2x coin booster purchased"
        elif coin_multiplier == 1:
            shop_message = "Not enough coins for the booster"
        else:
            shop_message = "2x coin booster already owned"
        shop_message_until = pygame.time.get_ticks() + 1800
        return
    for category, tab in tabs.items():
        if tab.collidepoint(position):
            shop_category = category
            return
    for item, card, action in cards:
        if not action.collidepoint(position):
            continue
        item_id = item[0]
        if item_id in owned_cosmetics[shop_category]:
            if equipped_cosmetics[shop_category] == item_id:
                default_item = SHOP_ITEMS[shop_category][0][0]
                if item_id == default_item:
                    shop_message = "Default item is always equipped"
                else:
                    equipped_cosmetics[shop_category] = default_item
                    save_player_data()
                    shop_message = f"Unequipped {item[1]}"
            else:
                equipped_cosmetics[shop_category] = item_id
                save_player_data()
                shop_message = f"Equipped {item[1]}"
        elif coins >= item[3]:
            coins -= item[3]
            owned_cosmetics[shop_category].append(item_id)
            equipped_cosmetics[shop_category] = item_id
            save_player_data()
            shop_message = f"Purchased and equipped {item[1]}"
        else:
            shop_message = "Not enough coins"
        shop_message_until = pygame.time.get_ticks() + 1800
        return

def draw_shop_screen():
    screen.fill(CREAM)
    title = big_font.render("Shop", True, CHARCOAL)
    screen.blit(title, title.get_rect(center=(W // 2, 22)))
    total = font.render(f"TOTAL COINS  {coins}", True, CHARCOAL)
    screen.blit(total, (W - total.get_width() - 12, 18))
    tabs, cards = shop_layout()
    for category, tab in tabs.items():
        active = category == shop_category
        pygame.draw.rect(screen, PRIMARY_GREEN if active else CARD_WHITE, tab, border_radius=6)
        pygame.draw.rect(screen, PRIMARY_GREEN if active else SHADOW, tab, 2, border_radius=6)
        label = font.render(SHOP_CATEGORIES[category], True, CARD_WHITE if active else CHARCOAL)
        screen.blit(label, label.get_rect(center=tab.center))
    rarity_colors = {"Common": (160, 177, 184), "Uncommon": (91, 202, 135), "Rare": (89, 166, 244), "Epic": (188, 113, 235), "Legendary": (247, 204, 70)}
    for item, card, action in cards:
        item_id, name, rarity, price, _ = item
        owned = item_id in owned_cosmetics[shop_category]
        equipped = equipped_cosmetics[shop_category] == item_id
        pygame.draw.rect(screen, CARD_WHITE, card, border_radius=8)
        pygame.draw.rect(screen, rarity_colors[rarity], card, 2, border_radius=8)
        draw_shop_preview(shop_category, item, (card.left + 34, card.top + 35))
        name_font = font if font.size(name)[0] <= card.width - 74 else pygame.font.SysFont("trebuchet ms", 14, bold=True)
        name_surface = name_font.render(name, True, CHARCOAL)
        screen.blit(name_surface, (card.left + 62, card.top + 12))
        rarity_surface = font.render(rarity, True, rarity_colors[rarity])
        screen.blit(rarity_surface, (card.left + 62, card.top + 35))
        action_label = "Equipped" if equipped else "Unequip" if owned else f"Buy {price}"
        pygame.draw.rect(screen, PRIMARY_GREEN if equipped else SKY_BLUE, action, border_radius=5)
        pygame.draw.rect(screen, SHADOW, action, 1, border_radius=5)
        action_surface = font.render(action_label, True, CARD_WHITE)
        screen.blit(action_surface, action_surface.get_rect(center=action.center))
    if pygame.time.get_ticks() < shop_message_until:
        message_surface = font.render(shop_message, True, CORAL)
        screen.blit(message_surface, message_surface.get_rect(center=(W // 2, SCREEN_HEIGHT - 22)))
    booster_label = "2x Coin Booster - 20" if coin_multiplier == 1 else "2x Coin Booster Owned"
    pygame.draw.rect(screen, SUNNY_YELLOW, shop_booster_button, border_radius=5)
    pygame.draw.rect(screen, SHADOW, shop_booster_button, 1, border_radius=5)
    booster_surface = font.render(booster_label, True, CHARCOAL)
    screen.blit(booster_surface, booster_surface.get_rect(center=shop_booster_button.center))

def draw_progress_screen(screen_type):
    screen.fill(CREAM)
    titles = {"missions": "Missions", "achievements": "Achievements", "daily": "Daily Challenge"}
    title = big_font.render(titles[screen_type], True, CHARCOAL)
    screen.blit(title, title.get_rect(center=(W // 2, 28)))
    if screen_type == "daily":
        ensure_daily_challenge()
        kind, description, target, reward = daily_target()
        progress = daily_state["progress"]
        status = "COMPLETED" if daily_state["completed"] else f"{progress} / {target}"
        lines = ["TODAY'S CHALLENGE", description, status, f"Reward: {reward} coins"]
        for index, line in enumerate(lines):
            color = CORAL if index in (0, 2) else CHARCOAL
            text = font.render(line, True, color)
            screen.blit(text, text.get_rect(center=(W // 2, 130 + index * 42)))
    else:
        entries = MISSIONS if screen_type == "missions" else ACHIEVEMENTS
        for index, (entry_id, entry) in enumerate(entries.items()):
            progress_data = mission_progress[entry_id] if screen_type == "missions" else achievement_progress[entry_id]
            completed = progress_data["completed"] if screen_type == "missions" else progress_data["unlocked"]
            title_text, description, kind, target, reward = entry
            row = pygame.Rect(18, 72 + index * 43, W - 36, 36)
            pygame.draw.rect(screen, CARD_WHITE, row, border_radius=5)
            label = f"{'OK' if completed else '  '} {title_text}  |  {description}  |  {progress_data['progress']}/{target}  |  +{reward}"
            text = font.render(label, True, PRIMARY_GREEN if completed else CHARCOAL)
            screen.blit(text, (row.left + 8, row.centery - text.get_height() // 2))
    back = font.render("Press ESC to return", True, MUTED_TEXT)
    screen.blit(back, back.get_rect(center=(W // 2, SCREEN_HEIGHT - 22)))

def draw_maps_screen():
    global map_buttons
    screen.fill(CREAM)
    title = big_font.render("Maps", True, CHARCOAL)
    screen.blit(title, title.get_rect(center=(W // 2, 30)))
    map_buttons = {}
    for index, (map_id, map_data) in enumerate(MAPS.items()):
        row, column = divmod(index, 2)
        card = pygame.Rect(20 + column * (W // 2 - 10), 70 + row * 78, W // 2 - 30, 64)
        map_buttons[map_id] = card
        unlocked = map_id in unlocked_maps
        selected = map_id == selected_map
        pygame.draw.rect(screen, map_data[2], card, border_radius=6)
        pygame.draw.rect(screen, PRIMARY_GREEN if selected else SHADOW, card, 2, border_radius=6)
        label = f"{map_data[0]}  {'SELECTED' if selected else 'UNLOCKED' if unlocked else f'{map_data[1]} coins'}"
        text = font.render(label, True, (239, 246, 241))
        screen.blit(text, text.get_rect(center=card.center))
    back = font.render("Press ESC to return", True, (174, 199, 202))
    screen.blit(back, back.get_rect(center=(W // 2, SCREEN_HEIGHT - 22)))

def handle_map_click(position):
    global selected_map, coins
    for map_id, button in map_buttons.items():
        if not button.collidepoint(position):
            continue
        price = MAPS[map_id][1]
        if map_id in unlocked_maps:
            selected_map = map_id
            save_player_data()
        elif coins >= price:
            coins -= price
            unlocked_maps.append(map_id)
            selected_map = map_id
            save_player_data()

def draw_profile_screen():
    screen.fill(CREAM)
    title = big_font.render("Profile", True, CHARCOAL)
    screen.blit(title, title.get_rect(center=(W // 2, 32)))
    equipped = equipped_cosmetics["skins"].replace("_", " ").title()
    subtitle = font.render(f"Equipped snake: {equipped}", True, MUTED_TEXT)
    screen.blit(subtitle, subtitle.get_rect(center=(W // 2, 72)))
    stats = [
        ("Highest Score", max(high_scores, default=0), PRIMARY_GREEN),
        ("Highest Combo", lifetime_stats.get("best_combo", 0), CORAL),
        ("Games Played", lifetime_stats.get("games", 0), SKY_BLUE),
        ("Food Eaten", lifetime_stats.get("foods", 0), PRIMARY_GREEN),
        ("Coins Collected", lifetime_stats.get("coins", 0), SUNNY_YELLOW),
        ("Achievements", sum(item["unlocked"] for item in achievement_progress.values()), CORAL),
        ("Maps Unlocked", len(unlocked_maps), SKY_BLUE),
    ]
    columns = 2 if W >= 460 else 1
    card_width = (W - 50) // columns
    for index, (label, value, color) in enumerate(stats):
        row, column = divmod(index, columns)
        card = pygame.Rect(18 + column * (card_width + 14), 105 + row * 62, card_width, 50)
        pygame.draw.rect(screen, CARD_WHITE, card, border_radius=10)
        pygame.draw.rect(screen, color, card, 2, border_radius=10)
        screen.blit(font.render(label, True, MUTED_TEXT), (card.left + 12, card.top + 7))
        value_surface = font.render(str(value), True, CHARCOAL)
        screen.blit(value_surface, (card.right - value_surface.get_width() - 12, card.top + 7))
    back = font.render("Press ESC to return", True, MUTED_TEXT)
    screen.blit(back, back.get_rect(center=(W // 2, SCREEN_HEIGHT - 22)))

def settings_control_buttons():
    button_width = min(360, W - 40)
    button_height = max(38, min(44, int(SCREEN_HEIGHT * 0.07)))
    left = (W - button_width) // 2
    start_y = max(190, int(SCREEN_HEIGHT * 0.30))
    return {
        "wasd": pygame.Rect(left, start_y, button_width, button_height),
        "touch": pygame.Rect(left, start_y + button_height + 14, button_width, button_height),
        "mouse": pygame.Rect(left, start_y + 2 * (button_height + 14), button_width, button_height),
    }

def draw_settings_screen():
    screen.fill(CREAM)
    title = big_font.render("Settings", True, CHARCOAL)
    screen.blit(title, title.get_rect(center=(W // 2, 90)))
    description = font.render("Choose how to steer", True, MUTED_TEXT)
    screen.blit(description, description.get_rect(center=(W // 2, 145)))
    labels = {"wasd": "WASD / Arrow Keys", "touch": "Touch Swipe", "mouse": "Follow Mouse"}
    for mode, button in settings_control_buttons().items():
        selected = mode == control_mode
        pygame.draw.rect(screen, PRIMARY_GREEN if selected else CARD_WHITE, button, border_radius=10)
        pygame.draw.rect(screen, PRIMARY_GREEN if selected else SHADOW, button, 2, border_radius=10)
        label = font.render(labels[mode], True, CARD_WHITE if selected else CHARCOAL)
        screen.blit(label, label.get_rect(center=button.center))
    back_text = font.render("Press ESC or click a selected mode to apply", True, MUTED_TEXT)
    screen.blit(back_text, back_text.get_rect(center=(W // 2, SCREEN_HEIGHT - 30)))

def handle_settings_click(position):
    global control_mode
    labels = settings_control_buttons()
    for mode, button in labels.items():
        if button.collidepoint(position):
            control_mode = mode
            save_player_data()
            return

screen_mode = "menu"
game_mode = "classic"
high_scores_return = "menu"
settings_return = "menu"
score_saved = False
touch_start = None

running = True
while running:
    current_speed = speed * (0.5 if effect_active("slow") else 1) * (1.25 if effect_active("energy") else 1)
    clock.tick(max(1, int(current_speed)) if screen_mode == "game" else 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            update_layout()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen_mode == "menu" and start_button.collidepoint(event.pos):
                screen_mode = "mode_select"
            elif screen_mode == "mode_select" and classic_button.collidepoint(event.pos):
                game_mode = "classic"
                respawn()
            elif screen_mode == "mode_select" and endless_button.collidepoint(event.pos):
                game_mode = "endless"
                respawn()
            elif screen_mode == "menu" and menu_high_score_button.collidepoint(event.pos):
                high_scores_return = "menu"
                screen_mode = "high_scores"
            elif screen_mode == "menu" and shop_button.collidepoint(event.pos):
                screen_mode = "shop"
            elif screen_mode == "menu" and menu_settings_button.collidepoint(event.pos):
                settings_return = "menu"
                screen_mode = "settings"
            elif screen_mode == "menu" and missions_button.collidepoint(event.pos):
                screen_mode = "missions"
            elif screen_mode == "menu" and daily_button.collidepoint(event.pos):
                screen_mode = "daily"
            elif screen_mode == "menu" and achievements_button.collidepoint(event.pos):
                screen_mode = "achievements"
            elif screen_mode == "menu" and maps_button.collidepoint(event.pos):
                screen_mode = "maps"
            elif screen_mode == "menu" and profile_button.collidepoint(event.pos):
                screen_mode = "profile"
            elif screen_mode == "menu" and quit_button.collidepoint(event.pos):
                running = False
            elif screen_mode == "game" and pause_button.collidepoint(event.pos):
                screen_mode = "paused"
            elif screen_mode == "game" and restart_button.collidepoint(event.pos):
                respawn()
            elif screen_mode == "game" and settings_button.collidepoint(event.pos):
                settings_return = "game"
                screen_mode = "settings"
            elif screen_mode == "paused" and resume_button.collidepoint(event.pos):
                screen_mode = "game"
            elif screen_mode == "paused" and pause_menu_button.collidepoint(event.pos):
                screen_mode = "menu"
            elif screen_mode == "score":
                if respawn_button.collidepoint(event.pos):
                    respawn()
                elif high_score_button.collidepoint(event.pos):
                    high_scores_return = "score"
                    screen_mode = "high_scores"
            elif screen_mode == "shop":
                handle_shop_click(event.pos)
            elif screen_mode == "maps":
                handle_map_click(event.pos)
            elif screen_mode == "settings":
                handle_settings_click(event.pos)
        if event.type == pygame.FINGERDOWN and screen_mode == "game":
            touch_start = (event.x * W, event.y * SCREEN_HEIGHT)
        elif event.type == pygame.FINGERUP and screen_mode == "game" and touch_start is not None:
            pointer_direction(touch_start, (event.x * W, event.y * SCREEN_HEIGHT))
            touch_start = None
        if event.type == pygame.KEYDOWN and screen_mode == "paused":
            if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                screen_mode = "game"
        elif event.type == pygame.KEYDOWN and screen_mode == "high_scores":
            if event.key == pygame.K_ESCAPE:
                screen_mode = high_scores_return
        elif event.type == pygame.KEYDOWN and screen_mode == "settings":
            if event.key == pygame.K_ESCAPE:
                screen_mode = settings_return
        elif event.type == pygame.KEYDOWN and screen_mode == "shop":
            if event.key == pygame.K_ESCAPE:
                screen_mode = "menu"
        elif event.type == pygame.KEYDOWN and screen_mode in ("missions", "daily", "achievements", "maps"):
            if event.key == pygame.K_ESCAPE:
                screen_mode = "menu"
        elif event.type == pygame.KEYDOWN and screen_mode == "profile":
            if event.key == pygame.K_ESCAPE:
                screen_mode = "menu"
        elif event.type == pygame.KEYDOWN and screen_mode == "mode_select":
            if event.key == pygame.K_ESCAPE:
                screen_mode = "menu"
        elif event.type == pygame.KEYDOWN and screen_mode == "score":
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.KEYDOWN and screen_mode == "game":
            if event.key == pygame.K_UP: change_direction((0, -20))
            if event.key == pygame.K_DOWN: change_direction((0, 20))
            if event.key == pygame.K_LEFT: change_direction((-20, 0))
            if event.key == pygame.K_RIGHT: change_direction((20, 0))
            if event.key == pygame.K_w: change_direction((0, -20))
            if event.key == pygame.K_s: change_direction((0, 20))
            if event.key == pygame.K_a: change_direction((-20, 0))
            if event.key == pygame.K_d: change_direction((20, 0))
            if event.key == pygame.K_p: screen_mode = "paused"

    if screen_mode == "menu":
        draw_home_scene()
        title = big_font.render("Phyton Saga", True, CHARCOAL)
        screen.blit(title, title.get_rect(center=(W // 2, 75)))
        profile_panel = profile_button
        pygame.draw.rect(screen, CARD_WHITE, profile_panel, border_radius=10)
        pygame.draw.rect(screen, SHADOW, profile_panel, 2, border_radius=10)
        profile_text = font.render("PROFILE", True, CHARCOAL)
        screen.blit(profile_text, profile_text.get_rect(center=profile_panel.center))
        coin_panel = pygame.Rect(max(14, W - min(190, W // 3) - 14), 12, min(190, W // 3), 38)
        pygame.draw.rect(screen, SUNNY_YELLOW, coin_panel, border_radius=10)
        coin_text = font.render(f"COINS  {coins}", True, CHARCOAL)
        screen.blit(coin_text, coin_text.get_rect(center=coin_panel.center))
        total_coins_text = font.render("READY TO SLITHER?", True, MUTED_TEXT)
        screen.blit(total_coins_text, total_coins_text.get_rect(center=(W // 2, 115)))
        draw_button(start_button, "Start")
        draw_button(menu_high_score_button, "High Score")
        draw_button(shop_button, "Shop")
        draw_button(menu_settings_button, "Settings")
        draw_button(quit_button, "Quit")
        draw_button(missions_button, "Missions")
        draw_button(daily_button, "Daily")
        draw_button(achievements_button, "Achievements")
        draw_button(maps_button, "Maps")
        copyright_text = font.render("\u00a9 2026 Phyton Saga. All rights reserved.", True, (174, 199, 202))
        screen.blit(copyright_text, copyright_text.get_rect(center=(W // 2, SCREEN_HEIGHT - 18)))
        pygame.display.flip()
        continue

    if screen_mode == "mode_select":
        screen.fill(CREAM)
        title = big_font.render("Choose Mode", True, CHARCOAL)
        screen.blit(title, title.get_rect(center=(W // 2, 150)))
        draw_button(classic_button, "Classic")
        draw_button(endless_button, "Endless")
        back_text = font.render("Press ESC to return", True, MUTED_TEXT)
        screen.blit(back_text, back_text.get_rect(center=(W // 2, 390)))
        pygame.display.flip()
        continue

    if screen_mode == "shop":
        draw_shop_screen()
        pygame.display.flip()
        continue

    if screen_mode in ("missions", "daily", "achievements"):
        draw_progress_screen(screen_mode)
        pygame.display.flip()
        continue

    if screen_mode == "maps":
        draw_maps_screen()
        pygame.display.flip()
        continue

    if screen_mode == "profile":
        draw_profile_screen()
        pygame.display.flip()
        continue

    if screen_mode == "paused":
        screen.fill(CREAM)
        title = big_font.render("Paused", True, CHARCOAL)
        screen.blit(title, title.get_rect(center=(W // 2, 150)))
        draw_button(resume_button, "Resume")
        draw_button(pause_menu_button, "Return to Menu")
        pygame.display.flip()
        continue

    if screen_mode == "settings":
        draw_settings_screen()
        pygame.display.flip()
        continue

    if screen_mode == "score":
        screen.fill(CREAM)
        title = big_font.render("RUN COMPLETE", True, CHARCOAL)
        screen.blit(title, title.get_rect(center=(W // 2, 100)))
        score_text = font.render(f"Your score: {score}", True, CHARCOAL)
        screen.blit(score_text, score_text.get_rect(center=(W // 2, 160)))
        draw_button(respawn_button, "Respawn")
        draw_button(high_score_button, "High Score")
        draw_high_score_effect()
        back_text = font.render("Press ESC to quit", True, MUTED_TEXT)
        screen.blit(back_text, back_text.get_rect(center=(W // 2, 410)))
        pygame.display.flip()
        continue

    if screen_mode == "high_scores":
        screen.fill(CREAM)
        title = big_font.render("High Scores", True, CHARCOAL)
        screen.blit(title, title.get_rect(center=(W // 2, 80)))
        for position, high_score in enumerate(high_scores, start=1):
            score_line = font.render(f"{position}. {high_score}", True, CHARCOAL)
            screen.blit(score_line, score_line.get_rect(center=(W // 2, 120 + position * 45)))
        back_text = font.render("Press ESC to return", True, MUTED_TEXT)
        screen.blit(back_text, back_text.get_rect(center=(W // 2, 410)))
        pygame.display.flip()
        continue

    if control_mode == "mouse":
        follow_mouse()
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if game_mode == "endless":
        head = (
            head[0] % W,
            TOP_BAR_HEIGHT + (head[1] - TOP_BAR_HEIGHT) % PLAY_HEIGHT,
        )
    if effect_active("magnet") and food != head:
        food = (
            max(0, min(W - 20, food[0] + (20 if head[0] > food[0] else -20 if head[0] < food[0] else 0))),
            max(TOP_BAR_HEIGHT, min(SCREEN_HEIGHT - 20, food[1] + (20 if head[1] > food[1] else -20 if head[1] < food[1] else 0))),
        )
    snake.insert(0,head)

    if powerup and head == powerup[0]:
        activate_powerup(powerup[1])
        powerup = None

    if special_food and head == special_food[0]:
        special_type = special_food[1]
        bonus = {"golden": 5, "crystal": 1, "ice": 2, "energy": 2, "fire": 4}[special_type]
        score += bonus
        coins_earned = bonus * coin_multiplier
        if effect_active("coin") or effect_active("double"):
            coins_earned *= 2
        coins += coins_earned
        round_coins += coins_earned
        if special_type == "golden":
            grant_progress("golden_food")
        grant_progress("score", bonus)
        grant_progress("coins", coins_earned)
        if special_type == "ice":
            active_effects["slow"] = pygame.time.get_ticks() + 5000
        elif special_type in ("energy", "fire"):
            active_effects["energy"] = pygame.time.get_ticks() + 5000
        spawn_particles(special_food[0])
        special_food = None

    if head == food :
        spawn_particles(food)
        speed += 0.2
        score += 1
        now = pygame.time.get_ticks()
        combo = combo + 1 if now <= combo_deadline else 1
        combo_deadline = now + 3000
        speed_milestones = int((speed - BASE_SPEED) // 2.5)
        coins_earned = (2 ** speed_milestones) * coin_multiplier
        coins_earned *= 2 if effect_active("coin") or effect_active("double") else 1
        coins_earned *= max(1, combo // 5)
        score += max(0, combo // 5) + (1 if effect_active("double") else 0)
        round_coins += coins_earned
        coins += coins_earned
        grant_progress("foods")
        grant_progress("score")
        grant_progress("coins", coins_earned)
        lifetime_stats["best_combo"] = max(lifetime_stats.get("best_combo", 0), combo)
        grant_progress("combo", combo)
        grant_progress("level", int((speed - BASE_SPEED) // 2.5))
        save_player_data()
        food = spawn_food()
    else :
        snake.pop()

    maybe_spawn_pickups()

    hit_wall = (
        head[0] < 0 or head[0] >= W or
        head[1] < TOP_BAR_HEIGHT or head[1] >= SCREEN_HEIGHT
    )
    hit_self = head in snake[1:] and not effect_active("ghost")
    hit_trap = trap is not None and head == trap[0]
    if (game_mode == "classic" and hit_wall) or hit_self or hit_trap:
        if shield_charges > 0:
            shield_charges -= 1
            active_effects.pop("shield", None)
            active_effects["shield_flash"] = pygame.time.get_ticks() + 900
            if snake:
                snake.pop(0)
        else:
            if not score_saved:
                record_score(score)
                score_saved = True
            screen_mode = "score"

    draw_grid()
    draw_food()
    draw_special_food()
    draw_powerup()
    draw_trap()
    draw_snake()
    update_particles()
    pygame.draw.rect(
        screen,
        (56, 105, 116),
        (0, TOP_BAR_HEIGHT, W, PLAY_HEIGHT),
        4,
    )
    draw_game_header()
    draw_button(restart_button, "Restart")
    draw_button(pause_button, "Pause")
    pygame.draw.rect(screen, (60, 90, 120), settings_button)
    outline_button(settings_button)
    settings_icon = icon_images.get("Settings")
    if settings_icon:
        icon_size = max(18, min(26, settings_button.height - 4))
        settings_icon = pygame.transform.smoothscale(settings_icon, (icon_size, icon_size))
        screen.blit(settings_icon, settings_icon.get_rect(center=settings_button.center))
    else:
        draw_gear(screen, settings_button.center, 10, (255, 255, 255))
    draw_high_score_effect()

    pygame.display.flip()

pygame.quit()

print("Top 5 scores:")
for position, high_score in enumerate(high_scores, start=1):
    print(f"{position}. {high_score}")
