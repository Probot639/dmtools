import fantasynames as names

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

syllable = random.randint(2, 4)
name = "[test]"
if syllable == 2:
    name = random.choice(prefixes) + random.choice(midixes)
elif syllable == 3:
    name = random.choice(prefixes) + random.choice(midixes) + random.choice(suffixes)
elif syllable == 4:
    name = random.choice(prefixes) + random.choice(midixes) + random.choice(midixes) + random.choice(suffixes)

print(syllable)
print(name)