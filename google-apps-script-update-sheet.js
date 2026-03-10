/**
 * Google Apps Script — Mettre a jour le Google Sheet Kenrak
 *
 * INSTRUCTIONS :
 * 1. Ouvrir le Google Sheet : https://docs.google.com/spreadsheets/d/1qP0CT3Xs-UxRfLjm4Oy6KROQarJbK7XtSKgVN449Axo/edit
 * 2. Menu > Extensions > Apps Script
 * 3. Coller ce script
 * 4. Executer la fonction principale : updateKenrakSheet()
 * 5. Autoriser l'acces au Google Sheet quand demande
 */

function updateKenrakSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();

  // Creer ou trouver l'onglet "Kenrak - Google Ads"
  var sheet = getOrCreateSheet(ss, "Kenrak - Google Ads");

  // Ecrire les donnees
  writeGoogleAdsData(sheet);

  // Creer ou trouver l'onglet "Kenrak - GTM & Tracking"
  var trackingSheet = getOrCreateSheet(ss, "Kenrak - GTM & Tracking");
  writeTrackingData(trackingSheet);

  // Creer ou trouver l'onglet "Kenrak - SEO & Content"
  var seoSheet = getOrCreateSheet(ss, "Kenrak - SEO & Content");
  writeSEOData(seoSheet);

  SpreadsheetApp.getUi().alert("Mise a jour terminee !");
}

function getOrCreateSheet(ss, name) {
  var sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
  } else {
    sheet.clear();
  }
  return sheet;
}

function writeGoogleAdsData(sheet) {
  // Titre
  sheet.getRange("A1").setValue("KENRAK.COM — GOOGLE ADS CAMPAIGNS").setFontSize(14).setFontWeight("bold");
  sheet.getRange("A2").setValue("Compte : 995-517-3698 | Ad Grant $10K/mois | aurelien@kenrak.com").setFontSize(10);
  sheet.getRange("A3").setValue("Derniere mise a jour : " + new Date().toLocaleDateString("fr-FR")).setFontSize(9).setFontColor("#666666");

  // En-tetes campagnes
  var headers = ["Campagne", "ID", "Budget/jour", "Budget/mois", "Type", "Statut", "Ad Groups", "Keywords", "Annonces RSA", "CSV Import"];
  sheet.getRange(5, 1, 1, headers.length).setValues([headers])
    .setFontWeight("bold")
    .setBackground("#1a73e8")
    .setFontColor("white");

  // Donnees campagnes
  var campaigns = [
    ["C1 - Formation IA Entreprise OPCO", "23643023932", "$120", "$3,600", "Search RSA", "PUBLIEE ✅", "2 (AG1.1, AG1.2)", "20 x 3 types = 60", "6 (3 par AG)", "google-ads-import-C1-C2-SOP.csv"],
    ["C2 - Alternance IA Formation Jeunes", "23638468049", "$80", "$2,400", "Search RSA", "PUBLIEE ✅", "2 (AG2.1, AG2.2)", "20 x 3 types = 60", "6 (3 par AG)", "google-ads-import-C1-C2-SOP.csv"],
    ["C3 - Credits Tech Startup", "-", "$80", "$2,400", "Search RSA", "CSV PRET 📋", "2 (AG3.1, AG3.2)", "20 x 3 types = 60", "6 (3 par AG)", "google-ads-import-C3-C4-C5-SOP.csv"],
    ["C4 - DSA Dynamic Search", "-", "$49", "$1,470", "DSA", "CSV PRET 📋", "1 (DSA toutes pages)", "Auto (DSA)", "1 (descriptions)", "google-ads-import-C3-C4-C5-SOP.csv"],
    ["C5 - Vibe Business Fund", "-", "$49", "$1,470", "Search RSA", "CSV PRET 📋", "1 (AG5.1)", "10 x 3 types = 30", "3", "google-ads-import-C3-C4-C5-SOP.csv"],
    ["TOTAL", "", "$378", "$11,340", "", "", "8", "210+", "22", ""]
  ];
  sheet.getRange(6, 1, campaigns.length, campaigns[0].length).setValues(campaigns);

  // Formatage ligne total
  sheet.getRange(11, 1, 1, headers.length).setFontWeight("bold").setBackground("#e8f0fe");

  // Section SOP
  sheet.getRange("A13").setValue("REGLES SOP APPLIQUEES").setFontSize(12).setFontWeight("bold");

  var sopData = [
    ["Regle", "Detail", "Statut"],
    ["DKI H1", "{KeyWord:Default} pinne position 1", "✅ Applique"],
    ["Location H2", "{LOCATION(City):en France} pinne position 2", "✅ Applique"],
    ["Location H3", "{LOCATION(State):France} pinne position 3", "✅ Applique"],
    ["3 Match Types", "Broad + Phrase + Exact pour chaque keyword", "✅ Applique"],
    ["3 RSA Ads/AG", "3 annonces RSA par Ad Group minimum", "✅ Applique"],
    ["Extensions", "Sitelinks, Callouts, Snippets, Call", "✅ CSV pret"],
    ["Naming", "C# + AG# + URL complete", "✅ Applique"],
    ["Negative Keywords", "17 mots-cles negatifs au niveau compte", "✅ Dans CSV"],
    ["Maximize Conversions", "Strategie d'encheres Ad Grant", "✅ Configure"]
  ];
  sheet.getRange(14, 1, sopData.length, 3).setValues(sopData);
  sheet.getRange(14, 1, 1, 3).setFontWeight("bold").setBackground("#34a853").setFontColor("white");

  // Section fichiers
  sheet.getRange("A25").setValue("FICHIERS CSV").setFontSize(12).setFontWeight("bold");
  var files = [
    ["Fichier", "Contenu", "Lignes", "Warnings"],
    ["google-ads-import-C1-C2-SOP.csv", "Mise a jour SOP C1 + C2 (keywords + ads)", "132", "0"],
    ["google-ads-import-C3-C4-C5-SOP.csv", "Campagnes 3, 4, 5 completes avec SOP", "123", "0"],
    ["google-ads-extensions.csv", "Sitelinks, Callouts, Snippets, Call", "18", "0"],
    ["generate-csv.py", "Script Python C3-C5", "-", "-"],
    ["generate-csv-C1-C2-SOP.py", "Script Python C1-C2", "-", "-"]
  ];
  sheet.getRange(26, 1, files.length, 4).setValues(files);
  sheet.getRange(26, 1, 1, 4).setFontWeight("bold").setBackground("#fbbc04").setFontColor("black");

  // Section prochaines etapes
  sheet.getRange("A33").setValue("PROCHAINES ETAPES").setFontSize(12).setFontWeight("bold");
  var steps = [
    ["Etape", "Action", "Priorite", "Statut"],
    ["1", "Importer C3-C5 via Google Ads Editor", "HAUTE", "A FAIRE"],
    ["2", "Appliquer SOP C1-C2 via Google Ads Editor", "HAUTE", "A FAIRE"],
    ["3", "Importer extensions sur toutes les campagnes", "MOYENNE", "A FAIRE"],
    ["4", "Configurer conversions GTM (GTM-PD6BHBZD)", "HAUTE", "A FAIRE"],
    ["5", "Verifier CTR > 5% apres 7 jours", "MOYENNE", "EN ATTENTE"],
    ["6", "Publier contenu SEO (blog, Reddit, LinkedIn)", "MOYENNE", "CONTENU PRET"],
    ["7", "Lancer sequences emailing", "BASSE", "TEMPLATES PRETS"]
  ];
  sheet.getRange(34, 1, steps.length, 4).setValues(steps);
  sheet.getRange(34, 1, 1, 4).setFontWeight("bold").setBackground("#ea4335").setFontColor("white");

  // Auto-resize columns
  for (var i = 1; i <= 10; i++) {
    sheet.autoResizeColumn(i);
  }
}

