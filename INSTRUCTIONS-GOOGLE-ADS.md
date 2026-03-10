# GUIDE COMPLET - Import Campagnes Google Ads pour kenrak.com

## Compte Google Ads
- **Compte** : kenrak.com (995-517-3698, aurelien@kenrak.com)
- **Type** : Google Ad Grant ($10K/mois)
- **GTM** : GTM-PD6BHBZD

## Statut des Campagnes
| Campagne | ID | Budget | Statut |
|----------|-----|--------|--------|
| C1 - Formation IA Entreprise OPCO | 23643023932 | $120/jour | PUBLIEE ✅ - CSV SOP pret (google-ads-import-C1-C2-SOP.csv) |
| C2 - Alternance IA Formation Jeunes | 23638468049 | $80/jour | PUBLIEE ✅ - CSV SOP pret (google-ads-import-C1-C2-SOP.csv) |
| C3 - Credits Tech Startup | - | $80/jour | CSV pret (google-ads-import-C3-C4-C5-SOP.csv) |
| C4 - DSA Dynamic Search | - | $49/jour | CSV pret (google-ads-import-C3-C4-C5-SOP.csv) |
| C5 - Vibe Business Fund | - | $49/jour | CSV pret (google-ads-import-C3-C4-C5-SOP.csv) |

## Fichiers du projet
### CSVs Google Ads
- **`google-ads-import-C1-C2-SOP.csv`** : Mise a jour SOP pour C1, C2 deja publiees (132 lignes, 120 keywords, 12 ads, 0 warnings)
- **`google-ads-import-C3-C4-C5-SOP.csv`** : Campagnes 3, 4, 5 avec toutes les regles SOP appliquees (123 lignes, 0 warnings)
- **`google-ads-extensions.csv`** : Extensions pour toutes les campagnes (sitelinks, callouts, snippets, call)
- **`generate-csv.py`** : Script Python pour regenerer le CSV C3-C5
- **`generate-csv-C1-C2-SOP.py`** : Script Python pour regenerer le CSV C1-C2

### Contenu SEO et Marketing
- **`seo-content/reddit-posts.md`** : 5 posts Reddit pour r/france, r/startups, r/artificial, r/smallbusiness
- **`seo-content/linkedin-posts.md`** : 5 posts LinkedIn (credits tech, OPCO, alternance, Vibe Business, agents IA)
- **`seo-content/x-twitter-posts.md`** : 2 threads + 7 tweets individuels pour X/Twitter
- **`seo-content/blog-articles.md`** : 5 structures d'articles SEO (credits tech, aides Etat, OPCO, alternance, Vibe Business)
- **`seo-content/emailing-workflow.md`** : Workflow emailing complet (3 segments, 8 templates, outils recommandes)

### Scripts et Outils
- **`google-apps-script-update-sheet.js`** : Google Apps Script pour mettre a jour le Google Sheet automatiquement
- **`gtm-conversion-tag.json`** : Configuration complete des tags GTM

## REGLES SOP OBLIGATOIRES (a appliquer a TOUTES les campagnes)

### Headlines RSA avec DKI et Location Insertion
- **H1** : `{KeyWord:Texte par defaut}` — Dynamic Keyword Insertion, **pinne en position 1**
- **H2** : `{LOCATION(City):en France}` — Insertion ville, **pinne en position 2**
- **H3** : `{LOCATION(State):France}` — Insertion region, **pinne en position 3**
- H4 a H15 : Headlines specifiques (non pinnes)

### Keywords : 3 types de correspondance obligatoires
Pour CHAQUE mot-cle, creer 3 versions :
- **Broad Match** : `mot cle` (sans symbole)
- **Phrase Match** : `"mot cle"` (guillemets)
- **Exact Match** : `[mot cle]` (crochets)

### Annonces RSA
- **3 annonces RSA par Ad Group** (minimum)
- Chaque annonce a 15 headlines + 4 descriptions
- H1/H2/H3 identiques (DKI + Location), H4-H15 varies entre les 3 annonces

