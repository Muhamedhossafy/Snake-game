# 🐍 **Snake Game** 

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Game](https://img.shields.io/badge/Genre-Classic%20Arcade-green)
![License](https://img.shields.io/badge/License-MIT-orange)

## 🎮 **Description**
A classic Snake game implementation using Python's Turtle graphics library. Control your snake to collect food, grow longer, and avoid collisions with walls and yourself!

## ✨ **Features**
- 🕹️ Intuitive keyboard controls (↑ ↓ ← →)
- 🍎 Food spawning system with collision detection
- 📊 Score tracking with high score system
- 🚀 Progressive difficulty (speed increases with score)
- 💥 Wall and self-collision detection
- 🎨 Clean visual design with Turtle graphics

## 🛠️ **Technical Implementation**
```python
# Core game components
from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
```

## 📦 **Dependencies**
- Python 3.8+
- Turtle module (standard library)

## ⚙️ **Installation**
```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```

## 🚀 **How to Run**
```bash
python snake_game.py
```

## 🎮 **Controls**
| Key | Action |
|-----|--------|
| ↑   | Move Up |
| ↓   | Move Down |
| ←   | Move Left |
| →   | Move Right |

## 📊 **Scoring System**
- +1 point per food collected
- High score persistence
- Visual score display

## 🖥️ **Game Screenshot**
```
[ASCII art of snake game]
  Score: 12   High Score: 24
  -------------------------
  |                       |
  |       ○ ○ ○ ●         |
  |           ▲           |
  |           ■           |
  |       ■ ■ ■           |
  |                       |
  -------------------------
```

## 📂 **Project Structure**
```
snake-game/
├── snake_game.py      # Main game file
├── snake.py          # Snake class
├── food.py           # Food class
├── scoreboard.py     # Score system
└── README.md        # Documentation
```

## 🤝 **Contributing**
Contributions welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📜 **License**
MIT License - See [LICENSE](LICENSE) for details

## 📧 Contact
- ✉️ **Email**: [muhamad.ammar09001@gmail.com](mailto:muhamad.ammar09001@gmail.com)  
- 🔗 **LinkedIn**: [Muhamad Ammar](https://www.linkedin.com/in/muhamad-ammar-18b427306)

---

**Happy gaming!** For issues or feature requests, please open an issue on GitHub.
