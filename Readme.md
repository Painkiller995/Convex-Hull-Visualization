# Convex Hull Visualization using Jarvis March Algorithm

This project visualizes the **Convex Hull** of a set of points using the **Jarvis March Algorithm** (also known as the Gift Wrapping Algorithm). The visualization is implemented in Python with the help of the **Pygame** library.

## Features

- **Interactive Visualization**: Watch the step-by-step construction of the convex hull.
- **Customizable Parameters**: Adjust the number of points, screen size, and colors.
- **Efficient Implementation**: Implements the Jarvis March algorithm to compute the convex hull.

## How It Works

The **Jarvis March Algorithm** works by:
1. Finding the leftmost point in the set of points.
2. Iteratively selecting the next point in the convex hull by determining the counterclockwise orientation of triplets.
3. Repeating the process until the hull is closed (returns to the starting point).

The visualization highlights the points and edges as they are added to the convex hull.

## Requirements

- Python 3.8 or higher
- Pygame library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Painkiller995/Convex-Hull-Visualization.git
   cd Convex-Hull-Visualization
