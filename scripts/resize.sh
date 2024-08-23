#!/usr/bin/env sh

# install prerequisites
if ! type xdotool > /dev/null; then
    sudo apt install xdotool
fi

# find window id
dofus_pid=$(pidof Dofus.x64)
dofus_window_id=$(xdotool search --pid $dofus_pid)

# debugging: get current sizing
xdotool getwindowgeometry $dofus_window_id

# standard 1080p
# width 0 - 1518 :: height 25 - 335
xdotool windowsize $dofus_window_id 1920 1080
xdotool windowmove $dofus_window_id 759 180

# dofus 2 pixel-perfect
# xdotool windowsize $dofus_window_id 2122 1098
# xdotool windowmove $dofus_window_id 658 173

# xfce max 16:9
# xdotool windowsize $dofus_window_id 2475 1392
# xdotool windowmove $dofus_window_id 963 0