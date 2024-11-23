# data tables for WadSmoosh
# every line in this file must be valid Python!

# pre-authored resources to copy
RES_FILES = [
    'mapinfo.txt', 'language.txt', 'endoom', 'smooshed.txt',
    'textures.common', 'textures.doom1', 'textures.doom2',
    'textures.freedoom1', 'textures.freedoom2',
    'textures.tnt', 'textures.plut','textures.perdgate', 'animdefs.txt',
    'textures.hell2pay','textures.neis', 'textures.tntr', 'textures.pl2', 
    'graphics/M_DOOM.lmp', 'graphics/TITLEPIC.lmp',
    'graphics/M_HELL.lmp', 'graphics/M_NOREST.lmp',
    'graphics/M_MASTER.lmp', 'graphics/M_TNT.lmp',
    'graphics/M_PLUT.lmp', 'graphics/M_ID1.lmp',
    'mapinfo/doom1_levels.txt', 'mapinfo/doom2_levels.txt',
    'mapinfo/tnt_levels.txt', 'mapinfo/plutonia_levels.txt',
    'mapinfo/masterlevels.txt', 'mapinfo/sigil_levels.txt',
    'mapinfo/sigil2_levels.txt', 'mapinfo/perdgate_levels.txt',
    'mapinfo/hell2pay_levels.txt','mapinfo/neis_levels.txt',
    'mapinfo/freedoom1_levels.txt', 'mapinfo/freedoom2_levels.txt',
    'mapinfo/tntr_levels.txt','mapinfo/pl2_levels.txt',
    'mapinfo/jptr_levels.txt',
    'mapinfo/tntr_levels.txt','mapinfo/pl2_levels.txt', 
    'menudef.txt', 'cvarinfo.txt', 'zscript.txt'
]

# files within pk3 dir that will be removed before a new run
TIDY_DIR_EXTENSIONS = {
    'flats/': ['lmp'],
    'graphics/': ['lmp'],
    'patches/': ['lmp'],
    'sounds/': ['lmp'],
    'sprites/': ['lmp'],
    'music/': ['mus'],
    'mapinfo/': ['txt'],
    'maps/': ['wad'],
    './': ['lmp', 'txt']
}

# list of files we can extract from
WADS = ['doom', 'doom2', 'doom2bfg', 'tnt', 'plutonia', 'nerve', 'sigil', 'sigil_shreds',
        'sigil2', 'doomunity', 'doom2unity', 'nerveu', 'tntu', 'plutoniau', 'extras', 'perdgate', 'hell2pay',
        'neis', 'freedoom1', 'freedoom2','doom3do', 'tntr', 'pl2', 'jptr_v40']

# wads to search for and report if found
REPORT_WADS = ['doom', 'sigil', 'sigil_shreds', 'sigil2',
               'doom2', 'nerve', 'attack', 'tnt', 'plutonia', 
               'sewers', 'betray', 'doomunity', 'doom2unity',
               'nerveu', 'tntu', 'plutoniau', 'extras', 'perdgate',
               'hell2pay', 'neis', 'pl2', 'tntr', 'jptr_v40',
               'hell2pay', 'neis', 'pl2', 'tntr',
               'freedoom1', 'freedoom2','doom3do']

# lists of lumps common to doom 1+2
COMMON_LUMPS = [
    'data_common', 'flats_common', 'graphics_common', 'patches_common',
    'sounds_common', 'sprites_common'
]

DOOM1_LUMPS = [
    'graphics_doom1', 'music_doom1', 'patches_doom1', 'sounds_doom1',
    # extract PNAMES and TEXTURE1 from both doom.wad and doom2.wad,
    # in case only one is present
    'txdefs_doom1'
]

DOOM2_LUMPS = [
    'flats_doom2', 'graphics_doom2', 'music_doom2', 'patches_doom2',
    'sounds_doom2', 'sprites_doom2', 'txdefs_doom2'
]

# lists of lumps to extract from each IWAD
WAD_LUMP_LISTS = {
    'doom': COMMON_LUMPS + DOOM1_LUMPS,
    'doom2': COMMON_LUMPS + DOOM2_LUMPS,
    'tnt': ['graphics_tnt', 'music_tnt', 'patches_tnt'],
    'plutonia': ['graphics_plutonia', 'music_plutonia', 'patches_plutonia'],
    'sigil': ['graphics_sigil', 'music_sigil', 'patches_sigil', 'data_sigil'],
    # (buckethead tracks use the same names as jimmy's midi)
    'sigil_shreds': ['music_sigil'],
    'sigil2': ['graphics_sigil2', 'music_sigil2', 'patches_sigil2', 'data_sigil2', 'flats_sigil2'],
    # widescreen assets from unity ports
    'doomunity': ['graphics_doomunity'],
    'doom2unity': ['graphics_doom2unity'],
    'nerveu': ['graphics_nerveu'],
    'tntu': ['graphics_tntu'],
    'plutoniau': ['graphics_plutoniau'],
    'tntr': ['graphics_tntr', 'patches_tntr', 'flats_tntr', 'music_tntr'],
    'pl2': ['graphics_pl2', 'patches_pl2', 'flats_pl2', 'music_pl2'],
    'perdgate': ['graphics_perdgate', 'music_perdgate'],
    'hell2pay': ['graphics_hell2pay', 'patches_hell2pay', 'flats_hell2pay', 'music_hell2pay'],
    'neis': ['graphics_neis', 'patches_neis', 'flats_neis'],
    # "found secret" sound from unity port
    'extras': ['sounds_unity'],
    # add live recorded music from Doom's 3DO port
    'doom3do': ['music_doom3do'],
    'freedoom1': ['graphics_freedoom1', 'patches_freedoom1', 'flats_freedoom1', 'music_freedoom1'],
    'freedoom2': ['graphics_freedoom2', 'patches_freedoom2', 'flats_freedoom2', 'music_freedoom2']
}

