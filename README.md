# Cell Simulator

**Cell Simulator** is an interactive and visually dynamic simulation built with Python and Pygame. The simulation features a physics-inspired system where individual cells interact based on predefined rules and parameters. Each cell can attract or repel others based on their colors, creating complex, emergent behaviors. Additionally, users can influence the simulation in real-time using mouse interactions. This project is ideal for learning basic simulation principles, exploring emergent systems, or simply enjoying a mesmerizing visual experience.

---

## Features
- **Dynamic Cell Interactions**: Cells attract or repel each other based on their colors using a configurable interaction matrix.
- **Mouse Interactivity**: Use the left mouse button to create an attraction field that influences cell movements.
- **Customizable Physics**: Adjust friction, force multipliers, and interaction distances for varied behavior.
- **Real-Time Performance Monitoring**: Displays FPS (frames per second) dynamically to gauge performance.
- **Highly Configurable Simulation**: Easily tweak cell count, sizes, colors, and interaction rules via the `config.py` file.

---

## Requirements
To run this simulation, ensure the following dependencies are installed:
- Python 3.8 or higher
- [Pygame](https://www.pygame.org/) library
- [NumPy](https://numpy.org/) library

---

## Installation

Follow these steps to set up and run the Cell Simulator:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/username/cell-simulator.git
    cd cell-simulator
    ```

2. **Install Dependencies**:
    ```bash
    pip install pygame numpy
    ```

3. **Run the Simulation**:
    ```bash
    python simulator.py
    ```

---

## Configuration
You can customize the simulation by modifying the `config.py` file. Below are some of the key parameters:

### General Settings
- **Window Dimensions**: `WIDTH`, `HEIGHT`
- **Background Color**: `BG_COLOR`

### Cell Properties
- **Number of Cells**: `CELL_COUNT`
- **Cell Size**: `CELL_SIZE`
- **Cell Colors**: `CELL_COLORS`

### Physics Parameters
- **Friction**: Controls how quickly cells lose momentum. (`FRICTION`)
- **Force Multiplier**: Adjusts the overall strength of interactions. (`FORCE_MULTIPLIER`)
- **Interaction Range**: Maximum distance where cells influence each other. (`EFFECTIVE_DISTANCE`)

### Mouse Interaction
- **Attraction Strength**: How strongly cells are pulled by the mouse. (`MOUSE_ATTRACTION_STRENGTH`)
- **Attraction Radius**: The effective range of mouse attraction. (`MOUSE_ATTRACTION_RADIUS`)

---

## Interaction Matrix
The interaction matrix defines how cells of different colors interact with each other. Each pairwise interaction is customizable. Example:
```python
INTERACTION_MATRIX = {
    'red': {
        'blue': -0.7,  # Red and Blue strongly repel
        'green': 0.5,  # Red and Green slightly attract
        'red': 1.2,    # Reds moderately attract each other
        ...
    },
    ...
}