### Extensions
- **Call Extension** : +33756812787 sur toutes les campagnes
- **Sitelinks** : 6 sitelinks (voir google-ads-extensions.csv)
- **Callouts** : 8 callouts (voir google-ads-extensions.csv)
- **Structured Snippets** : 3 snippets (Types, Certifications, Programmes)

### Naming Conventions
- Campagnes RSA : "C# - Nom Campagne" (ex: "C3 - Credits Tech Startup")
- Campagne DSA : "C4 - DSA Francais kenrak.com"
- Ad Groups : URL complete (ex: "kenrak.com/#credits", "kenrak.com/#aides")

---

## ETAPE 1 : Ouvrir Google Ads Editor
1. Telecharger Google Ads Editor : https://ads.google.com/intl/fr/home/tools/ads-editor/
2. Ouvrir Google Ads Editor
3. Selectionner le compte **kenrak.com** (Ad Grant - 995-517-3698)
4. Cliquer "Telecharger les donnees recentes"

## ETAPE 2 : Configurer la strategie d'encheres
**IMPORTANT pour Ad Grant :**
- Aller dans Compte > Parametres
- Strategie d'encheres : **Maximiser les conversions**
- Cela permet de depasser le cap $2 CPC du Ad Grant

## ETAPE 2bis : Importer les campagnes 3-5 via CSV
1. Dans Google Ads Editor : **Compte > Importer > Coller le texte**
2. Ouvrir `google-ads-import-C3-C4-C5-SOP.csv` et copier le contenu
3. Coller dans la fenetre d'import
4. Verifier que toutes les colonnes sont mappees correctement
5. Resoudre les conflits eventuels
6. **Publier les modifications**

## ETAPE 2ter : Appliquer les regles SOP aux campagnes 1 et 2
Les campagnes C1 et C2 sont deja publiees mais sans les regles SOP. Il faut :
1. Ouvrir chaque Ad Group de C1 et C2
2. **Ajouter les keywords Broad et Exact** (actuellement seulement Phrase match)
3. **Modifier chaque annonce RSA** :
   - Remplacer H1 par `{KeyWord:Texte par defaut}` (pinne pos 1)
   - Remplacer H2 par `{LOCATION(City):en France}` (pinne pos 2)
   - Remplacer H3 par `{LOCATION(State):France}` (pinne pos 3)
4. **Creer 2 annonces RSA supplementaires** par Ad Group (il y en a 1 actuellement, il en faut 3)

## ETAPE 3 : Creer les campagnes manuellement dans Google Ads Editor

### CAMPAGNE 1 : C1 - Formation IA Entreprise OPCO
- Type : Search
- Budget quotidien : $120
- Strategie : Maximize Conversions
- Reseaux : Google Search uniquement
- Ciblage geo : France
- Langue : Francais

**Ad Group 1.1 : AG1 - Formation IA OPCO**
Keywords (Phrase Match - ajouter guillemets) :
```
"formation intelligence artificielle opco"
"formation ia financee opco"
"formation chatgpt entreprise opco"
"formation ia entreprise gratuite"
"formation intelligence artificielle entreprise"
"formation ia prise en charge opco"
"opco formation intelligence artificielle"
"formation agent ia entreprise"
"formation automation ia entreprise"
"formation ia certifiante opco"
```

