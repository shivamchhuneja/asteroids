# Asteroids (Boot.dev Project)

This is a recreation of the classic Asteroids arcade game, built as part of the Boot.dev Backend Engineering pathway. The project was primarily a part of the "learn object oriented programming better" section.

## 🎮 Features

- **Spaceship movement & rotation**
- **Procedurally drifting asteroids(that also split into multiple asteroids when shot)**
- **Bullet firing & asteroid destruction**
- **Collision detection** between ship, bullets, and asteroids
- **Game restart + score progression**

## ✨ Enhancements Added Beyond the Course
I customized and extended the base project with:

- **Starfield Background**  
  Adds visual depth and real Star Wars type of feel.

- **Score Counter (Top-left)**  
  Score increases based on destroyed asteroids.

- **Custom Background Color / Theme**  
  Small polish changes to make the game visually cleaner. I like purple better than simple black.


## ⌨️ Controls

| Input | Action |
|------|--------|
| W / S    | Thrust / Move Backward |
| A / D | Rotate ship |
| Space | Fire bullets |

## 🧰 Tech Used

- **Python**
- **Pygame**
- **uv** for dependency & environment management

## 🚀 Run Locally

Make sure you have **uv** installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
Then simply clone the repo, and run with "uv run main.py"