function writeTrackingData(sheet) {
  sheet.getRange("A1").setValue("KENRAK.COM — GTM & CONVERSION TRACKING").setFontSize(14).setFontWeight("bold");
  sheet.getRange("A2").setValue("GTM Container : GTM-PD6BHBZD").setFontSize(10);

  var data = [
    ["Element", "Detail", "Statut"],
    ["GTM Container ID", "GTM-PD6BHBZD", "✅ Installe sur kenrak.com"],
    ["GTM Script", "Ligne 15-19 de index.html", "✅ En place"],
    ["Noscript Fallback", "Ligne 53 de index.html", "✅ En place"],
    ["", "", ""],
    ["CONVERSIONS A TRACKER", "", ""],
    ["Clic #credits", "Scroll ou clic vers section Credits Tech", "A configurer"],
    ["Clic #aides", "Scroll ou clic vers section Aides Etat", "A configurer"],
    ["Clic #entreprise", "Scroll ou clic vers section Formation Entreprise", "A configurer"],
    ["Clic #alternance", "Scroll ou clic vers section Alternance", "A configurer"],
    ["Clic #fund", "Scroll ou clic vers section Vibe Business Fund", "A configurer"],
    ["Clic #inscription", "Clic sur bouton d'inscription", "A configurer"],
    ["Scroll 50%+", "Utilisateur scrolle plus de 50% de la page", "A configurer"],
    ["Temps > 60s", "Utilisateur reste plus de 60 secondes", "A configurer"],
    ["", "", ""],
    ["CONFIGURATION GTM", "", ""],
    ["Tag type", "Google Ads Conversion Tracking", ""],
    ["Conversion ID", "A recuperer dans Google Ads > Outils > Conversions", ""],
    ["Trigger Scroll", "Scroll Depth > 50%", ""],
    ["Trigger Timer", "Timer > 60000ms", ""],
    ["Trigger Click", "Click URL contains #credits/#aides/etc.", ""],
    ["", "", ""],
    ["FICHIER CONFIG", "", ""],
    ["gtm-conversion-tag.json", "Configuration complete des tags GTM", "✅ Cree"]
  ];

  sheet.getRange(4, 1, data.length, 3).setValues(data);
  sheet.getRange(4, 1, 1, 3).setFontWeight("bold").setBackground("#1a73e8").setFontColor("white");
  sheet.getRange(9, 1, 1, 3).setFontWeight("bold").setBackground("#e8f0fe");
  sheet.getRange(19, 1, 1, 3).setFontWeight("bold").setBackground("#e8f0fe");
  sheet.getRange(25, 1, 1, 3).setFontWeight("bold").setBackground("#e8f0fe");

  for (var i = 1; i <= 3; i++) {
    sheet.autoResizeColumn(i);
  }
}