RSA Ad :
- URL finale : https://kenrak.com/#entreprise
- Path 1 : formation-ia / Path 2 : opco
- H1: Formation IA Financee par OPCO
- H2: 0€ a Avancer - 100% Pris en Charge
- H3: Centre Certifie Qualiopi
- H4: Formation IA Entreprise 2026
- H5: Automatisez avec l'IA
- H6: Jusqu'a 9 000€/an Finance
- H7: Agents IA pour votre Business
- H8: Demarrez en 2 Semaines
- H9: +200 Entreprises Formees
- H10: Atlas, AKTO, OPCO 2i, OPCO EP
- H11: Formation Certifiante IA
- H12: Resultat Garanti ou Rembourse
- H13: Audit Gratuit de vos Besoins IA
- H14: ChatGPT, Claude, Agents IA
- H15: Votre OPCO Finance Tout
- D1: Formation IA 100% financee par votre OPCO. Automatisez votre business avec des agents IA. Centre certifie Qualiopi. Demandez votre audit gratuit.
- D2: Votre OPCO prend en charge 3 000 a 9 000€/an de formation IA. On deploie des agents IA qui automatisent vos processus. 0€ a avancer.
- D3: Transformez votre entreprise avec l'IA. Formation certifiante financee a 100% par Atlas, AKTO, OPCO 2i ou OPCO EP. Resultats garantis.
- D4: Arretez de perdre du temps sur des taches repetitives. Nos formations IA deployent des agents autonomes dans votre entreprise. Eligible OPCO.

**Ad Group 1.2 : AG2 - Automatisation IA Business**
Keywords (Phrase Match) :
```
"automatiser entreprise intelligence artificielle"
"automatisation ia pme"
"agent ia entreprise"
"chatbot ia entreprise"
"deployer ia dans son entreprise"
"ia pour pme"
"intelligence artificielle pour business"
"solution ia entreprise france"
"integrer ia dans entreprise"
"consultant ia entreprise"
```

RSA Ad :
- URL finale : https://kenrak.com/#entreprise
- Path 1 : agents-ia / Path 2 : entreprise
- H1: Automatisez votre Business avec l'IA
- H2: Agents IA - 0€ a Avancer
- H3: Formation Financee OPCO
- H4: Deploiement IA en 2 Semaines
- H5: +80% de Taches Automatisees
- H6: IA sur Mesure pour votre PME
- H7: Agents IA Autonomes
- H8: Support, Ventes, Marketing IA
- H9: Solution IA Clef en Main
- H10: Audit IA Gratuit
- H11: ROI Mesurable des 30 Jours
- H12: Expert IA Certifie Qualiopi
- H13: On Cree vos Agents IA
- H14: GPT + Claude pour votre Equipe
- H15: Demandez une Demo IA
- D1: On deploie des agents IA qui automatisent ventes, support et marketing. Formation financee a 100% par votre OPCO. Audit gratuit en 48h.
- D2: Plus de 80% de vos taches repetitives automatisees avec l'IA. Agents intelligents sur mesure. Centre certifie Qualiopi. ROI en 30 jours.
- D3: Votre PME merite aussi l'IA. On cree des solutions sur mesure financees par votre OPCO. Chatbots, automations, agents IA autonomes.
- D4: Arretez de tout faire manuellement. Nos agents IA gerent emails, leads, support client 24/7. Formation complete + deploiement inclus.

---

### CAMPAGNE 2 : C2 - Alternance IA Formation Jeunes
- Type : Search
- Budget quotidien : $80
- Strategie : Maximize Conversions
- Ciblage geo : France
- Langue : Francais

**Ad Group 2.1 : AG1 - Alternance IA**
Keywords (Phrase Match) :
```
"alternance intelligence artificielle"
"alternance ia 2026"
"apprentissage intelligence artificielle"
"bts intelligence artificielle alternance"
"formation alternance ia"
"contrat apprentissage ia"
"alternance chatgpt"
"alternance data ia"
"formation ia alternance remuneree"
"alternance startup ia"
```

