import tkinter as tk
from tkinter import colorchooser
import math

root = tk.Tk()
root.title("Paint")
root.configure(bg='#ffffff')
root.geometry("1000x700")

# Drawing settings
current_tool = "brush"
current_color = "#000000"
current_width = 3

# Modern color scheme
BG_COLOR = '#ffffff'
SIDEBAR_BG = '#f5f5f5'
BUTTON_ACTIVE = '#e3f2fd'
BUTTON_HOVER = '#f0f0f0'
ACCENT_COLOR = '#1976d2'

# Create main layout
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True)

# Left sidebar for tools
sidebar = tk.Frame(main_frame, bg=SIDEBAR_BG, width=80)
sidebar.pack(side=tk.LEFT, fill=tk.Y)
sidebar.pack_propagate(False)

tk.Label(sidebar, text="Tools", bg=SIDEBAR_BG, fg='#333',
         font=('Segoe UI', 9, 'bold')).pack(pady=(15, 10))

# Tool buttons with icons
tool_buttons = {}

def create_tool_button(parent, text, tool_name, icon_text):
    btn_frame = tk.Frame(parent, bg=SIDEBAR_BG)
    btn_frame.pack(pady=5)
    
    btn = tk.Canvas(btn_frame, width=50, height=50, bg=SIDEBAR_BG,
                    highlightthickness=0, cursor='hand2')
    btn.pack()
    
    # Draw rounded rectangle background
    def draw_button(is_active=False):
        btn.delete('all')
        bg = BUTTON_ACTIVE if is_active else SIDEBAR_BG
        btn.config(bg=SIDEBAR_BG)
        btn.create_rectangle(5, 5, 45, 45, fill=bg, outline='#ddd' if not is_active else ACCENT_COLOR,
                           width=2, tags='bg')
        btn.create_text(25, 25, text=icon_text, font=('Segoe UI', 18), fill='#333', tags='icon')
    
    draw_button(tool_name == current_tool)
    
    def on_click(e):
        global current_tool
        current_tool = tool_name
        update_tool_buttons()
    
    def on_enter(e):
        if current_tool != tool_name:
            btn.delete('bg')
            btn.create_rectangle(5, 5, 45, 45, fill=BUTTON_HOVER, outline='#ccc',
                               width=2, tags='bg')
            btn.tag_lower('bg')
    
    def on_leave(e):
        draw_button(current_tool == tool_name)
    
    btn.bind('<Button-1>', on_click)
    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)
    
    tool_buttons[tool_name] = (draw_button, tool_name)
    
    # Label
    tk.Label(btn_frame, text=text, bg=SIDEBAR_BG, fg='#666',
            font=('Segoe UI', 8)).pack()
    
    return btn

def update_tool_buttons():
    for tool_name, (draw_func, _) in tool_buttons.items():
        draw_func(tool_name == current_tool)

create_tool_button(sidebar, "Brush", "brush", "🖌")
create_tool_button(sidebar, "Eraser", "eraser", "⬜")

# Separator
tk.Frame(sidebar, bg='#ddd', height=1).pack(fill=tk.X, pady=15, padx=10)

# Width presets
tk.Label(sidebar, text="Size", bg=SIDEBAR_BG, fg='#333',
         font=('Segoe UI', 9, 'bold')).pack(pady=(5, 10))

width_presets = [2, 5, 10, 15]
for w in width_presets:
    btn = tk.Button(sidebar, text=f"{w}px", command=lambda x=w: set_width(x),
                   bg=SIDEBAR_BG, fg='#333', font=('Segoe UI', 8),
                   relief=tk.FLAT, cursor='hand2', pady=5, padx=10)
    btn.pack(pady=2)
    btn.bind('<Enter>', lambda e, b=btn: b.config(bg=BUTTON_HOVER))
    btn.bind('<Leave>', lambda e, b=btn: b.config(bg=SIDEBAR_BG))

def set_width(w):
    global current_width
    current_width = w

# Right side - canvas and top toolbar
right_frame = tk.Frame(main_frame, bg=BG_COLOR)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Top toolbar for colors
color_toolbar = tk.Frame(right_frame, bg=BG_COLOR, height=80)
color_toolbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Color palette
color_palette_frame = tk.Frame(color_toolbar, bg=BG_COLOR)
color_palette_frame.pack(side=tk.LEFT)

