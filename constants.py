def load_image(path, size):
    img = pygame.image.load(path)
    img = pygame.transform.scale(img, size)
    return img


def mouse_on_image(pos, img, location):
    rect = img.get_rect()
    rect.x = location[0]
    rect.y = location[1]
    return rect.collidepoint(pos)


def draw_image(screen, img, location):
    screen.blit(img, location)