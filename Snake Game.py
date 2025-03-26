import pygame
import sys
import time
import random

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class SnakeGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.direction = RIGHT
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.apple = self.generate_apple()

    def generate_apple(self):
        while True:
            x = random.randint(0, self.width - 20) // 20 * 20
            y = random.randint(0, self.height - 20) // 20 * 20
            if (x, y) not in self.snake:
                return (x, y)

    def draw(self):
        self.display.fill((0, 0, 0))
        for pos in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.apple[0], self.apple[1], 20, 20))
        text = self.font.render(f"Score: {len(self.snake)}", True, (255, 255, 255))
        self.display.blit(text, (10, 10))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != DOWN:
                    self.direction = UP
                elif event.key == pygame.K_DOWN and self.direction != UP:
                    self.direction = DOWN
                elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                    self.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                    self.direction = RIGHT

    def update(self):
        head = self.snake[-1]
        if self.direction == UP:
            new_head = (head[0], head[1] - 20)
        elif self.direction == DOWN:
            new_head = (head[0], head[1] + 20)
        elif self.direction == LEFT:
            new_head = (head[0] - 20, head[1])
        elif self.direction == RIGHT:
            new_head = (head[0] + 20, head[1])

        self.snake.append(new_head)

        if self.snake[-1] == self.apple:
            self.apple = self.generate_apple()
        else:
            self.snake.pop(0)

        if (self.snake[-1][0] < 0 or self.snake[-1][0] >= self.width or
            self.snake[-1][1] < 0 or self.snake[-1][1] >= self.height or
            self.snake[-1] in self.snake[:-1]):
            self.reset_game()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
