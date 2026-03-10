#!/usr/bin/env python3
"""
Generate Google Ads Editor CSV import file for kenrak.com
Campaigns C1, C2 with SOP rules applied:
- H1: {KeyWord:Default} (DKI, pinned pos 1)
- H2: {LOCATION(City):en France} (pinned pos 2)
- H3: {LOCATION(State):France} (pinned pos 3)
- 3 RSA ads per ad group (replace existing 1 ad + add 2 new)
- All 3 keyword match types: Broad, Exact, Phrase
- These campaigns are ALREADY PUBLISHED, so this CSV adds missing match types + new ads

NOTE: After import, PAUSE the original ad in each ad group (it lacks DKI/Location pinning).
"""
import csv

COLS = [
    "Campaign", "Campaign Type", "Campaign Daily Budget", "Bidding Strategy",
    "Networks", "Ad Group", "Ad Group Type", "Max CPC", "Keyword", "Match Type",
    "Headline 1", "Headline 2", "Headline 3", "Headline 4", "Headline 5",
    "Headline 6", "Headline 7", "Headline 8", "Headline 9", "Headline 10",
    "Headline 11", "Headline 12", "Headline 13", "Headline 14", "Headline 15",
    "Description 1", "Description 2", "Description 3", "Description 4",
    "Final URL", "Path 1", "Path 2", "Ad Type",
    "Headline 1 position", "Headline 2 position", "Headline 3 position",
    "Campaign Status", "Ad Group Status"
]

rows = []

def make_row(**kwargs):
    row = {c: "" for c in COLS}
    row.update(kwargs)
    rows.append(row)

def check_headline(text, num):
    if len(text) > 30:
        print(f"  WARNING: H{num} = {len(text)} chars (max 30): {text}")
    return text

def check_desc(text, num):
    if len(text) > 90:
        print(f"  WARNING: D{num} = {len(text)} chars (max 90): {text}")
    return text

def add_keywords_all_types(campaign, ag_name, keywords):
    """Add each keyword in Broad, Phrase, and Exact match types.
    Since Phrase already exists for C1/C2, only Broad and Exact are truly new,
    but including all 3 for completeness (Editor will skip duplicates)."""
    for kw in keywords:
        for match_type in ["Broad", "Phrase", "Exact"]:
            make_row(**{
                "Campaign": campaign,
                "Ad Group": ag_name,
                "Keyword": kw,
                "Match Type": match_type
            })

def add_rsa_ad(campaign, ag_name, h1_dki, h2_city, h3_state,
               headlines_4_15, descs, final_url, path1, path2):
    h1 = check_headline(h1_dki, 1)
    h2 = check_headline(h2_city, 2)
    h3 = check_headline(h3_state, 3)

    while len(headlines_4_15) < 12:
        headlines_4_15.append("")
    headlines_4_15 = headlines_4_15[:12]

    for i, h in enumerate(headlines_4_15):
        if h:
            check_headline(h, i+4)

    for i, d in enumerate(descs):
        if d:
            check_desc(d, i+1)
    while len(descs) < 4:
        descs.append("")

    row_data = {
        "Campaign": campaign,
        "Ad Group": ag_name,
        "Headline 1": h1,
        "Headline 2": h2,
        "Headline 3": h3,
        "Headline 1 position": "1",
        "Headline 2 position": "2",
        "Headline 3 position": "3",
        "Description 1": descs[0],
        "Description 2": descs[1],
        "Description 3": descs[2],
        "Description 4": descs[3],
        "Final URL": final_url,
        "Path 1": path1,
        "Path 2": path2,
        "Ad Type": "RSA"
    }

    for i, h in enumerate(headlines_4_15):
        row_data[f"Headline {i+4}"] = h

    make_row(**row_data)


# ============================================================
# CAMPAIGN 1: C1 - Formation IA Entreprise OPCO ($120/day)
# Already published: ID 23643023932
# ============================================================
C1 = "C1 - Formation IA Entreprise OPCO"
print(f"\n=== {C1} ===")
# Don't create campaign row since it already exists - just add keywords and ads