# prefixes for filenames of maps extracted from IWADs
WAD_MAP_PREFIXES = {
    'doom': '',
    'doom2': '',
    'tnt': 'TN_',
    'plutonia': 'PL_',
    'nerve': 'NV_',
    # master levels not processed like other wads, bespoke prefix lookup
    'masterlevels': 'ML_',
    'sigil': '',
    'sigil2': '',
    'hell2pay': 'HP_',
    'perdgate': 'PG_',
    'neis': 'NS_',
    'freedoom1': 'FD1_',
    'freedoom2': 'FD2_',
    'tntr': 'TR_',
    'pl2': 'P2_',
    'jptr_v40' : 'JPTR_'
}

# texture patches to extract from specific master levels PWADs
MASTER_LEVELS_PATCHES = {
    'combine': ('RSKY1', 'ML_SKY1'),
    'manor': ('STARS', 'ML_SKY2'),
    'virgil': ('RSKY1', 'ML_SKY3')
}

#
# master levels MAPINFO data
# (because they can be reordered, mapinfo is generated by WadSmoosh)
#

# RSKY1 unless defined here
MASTER_LEVELS_SKIES = {
    'combine': 'ML_SKY1',
    'manor': 'ML_SKY2',
    'ttrap': 'ML_SKY2',
    'virgil': 'ML_SKY3',
    'minos': 'ML_SKY3',
    'nessus': 'ML_SKY3',
    'geryon': 'ML_SKY3',
    'vesperas': 'ML_SKY3',
    'blacktwr': 'RSKY3' # map25
}

# doom2 music lumps for each map
MASTER_LEVELS_MUSIC = {
    'attack': 'RUNNIN',
    'canyon': 'STALKS',
    'catwalk': 'COUNTD',
    'combine': 'BETWEE',
    'fistula': 'DOOM',
    'garrison': 'THE_DA',
    'manor': 'SHAWN',
    'paradox': 'DDTBLU',
    'subspace': 'IN_CIT',
    'subterra': 'DEAD',
    'ttrap': 'STLKS2',
    'virgil': 'COUNTD', # map03
    'minos': 'DOOM', # map05
    'bloodsea': 'SHAWN', # map07
    'mephisto': 'OPENIN', # (normally SHAWN)
    'nessus': 'SHAWN', # map07
    'geryon': 'DDTBLU', # map08
    'vesperas': 'IN_CIT', # map09
    'blacktwr': 'ADRIAN', # map25
    'teeth': 'EVIL', # map31
    'teeth2': 'ULTIMA' # map32
}

# maps in this list use the map07 special (trigger on last mancubus death)
MASTER_LEVELS_MAP07_SPECIAL = ['bloodsea', 'mephisto']

# substitutions done in wadsmoosh.extract_master_levels()
MASTER_LEVELS_SECRET_DEF = """
map ML_MAP21 lookup "ML_TEETH_SECRET"
{
    next = "%s"
    sky1 = "RSKY1"
    music = "$MUSIC_%s"
    Author = "$%s_%s"
}
"""

MASTER_LEVELS_CLUSTER_DEF = """
cluster 24
{
	flat = "$BGFLAT06"
	music = "$MUSIC_READ_M"
	exittext = lookup, "M1TEXT"
}
"""

MASTER_LEVELS_AUTHOR_PREFIX = 'WS_AU'

# author strings
MASTER_LEVELS_AUTHORS = {
    'attack':   'WILLITS_CHASAR',
    'canyon':   'WILLITS_CHASAR',
    'catwalk':  'KLIE',
    'fistula':  'KLIE',
    'combine':  'KLIE',
    'subspace': 'KLIE',
    'paradox':  'MUSTAINE',
    'subterra': 'KLIE',
    'garrison': 'KLIE',
    'blacktwr': 'KVERNMO',
    'virgil':   'ANDERSON',
    'minos':    'ANDERSON',
    'nessus':   'ANDERSON',
    'geryon':   'ANDERSON',
    'vesperas': 'ANDERSON',
    'manor':    'FLYNN',
    'ttrap':    'FLYNN',
    'teeth':    'KVERNMO',
    'bloodsea': 'KVERNMO',
    'mephisto': 'KVERNMO',
    'teeth2':   'KVERNMO'
}

# lines that will be placed at the top of the generated master levels mapinfo
MASTER_LEVELS_MAPINFO_HEADER = """
// master levels for doom 2
// generated from file '%s' by WadSmoosh

defaultmap
{
    cluster = 24
}

"""

# help the initial source wad reporting find sigil by any of its released names
SIGIL_ALT_FILENAMES = ['sigil_v1_0', 'sigil_v1_1', 'sigil_v1_2', 'sigil_v1_21']
# same for sigil2 - no sigil_shreds equivalent; MP3 music just an alternate wad
SIGIL2_ALT_FILENAMES = ['sigil_ii_v1_0', 'sigil_ii_mp3_v1_0']

# lump whose presence distinguishes BFG & Unity vs original doom2.wad
BFG_ONLY_LUMP = 'DMENUPIC'
