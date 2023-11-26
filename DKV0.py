import ursina as ue

# Initialize the game engine
app = ue.Ursina()

# Define colors
ground_color = ue.color.rgb(100, 50, 0)  # Brown for platforms
barrel_color = ue.color.rgb(255, 165, 0)  # Orange for barrels
mario_color = ue.color.rgb(0, 0, 255)  # Blue for Mario
donkey_kong_color = ue.color.rgb(165, 42, 42)  # Dark red for Donkey Kong

# Create platforms
platforms = []
for i in range(5):
    platform = ue.Entity(model='cube', color=ground_color, position=(0, -i * 2 - 1), scale=(10, 0.5, 1))
    platforms.append(platform)

# Create barrels
barrels = []

# Create Mario
mario = ue.Entity(model='cube', color=mario_color, position=(-4, 0), scale=(0.5, 0.5, 0.5))

# Create Donkey Kong
donkey_kong = ue.Entity(model='cube', color=donkey_kong_color, position=(4, platforms[-1].y + 1), scale=(1, 1, 1))

# Define game mechanics
def update():
    # Move Mario
    speed = 2 * ue.time.dt
    if ue.held_keys['left arrow']:
        mario.x -= speed
    if ue.held_keys['right arrow']:
        mario.x += speed

    # Throw barrels
    if ue.held_keys['space']:
        barrel = ue.Entity(model='cube', color=barrel_color, position=(donkey_kong.x, donkey_kong.y), scale=(0.5, 0.5, 0.5))
        barrels.append(barrel)

    # Move barrels
    for barrel in barrels:
        barrel.x -= speed

        # Check if barrel falls off the platforms
        for platform in platforms:
            if barrel.y > platform.y and barrel.x < platform.x + 5 and barrel.x > platform.x - 5:
                barrel.y = platform.y + 0.5
                break

    # Check for collisions with Mario
    for barrel in barrels:
        if abs(barrel.x - mario.x) < 0.5 and abs(barrel.y - mario.y) < 0.5:
            app.quit()
            print("Game Over!")

    # Check if Mario reaches Donkey Kong
    if abs(mario.x - donkey_kong.x) < 0.5 and abs(mario.y - donkey_kong.y) < 0.5:
        app.quit()
        print("You win!")

# Start the game loop
app.run()