# --- AG1.1: Formation IA OPCO ---
AG1_1 = "kenrak.com/#entreprise"
# Don't create ad group row since it may conflict - we add keywords + ads directly

ag11_keywords = [
    "formation intelligence artificielle opco",
    "formation ia financee opco",
    "formation chatgpt entreprise opco",
    "formation ia entreprise gratuite",
    "formation intelligence artificielle entreprise",
    "formation ia prise en charge opco",
    "opco formation intelligence artificielle",
    "formation agent ia entreprise",
    "formation automation ia entreprise",
    "formation ia certifiante opco",
]
add_keywords_all_types(C1, AG1_1, ag11_keywords)

# SOP Ad 1
print("AG1.1 Ad 1:")
add_rsa_ad(C1, AG1_1,
    h1_dki="{KeyWord:Formation IA OPCO}",         # 25 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Formation IA Financee OPCO",              # 26
        "0E a Avancer - 100% Finance",             # 28
        "Centre Certifie Qualiopi",                # 24
        "Formation IA Entreprise 2026",            # 28
        "Automatisez avec l'IA",                   # 21
        "Jusqu'a 9 000E/an Finance",               # 26
        "Agents IA pour votre Business",           # 29
        "Demarrez en 2 Semaines",                  # 22
        "+200 Entreprises Formees",                # 25
        "Atlas, AKTO, OPCO 2i, OPCO EP",           # 30
        "Formation Certifiante IA",                # 24
        "Audit Gratuit de vos Besoins",            # 29
    ],
    descs=[
        "Formation IA financee OPCO. Automatisez avec des agents IA. Qualiopi. Audit gratuit.",  # 83
        "OPCO finance 3000 a 9000E/an de formation IA. Agents IA pour vos processus. 0E a avancer.",  # 90
        "Transformez votre entreprise avec l'IA. Formation certifiante financee OPCO. Resultats.",  # 87
        "Arretez les taches repetitives. Formations IA : agents autonomes dans votre entreprise.",  # 87
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="formation-ia", path2="opco"
)

# SOP Ad 2
print("AG1.1 Ad 2:")
add_rsa_ad(C1, AG1_1,
    h1_dki="{KeyWord:Formation IA}",              # 20 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "100% Finance par votre OPCO",            # 27
        "Centre Agree Qualiopi",                   # 21
        "Deploiement IA en 2 Semaines",            # 28
        "Formation ChatGPT Entreprise",            # 28
        "9 000E/an Finance OPCO",                  # 22
        "Agents IA Autonomes",                     # 19
        "Support, Ventes, Marketing IA",           # 29
        "ROI Mesurable des 30 Jours",              # 27
        "On Cree vos Agents IA",                   # 21
        "Audit IA Gratuit 48h",                    # 20
        "GPT + Claude pour Equipe",                # 25
        "Demandez une Demo IA",                    # 20
    ],
    descs=[
        "Agents IA ventes, support, marketing. Formation OPCO 100% financee. Audit gratuit 48h.",  # 87
        "+80% de taches automatisees avec l'IA. Agents sur mesure. Qualiopi. ROI en 30 jours.",  # 86
        "Votre PME merite aussi l'IA. Solutions sur mesure financees OPCO. Chatbots, agents IA.",  # 87
        "Arretez de tout faire manuellement. Agents IA emails, leads, support 24/7. Formation.",  # 86
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="agents-ia", path2="entreprise"
)

# SOP Ad 3
print("AG1.1 Ad 3:")
add_rsa_ad(C1, AG1_1,
    h1_dki="{KeyWord:IA Entreprise}",             # 21 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Formation IA 0E a Avancer",              # 25
        "Financee OPCO a 100%",                    # 20
        "Qualiopi - Agents IA",                    # 20
        "Automatisez en 2 Semaines",               # 25
        "IA sur Mesure pour votre PME",            # 28
        "ChatGPT, Claude, Agents IA",              # 26
        "Solution IA Clef en Main",                # 24
        "Expert IA Certifie",                      # 18
        "Resultat Garanti ou Rembourse",           # 30
        "+200 Entreprises Satisfaites",            # 29
        "OPCO Finance Tout",                       # 17
        "Votre Equipe Formee a l'IA",              # 26
    ],
    descs=[
        "Formation IA entreprise OPCO. Agents IA, ChatGPT, Claude. Centre Qualiopi. Postulez.",  # 84
        "Solution IA clef en main pour PME. Formation + deploiement inclus. OPCO finance 100%.",  # 85
        "Resultat garanti ou rembourse. Formation IA + agents autonomes. OPCO finance tout.",  # 83
        "Votre equipe formee a l'IA en 2 semaines. Agents autonomes deployes. 0E a avancer.",  # 84
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="ia", path2="entreprise"
)


