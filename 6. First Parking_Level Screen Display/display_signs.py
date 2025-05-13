import pygame
import sys
import os
import time

# Initialize Pygame
pygame.init()

# Get full screen resolution
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("First Parking Display")

# Load 'zero' image
zero_image_path = r"C:\\Users\\f8878760\\OneDrive - FRG\\First Parking\\6. First Parking_Level Screen Display\\6.6 First Parking_No Parking Sign.png"
if not os.path.exists(zero_image_path):
    print("Missing zero image.")
    pygame.quit()
    sys.exit()
zero_image_original = pygame.image.load(zero_image_path).convert_alpha()

# Font and colors
text_color = (0, 255, 0)  # Bright green
bg_color = (0, 0, 0)      # Black background

# Load images from folder
image_folder = "Traffic Signs"
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(".png") and "no parking" not in f.lower()]

if not image_files:
    print("No images found.")
    pygame.quit()
    sys.exit()

# Load and prepare image-count pairs
images = []
for i, filename in enumerate(image_files[:12]):  # Support up to 12 items for 6x2 layout
    path = os.path.join(image_folder, filename)
    img = pygame.image.load(path).convert_alpha()
    count = 10 + i * 3  # Sample countdown values
    images.append({"image": img, "count": count})

# Layout: 6 columns, 2 rows
columns, rows = 6, 2
cell_width = screen_width // columns
cell_height = screen_height // rows
img_size = int(min(cell_width, cell_height) * 0.6)
font = pygame.font.SysFont("Arial", img_size // 2, bold=True)

# Timing
last_update_time = time.time()
countdown_interval = 3  # seconds

running = True
while running:
    current_time = time.time()

    # Update counts
    if current_time - last_update_time >= countdown_interval:
        for item in images:
            if item["count"] > 0:
                item["count"] -= 1
        last_update_time = current_time

    screen.fill(bg_color)

    for idx, item in enumerate(images):
        row = idx // columns
        col = idx % columns
        x = col * cell_width
        y = row * cell_height

        # Resize and blit main image
        scaled_img = pygame.transform.scale(item["image"], (img_size, img_size))
        img_x = x + (cell_width - img_size) // 2
        img_y = y + (cell_height - img_size) // 2 - img_size // 6
        screen.blit(scaled_img, (img_x, img_y))

        if item["count"] > 0:
            count_text = font.render(str(item["count"]), True, text_color)
            count_rect = count_text.get_rect(center=(x + cell_width // 2, img_y + img_size + img_size // 8))
            screen.blit(count_text, count_rect)
        else:
            scaled_zero = pygame.transform.scale(zero_image_original, (img_size, img_size))
            zero_rect = scaled_zero.get_rect(center=(x + cell_width // 2, img_y + img_size + img_size // 2))
            screen.blit(scaled_zero, zero_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False

pygame.quit()
sys.exit()