RSA Ad :
- URL finale : https://kenrak.com/#alternance
- Path 1 : alternance / Path 2 : ia
- H1: Alternance IA - Salaire des 492€
- H2: BTS Intelligence Artificielle
- H3: Formation 100% Gratuite (CFA)
- H4: Alternance IA 2026 - Postulez
- H5: Diplome Niveau 5 Reconnu Etat
- H6: Creez votre Startup en Alternance
- H7: 0€ de Frais de Formation
- H8: Inscriptions Ouvertes
- H9: Ton Projet = Ta Future Startup
- H10: Apprenez ChatGPT, Claude, IA
- H11: CFA Agree - Qualiopi
- H12: Alternance IA Remuneree
- H13: Construis ton Business IA
- H14: Aide Embauche 5 000€
- H15: Formation IA Pratique
- D1: Alternance IA remuneree des 492€/mois. Diplome BTS reconnu par l'Etat. Formation 100% gratuite en CFA agree. Ton projet scolaire = ta future startup.
- D2: Rejoins notre programme alternance IA. Tu apprends a creer des agents IA, deployer des solutions business. Salaire garanti + formation gratuite.
- D3: Pas besoin de Bac+5 pour travailler dans l'IA. Notre BTS en alternance te forme aux outils concrets : ChatGPT, Claude, agents autonomes.
- D4: Programme alternance IA unique en France. Tu construis ta startup pendant ta formation. Diplome reconnu Etat + salaire des 492€/mois.

**Ad Group 2.2 : AG2 - Formation IA Gratuite**
Keywords (Phrase Match) :
```
"formation ia gratuite"
"formation intelligence artificielle gratuite france"
"formation chatgpt gratuite certifiante"
"formation ia remuneree"
"formation ia financee"
"apprendre ia gratuitement france"
"formation agent ia"
"formation ia certifiante gratuite"
"se former a l'ia en france"
"formation ia debutant france"
```

RSA Ad :
- URL finale : https://kenrak.com/#alternance
- Path 1 : formation-ia / Path 2 : gratuite
- H1: Formation IA Gratuite et Certifiante
- H2: Financee a 100% (OPCO ou CFA)
- H3: Certifie Qualiopi
- H4: Devenez Expert IA en 2026
- H5: 0€ de Frais - Formation IA
- H6: Agents IA, ChatGPT, Claude
- H7: Formation IA Pratique France
- H8: Inscriptions Ouvertes
- H9: Diplome Reconnu par l'Etat
- H10: Apprenez l'IA qui Compte
- H11: Centre Agree CFA Qualiopi
- H12: Formation IA pour Tous
- H13: Pas de Pre-Requis Technique
- H14: Commencez en 2 Semaines
- H15: Formation IA Concrete
- D1: Formation IA certifiante 100% financee. Que vous soyez salarie (OPCO) ou candidat (alternance CFA), vous ne payez rien. Centre certifie Qualiopi.
- D2: Apprenez a creer des agents IA, automatiser des processus, utiliser ChatGPT et Claude comme un pro. Formation financee et certifiante.
- D3: Pas besoin d'etre developpeur pour se former a l'IA. Notre programme vous rend operationnel en quelques semaines. 100% finance.
- D4: La meilleure formation IA en France. Gratuite pour les salaries (OPCO) et alternants (CFA). On vous forme aux outils qui comptent vraiment.

---

### CAMPAGNE 3 : C3 - Credits Tech Startup
- Type : Search
- Budget quotidien : $80
- Strategie : Maximize Conversions
- Ciblage geo : France
- Langue : Francais

**Ad Group 3.1 : AG1 - Credits Cloud Startup**
Keywords (Phrase Match) :
```
"credits google cloud startup"
"credits aws startup gratuit"
"credits cloud startup france"
"google for startups credits"
"microsoft for startups azure"
"credits tech startup gratuit"
"programme startup cloud"
"credits hebergement startup"
"offres startups tech gratuites"
"avantages startup tech france"
```