# --- AG1.2: Automatisation IA Business ---
AG1_2 = "kenrak.com/#entreprise"  # Same URL as AG1.1 per naming convention
# NOTE: In original C1, AG2 was "AG2 - Automatisation IA Business" with same URL
# For SOP naming, we need a distinct ad group name. Use the original name since it already exists.
AG1_2_NAME = "AG2 - Automatisation IA Business"

ag12_keywords = [
    "automatiser entreprise intelligence artificielle",
    "automatisation ia pme",
    "agent ia entreprise",
    "chatbot ia entreprise",
    "deployer ia dans son entreprise",
    "ia pour pme",
    "intelligence artificielle pour business",
    "solution ia entreprise france",
    "integrer ia dans entreprise",
    "consultant ia entreprise",
]
add_keywords_all_types(C1, AG1_2_NAME, ag12_keywords)

# SOP Ad 1
print("AG1.2 Ad 1:")
add_rsa_ad(C1, AG1_2_NAME,
    h1_dki="{KeyWord:Automatisation IA}",         # 25 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Automatisez votre Business IA",           # 29
        "Agents IA - 0E a Avancer",                # 24
        "Formation Financee OPCO",                 # 22
        "Deploiement IA en 2 Semaines",            # 28
        "+80% de Taches Automatisees",             # 28
        "IA sur Mesure pour votre PME",             # 28
        "Agents IA Autonomes",                      # 19
        "Support, Ventes, Marketing IA",            # 29
        "Solution IA Clef en Main",                 # 24
        "Audit IA Gratuit",                          # 16
        "ROI Mesurable des 30 Jours",               # 27
        "Expert IA Certifie Qualiopi",               # 28
    ],
    descs=[
        "Agents IA ventes, support, marketing. Formation OPCO 100% financee. Audit gratuit 48h.",  # 87
        "+80% de taches automatisees avec l'IA. Agents sur mesure. Qualiopi. ROI en 30 jours.",  # 86
        "Votre PME merite l'IA. Solutions sur mesure financees OPCO. Chatbots, agents autonomes.",  # 88
        "Arretez de tout faire manuellement. Agents IA emails, leads, support 24/7. Formation.",  # 86
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="agents-ia", path2="entreprise"
)

# SOP Ad 2
print("AG1.2 Ad 2:")
add_rsa_ad(C1, AG1_2_NAME,
    h1_dki="{KeyWord:Agent IA}",                  # 18 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Deploiement IA Entreprise",              # 25
        "0E a Avancer - OPCO Finance",             # 28
        "Agents IA sur Mesure",                    # 20
        "Chatbot IA Entreprise",                   # 21
        "Automatisation Complete",                 # 22
        "On Cree vos Agents IA",                   # 21
        "GPT + Claude pour Equipe",                # 25
        "Demandez une Demo IA",                    # 20
        "Integrer l'IA en Entreprise",              # 28
        "Consultant IA Certifie",                   # 22
        "+200 Entreprises Formees",                 # 25
        "Resultats en 30 Jours",                    # 21
    ],
    descs=[
        "Deploiement agents IA sur mesure. Ventes, marketing automatises. OPCO 100% finance.",  # 83
        "On cree vos agents IA : chatbots, automations, GPT + Claude. Formation incluse. 0E.",  # 83
        "Integrez l'IA dans votre entreprise en 2 semaines. Agents autonomes + formation OPCO.",  # 86
        "Consultant IA certifie Qualiopi. On deploie des agents pour vos processus. 0E.",  # 79
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="ia-pme", path2="agents"
)

