def get_lang_symbol(i):
    switcher = {
        'Afrikaans': 'af',
        'Albanais': 'sq',
        'Amharique': 'am',
        'Arabe': 'ar',
        'Arménien': 'hy',
        'Azéri': 'az',
        'Basque': 'eu',
        'Biélorusse': 'be',
        'Bengali': 'bn',
        'Bosnien': 'bs',
        'Bulgare': 'bg',
        'Catalan': 'ca',
        'Cebuano': 'ceb',
        'Chinois': 'zh',
        'Corse': 'co',
        'Croate': 'hr',
        'Tchèque': 'cs',
        'Danois': 'da',
        'Néerlandais': 'nl',
        'Anglais': 'en',
        'Espéranto': 'eo',
        'Estonien': 'et',
        'Finlandais': 'fi',
        'Français': 'fr',
        'Frison': 'fy',
        'Galicien': 'gl',
        'Géorgien': 'ka',
        'Allemand': 'de',
        'Grec': 'el',
        'Gujarati': 'gu',
        'Créole': 'ht',
        'Haoussa': 'ha',
        'Hawaïen':'haw',
        'Hébreu':'he',
        'Hindi':'hi',
        'Hmong':'hmn',
        'Hongrois':'hu',
        'Islandais':'is',
        'Igbo':'ig',
        'Indonésien':'id',
        'Irlandais':'ga',
        'Italien':'it',
        'Japonais':'ja',
        'Javanais':'jw',
        'Kannada':'kn',
        'Kazakh':'kk',
        'Khmer':'km',
        'Coréen':'ko',
        'Kurde':'ku',
        'Kirghyz':'ky',
        'Laotien':'lo',
        'Latin':'la',
        'Letton':'lv',
        'Lituanien':'lt',
        'Luxembourgeois':'lb',
        'Macédonien':'mk',
        'Malgache':'mg',
        'Malais':'ms',
        'Malayâlam':'ml',
        'Maltais':'mt',
        'Maori':'mi',
        'Marathi':'mr',
        'Mongol':'mn',
        'Birman':'my',
        'Népalais':'ne',
        'Norvégien':'no',
        'Nyanja':'ny',
        'Pachto':'ps',
        'Perse':'fa',
        'Polonais':'pl',
        'Portugais':'pt',
        'Panjabi':'pa',
        'Roumain':'ro',
        'Russe':'ru',
        'Samoan':'sm',
        'Gaélique':'gd',
        'Serbe':'sr',
        'Sesotho':'st',
        'Shona':'sn',
        'Sindhî':'sd',
        'Singhalais':'si',
        'Slovaque':'sk',
        'Slovène':'sl',
        'Somali':'so',
        'Spanish':'es',
        'Soundanais':'su',
        'Swahili':'sw',
        'Suédois':'sv',
        'Tagalog':'tl',
        'Tadjik':'tg',
        'Tamoul':'ta',
        'Télougou':'te',
        'Thaï':'th',
        'Turc':'tr',
        'Ukrainien':'uk',
        'Urdu':'ur',
        'Ouzbek':'uz',
        'Vietnamien':'vi',
        'Gallois':'cy',
        'Xhosa':'xh',
        'Yiddish':'yi',
        'Yoruba':'yo',
        'Zulu':'zu',
    }
    return switcher.get(i, "Invalid language")