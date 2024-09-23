# WadSmoosh Plus - WAD merge utility

WadSmoosh Plus merges supported IWADs into a single IWAD file that can be played in GZDoom expanding the episode list. This makes it very convenient to play all of classic Doom's official releases and more without relaunching the game with different settings.

It's fine if you don't have all of the Doom games, eg you have Doom 2 but not Final Doom - WadSmoosh will package up everything it can find.

If you're not a Doom expert and just bought these games off [Steam](http://store.steampowered.com/sub/18397/) etc, see the **Absolute Beginner's Guide** section below.

## Usage

Simply copy all your WADs into the `source_wads/` subfolder, then run WadSmoosh. A log will appear showing progress and any errors that arise.

If you're in Windows, click `wadsmoosh.exe`.

If you're in macOS or Linux, run the `wadsmoo.sh` shell script - Python 2 and 3 are both supported now.

WadSmoosh will create a new file called `doom_complete.pk3` with all the game content in it. You can run this in GZDoom with `-iwad doom_complete.pk3` at the command line, or even rename it to `doom2.wad` and run without any command line needed. GZDoom 2.4 and later will recognize the `doom_complete.pk3` file as a valid IWAD without any name change needed.

If you've extracted the No Rest for the Living add-on episode for Doom 2 from Doom 3: BFG Edition or the PSN or XBLA versions, make sure it's named `nerve.wad` in the `source_wads/` folder.

In rare cases, you may need to uncheck the `source_wads/` folder's read-only status.