# SOP Ad 3
print("AG1.2 Ad 3:")
add_rsa_ad(C1, AG1_2_NAME,
    h1_dki="{KeyWord:IA PME}",                    # 16 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "IA pour PME - 0E a Avancer",             # 27
        "Agents IA Deployes en 14 Jours",          # 30
        "Formation OPCO Financee",                 # 22
        "Chatbot, Email, Support IA",              # 26
        "Solution IA Business France",             # 27
        "ROI Mesurable Garanti",                   # 21
        "Centre Certifie Qualiopi",                # 24
        "Automatisez vos Processus",               # 25
        "IA Accessible pour Tous",                 # 23
        "Demo Gratuite en 48h",                    # 20
        "On Automatise votre Business",            # 28
        "Expertise IA sur Mesure",                 # 23
    ],
    descs=[
        "IA accessible pour toutes les PME. Agents autonomes, formation OPCO. Qualiopi. Demo.",  # 83
        "On automatise votre business avec l'IA. Chatbot, email, support 24/7. Formation OPCO.",  # 86
        "PME : deploiement IA en 14 jours. Agents autonomes + formation OPCO. ROI garanti.",  # 83
        "L'IA n'est plus reservee aux grands groupes. On deploie des agents pour votre PME.",  # 83
    ],
    final_url="https://kenrak.com/#entreprise",
    path1="solution-ia", path2="pme"
)


# ============================================================
# CAMPAIGN 2: C2 - Alternance IA Formation Jeunes ($80/day)
# Already published: ID 23638468049
# ============================================================
C2 = "C2 - Alternance IA Formation Jeunes"
print(f"\n=== {C2} ===")

# --- AG2.1: Alternance IA ---
AG2_1 = "kenrak.com/#alternance"

ag21_keywords = [
    "alternance intelligence artificielle",
    "alternance ia 2026",
    "apprentissage intelligence artificielle",
    "bts intelligence artificielle alternance",
    "formation alternance ia",
    "contrat apprentissage ia",
    "alternance chatgpt",
    "alternance data ia",
    "formation ia alternance remuneree",
    "alternance startup ia",
]
add_keywords_all_types(C2, AG2_1, ag21_keywords)

# SOP Ad 1
print("AG2.1 Ad 1:")
add_rsa_ad(C2, AG2_1,
    h1_dki="{KeyWord:Alternance IA}",             # 22 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Alternance IA - Salaire 492E",           # 28
        "BTS Intelligence Artificielle",           # 29
        "Formation 100% Gratuite (CFA)",           # 29
        "Alternance IA 2026 - Postulez",           # 29
        "Diplome Niveau 5 Reconnu Etat",           # 30
        "Cree ta Startup en Alternance",           # 29
        "0E de Frais de Formation",                # 24
        "Inscriptions Ouvertes",                   # 21
        "Ton Projet = Ta Future Startup",          # 30
        "Apprenez ChatGPT, Claude, IA",            # 29
        "CFA Agree - Qualiopi",                    # 20
        "Alternance IA Remuneree",                 # 23
    ],
    descs=[
        "Alternance IA remuneree des 492E/mois. BTS reconnu Etat. Formation CFA gratuite.",  # 80
        "Programme alternance IA. Agents IA, solutions business. Salaire + formation gratuite.",  # 85
        "Pas besoin de Bac+5 pour l'IA. BTS alternance : ChatGPT, Claude, agents autonomes.",  # 83
        "Programme alternance IA unique en France. Construis ta startup en formation. 492E/mois.",  # 87
    ],
    final_url="https://kenrak.com/#alternance",
    path1="alternance", path2="ia"
)

