#!/usr/bin/env python3
"""
Generate Google Ads Editor CSV import file for kenrak.com
Campaigns C3, C4, C5 with SOP rules applied:
- H1: {KeyWord:Default} (DKI, pinned pos 1)
- H2: {LOCATION(City):Default} (pinned pos 2)
- H3: {LOCATION(State):France} (pinned pos 3)
- 3 RSA ads per ad group
- All 3 keyword match types: Broad, Exact, Phrase
- Phone extension: +33756812787
"""
import csv
import io

# CSV columns
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

def add_campaign(name, budget, status="Enabled"):
    make_row(**{
        "Campaign": name,
        "Campaign Type": "Search",
        "Campaign Daily Budget": str(budget),
        "Bidding Strategy": "Maximize Conversions",
        "Networks": "Google Search",
        "Campaign Status": status
    })

def add_ad_group(campaign, ag_name, status="Enabled"):
    make_row(**{
        "Campaign": campaign,
        "Ad Group": ag_name,
        "Ad Group Type": "Standard",
        "Max CPC": "2.00",
        "Ad Group Status": status
    })

def add_keywords_all_types(campaign, ag_name, keywords):
    """Add each keyword in Broad, Phrase, and Exact match types"""
    for kw in keywords:
        for match_type in ["Broad", "Phrase", "Exact"]:
            make_row(**{
                "Campaign": campaign,
                "Ad Group": ag_name,
                "Keyword": kw,
                "Match Type": match_type
            })

def add_negative_keywords(campaign, ag_name, neg_kws):
    for kw in neg_kws:
        make_row(**{
            "Campaign": campaign,
            "Ad Group": ag_name,
            "Keyword": f"-{kw}",
            "Match Type": "Broad"
        })

def add_rsa_ad(campaign, ag_name, h1_dki, h2_city, h3_state,
               headlines_4_15, descs, final_url, path1, path2):
    """Add RSA ad with SOP pinned headlines"""
    h1 = check_headline(h1_dki, 1)
    h2 = check_headline(h2_city, 2)
    h3 = check_headline(h3_state, 3)

    # Ensure exactly 12 additional headlines (H4-H15)
    while len(headlines_4_15) < 12:
        headlines_4_15.append("")
    headlines_4_15 = headlines_4_15[:12]

    for i, h in enumerate(headlines_4_15):
        if h:
            check_headline(h, i+4)

    # Check descriptions
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
# CAMPAIGN 3: RSA - Credits Tech Startup ($80/day)
# ============================================================
C3 = "C3 - Credits Tech Startup"
print(f"\n=== {C3} ===")
add_campaign(C3, 80)

# --- AG3.1: Credits Cloud Startup ---
AG3_1 = "kenrak.com/#credits"
add_ad_group(C3, AG3_1)

ag31_keywords = [
    "credits google cloud startup",
    "credits aws startup gratuit",
    "credits cloud startup france",
    "google for startups credits",
    "microsoft for startups azure",
    "credits tech startup gratuit",
    "programme startup cloud",
    "credits hebergement startup",
    "offres startups tech gratuites",
    "avantages startup tech france",
]
add_keywords_all_types(C3, AG3_1, ag31_keywords)

ag31_neg = ["coupon", "promo code", "crack", "hack", "pirate"]
add_negative_keywords(C3, AG3_1, ag31_neg)

# Ad 1
print("AG3.1 Ad 1:")
add_rsa_ad(C3, AG3_1,
    h1_dki="{KeyWord:Credits Tech}",           # 22 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "+5ME de Credits Tech Gratuits",        # 29
        "Google Cloud, AWS, Azure",             # 24
        "200+ Offres Startup Gratuites",        # 29
        "Jusqu'a 350KE Google Cloud",           # 26
        "300KE Credits AWS Gratuits",            # 26
        "Acces 100% Gratuit",                    # 18
        "Obtenez vos Credits en 48h",            # 26
        "OpenAI, Anthropic, Datadog",            # 26
        "+5ME d'Outils Tech Offerts",            # 27
        "Startup France Credits",                # 22
        "On vous Aide a Postuler",               # 23
        "Lancez sans Depenser 1E",               # 24
    ],
    descs=[
        "+5ME de credits tech gratuits : Google Cloud 350KE, AWS 300KE, Azure 150KE. On vous guide.",  # 90
        "200+ offres startup gratuites en un seul endroit. Credits cloud, IA, paiements. Gratuit.",  # 87
        "Jusqu'a 350KE Google Cloud, 300KE AWS, 150KE Azure. Acces 100% gratuit et accompagne.",  # 87
        "Lancez votre startup IA sans avancer 1E. Meilleurs credits tech : Google, AWS, Microsoft.",  # 90
    ],
    final_url="https://kenrak.com/#credits",
    path1="credits-tech", path2="startup"
)

