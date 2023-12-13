from libqtile import layout
import theme

themeName = "cyberpunk"

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_normal=theme.get_theme(themeName)["monandtall"][0],
        border_focus=theme.get_theme(themeName)["monandtall"][1],
        border_width=theme.get_theme(themeName)["monandtall"][2],
        single_border_width=theme.get_theme(themeName)["monandtall"][3],
        margin=theme.get_theme(themeName)["monandtall"][4],
        single_margin=theme.get_theme(themeName)["monandtall"][5],
        font=theme.get_theme(themeName)["monandtall"][6],
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

print(theme.get_theme(themeName)["monandtall"][0])