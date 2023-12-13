import os

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from Settings.keys import keys
from Settings.mouse import mouse

from Settings import theme
#from Settings import layout

mod = "mod4"
terminalAlacritty = "alacritty"
themeName = "cyberpunk"

__groups = {
    1: Group(""),
    2: Group("", matches=[Match(wm_class=["Brave-browser"])]),
    3: Group("", matches=[Match(wm_class=["Code"])]),
    4: Group(""),
    5: Group(""),
    6: Group("󰙯", matches=[Match(wm_class=["Discord"])])
}

groups = [__groups[i] for i in __groups]

def get_group(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

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
        border_width=1,
        single_border_width=0,
        margin=6,
        single_margin=0,
        font=theme.get_theme(themeName)["monandtall"][2],
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=theme.get_theme(themeName)["widget_defaults"][0],
    fontsize=16,
    padding=3,
    background = theme.get_theme(themeName)["widget_defaults"][1]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_color=theme.get_theme(themeName)["screen"]["groupBox"][0],
                    highlight_method="line",
                    spacing=0,
                    inactive=theme.get_theme(themeName)["screen"]["groupBox"][1],
                    active=theme.get_theme(themeName)["screen"]["groupBox"][2],
                    block_highlight_text_color=theme.get_theme(themeName)["screen"]["groupBox"][3],
                    borderwidth=0,
                    padding=10,
                    fontsize=26,
                ),
                widget.Prompt(),
                widget.WindowName(
                    foreground = theme.get_theme(themeName)["screen"]["windowName"][0],
                    empty_group_string = ""
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Systray(),
                widget.Volume(
                    foreground = theme.get_theme(themeName)["screen"]["volume"][0],
                    padding=8
                ),
                widget.QuickExit(
                    default_text = theme.get_theme(themeName)["screen"]["quickExit"][0],
                    fontsize=22,
                    padding = 10,
                    foreground = theme.get_theme(themeName)["screen"]["quickExit"][1]
                ),
                widget.TextBox(
                    text = theme.get_theme(themeName)["screen"]["net"]["textBox"][0],
                    fontsize= 25,
                    foreground = theme.get_theme(themeName)["screen"]["net"]["textBox"][1],
                    background = theme.get_theme(themeName)["screen"]["net"]["textBox"][2],
                    border_color= theme.get_theme(themeName)["screen"]["net"]["textBox"][3],
                    border_width = 4
                ),
                widget.Net(
                    format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}",
                    background = theme.get_theme(themeName)["screen"]["net"]["net"][0],
                    foreground = theme.get_theme(themeName)["screen"]["net"]["net"][1],
                    update_interval = 10,
                    padding = 10
                ),
                widget.TextBox(
                    text = theme.get_theme(themeName)["screen"]["currentLayout"]["textBox"][0],
                    fontsize = 25,
                    foreground = theme.get_theme(themeName)["screen"]["currentLayout"]["textBox"][1],
                    background = theme.get_theme(themeName)["screen"]["currentLayout"]["textBox"][2],
                ),
                widget.CurrentLayout(
                    background = theme.get_theme(themeName)["screen"]["currentLayout"]["layout"][0],
                    padding = 10,
                    foreground = theme.get_theme(themeName)["screen"]["currentLayout"]["layout"][1]
                ),
                widget.TextBox(
                    text = theme.get_theme(themeName)["screen"]["clock"]["textBox"][0],
                    fontsize = 25,
                    background = theme.get_theme(themeName)["screen"]["clock"]["textBox"][1]
                ),
                widget.Clock(
                    format = "%Y-%m-%d %a %I:%M %p",
                    padding = 10,
                    background = theme.get_theme(themeName)["screen"]["clock"]["clock"][0]
                ),
                widget.TextBox(
                    text = theme.get_theme(themeName)["screen"]["battery"]["textBox"][0],
                    fontsize = 18,
                    background = theme.get_theme(themeName)["screen"]["battery"]["textBox"][1],
                    foreground = theme.get_theme(themeName)["screen"]["battery"]["textBox"][2],
                ),
                widget.Battery(
                    #Bateria Normal
                    background = theme.get_theme(themeName)["screen"]["battery"]["battery"][0],
                    foreground = theme.get_theme(themeName)["screen"]["battery"]["battery"][1],
                    update_interval = 30,
                    padding = 8,
                    #Bateria baja
                    low_background = theme.get_theme(themeName)["screen"]["battery"]["battery"][2],
                    low_foreground = theme.get_theme(themeName)["screen"]["battery"]["battery"][3],
                ),
            ],
            24,
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

autostart = [
    "feh --bg-fill /home/maegor/Pictures/Cyberpunk-City.jpg",
    "picom &",
    "xinput set-prop 9 'libinput Tapping Enabled' 1"
]

for x in autostart:
    os.system(x)