tk.Label(color_palette_frame, text="Colors", bg=BG_COLOR, fg='#333',
         font=('Segoe UI', 10, 'bold')).pack(anchor='w', pady=(0, 8))

colors_container = tk.Frame(color_palette_frame, bg=BG_COLOR)
colors_container.pack()

# Quick color palette
colors = [
    ['#000000', '#424242', '#666666', '#9e9e9e', '#ffffff'],
    ['#f44336', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5'],
    ['#2196f3', '#03a9f4', '#00bcd4', '#009688', '#4caf50'],
    ['#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff9800'],
    ['#ff5722', '#795548', '#607d8b', '#000080', '#ffa500']
]

selected_color_indicator = None

def create_color_button(parent, color, row, col):
    global selected_color_indicator
    
    frame = tk.Frame(parent, bg=BG_COLOR)
    frame.grid(row=row, column=col, padx=2, pady=2)
    
    size = 28
    btn = tk.Canvas(frame, width=size, height=size, bg=BG_COLOR,
                   highlightthickness=0, cursor='hand2')
    btn.pack()
    
    # Draw color circle
    def draw_color(is_selected=False):
        btn.delete('all')
        if is_selected:
            btn.create_oval(2, 2, size-2, size-2, fill=color, outline=ACCENT_COLOR, width=3)
        else:
            btn.create_oval(4, 4, size-4, size-4, fill=color, outline='#ddd', width=1)
    
    draw_color(color == current_color)
    
    if color == current_color:
        selected_color_indicator = (btn, color, draw_color)
    
    def on_click(e):
        global current_color, selected_color_indicator
        current_color = color
        
        # Update previous selected
        if selected_color_indicator:
            prev_btn, prev_color, prev_draw = selected_color_indicator
            prev_draw(False)
        
        # Update current
        draw_color(True)
        selected_color_indicator = (btn, color, draw_color)
        custom_color_display.config(bg=color)
    
    def on_enter(e):
        if color != current_color:
            btn.delete('all')
            btn.create_oval(2, 2, size-2, size-2, fill=color, outline='#999', width=2)
    
    def on_leave(e):
        draw_color(color == current_color)
    
    btn.bind('<Button-1>', on_click)
    btn.bind('<Enter>', on_enter)
    btn.bind('<Leave>', on_leave)

for i, row in enumerate(colors):
    for j, color in enumerate(row):
        create_color_button(colors_container, color, i, j)

# Custom color picker
custom_frame = tk.Frame(color_toolbar, bg=BG_COLOR)
custom_frame.pack(side=tk.LEFT, padx=30)

tk.Label(custom_frame, text="Custom", bg=BG_COLOR, fg='#333',
         font=('Segoe UI', 10, 'bold')).pack(anchor='w', pady=(0, 8))

custom_container = tk.Frame(custom_frame, bg=BG_COLOR)
custom_container.pack()

custom_color_display = tk.Canvas(custom_container, width=40, height=40,
                                bg=current_color, highlightthickness=2,
                                highlightbackground='#ddd', cursor='hand2')
custom_color_display.pack()

def pick_custom_color(e=None):
    global current_color, selected_color_indicator
    color = colorchooser.askcolor(title="Choose color", initialcolor=current_color)
    if color[1]:
        current_color = color[1]
        custom_color_display.config(bg=current_color)
        if selected_color_indicator:
            prev_btn, prev_color, prev_draw = selected_color_indicator
            prev_draw(False)
            selected_color_indicator = None

custom_color_display.bind('<Button-1>', pick_custom_color)

# Clear button
clear_frame = tk.Frame(color_toolbar, bg=BG_COLOR)
clear_frame.pack(side=tk.RIGHT, padx=10)

def clear_canvas():
    canvas.delete("all")

clear_btn = tk.Button(clear_frame, text="⟲\nClear", command=clear_canvas,
                     relief=tk.FLAT, bg=SIDEBAR_BG, fg='#d32f2f',
                     font=('Segoe UI', 10, 'bold'), padx=15, pady=10,
                     cursor='hand2', bd=0)
clear_btn.pack()

clear_btn.bind('<Enter>', lambda e: clear_btn.config(bg='#ffebee'))
clear_btn.bind('<Leave>', lambda e: clear_btn.config(bg=SIDEBAR_BG))

# Canvas area
canvas_frame = tk.Frame(right_frame, bg='#e0e0e0', padx=1, pady=1)
canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

canvas = tk.Canvas(canvas_frame, bg='white', highlightthickness=0, bd=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Store points for the current stroke
raw_points = []
lines = []

def distance(p1, p2):
    """Calculate distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def average_points(pts, window=3):
    """Apply moving average to smooth out jitter"""
    if len(pts) < window:
        return pts
    
    smoothed = []
    for i in range(len(pts)):
        # Calculate window bounds
        start = max(0, i - window // 2)
        end = min(len(pts), i + window // 2 + 1)
        
        # Average the points in window
        window_points = pts[start:end]
        avg_x = sum(p[0] for p in window_points) / len(window_points)
        avg_y = sum(p[1] for p in window_points) / len(window_points)
        smoothed.append((avg_x, avg_y))
    
    return smoothed

def simplify_points(pts, tolerance=5):
    """Remove points that are too close together"""
    if len(pts) <= 2:
        return pts
    
    simplified = [pts[0]]
    for point in pts[1:]:
        if distance(simplified[-1], point) >= tolerance:
            simplified.append(point)
    return simplified

def interpolate_points(pts, resolution=20):
    """Create high-resolution interpolation between points"""
    if len(pts) < 2:
        return pts
    
    interpolated = [pts[0]]
    
    for i in range(len(pts) - 1):
        p1 = pts[i]
        p2 = pts[i + 1]
        
        # Add interpolated points between p1 and p2
        for j in range(1, resolution):
            t = j / resolution
            x = p1[0] + (p2[0] - p1[0]) * t
            y = p1[1] + (p2[1] - p1[1]) * t
            interpolated.append((x, y))
        
        interpolated.append(p2)
    
    return interpolated

def draw(event):
    x, y = event.x, event.y
    
    # Add point to current stroke
    raw_points.append((x, y))
    
    # Determine color and width based on current tool
    draw_color = 'white' if current_tool == "eraser" else current_color
    draw_width = current_width * 3 if current_tool == "eraser" else current_width
    
    # Draw preview while moving
    if len(raw_points) >= 2:
        # Use only recent points for preview
        recent = raw_points[-10:] if len(raw_points) > 10 else raw_points
        
        # Quick smoothing for preview
        smoothed = average_points(recent, window=3)
        
        if len(smoothed) >= 2:
            coords = []
            for point in smoothed:
                coords.extend(point)
            
            line = canvas.create_line(coords,
                                     fill=draw_color,
                                     width=draw_width,
                                     capstyle=tk.ROUND,
                                     joinstyle=tk.ROUND,
                                     smooth=True)
            lines.append(line)

def start_draw(event):
    # Start a new stroke
    global raw_points, lines
    raw_points = [(event.x, event.y)]
    lines = []

def end_draw(event):
    # Finalize and redraw the complete stroke with full smoothing
    global raw_points, lines
    
    if len(raw_points) > 1:
        # Clear temporary preview lines
        for line in lines:
            canvas.delete(line)
        lines = []
        
        # Determine color and width based on current tool
        draw_color = 'white' if current_tool == "eraser" else current_color
        draw_width = current_width * 3 if current_tool == "eraser" else current_width
        
        # Process points: simplify, smooth, then interpolate
        simplified = simplify_points(raw_points, tolerance=3)
        smoothed = average_points(simplified, window=5)
        interpolated = interpolate_points(smoothed, resolution=15)
        final_smooth = average_points(interpolated, window=3)
        
        if len(final_smooth) >= 2:
            coords = []
            for point in final_smooth:
                coords.extend(point)
            
            canvas.create_line(coords,
                             fill=draw_color,
                             width=draw_width,
                             capstyle=tk.ROUND,
                             joinstyle=tk.ROUND,
                             smooth=True)
    
    raw_points = []

canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', end_draw)

root.mainloop()