function writeSEOData(sheet) {
  sheet.getRange("A1").setValue("KENRAK.COM — SEO & CONTENT STRATEGY").setFontSize(14).setFontWeight("bold");
  sheet.getRange("A2").setValue("Site : https://kenrak.com | GitHub : https://github.com/franckparienti/kenrak.com").setFontSize(10);

  var data = [
    ["Plateforme", "Type de contenu", "Titre/Theme", "Cible", "Statut"],
    ["Reddit r/france", "Post long format", "Toutes les aides pour business IA en France", "Entrepreneurs FR", "Template pret"],
    ["Reddit r/startups", "Post long format", "Bootstrapped AI business with $0", "Startups internationales", "Template pret"],
    ["Reddit r/artificial", "Post liste", "Complete list of free AI credits 2026", "Devs/ML engineers", "Template pret"],
    ["Reddit r/france", "Post guide", "Alternance IA 2026 : se former gratuitement", "Jeunes/etudiants", "Template pret"],
    ["Reddit r/smallbusiness", "Post cas d'usage", "AI agents for small businesses", "PME", "Template pret"],
    ["LinkedIn", "Post accroche", "5M EUR de credits tech gratuits", "Decision makers", "Template pret"],
    ["LinkedIn", "Post education", "Formation IA OPCO financee", "DRH/RF", "Template pret"],
    ["LinkedIn", "Post carrousel", "Alternance IA — programme et debouches", "Jeunes/parents", "Template pret"],
    ["LinkedIn", "Post thought leadership", "Vibe Business — la revolution", "Entrepreneurs", "Template pret"],
    ["LinkedIn", "Post cas d'usage", "5 agents IA pour PME", "Dirigeants PME", "Template pret"],
    ["X/Twitter", "Thread 7 tweets", "5M EUR credits tech gratuits", "Tech/startup", "Template pret"],
    ["X/Twitter", "Thread 5 tweets", "Vibe Business manifesto", "Entrepreneurs", "Template pret"],
    ["X/Twitter", "Tweets individuels x7", "Credits, OPCO, alternance, agents IA", "Audience mixte", "Template pret"],
    ["", "", "", "", ""],
    ["BLOG ARTICLES (SEO)", "", "", "", ""],
    ["Blog kenrak.com", "Article 2000+ mots", "Credits Tech Gratuits Startup 2026", "credits tech startup", "Structure prete"],
    ["Blog kenrak.com", "Article 2000+ mots", "Aides Etat Startup IA France 2026", "aide startup ia france", "Structure prete"],
    ["Blog kenrak.com", "Article 2000+ mots", "Formation IA OPCO 2026", "formation ia opco", "Structure prete"],
    ["Blog kenrak.com", "Article 2000+ mots", "Alternance IA 2026", "alternance intelligence artificielle", "Structure prete"],
    ["Blog kenrak.com", "Article 2000+ mots", "Vibe Business France 2026", "lancer business ia", "Structure prete"],
    ["", "", "", "", ""],
    ["EMAILING", "", "", "", ""],
    ["Segment Entreprises", "Sequence 4 emails", "Formation OPCO + Agents IA", "PME/ETI", "Templates prets"],
    ["Segment Alternance", "Sequence 2 emails", "BTS IA + inscription", "Jeunes 16-30", "Templates prets"],
    ["Segment Startups", "Sequence 2 emails", "Credits tech + Vibe Business", "Entrepreneurs", "Templates prets"]
  ];

  sheet.getRange(4, 1, data.length, 5).setValues(data);
  sheet.getRange(4, 1, 1, 5).setFontWeight("bold").setBackground("#34a853").setFontColor("white");
  sheet.getRange(19, 1, 1, 5).setFontWeight("bold").setBackground("#e8f0fe");
  sheet.getRange(25, 1, 1, 5).setFontWeight("bold").setBackground("#e8f0fe");

  for (var i = 1; i <= 5; i++) {
    sheet.autoResizeColumn(i);
  }
}
