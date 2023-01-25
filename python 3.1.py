kun=int(input("oy tartib raqamini kiriting: "))
match kun:
    case 1:
        oy=f'yanvarda 31 kun bor'
    case 2:
        oy=f'fevralda 28(29) kun bor'
    case 3:
        oy=f'martda 31 kun bor'
    case 4:
        oy=f'aprelda 30 kun bor'
    case 5:
        oy=f'mayda 31 kun bor'
    case 6:
        oy=f'iyunda 30 kun bor'
    case 7:
        oy=f'iyulda 31 kun bor'
    case 8:
        oy=f'avgustda 31 kun bor'
    case 9:
        oy=f'sentabrda 30 kun bor'
    case 10:
        oy=f'oktabrda 31 kun bor'
    case 11:
        oy=f'noyabrda 30 kun bor'
    case 12:
        oy=f'dekabrda 31 kun bor'
    case _:
        oy=f'bunday oy raqami yoq'
print(oy)