# Ad 2
print("AG3.1 Ad 2:")
add_rsa_ad(C3, AG3_1,
    h1_dki="{KeyWord:Credits Cloud}",           # 23 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Credits Cloud Startup France",          # 28
        "Jusqu'a 350KE Google Cloud",           # 26
        "300KE AWS + 150KE Azure",               # 24
        "12 Partenaires Tech",                   # 19
        "Credits IA Startup Gratuits",            # 27
        "Stripe, Cloudflare, Datadog",            # 27
        "Acces Gratuit en 48h",                  # 20
        "+5ME de Credits Offerts",                # 23
        "100% Gratuit pour Startups",             # 26
        "On Gere vos Candidatures",              # 24
        "Offres Tech au meme Endroit",            # 28
        "Demarrez votre Startup",                 # 22
    ],
    descs=[
        "Votre startup merite les meilleurs outils. +5ME de credits tech gratuits. On vous guide.",  # 88
        "Google Cloud 350KE, AWS 300KE, Azure 150KE, Cloudflare 250KE. Credits en un clic.",  # 85
        "Arretez de payer le cloud. Credits startup gratuits Google, AWS, Azure. 200+ offres.",  # 88
        "Programme exclusif : on vous aide a obtenir vos credits tech startup. Accompagnement.",  # 89
    ],
    final_url="https://kenrak.com/#credits",
    path1="credits", path2="gratuits"
)

# Ad 3
print("AG3.1 Ad 3:")
add_rsa_ad(C3, AG3_1,
    h1_dki="{KeyWord:Credits Startup}",         # 25 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "+5ME Credits Tech Offerts",             # 25
        "Google Cloud + AWS + Azure",             # 26
        "200+ Offres Tech Gratuites",             # 26
        "Acces Guide et 100% Gratuit",            # 28
        "350KE Google Cloud Gratuits",            # 27
        "Startup IA : Credits Offerts",           # 28
        "Cloudflare 250KE Gratuits",              # 25
        "OpenAI + Anthropic Credits",             # 26
        "Credits Paiement Stripe",                # 23
        "On Postule pour Vous",                   # 20
        "Obtenez tout en 48 Heures",              # 26
        "Programme Credits Startup",              # 25
    ],
    descs=[
        "Startup sans depenser 1E en infra. +5ME credits tech gratuits : cloud, IA, analytics.",  # 89
        "Pourquoi payer le cloud ? Credits Google, AWS, Azure et 200+ offres. On vous guide.",  # 86
        "Guide des credits tech startup en France. 12 partenaires, +5ME d'outils. Acces gratuit.",  # 90
        "Tous les credits startup au meme endroit. Google 350KE, AWS 300KE, Azure 150KE. Gratuit.",  # 90... check
    ],
    final_url="https://kenrak.com/#credits",
    path1="offres", path2="startup"
)

# --- AG3.2: Aides Etat Startup IA ---
AG3_2 = "kenrak.com/#aides"
add_ad_group(C3, AG3_2)

ag32_keywords = [
    "aide creation startup ia france",
    "bpi france startup ia",
    "subvention startup ia",
    "aide etat intelligence artificielle",
    "france 2030 ia",
    "cir credit impot recherche ia",
    "financement startup ia france",
    "bourse french tech",
    "aide innovation ia france",
    "subvention intelligence artificielle france",
]
add_keywords_all_types(C3, AG3_2, ag32_keywords)

# Ad 1
print("AG3.2 Ad 1:")
add_rsa_ad(C3, AG3_2,
    h1_dki="{KeyWord:Aides Startup IA}",        # 26 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Aides Etat IA Jusqu'a 250KE",          # 27
        "BPI France, CIR, CII, OPCO",            # 27
        "France 2030 - Pionniers IA",             # 26
        "Subvention IA jusqu'a 100%",             # 26
        "CIR : 30% de vos Depenses R&D",         # 30
        "Bourse French Tech 30 000E",            # 27
        "Aide Startup IA France 2026",            # 27
        "On vous Guide pour Postuler",            # 28
        "Audit Aides Gratuit",                    # 19
        "CII : 20% Innovation 80KE",              # 26
        "France Num Pret 50 000E",                # 24
        "Simulez vos Aides IA",                   # 20
    ],
    descs=[
        "Aides Etat projet IA : CIR 30%, CII 20%, BPI France 90KE, France 2030. Simulez gratuit.",  # 89
        "15 dispositifs d'aide startups IA en France. BPI, CIR, CII, OPCO, France 2030. Gratuit.",  # 90
        "Ne laissez pas d'argent sur la table. France finance l'IA : CIR, CII, BPI. Audit gratuit.",  # 90
        "L'Etat finance jusqu'a 100% (France 2030). + CIR 30% + Bourse French Tech 30KE. Postulez.",  # 90.. check
    ],
    final_url="https://kenrak.com/#aides",
    path1="aides-etat", path2="ia"
)

