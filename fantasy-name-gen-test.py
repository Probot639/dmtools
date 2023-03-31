import random

prefixes = ["Ara", "Ari", "Atha", "Auri", "Azur", "Bael", "Calen", "Cele", "Ceru", "Ciri", "Dara", "Dari", "Dro",
            "Elda", "Eli", "Elu", "Ena", "Eno", "Eri", "Ero", "Fae", "Fara", "Fira", "Gala", "Gale", "Gila", "Gira",
            "Hela", "Hira", "Ili", "Iro", "Jara", "Jiri", "Kael", "Kiri", "Lari", "Lei", "Lira", "Lori", "Mael", "Mara",
            "Meli", "Mira", "Myra", "Nara", "Nira", "Nuri", "Ori", "Oru", "Pael", "Phira", "Quara", "Rael", "Rana",
            "Rava", "Riha", "Rina", "Risa", "Sara", "Selu", "Seri", "Sila", "Siri", "Tala", "Tara", "Tela", "Thara",
            "Tira", "Tiri", "Uri", "Vael", "Vali", "Vana", "Vira", "Vora", "Wira", "Xara", "Xiri", "Xura", "Yela",
            "Yira", "Yora", "Yuri", "Zael", "Zara", "Zela", "Zira", "Zora"]
suffixes = ["an", "ara", "aria", "as", "ath", "ax", "ea", "el", "en", "era", "eri", "es", "eth", "ex", "ia", "il", "in",
            "ira", "iri", "is", "ith", "ix", "oa", "ol", "on", "ora", "ori", "os", "oth", "ox", "ua", "ul", "un", "ura",
            "uri", "us", "uth", "ux", "ya", "yl", "yn", "yra", "yri", "ys", "yth", "yx", "za", "zl", "zn", "zra", "zri",
            "zs", "zth", "zx", "ja", "je", "ji", "jo", "ju", "ka", "ke", "ki", "ko", "ku", "la", "le", "li", "lo", "lu",
            "ma", "me", "mi", "mo", "mu", "na", "ne", "ni", "no", "nu", "oa", "oe", "oi", "oo", "ou", "pa", "pe", "pi",
            "po", "pu", "ra", "re", "ri", "ro", "ru", "sa", "se", "si", "so", "su", "ta", "te", "ti", "to", "tu", "va",
            "ve", "vi", "vo", "vu", "xa", "xe", "xi", "xo", "xu", "ya", "ye", "yi", "yo", "yu", "za", "ze", "zi", "zo",
            "zu"]
midixes = ["ae", "ai", "al", "an", "ar", "as", "ath", "ax", "ea", "ei", "el", "en", "er", "es", "eth", "ex", "ia", "ie",
           "il", "in", "ir", "is", "ith", "ix", "oa", "oi", "ol", "on", "or", "os", "oth", "ox", "ua", "ui", "ul", "un",
           "ur", "us", "uth", "ux", "ya", "yi", "yl", "yn", "yr", "ys", "yth", "yx", "za", "zi", "zl", "zn", "zr", "zs",
           "zth", "zx", "ja", "je", "ji", "jo", "ju", "ka", "ke", "ki", "ko", "ku", "la", "le", "li", "lo", "lu", "ma",
           "me", "mi", "mo", "mu", "na", "ne", "ni", "no", "nu", "oa", "oe", "oi", "oo", "ou", "pa", "pe", "pi", "po",
           "pu", "ra", "re", "ri", "ro", "ru"]

lsprefixes = ["Black", "Bright", "Dark", "Deep", "Eagle", "East", "Elm", "Fair", "Far", "Fire", "Flame", "Forest",
              "Frost", "Gold", "Gray", "Green", "Grim", "Hawk", "Hazel", "High", "Iron", "Jade", "Lake", "Light",
              "Lion", "Long", "Low", "Maple", "Meadow", "Mist", "Moon", "Mountain", "Night", "North", "Oak", "Old",
              "Pale", "Pine", "Rain", "Red", "River", "Rock", "Rose", "Rune", "Sea", "Shadow", "Sharp", "Short",
              "Silent", "Silver", "Sky", "Snow", "South", "Spring", "Star", "Stone", "Storm", "Strong", "Swift", "Tall",
              "Thorn", "Thunder", "Timber", "True", "West", "Whisper", "White", "Wild", "Willow", "Wind", "Winter",
              "Wise", "Wood", "Young", "Yew", "Amber", "Ancient", "Ashen", "Autumn", "Blaze", "Boulder", "Crimson",
              "Crystal", "Dawn", "Dream", "Dusk", "Ember", "Endless", "Falcon", "Flower", "Gentle", "Glacier",
              "Harvest", "Hidden", "Hollow", "Journey", "Lone", "Lost", "Midnight", "Mystic", "Noble", "Phoenix",
              "Proud", "Quiet", "Raven", "Royal", "Sable", "Sapphire", "Scarlet", 'Ash', "Black", "Blaze", "Blue",
              "Bolt", "Brass", "Bronze", "Copper", "Crimson", "Crystal", "Diamond", "Dragon", "Emerald", "Fire",
              "Flame", "Frost", "Garnet", "Gold", "Green", "Heart", "Ice", "Iron", "Jade", "Lava", "Lightning", "Magma",
              "Metal", "Moon", "Night", "Obsidian", "Onyx", "Opal", "Phoenix", "Platinum", "Pyro", "Red", "Ruby",
              "Sapphire", "Scarlet", "Shadow", "Silver", "Sky", "Smoke", "Snow", "Solar", "Sonic", "Spark", "Steel",
              "Storm", "Sun", "Thorn", "Thunder", "Topaz", "Turquoise", "Twilight", "Vapor"]


lssuffixes = ["arrow", "bane", "beam", "blade", "born", "breaker", "brew", "brook", "caller", "claw", "crest", "dancer",
              "dawn", "dream", "dust", "eye", "fall", "fang", "feather", "fire", "flare", "flower", "foot", "force",
              "fury", "gaze", "glade", "glimmer", "glow", "guard", "hammer", "hand", "heart", "hunter", "jaw", "keeper",
              "knight", "leaf", "light", "maker", "moon", "mourner", "peak", "rage", "rain", "rider", "river", "rock",
              "runner", "scar", "shade", "shadow", "shard", "shield", "shout", "singer", "sky", "slayer", "smoke",
              "song", "spear", "spell", "spike", "spring", "star", "steel", "stone", "storm", "stride", "strike", "sun",
              "sworn", "talon", "thorn", "thunder", "tide", "tracker", "trail", "vale", "walker", "ward", "watcher",
              "water", "weaver", "whisper", "wind", "wing", "winter", "wise", "witch", "wolf"]


syllable = random.randint(2, 4)
firstname = "[firstname]"
if syllable == 2:
    firstname = random.choice(prefixes) + random.choice(midixes)
elif syllable == 3:
    firstname = random.choice(prefixes) + random.choice(midixes) + random.choice(suffixes)
elif syllable == 4:
    firstname = random.choice(prefixes) + random.choice(midixes) + random.choice(midixes) + random.choice(suffixes)

lastname = random.choice(lsprefixes) + random.choice(lssuffixes)

print(syllable)
print(firstname, lastname)