Advanced users can edit `wadsmoosh_data.py` to customize how and what WadSmoosh extracts. This file is Python code, read by the main program at runtime, so no recompile is required. You can also customize the ordering of the Master Levels by running WadSmoosh from the command line with a text file defining the ordering as an extra parameter. The ["Xaser ordering"](https://forum.zdoom.org/viewtopic.php?p=634600#p634600) is the default, but `masterlevels_order.txt` provides the mostly-alphabetical "PSN ordering", and more info on this customization option is included in comments at the top of that file. This is the only configuration option that WadSmoosh supports, and in general I'm opposed to adding more such options without turning WadSmoosh into a full-on GUI program.

## Supported WADs

WadSmoosh is not a general-purpose tool for merging Doom WADs; it is for *merging retail content* only - it was created in 2016 out of a desire for a "complete" retail version of Doom and Doom II, and only exists as a program because the IWAD file that it generates cannot be distributed legally. Please do not ask if WadSmoosh will support any specific WAD. If you want to add your own content to a custom IWAD, please either modify [WadSmoosh's source code](https://heptapod.host/jp-lebreton/wadsmoosh) yourself, or simply edit the `doom_complete.pk3` file WadSmoosh generated on your computer by opening it in a ZIP archive management program. Please do not ask me for support when doing either.

Here is the official list of WADs that WadSmoosh Plus will recognize:
- Doom/Ultimate Doom (original registered/retail version of `doom.wad`)
- Sigil (`sigil.wad` and its optional music addon `sigil_shreds.wad`)
- Sigil II (`sigil2.wad`, either its MIDI or MP3 soundtrack versions)
- Xbox Doom's extra levels (`sewers.wad` and `betray.wad`)
- Doom II (`doom2.wad`)
- The extra content in the Unity releases of Doom and Doom 2. (`doomunity.wad`, `doom2unity.wad` and `extras.wad`)
- The extras file from the Unity releases (`extras.wad`)
- The extra content in the BFG release of Doom 2. (`doom2bfg.wad`)
- No Rest for the Living (`nerve.wad`)
- The Master Levels (the 20 unmodified WAD files from the retail release)
- Final Doom (`tnt.wad` and `plutonia.wad`)
- TNT: Revilution (`tntr.wad`)
- Plutonia 2 (`pl2.wad`)
- Perdition's Gate (`perdgate.wad`)
- Hell To Pay (`hell2pay.wad`)
- No End in Sight (`neis.wad`)
- Freedoom Phase 1 (`freedoom1.wad`)
- Freedoom Phase 2 (`freedoom2.wad`)
- Doom 3DO Soundtrack (`doom3do.wad`)

For Sigil and Sigil II, all the filenames for different releases of those WADs are also recognized; you shouldn't have to rename your original files.

None of the "official add-on" content from the [Unity-based rereleases of Doom and Doom II](https://doomwiki.org/wiki/Doom_Classic_Unity_port) is supported. Only the versions of `doom.wad` and `doom2.wad` in the install folders for these ports are supported; they are virtually identical to the original data files.

# Where to find each wad file?

Doom/Ultimate Doom:
https://store.steampowered.com/app/2280/DOOM_1993/
Use `doom.wad`

Sigil & Sigil II:
https://romero.com/sigil

Xbox Doom's extra levels:
`Sewers.wad`: https://www.doomworld.com/idgames/levels/doom/s-u/sewers2
`Betray.wad`: https://www.doomworld.com/forum/topic/128173-known-lost-wads-of-our-history/?page=4&tab=comments#comment-2481490

Doom II:
https://store.steampowered.com/app/2300/DOOM_II
Use `doom2.wad`

Unity Doom and Doom 2 extra content:
Navigate to the game's directory. (If in Steam just right click the game and click Manage > Browse Local Files)
Then navigate to rerelease > DOOM_Data > StreamingAssets
Use `doom.wad`/`doom2.wad` and `extras.wad`
For The Ultimate Doom, your copy of doom.wad for this script must be renamed to `doomunity.wad`.
For Doom II, your copy of doom2.wad for this script must be renamed to `doom2unity.wad`.

Final Doom:
Download TNT: Evilution and The Plutonia Experiment from the add-ons in the Unity version of Doom 1993 or Doom II
Then navigate to the game's directory. (If in Steam just right click the game and click Manage > Browse Local Files)
Then open the finaldoombase directory two iWAD files should be there.
They are named `tnt.wad` and `plutonia.wad`

TNT: Revilution:
https://www.doomworld.com/idgames/levels/doom2/megawads/tntr
Use `tntr.wad`

Plutonia 2:
https://www.doomworld.com/idgames/levels/doom2/megawads/pl2
Use `pl2.wad`

Perdition's Gate:
This was a retail release. You will have to find a copy on your own. After you install it, you can use the `PERDGATE.WAD` it creates.

Hell To Pay:
This was a retail release. You will have to find a copy on your own. After you install it, you can use the `HELL2PAY.WAD` it creates.

No End in Sight:
https://www.doomworld.com/idgames/levels/doom/Ports/megawads/neis
use `neis.wad`

Freedoom Phase 1 & Phase 2 (version 0.13.o supported only):
https://github.com/freedoom/freedoom/releases/tag/v0.13.0
Use `freedoom1.wad` and `freedoom2.wad`

Doom 3DO Soundtrack:
https://www.moddb.com/games/doom/addons/doom-3do-music
Use `doom3do.wad`

## Absolute Beginner's Guide

1. [Download WadSmoosh](https://jp.itch.io/wadsmoosh) and extract it to a folder.
2. Find the folder(s) where Steam/GoG installed your game(s). For Steam, this will be something like `<Steam folder>\SteamApps\Common\<game name>\base`.
3. Copy any files you find with a `.WAD` extension to the `source_wads/` subfolder where you extracted WadSmoosh.
4. Run `wadsmoosh.sh`. Then the console will prompt confirmation and then show progress.
5. When it closes, you should have a file in the WadSmoosh folder called `doom_complete.pk3`.
6. Download [GZDoom](http://gzdoom.drdteam.org) and extract it to a folder.
7. Copy the `doom_complete.pk3` file to GZDoom's folder.
8. Launch GZDoom and play!

If you have any issues, the [How_to_download_and_run_Doom](http://doomwiki.org/wiki/How_to_download_and_run_Doom) page on the [Doom wiki](http://doomwiki.org) might be helpful.

# Notes

This fork enables the support for both Freedoom Phase 1 and 2 maps, music and *NEW* textures. It does not use the sprites nor the Doom-replacing textures since they will use the original ones. (I might add support for them in a future release but it's not on my to-do list right now.)

This fork uses the actual episode names rather than simply adding all of Fredoom Phase 1 as a single episode and uses the name "Destination: Earth" as the name for Phase 2 based on the exit text of Phase 1.

_Copyright © 2001-2022 Contributors to the Freedoom project. All rights reserved._