RSA Ad :
- URL finale : https://kenrak.com/#credits
- Path 1 : credits-tech / Path 2 : startup
- H1: +5M€ de Credits Tech Gratuits
- H2: Google Cloud, AWS, Azure, Stripe
- H3: 200+ Offres Startup Gratuites
- H4: Credits Cloud Startup France
- H5: Jusqu'a 350K€ Google Cloud
- H6: 300K€ Credits AWS Gratuits
- H7: Acces 100% Gratuit
- H8: Obtenez vos Credits en 48h
- H9: OpenAI, Anthropic, Datadog
- H10: +5M€ d'Outils Tech Offerts
- H11: Startup France - Credits Gratuits
- H12: On vous Aide a Postuler
- H13: 12 Partenaires Tech
- H14: Credits IA Startup Gratuits
- H15: Lancez sans Depenser 1€
- D1: Accedez a +5M€ de credits tech gratuits : Google Cloud 350K€, AWS 300K€, Azure 150K€, Cloudflare 250K€, et plus. 100% gratuit, on vous guide.
- D2: Plus de 200 offres startup gratuites en un seul endroit. Credits cloud, IA, analytics, paiements. Demandez votre acces gratuit maintenant.
- D3: Pourquoi payer pour du cloud ? Obtenez jusqu'a 350 000€ de credits Google Cloud, 300 000€ AWS et 150 000€ Azure. Acces guide et gratuit.
- D4: Lancez votre startup IA sans avancer 1€. On vous donne acces aux meilleurs programmes de credits tech : Google, AWS, Microsoft, Stripe, OpenAI.

**Ad Group 3.2 : AG2 - Aides Etat Startup IA**
Keywords (Phrase Match) :
```
"aide creation startup ia france"
"bpi france startup ia"
"subvention startup ia"
"aide etat intelligence artificielle"
"france 2030 ia"
"cir credit impot recherche ia"
"financement startup ia france"
"bourse french tech"
"aide innovation ia france"
"subvention intelligence artificielle france"
```

RSA Ad :
- URL finale : https://kenrak.com/#aides
- Path 1 : aides-etat / Path 2 : ia
- H1: Aides Etat IA - Jusqu'a 250K€
- H2: BPI France, CIR, CII, OPCO
- H3: France 2030 - Pionniers IA
- H4: Subvention IA jusqu'a 100%
- H5: CIR : 30% de vos Depenses R&D
- H6: Bourse French Tech 30 000€
- H7: Aide Startup IA France 2026
- H8: On vous Guide pour Postuler
- H9: Audit Aides Gratuit
- H10: CII : 20% Innovation (80K€)
- H11: France Num Pret 50 000€
- H12: Simulez vos Aides IA
- H13: Aides Regionales jusqu'a 250K€
- H14: Expert en Financement IA
- H15: Obtenez vos Aides en 30 Jours
- D1: Decouvrez toutes les aides Etat pour votre projet IA : CIR 30%, CII 20%, BPI France 90K€, France 2030 jusqu'a 100%. Simulez vos aides gratuit.
- D2: Plus de 15 dispositifs d'aide pour les startups IA en France. BPI, CIR, CII, OPCO, France 2030, aides regionales. On vous accompagne gratuitement.
- D3: Ne laissez pas d'argent sur la table. La France finance massivement l'IA : CIR, CII, BPI France, France 2030. Audit gratuit de votre eligibilite.
- D4: Vous developpez un projet IA ? L'Etat peut financer jusqu'a 100% en phase 1 (France 2030). + CIR 30% + Bourse French Tech 30K€. Contactez-nous.

---

### CAMPAGNE 4 : C4 - DSA Dynamic Search
- Type : Search (Dynamic Search Ads)
- Budget quotidien : $49
- Strategie : Maximize Conversions
- Ciblage geo : France
- Langue : Francais
- Domain source : kenrak.com

**Ad Group 4.1 : DSA - Toutes pages**
- Ciblage : URL contient "kenrak.com"
- D1: Lancez votre business IA sans avancer 1€. Credits tech + aides Etat + formation financee. Centre certifie Qualiopi. Demandez votre acces gratuit.
- D2: +5M€ de credits tech gratuits + formation IA financee a 100% par votre OPCO. Alternance ou entreprise. On s'occupe de tout pour vous.

---

### CAMPAGNE 5 : C5 - Vibe Business Fund Startup Studio
- Type : Search
- Budget quotidien : $49
- Strategie : Maximize Conversions
- Ciblage geo : France
- Langue : Francais

**Ad Group 5.1 : AG1 - Startup Studio IA**
Keywords (Phrase Match) :
```
"startup studio ia france"
"creer startup intelligence artificielle"
"lancer business ia"
"incubateur ia france"
"accelerateur startup ia"
"creer entreprise ia sans argent"
"business ia rentable"
"vibe business ia"
"entrepreneuriat ia france"
"creer saas ia"
```