# SOP Ad 2
print("AG2.1 Ad 2:")
add_rsa_ad(C2, AG2_1,
    h1_dki="{KeyWord:Apprentissage IA}",          # 24 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "BTS IA en Alternance",                   # 20
        "Salaire Garanti des 492E",                # 24
        "Formation CFA 100% Gratuite",             # 27
        "Alternance IA 2026",                      # 18
        "Construis ton Business IA",               # 25
        "Aide Embauche 5 000E",                    # 20
        "Formation IA Pratique",                   # 20
        "CFA Agree Qualiopi",                      # 18
        "Diplome Reconnu par l'Etat",               # 26
        "0E de Frais - Tout Finance",               # 27
        "Inscriptions Ouvertes 2026",               # 26
        "Projet Scolaire = Startup",                # 25
    ],
    descs=[
        "Apprentissage IA : BTS alternance remuneree. CFA agree Qualiopi. Pas de frais. Postulez.",  # 87
        "Formation IA pratique en alternance. ChatGPT, Claude, agents IA. Salaire 492E/mois. CFA.",  # 88
        "Ton projet scolaire devient ta startup. Alternance IA remuneree + diplome Etat. 0E.",  # 84
        "Aide embauche 5000E pour l'employeur. BTS IA alternance. CFA agree. Inscriptions.",  # 84
    ],
    final_url="https://kenrak.com/#alternance",
    path1="apprentissage", path2="ia"
)

# SOP Ad 3
print("AG2.1 Ad 3:")
add_rsa_ad(C2, AG2_1,
    h1_dki="{KeyWord:Formation IA}",              # 20 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Alternance IA Remuneree",                # 23
        "BTS IA - Diplome Etat",                   # 21
        "Formation CFA Gratuite",                  # 22
        "Salaire des 492E par Mois",               # 25
        "ChatGPT, Claude, Agents IA",              # 26
        "Cree ta Startup pendant BTS",             # 28
        "CFA Agree par l'Etat",                    # 20
        "0E a Avancer",                            # 12
        "Inscriptions Ouvertes",                   # 21
        "Rejoins le Programme IA",                 # 23
        "Alternance + Entrepreneuriat",            # 29
        "Pas de Pre-Requis",                       # 17
    ],
    descs=[
        "Formation IA en alternance. BTS reconnu, CFA agree Qualiopi. 492E/mois. 0E de frais.",  # 83
        "Meilleure formation IA en France. Alternance remuneree + diplome Etat. Formation gratuite.",  # 89
        "Rejoins notre BTS IA en alternance. Projet = startup. Salaire garanti. CFA gratuite.",  # 85
        "Pas de pre-requis technique. On te forme a l'IA. Alternance remuneree. CFA Qualiopi.",  # 87
    ],
    final_url="https://kenrak.com/#alternance",
    path1="bts-ia", path2="alternance"
)

# --- AG2.2: Formation IA Gratuite ---
AG2_2_NAME = "AG2 - Formation IA Gratuite"

ag22_keywords = [
    "formation ia gratuite",
    "formation intelligence artificielle gratuite france",
    "formation chatgpt gratuite certifiante",
    "formation ia remuneree",
    "formation ia financee",
    "apprendre ia gratuitement france",
    "formation agent ia",
    "formation ia certifiante gratuite",
    "se former a l'ia en france",
    "formation ia debutant france",
]
add_keywords_all_types(C2, AG2_2_NAME, ag22_keywords)

# SOP Ad 1
print("AG2.2 Ad 1:")
add_rsa_ad(C2, AG2_2_NAME,
    h1_dki="{KeyWord:Formation IA}",              # 20 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Formation IA Gratuite",                  # 21
        "Financee 100% (OPCO ou CFA)",             # 28
        "Certifie Qualiopi",                       # 17
        "Devenez Expert IA en 2026",               # 25
        "0E de Frais - Formation IA",              # 26
        "Agents IA, ChatGPT, Claude",              # 26
        "Formation IA Pratique France",            # 28
        "Inscriptions Ouvertes",                   # 21
        "Diplome Reconnu par l'Etat",              # 26
        "Apprenez l'IA qui Compte",                # 24
        "Centre Agree CFA Qualiopi",               # 25
        "Formation IA pour Tous",                  # 22
    ],
    descs=[
        "Formation IA certifiante 100% financee. Salarie (OPCO) ou candidat (CFA) : 0E. Qualiopi.",  # 89
        "Apprenez agents IA, automatisation, ChatGPT et Claude. Formation financee et certifiante.",  # 89
        "Pas besoin d'etre dev pour l'IA. On vous rend operationnel en semaines. 100% finance.",  # 86
        "Meilleure formation IA en France. Gratuite salaries (OPCO) et alternants (CFA). Postulez.",  # 89
    ],
    final_url="https://kenrak.com/#alternance",
    path1="formation-ia", path2="gratuite"
)