# Ad 2
print("AG3.2 Ad 2:")
add_rsa_ad(C3, AG3_2,
    h1_dki="{KeyWord:Financement IA}",          # 24 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Jusqu'a 250KE d'Aides Etat",           # 26
        "CIR 30% + CII 20% Cumules",             # 26
        "BPI France 90KE pour l'IA",              # 25
        "France 2030 : 100% Finance",             # 26
        "Expert en Financement IA",               # 24
        "Aides Regionales Startup IA",            # 27
        "Obtenez vos Aides en 30 Jours",         # 30
        "Audit Eligibilite Gratuit",              # 25
        "Bourse French Tech 30KE",                # 24
        "+15 Dispositifs d'Aide IA",              # 26
        "On Gere vos Dossiers",                   # 20
        "Simulateur Aides en Ligne",              # 25
    ],
    descs=[
        "Expert financement IA. On monte vos dossiers : CIR, CII, BPI, France 2030. Gratuit.",  # 87
        "Cumul : CIR 30% + CII 20% + BPI 90KE + Bourse French Tech 30KE + aides regionales.",  # 87
        "Votre startup IA a droit a des aides. On vous accompagne : eligibilite et obtention.",  # 87
        "France 2030, BPI, CIR, CII : ne passez a cote d'aucune aide. Audit gratuit 48 heures.",  # 90
    ],
    final_url="https://kenrak.com/#aides",
    path1="financement", path2="startup-ia"
)

# Ad 3
print("AG3.2 Ad 3:")
add_rsa_ad(C3, AG3_2,
    h1_dki="{KeyWord:Subvention IA}",           # 23 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Aides IA : CIR + CII + BPI",            # 27
        "France 2030 Finance votre IA",           # 28
        "30% Remboursement R&D (CIR)",            # 28
        "Subvention Startup IA 2026",             # 26
        "Jusqu'a 250KE Aides Cumulees",          # 29
        "Bourse French Tech",                     # 19
        "On Monte vos Dossiers",                  # 21
        "Audit Gratuit en 48h",                   # 20
        "Aides Nationales + Regionales",          # 29
        "Financement 100% Possible",              # 25
        "Pas de Frais Pas de Risque",             # 26
        "Accompagnement Complet",                  # 22
    ],
    descs=[
        "Subventions IA en France : CIR, CII, BPI, France 2030, aides regionales. Audit gratuit.",  # 90
        "Montez votre startup IA avec les aides de l'Etat. On gere vos dossiers. 100% gratuit.",  # 89
        "CIR 30% + CII 20% + BPI 90KE : cumulez les aides pour votre projet IA. Simulez gratuit.",  # 90
        "L'Etat investit dans l'IA. Profitez de France 2030, CIR, BPI, +15 dispositifs. Postulez.",  # 90
    ],
    final_url="https://kenrak.com/#aides",
    path1="subvention", path2="ia"
)


# ============================================================
# CAMPAIGN 4: DSA - Dynamic Search Ads ($49/day)
# ============================================================
C4 = "C4 - DSA Dynamic Search"
print(f"\n=== {C4} ===")
add_campaign(C4, 49)

# DSA uses different structure - auto-generated headlines, only descriptions needed
# For Google Ads Editor CSV, DSA ads have Ad Type = "Dynamic search ad"

# AG4.1 - DSA Toutes pages
AG4_1 = "DSA - Toutes pages kenrak.com"
add_ad_group(C4, AG4_1)

# DSA targeting: URL contains kenrak.com (this is set in Editor, not CSV typically)
# DSA Ad 1
make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_1,
    "Description 1": "Lancez votre business IA sans avancer 1E. Credits tech + aides Etat + formation financee. Centre Qualiopi.",
    "Description 2": "+5ME de credits tech gratuits + formation IA financee a 100% par votre OPCO. On s'occupe de tout pour vous.",
    "Final URL": "https://kenrak.com",
    "Ad Type": "Dynamic search ad"
})

