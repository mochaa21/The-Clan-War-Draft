from typing import List

clan_members = [
    "  Zane | TH11 | 45 | 2800",
    "Ariel | TH11 | 50 | 2900 ",
    "Bob | TH10 | 40 | 2500",
    "  Charlie | TH11 | 45 | 2800  "
]

def clan_war_draft(x):
    def draft_selection(data):
        raw_data = data.split('|')
        name = raw_data[0]
        th = int(raw_data[1].replace('TH', ''))
        hero_level = int(raw_data[2])
        trophy = int(raw_data[3])
        new_data = (-th, -hero_level, -trophy, name)
        return new_data
    return sorted(x, key=draft_selection)



# --- EKSEKUSI ---
hasil_draft = clan_war_draft(clan_members)
for member in hasil_draft:
    print(member.strip())