# SOP Ad 2
print("AG2.2 Ad 2:")
add_rsa_ad(C2, AG2_2_NAME,
    h1_dki="{KeyWord:IA Gratuite}",               # 19 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Formation IA Certifiante",               # 24
        "100% Financee OPCO ou CFA",               # 25
        "Qualiopi - Centre Agree",                 # 23
        "Apprenez l'IA Gratuitement",              # 26
        "Agents IA en Formation",                  # 22
        "ChatGPT Claude en Pratique",              # 26
        "Pas de Pre-Requis",                       # 17
        "Commencez en 2 Semaines",                 # 23
        "Formation IA Concrete",                   # 21
        "0E de Frais Formation IA",                # 24
        "Diplome Etat Reconnu",                    # 20
        "Formation IA Debutant",                   # 21
    ],
    descs=[
        "Formation IA gratuite et certifiante en France. OPCO ou CFA 100% finance. Qualiopi.",  # 83
        "Se former a l'IA sans frais. Agents IA, ChatGPT, Claude. Certifiant et pratique. Postulez.",  # 89
        "Pas de pre-requis technique pour l'IA. On vous rend operationnel. Finance OPCO. Postulez.",  # 88
        "Formation IA debutant en France. Diplome reconnu. 0E de frais. OPCO ou alternance CFA.",  # 88
    ],
    final_url="https://kenrak.com/#alternance",
    path1="ia-gratuite", path2="france"
)

# SOP Ad 3
print("AG2.2 Ad 3:")
add_rsa_ad(C2, AG2_2_NAME,
    h1_dki="{KeyWord:Certifiante IA}",            # 22 chars
    h2_city="{LOCATION(City):en France}",          # 26 chars
    h3_state="{LOCATION(State):France}",           # 24 chars
    headlines_4_15=[
        "Formation IA Financee",                  # 21
        "OPCO ou CFA - 0E a Avancer",              # 27
        "Centre Agree Qualiopi",                   # 21
        "Devenez Expert IA 2026",                  # 22
        "ChatGPT, Claude, Agents IA",              # 26
        "Formation IA Operationnelle",             # 27
        "Diplome Reconnu Etat",                    # 20
        "Inscriptions Ouvertes",                   # 21
        "Formation IA France 2026",                # 24
        "Resultats Concrets en IA",                # 24
        "Se Former a l'IA en France",              # 26
        "Programme IA Accessible",                 # 23
    ],
    descs=[
        "Formation IA certifiante financee OPCO ou alternance CFA. Centre Qualiopi. Inscrivez-vous.",  # 88
        "Apprenez a utiliser l'IA concretement. Agents IA, automations. Formation financee.",  # 81
        "Se former a l'IA en France n'a jamais ete aussi simple. 100% finance. Qualiopi. 0E.",  # 83
        "Formation IA operationnelle. Diplome reconnu. OPCO ou CFA finance tout. 2 semaines.",  # 84
    ],
    final_url="https://kenrak.com/#alternance",
    path1="formation", path2="certifiante"
)


# ============================================================
# Write CSV
# ============================================================
output_path = "/Users/franck24/MES_SITES_GENERES/kenrak.com/google-ads-import-C1-C2-SOP.csv"

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=COLS, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"\n=== CSV generated: {output_path} ===")
print(f"   Total rows: {len(rows)}")

# Count elements
keywords = 0
ads = 0
for row in rows:
    if row.get("Keyword") and not row["Keyword"].startswith("-"):
        keywords += 1
    if row.get("Ad Type"):
        ads += 1

print(f"   Keywords: {keywords} (across all match types)")
print(f"   Ads: {ads}")
print(f"\nNOTE: After import in Google Ads Editor, PAUSE the original 1 ad")
print(f"      in each ad group (they lack DKI/Location pinning).")
print(f"      The 3 new SOP-compliant ads per ad group will replace them.")