# DSA Ad 2
make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_1,
    "Description 1": "Formation IA et credits tech startup en France. OPCO, alternance CFA, aides Etat. Acces 100% gratuit.",
    "Description 2": "Centre certifie Qualiopi. Credits Google Cloud, AWS, Azure gratuits + formation IA financee. Demandez votre acces.",
    "Final URL": "https://kenrak.com",
    "Ad Type": "Dynamic search ad"
})

# AG4.2 - DSA Pages Credits
AG4_2 = "DSA - Pages Credits kenrak.com"
add_ad_group(C4, AG4_2)

make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_2,
    "Description 1": "Accedez a +5ME de credits tech gratuits : Google Cloud, AWS, Azure et 200+ offres startup. Acces gratuit.",
    "Description 2": "Tous les credits tech startup en un seul endroit. Google Cloud 350KE, AWS 300KE, Azure 150KE. Gratuit.",
    "Final URL": "https://kenrak.com/#credits",
    "Ad Type": "Dynamic search ad"
})

make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_2,
    "Description 1": "Credits cloud startup gratuits : Google 350KE, AWS 300KE, Azure 150KE, Cloudflare 250KE. On vous guide.",
    "Description 2": "Pourquoi payer pour du cloud ? Obtenez tous vos credits tech startup gratuitement. 12 partenaires. 100% gratuit.",
    "Final URL": "https://kenrak.com/#credits",
    "Ad Type": "Dynamic search ad"
})

# AG4.3 - DSA Pages Formation/Alternance
AG4_3 = "DSA - Pages Formation kenrak.com"
add_ad_group(C4, AG4_3)

make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_3,
    "Description 1": "Formation IA financee a 100% par OPCO ou alternance CFA. Centre certifie Qualiopi. Inscriptions ouvertes 2026.",
    "Description 2": "Salarie ou candidat ? Votre formation IA est financee. OPCO pour entreprises, CFA pour alternance. 0E a avancer.",
    "Final URL": "https://kenrak.com/#entreprise",
    "Ad Type": "Dynamic search ad"
})

make_row(**{
    "Campaign": C4,
    "Ad Group": AG4_3,
    "Description 1": "Alternance IA remuneree + formation entreprise OPCO. Centre CFA agree Qualiopi. Agents IA, ChatGPT, automations.",
    "Description 2": "La meilleure formation IA en France. 100% financee pour salaries (OPCO) et alternants (CFA). Postulez maintenant.",
    "Final URL": "https://kenrak.com/#alternance",
    "Ad Type": "Dynamic search ad"
})


# ============================================================
# CAMPAIGN 5: RSA - Vibe Business Fund ($49/day)
# ============================================================
C5 = "C5 - Vibe Business Fund"
print(f"\n=== {C5} ===")
add_campaign(C5, 49)

# AG5.1 - Startup Studio IA
AG5_1 = "kenrak.com/#fund"
add_ad_group(C5, AG5_1)

ag51_keywords = [
    "startup studio ia france",
    "creer startup intelligence artificielle",
    "lancer business ia",
    "incubateur ia france",
    "accelerateur startup ia",
    "creer entreprise ia sans argent",
    "business ia rentable",
    "vibe business ia",
    "entrepreneuriat ia france",
    "creer saas ia",
]
add_keywords_all_types(C5, AG5_1, ag51_keywords)

ag51_neg = ["stage", "emploi", "salaire", "CDI"]
add_negative_keywords(C5, AG5_1, ag51_neg)

# Ad 1
print("AG5.1 Ad 1:")
add_rsa_ad(C5, AG5_1,
    h1_dki="{KeyWord:Business IA}",             # 21 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Lancez votre Business IA a 0E",        # 29
        "Startup Studio IA France",              # 24
        "Credits + Aides + Formation",            # 27
        "Vibe Business France 2026",              # 25
        "Creez votre Startup IA",                 # 22
        "On Finance votre Projet IA",             # 26
        "De 0 a Startup en 3 Mois",               # 25
        "Marketplace Business IA",                # 23
        "Incubateur IA France",                   # 20
        "L'IA Cree votre Business",               # 24
        "Startup IA Sans Capital",                # 23
        "Programme Exclusif IA",                  # 21
    ],
    descs=[
        "Startup IA sans avancer 1E. 5ME credits tech + aides Etat 250KE + formation financee.",  # 85
        "Le Startup Studio IA. Credits, formation et financement pour lancer votre business IA.",  # 88
        "Micro-entreprises IA autonomes. Marketplace achat/vente business IA. Vibe Business Fund.",  # 90
        "Plus besoin de capital pour un business IA. Credits tech + aides Etat + formation OPCO.",  # 89
    ],
    final_url="https://kenrak.com/#fund",
    path1="vibe-business", path2="ia"
)

