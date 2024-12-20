import pygame
import random
import time
import numpy as np
from cell import Cell
from config import Config

class Simulator:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Cell Simulator - FPS: 0")
        
        self.clock = pygame.time.Clock()
        self._initialize_cells()
        
        self.frame_count = 0
        self.last_time = time.time()
        self.running = True
        
        self.cell_positions = np.zeros((Config.CELL_COUNT, 2), dtype=np.float32)
        self.cell_velocities = np.zeros((Config.CELL_COUNT, 2), dtype=np.float32)
        
        self.mouse_attraction_strength = Config.MOUSE_ATTRACTION_STRENGTH
        self.mouse_attraction_radius = Config.MOUSE_ATTRACTION_RADIUS
        
        self.run()

    def _initialize_cells(self):
        self.cells = [
            Cell(
                random.randint(0, Config.WIDTH),
                random.randint(0, Config.HEIGHT),
                Config.CELL_SIZE,
                random.choice(Config.CELL_COLORS)
            ) for _ in range(Config.CELL_COUNT)
        ]

    def calculate_forces(self, cell1: Cell, cell2: Cell):
        dx = cell2.x - cell1.x
        dy = cell2.y - cell1.y
        distance_squared = dx**2 + dy**2
        
        if distance_squared > Config.EFFECTIVE_DISTANCE**2:
            return
            
        distance = np.sqrt(distance_squared)
        interaction_strength = Config.INTERACTION_MATRIX[cell1.color][cell2.color]
        
        if distance < cell1.size + cell2.size:
            force = -(cell1.size + cell2.size) / (distance + 0.1) * 15
        else:
            force = interaction_strength * (1 - (distance/Config.EFFECTIVE_DISTANCE)**2)
        
        if distance > 0.1:
            force = force / (1 + abs(force))
            force_x = force * dx/distance * Config.FORCE_MULTIPLIER
            force_y = force * dy/distance * Config.FORCE_MULTIPLIER
            
            cell1.vx += force_x
            cell1.vy += force_y

    def apply_mouse_attraction(self):
        if pygame.mouse.get_pressed()[0]:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            for cell in self.cells:
                dx = mouse_x - cell.x
                dy = mouse_y - cell.y
                distance_squared = dx**2 + dy**2
                
                if distance_squared < self.mouse_attraction_radius**2:
                    distance = np.sqrt(distance_squared)
                    if distance > 0.1:
                        
                        force = self.mouse_attraction_strength * (1 - (distance/self.mouse_attraction_radius)**2)
                        force = force / (1 + abs(force))
                        
                        cell.vx += force * dx/distance
                        cell.vy += force * dy/distance
        

    def update_cells(self):
        for i, cell1 in enumerate(self.cells):
            for j, cell2 in enumerate(self.cells[i+1:], start=i+1):
                self.calculate_forces(cell1, cell2)
                self.calculate_forces(cell2, cell1)
            
            self.apply_mouse_attraction()
            
            if cell1.x < 0:
                cell1.x = Config.WIDTH
                cell1.vx -= Config.BORDER_FORCE
            elif cell1.x > Config.WIDTH:
                cell1.x = 0
                cell1.vx += Config.BORDER_FORCE
            
            if cell1.y < 0:
                cell1.y = Config.HEIGHT
                cell1.vy -= Config.BORDER_FORCE
            elif cell1.y > Config.HEIGHT:
                cell1.y = 0
                cell1.vy += Config.BORDER_FORCE
            
            cell1.x += cell1.vx
            cell1.y += cell1.vy
            
            cell1.vx *= Config.FRICTION
            cell1.vy *= Config.FRICTION

    def draw_cells(self):
        self.screen.fill(Config.BG_COLOR)
        
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.circle(
                self.screen,
                (255, 255, 255, 50),
                mouse_pos,
                self.mouse_attraction_radius,
                1  # Circle outline width
            )
        
        for cell in self.cells:
            pygame.draw.circle(
                self.screen,
                cell.color,
                (int(cell.x), int(cell.y)),
                cell.size // 2
            )
        
        pygame.display.flip()

    def calculate_fps(self):
        current_time = time.time()
        self.frame_count += 1
        
        if current_time - self.last_time >= 1:
            fps = int(self.frame_count / (current_time - self.last_time))
            pygame.display.set_caption(f"Cell Simulator - FPS: {fps}")
            self.frame_count = 0
            self.last_time = current_time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update_cells()
            self.draw_cells()
            self.calculate_fps()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    Simulator()
