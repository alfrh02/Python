#!/usr/bin/env python3
import os
import argparse

parser = argparse.ArgumentParser(description="Swap mods folder at ~/.minecraft.")
parser.add_argument("lite_or_full", type=str, help="Mod folder to swap to. Lite or Full.")

args = parser.parse_args()

decision = args.lite_or_full

os.chdir('/home/alfred/.minecraft')


if decision == "lite":
    os.rename("mods", "mods-full")
    os.rename("mods-lite", "mods")
    print("Lite modlist enabled.")
elif decision == "full":
    os.rename("mods", "mods-lite")
    os.rename("mods-full", "mods")
    print("Full modlist enabled.")


