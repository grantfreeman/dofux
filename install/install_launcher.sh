#!/usr/bin/env sh

script_dir=$(dirname $(realpath -s "$0"))
user=$(whoami)
ankama_dir=/home/$user/games/ankama
launcher_url=https://launcher.cdn.ankama.com/installers/production/Ankama%20Launcher-Setup-x86_64.AppImage
launcher_app=Ankama\ Launcher-Setup-x86_64.AppImage

# move over relevant files
mkdir -p $ankama_dir
cp $script_dir/ankama_logo.png $ankama_dir
cp $script_dir/ankama.desktop $ankama_dir
cp $script_dir/remove_cinematics.sh $ankama_dir

# update home folder username
sed -i "s|<USER>|${user}|g" $ankama_dir/ankama.desktop

# download 
wget -P $ankama_dir $launcher_url
chmod 755 "$ankama_dir/$launcher_app"

# create freedesktop link
ln $ankama_dir/ankama.desktop ~/.local/share/applications/ankama.desktop