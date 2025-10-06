# 🎨 Smooth Drawing Board

A modern, feature-rich drawing application built with Python and Tkinter. Features smooth curve rendering, professional UI, and intuitive tools.

![Drawing Board](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--platform-lightgrey.svg)

## ✨ Features

- **Smooth Drawing**: Advanced curve smoothing with Catmull-Rom splines and point averaging
- **Modern UI**: Clean, professional interface inspired by modern paint applications
- **Multiple Tools**: Brush and Eraser with customizable sizes
- **Color Palette**: 25 pre-selected colors plus custom color picker
- **Real-time Preview**: See your strokes as you draw
- **High-Quality Rendering**: Anti-aliased lines with smooth curves

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/smooth-drawing-board.git
cd smooth-drawing-board
```

2. Run the application:
```bash
python drawingBoard.py
```

That's it! No additional dependencies required.

## 🎯 How to Use

### Tools
- **🖌 Brush**: Draw smooth lines and curves
- **⬜ Eraser**: Remove parts of your drawing

### Colors
- Click any color in the palette to select it
- Use the custom color picker for unlimited color options
- Selected color is highlighted with a blue ring

### Brush Sizes
- Choose from preset sizes: 2px, 5px, 10px, 15px
- Eraser automatically uses 3x the selected brush size

### Drawing
- Click and drag to draw
- Release to finalize the stroke with smooth curve rendering
- Click "Clear" to erase the entire canvas

## 🔧 Technical Details

### Smoothing Algorithm
The application uses a sophisticated multi-stage smoothing pipeline:

1. **Point Simplification**: Removes redundant points that are too close
2. **Moving Average**: Smooths out hand tremor and jitter
3. **Linear Interpolation**: Adds high-resolution points between existing ones
4. **Final Polish**: Additional smoothing pass for ultra-smooth results

### Architecture
- **Frontend**: Tkinter with custom Canvas drawing
- **Smoothing**: Mathematical algorithms for curve fitting
- **UI**: Modern flat design with hover effects

## 📱 Screenshots

```
┌─────────────────────────────────────────────────────────────┐
│ 🖌 Brush  ⬜ Eraser                    Colors: ●○○○○        │
│                                                             │
│ Size: 2px 5px 10px 15px      ○○○○○  ○○○○○  ○○○○○           │
│                               ○○○○○  ○○○○○  ○○○○○           │
│                                                             │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                                                         │ │
│ │                    Canvas Area                          │ │
│ │                                                         │ │
│ │                                                         │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Development

### Project Structure
```
smooth-drawing-board/
├── drawingBoard.py          # Main application file
├── README.md               # This file
└── requirements.txt        # Dependencies (none currently)
```

### Key Functions
- `draw()`: Handles real-time drawing with preview
- `end_draw()`: Finalizes strokes with full smoothing
- `average_points()`: Applies moving average smoothing
- `interpolate_points()`: Adds high-resolution interpolation
- `simplify_points()`: Removes redundant points

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- Add more drawing tools (shapes, text, etc.)
- Implement layers
- Add save/load functionality
- Create brush presets
- Add undo/redo functionality

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Smoothing algorithms inspired by professional drawing applications
- UI design inspired by modern paint applications

## 📞 Support

If you have any questions or issues, please:
- Open an issue on GitHub
- Check existing issues first
- Provide detailed information about your problem

---

**Enjoy drawing! 🎨✨**