# Ad 2
print("AG5.1 Ad 2:")
add_rsa_ad(C5, AG5_1,
    h1_dki="{KeyWord:Startup IA}",              # 22 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Creez votre Startup IA a 0E",           # 27
        "Vibe Business Fund France",              # 25
        "+5ME Credits Tech Offerts",              # 25
        "Aides Etat jusqu'a 250KE",              # 24
        "Formation IA Financee OPCO",             # 26
        "Accelerateur Startup IA",                # 23
        "Portefeuille Business IA",               # 24
        "Rejoignez le Mouvement IA",              # 26
        "Lancez en 3 Mois",                       # 16
        "Achat/Vente Business IA",                # 23
        "Sans Investissement Initial",             # 27
        "Accompagnement A a Z",                   # 20
    ],
    descs=[
        "Le programme qui lance votre startup IA : credits tech + aides Etat + formation. 0E.",  # 89
        "Rejoignez le Vibe Business Fund. Outils, financement et formation pour l'IA. Postulez.",  # 90
        "Achetez ou creez des micro-business IA rentables. Marketplace exclusive. Rejoignez-nous.",  # 90
        "Pas de capital ? Credits Google/AWS/Azure + aides BPI/CIR + formation OPCO. Lancez-vous.",  # 90
    ],
    final_url="https://kenrak.com/#fund",
    path1="startup", path2="studio-ia"
)

# Ad 3
print("AG5.1 Ad 3:")
add_rsa_ad(C5, AG5_1,
    h1_dki="{KeyWord:Entrepreneur IA}",         # 25 chars
    h2_city="{LOCATION(City):en France}",       # 26 chars
    h3_state="{LOCATION(State):France}",        # 24 chars
    headlines_4_15=[
        "Business IA Sans Capital",              # 24
        "Startup Studio IA 2026",                 # 22
        "Credits + Formation + Aides",            # 27
        "Le Vibe Business commence ici",          # 30
        "Creez un SaaS IA Rentable",              # 25
        "On Finance votre Lancement",             # 26
        "Incubateur IA Exclusif",                 # 22
        "+200 Offres Tech Gratuites",              # 26
        "Marketplace Business IA",                # 23
        "De l'Idee au Business IA",                # 24
        "Programme IA France 2026",                # 24
        "Postulez Maintenant",                     # 19
    ],
    descs=[
        "Entrepreneur IA sans argent. Credits tech, formation OPCO, aides Etat. Apportez l'idee.",  # 87
        "Vibe Business Fund : accelerateur IA. Credits, formation et financement. Programme France.",  # 90
        "Business IA rentable en 3 mois. Startup Studio + accompagnement. Credits + aides inclus.",  # 90
        "L'IA rend l'entrepreneuriat accessible. 0E d'investissement. On vous donne tout. Postulez.",  # 90
    ],
    final_url="https://kenrak.com/#fund",
    path1="entrepreneur", path2="ia"
)


# ============================================================
# EXTENSIONS - Sitelinks
# ============================================================
# Note: Extensions are added as separate rows with specific columns
# Google Ads Editor uses different format for extensions
# We'll create a separate section

print("\n=== EXTENSIONS ===")
# Sitelinks, Callouts, etc. are typically added in Editor UI or via separate CSV
# Adding them as comments in the CSV won't work, but we can create a reference


# ============================================================
# Write CSV
# ============================================================
output_path = "/Users/franck24/MES_SITES_GENERES/kenrak.com/google-ads-import-C3-C4-C5-SOP.csv"

with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=COLS, extrasaction='ignore')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"\n✅ CSV generated: {output_path}")
print(f"   Total rows: {len(rows)}")

# Count elements
campaigns = set()
ad_groups = set()
keywords = 0
ads = 0
for row in rows:
    if row.get("Campaign Daily Budget"):
        campaigns.add(row["Campaign"])
    if row.get("Max CPC") and row.get("Ad Group"):
        ad_groups.add((row["Campaign"], row["Ad Group"]))
    if row.get("Keyword") and not row["Keyword"].startswith("-"):
        keywords += 1
    if row.get("Ad Type"):
        ads += 1

print(f"   Campaigns: {len(campaigns)}")
print(f"   Ad Groups: {len(ad_groups)}")
print(f"   Keywords: {keywords} (across all match types)")
print(f"   Ads: {ads}")
