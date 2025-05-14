import pygame
import sys
import os
import time

# Initialize Pygame
pygame.init()

# Fullscreen mode
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("First Parking Display")

# Font and colors
font = pygame.font.SysFont("Arial", 100, bold=True)
text_color = (0, 255, 0)
bg_color = (0, 0, 0)

# Load "count-zero" image (displayed instead of number)
zero_count_image_path = "6.6 First Parking_No Parking Sign.png"
try:
    zero_count_img = pygame.image.load(zero_count_image_path).convert_alpha()
except Exception as e:
    print(f"Error loading 'zero count' image: {e}")
    pygame.quit()
    sys.exit()

# Load traffic sign images
image_folder = "Traffic Signs"
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(".png")]

if not image_files:
    print("No PNG images found in Traffic Signs folder.")
    pygame.quit()
    sys.exit()

# Use up to 6 images
image_files = image_files[:6]

# Prepare image-count pairs
images = []
for i, filename in enumerate(image_files):
    path = os.path.join(image_folder, filename)
    img = pygame.image.load(path).convert_alpha()
    count = 10 + i * 2  # Example starting values
    images.append((img, count))

# Grid layout: 6 columns (image+count pairs) and 2 rows
columns = 6
rows = 2
cell_width = screen_width // columns
cell_height = screen_height // rows
img_max_size = int(min(cell_width, cell_height) * 0.8)

# Countdown timer config
last_update_time = time.time()

# Main loop
running = True
while running:
    screen.fill(bg_color)

    for idx, (img, count) in enumerate(images):
        row = idx // 3
        img_col = (idx % 3) * 2
        count_col = img_col + 1

        # Image position
        img_x = img_col * cell_width + (cell_width - img_max_size) // 2
        img_y = row * cell_height + (cell_height - img_max_size) // 2
        img_scaled = pygame.transform.scale(img, (img_max_size, img_max_size))
        screen.blit(img_scaled, (img_x, img_y))

        # Count or zero-image
        if count > 0:
            number_text = font.render(str(count), True, text_color)
            text_rect = number_text.get_rect(center=(
                count_col * cell_width + cell_width // 2,
                row * cell_height + cell_height // 2))
            screen.blit(number_text, text_rect)
        else:
            # Display zero-count image in place of the number
            zero_scaled = pygame.transform.scale(zero_count_img, (img_max_size, img_max_size))
            zero_x = count_col * cell_width + (cell_width - img_max_size) // 2
            zero_y = row * cell_height + (cell_height - img_max_size) // 2
            screen.blit(zero_scaled, (zero_x, zero_y))

    # Countdown logic
    if time.time() - last_update_time >= 3:
        last_update_time = time.time()
        for i in range(len(images)):
            img, count = images[i]
            if count > 0:
                count -= 1
            images[i] = (img, count)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            running = False

pygame.quit()
sys.exit()