RSA Ad :
- URL finale : https://kenrak.com/#fund
- Path 1 : vibe-business / Path 2 : ia
- H1: Lancez votre Business IA a 0€
- H2: Startup Studio IA France
- H3: Credits + Aides + Formation
- H4: Vibe Business France 2026
- H5: Creez votre Startup IA
- H6: On Finance votre Projet IA
- H7: De 0 a Startup en 3 Mois
- H8: Marketplace Business IA
- H9: Achat/Vente de Business IA
- H10: Incubateur IA France
- H11: Portefeuille Micro-Entreprises IA
- H12: L'IA Cree votre Business
- H13: Startup IA Sans Capital
- H14: Rejoignez le Mouvement
- H15: Programme Exclusif IA
- D1: Creez votre startup IA sans avancer 1€. Acces a 5M€ de credits tech + aides Etat jusqu'a 250K€ + formation financee. Le Vibe Business commence ici.
- D2: Le Startup Studio IA qui change les regles. On vous donne credits, formation et financement pour lancer votre business IA. Programme exclusif France.
- D3: Investissez dans un portefeuille de micro-entreprises IA autonomes. Marketplace achat/vente de business IA. Rejoignez le Vibe Business Fund.
- D4: Plus besoin de capital pour lancer un business IA. Credits tech gratuits + aides Etat + formation OPCO. On s'occupe de l'infra, vous de la vision.

---

## ETAPE 4 : Extensions d'annonces (a ajouter a TOUTES les campagnes)
**Fichier CSV d'import : `google-ads-extensions.csv`**

### Sitelinks (6) :
1. Titre: Credits Tech Gratuits | Desc1: +5ME de credits tech | Desc2: Google AWS Azure Cloudflare | URL: https://kenrak.com/#credits
2. Titre: Aides Etat IA | Desc1: CIR BPI France 2030 | Desc2: Jusqu'a 250KE d'aides | URL: https://kenrak.com/#aides
3. Titre: Formation Entreprise OPCO | Desc1: 100% financee OPCO | Desc2: Centre certifie Qualiopi | URL: https://kenrak.com/#entreprise
4. Titre: Alternance IA | Desc1: BTS des 492E/mois | Desc2: Formation CFA gratuite | URL: https://kenrak.com/#alternance
5. Titre: Vibe Business Fund | Desc1: Startup Studio IA | Desc2: Lancez votre business | URL: https://kenrak.com/#fund
6. Titre: Simulateur Aides | Desc1: Calculez vos aides IA | Desc2: Eligibilite en 2 minutes | URL: https://kenrak.com/#simulateur

### Callout Extensions (8) :
- Centre Certifie Qualiopi
- CFA Agree par l'Etat
- 0€ a Avancer
- +200 Offres Gratuites
- Formation 100% Financee
- Aides jusqu'a 250K€
- +5M€ Credits Tech
- Partenaire BPI France

### Structured Snippets (3) :
- En-tete: Types | Valeurs: Formation IA, Alternance IA, Credits Cloud, Aides Etat, Startup Studio, Agents IA
- En-tete: Certifications | Valeurs: Qualiopi, CFA Agree, Partenaire BPI, France 2030, OPCO
- En-tete: Programmes | Valeurs: Google Cloud 350KE, AWS 300KE, Azure 150KE, Cloudflare 250KE, Stripe 50KE

### Call Extension :
- Numero : +33756812787

---

## ETAPE 5 : Keywords negatifs (au niveau du compte)
```
-emploi
-stage
-etudiant gratuit
-youtube
-tuto
-mooc
-coupon
-promo code
-crack
-hack
-pirate
-master
-ingenieur
-bac+5
-doctorat
-these
-stage non remunere
```

## ETAPE 6 : Publier et verifier
1. Dans Google Ads Editor : Verifier > Publier les modifications
2. Attendre 24h pour l'approbation des annonces
3. Verifier le CTR apres 7 jours (doit etre > 5% pour Ad Grant)
4. Ajuster les encheres si necessaire

