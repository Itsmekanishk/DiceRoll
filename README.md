# 🎲 DiceRoll

A beautiful, interactive web application for rolling dice with smooth 3D animations and sound effects.

## ✨ Features

- 🎯 **Roll multiple dice** - Select between 1 and 6 dice to roll simultaneously
- 🎬 **3D animations** - Smooth rolling animations with realistic dice rotations
- 🔊 **Sound effects** - Audio feedback for dice rolls
- 📱 **Responsive design** - Works seamlessly on desktop and mobile devices
- 🎨 **Modern UI** - Beautiful gradient background and smooth transitions
- ⚡ **Real-time results** - Instant calculation of totals and individual results

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Flask
- A modern web browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DiceRoll.git
cd DiceRoll
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## 📁 Project Structure

```
DiceRoll/
├── app.py                 # Flask backend server
├── index.html             # Root HTML template
├── templates/
│   └── index.html         # Main application template
├── static/
│   └── dice-sound.mp3     # Sound effect for dice rolls
└── README.md              # This file
```

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Animations**: CSS 3D transforms
- **Audio**: HTML5 Audio API

## 📖 How to Use

1. Open the application in your browser
2. Click the dice buttons (1-6) to select how many dice you want to roll
3. Click the "ROLL DICE" button to roll
4. Watch the 3D animation and see the results
5. The total sum is displayed at the bottom

## 🎮 Features Explained

### Dice Selection
Choose between 1 to 6 dice to roll. The selected number is highlighted in the UI.

### 3D Rolling Animation
Each dice features a complete 3D rotation animation with realistic movement. The animation includes:
- Rapid spinning during the roll phase
- Wobble effect at the end for a realistic finish

### Sound Effects
A satisfying dice-rolling sound plays with each roll, enhancing the user experience.

### Results Display
Clear display of:
- Individual dice results
- Total sum of all dice

## 🔧 API Endpoints

### POST `/roll`
Rolls the specified number of dice and returns the results.

**Parameters:**
- `num_dice` (int): Number of dice to roll (1-6)

**Response:**
```json
{
  "results": [4, 2, 5],
  "total": 11,
  "num_dice": 3
}
```

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 👨‍💻 Author

Created by Kanishk Dongardive

---

Enjoy rolling the dice! 🎲