## ETAPE 7 : Conversion Tracking (GTM)
- **GTM Container** : GTM-PD6BHBZD
- Voir le fichier gtm-conversion-tag.json pour la configuration complete
- Conversions a tracker : clics sur sections (#credits, #aides, #entreprise, #alternance, #fund), scroll 50%+, temps sur page > 60s

## Recapitulatif Budget Total
| Campagne | Budget/jour | Budget/mois |
|----------|------------|-------------|
| C1 - Formation IA Entreprise OPCO | $120 | $3,600 |
| C2 - Alternance IA Formation Jeunes | $80 | $2,400 |
| C3 - Credits Tech Startup | $80 | $2,400 |
| C4 - DSA Dynamic Search | $49 | $1,470 |
| C5 - Vibe Business Fund | $49 | $1,470 |
| **TOTAL** | **$378** | **$11,340** |

> Note : Le budget total depasse legerement le Ad Grant de $10K/mois.
> Google ajustera automatiquement les depenses reelles au plafond du grant.
> Prioriser C1 et C2 si necessaire (budgets les plus eleves).

---

## ACTIONS MANUELLES REQUISES (par ordre de priorite)

### 1. Importer C3-C5 dans Google Ads Editor (HAUTE)
1. Ouvrir Google Ads Editor
2. Telecharger les donnees recentes du compte 995-517-3698
3. Menu : Compte > Importer > Coller le texte
4. Copier le contenu de `google-ads-import-C3-C4-C5-SOP.csv`
5. Coller et verifier le mapping des colonnes
6. Publier les modifications

### 2. Appliquer SOP a C1 et C2 (HAUTE)
1. Dans Google Ads Editor : Compte > Importer > Coller le texte
2. Copier le contenu de `google-ads-import-C1-C2-SOP.csv`
3. Coller et resoudre les conflits (ajouter les nouveaux keywords et ads)
4. **IMPORTANT** : Mettre en pause les anciennes annonces RSA (celles sans DKI/Location)
5. Publier les modifications

### 3. Importer les extensions (HAUTE)
1. Dans Google Ads Editor : utiliser `google-ads-extensions.csv`
2. Appliquer les sitelinks, callouts, snippets et call a TOUTES les campagnes
3. Publier

### 4. Configurer GTM Conversions (HAUTE)
1. Ouvrir GTM (GTM-PD6BHBZD) : https://tagmanager.google.com
2. Creer les tags de conversion Google Ads (voir gtm-conversion-tag.json)
3. Configurer les triggers : clics sections, scroll 50%+, temps > 60s
4. Publier le container GTM

### 5. Mettre a jour le Google Sheet (MOYENNE)
1. Ouvrir le Google Sheet : https://docs.google.com/spreadsheets/d/1qP0CT3Xs-UxRfLjm4Oy6KROQarJbK7XtSKgVN449Axo/edit
2. Menu : Extensions > Apps Script
3. Coller le contenu de `google-apps-script-update-sheet.js`
4. Executer `updateKenrakSheet()`
5. Autoriser l'acces quand demande

### 6. Publier contenu SEO (MOYENNE)
1. Publier les posts Reddit (voir `seo-content/reddit-posts.md`)
2. Publier les posts LinkedIn (voir `seo-content/linkedin-posts.md`)
3. Publier les tweets/threads X (voir `seo-content/x-twitter-posts.md`)
4. Creer les articles de blog (voir `seo-content/blog-articles.md`)

### 7. Lancer les sequences emailing (BASSE)
1. Choisir un outil : Brevo, HubSpot, ou Make.com
2. Configurer les 3 segments (Entreprises, Alternance, Startups)
3. Importer les templates (voir `seo-content/emailing-workflow.md`)
4. Lancer les sequences

---

## GitHub Repository
- **URL** : https://github.com/franckparienti/kenrak.com
- **Branche** : main
- **Deploiement** : Cloudflare Pages (kenrak.com)
