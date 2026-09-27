import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURAZIONE PAGINA & STILE ---
st.set_page_config(
    page_title="Comparatore Energia & Legenda",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stile visivo globale e colori Blue Navy coordinati
st.markdown("""
    <style>
    .main { color: #ffffff; }
    .stMetric { 
        background-color: #1e3a8a !important; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #3b82f6 !important; 
    }
    .stMetric label { color: #93c5fd !important; font-weight: 600; font-size: 0.95em; }
    .stMetric [data-testid="stMetricValue"] { color: #ffffff !important; font-weight: bold; }
    .blue-card {
        background-color: #1e3a8a;
        color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #3b82f6;
        margin-top: 25px;
        font-family: sans-serif;
    }
    .legend-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. MENU DI NAVIGAZIONE ---
st.sidebar.title("⚡ Menu di Navigazione")
menu = st.sidebar.radio(
    "Seleziona Sezione:",
    [
        "🧮 Motore di Calcolo & Confronto", 
        "📖 Legenda & Glossario Energetico"
    ]
)

# =====================================================================
# SEZIONE 1: MOTORE DI CALCOLO & CONFRONTO
# =====================================================================
if menu == "🧮 Motore di Calcolo & Confronto":
    st.title("🧮 Motore di Calcolo & Confronto Offerte")
    st.markdown("Inserisci i dati della tua fornitura attuale per confrontarli in tempo reale con le migliori tariffe sul mercato.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("I tuoi dati attuali")
        bolletta_attuale = st.number_input("Spesa annua attuale stimata (€)", min_value=0.0, value=1200.0, step=50.0)
        consumo_annuo = st.number_input("Consumo annuo stimato (kWh o Smc)", min_value=0.0, value=2700.0, step=100.0)
    
    with col2:
        st.subheader("Simulazione Offerte Disponibili")
        tipo_mercato = st.selectbox("Tipo di Offerta", ["Prezzo Fisso", "Prezzo Variabile (Indicizzato)"])
        spread_offert = st.slider("Spread / Margine fornitore (€)", 0.0, 0.10, 0.02, 0.005)

    st.markdown("---")
    st.subheader("Risultati del Confronto")

    # Simulazione calcolo risparmio
    spesa_nuova_stimata = consumo_annuo * (0.22 + spread_offert) + 120.0 # stima indicativa
    risparmio = bolletta_attuale - spesa_nuova_stimata

    m1, m2, m3 = st.columns(3)
    m1.metric("Spesa Attuale", f"€ {bolletta_attuale:,.2f}")
    m2.metric("Nuova Spesa Stimata", f"€ {spesa_nuova_stimata:,.2f}")
    m3.metric("Risparmio Annuo Potenziale", f"€ {risparmio:,.2f}", delta="Conveniente" if risparmio > 0 else "Da valutare")

    # --- CARTELLINO BLUE NAVY CON LA SPIEGAZIONE RICHIESTA ---
    st.markdown("""
        <div class="blue-card">
            <h4 style="color: #93c5fd; margin-top: 0; margin-bottom: 12px;">ℹ️ Come funziona il motore di calcolo</h4>
            <p style="margin-bottom: 8px;">• L'utente inserisce i dati della sua bolletta attuale (o i suoi consumi annui e la spesa che affronta oggi).</p>
            <p style="margin-bottom: 8px;">• L'app calcola e confronta la spesa attuale con le stime delle offerte disponibili.</p>
            <p style="margin-bottom: 0;">• Il risultato finale mostra chiaramente quanto si spende in totale all'anno con la nuova offerta e quanto si riesce a risparmiare rispetto a ciò che si paga oggi.</p>
        </div>
    """, unsafe_allow_html=True)

# =====================================================================
# SEZIONE 2: LEGENDA & GLOSSARIO ENERGETICO
# =====================================================================
elif menu == "📖 Legenda & Glossario Energetico":
    st.title("📖 Legenda & Glossario Energetico")
    st.markdown("Una guida completa a tutti i parametri presi in considerazione dal comparatore e al motivo per cui sono fondamentali per scegliere consapevolmente.")

    st.markdown("""
    <div class="legend-box">
        <h3>1. Spesa Annua Stimata</h3>
        <p><b>Definizione:</b> È la previsione del costo totale che sosterrai in un intero anno (12 mesi) con una specifica offerta, calcolata sulla base dei tuoi consumi stimati o storici.</p>
        <p><b>Perché è utile prenderla in considerazione:</b> È il parametro fondamentale per confrontare le offerte in modo diretto. Ti permette di capire immediatamente, a parità di consumi, quale operatore ti farà spendere meno in totale alla fine dell'anno, evitando brutte sorprese.</p>
    </div>

    <div class="legend-box">
        <h3>2. Costo Commerciale Annuo (Quota Fissa / PCV / QVD)</h3>
        <p><b>Definizione:</b> È una componente di prezzo fissa stabilita dal fornitore (spesso chiamata <i>Prezzo di Commercializzazione e Vendita</i> per la luce o <i>QVD</i> per il gas) espressa in euro all'anno.</p>
        <p><b>Perché è utile prenderla in considerazione:</b> Si paga a prescindere da quanto consumi (anche se consumi zero). Se hai consumi bassi (es. seconda casa), un costo commerciale basso incide moltissimo sul risparmio complessivo.</p>
    </div>

    <div class="legend-box">
        <h3>3. Consumo Annuo (kWh per Luce / Smc per Gas)</h3>
        <p><b>Definizione:</b> La quantità complessiva di energia elettrica (in chilowattora) o di gas naturale (in standard metri cubi) consumata in un anno solare.</p>
        <p><b>Perché è utile prenderla in considerazione:</b> È il dato di partenza indispensabile per il calcolo. Conoscere il consumo reale evita stime errate e permette di dimensionare correttamente l'offerta sulle proprie reali abitudini di vita.</p>
    </div>

    <div class="legend-box">
        <h3>4. Prezzo della Materia Prima (Quota Variabile)</h3>
        <p><b>Definizione:</b> Il costo effettivo della singola unità di energia o gas (es. €/kWh o €/Smc) stabilito dal gestore. Può essere <i>Fisso</i> (bloccato per 12-24 mesi) o <i>Variabile</i> (indicizzato agli indici di borsa PUN per la luce e PSV per il gas).</p>
        <p><b>Perché è utile prenderla in considerazione:</b> Determina quanto paghi effettivamente per ogni singolo elettrofondo o riscaldamento acceso. Aiuta a scegliere tra la tranquillità di un prezzo fisso e la convenienza potenziale di un prezzo variabile.</p>
    </div>

    <div class="legend-box">
        <h3>5. Spesa per il Trasporto e Gestione del Contatore</h3>
        <p><b>Definizione:</b> Importi stabiliti dall'Autorità (ARERA) per remunerare i servizi di trasmissione, distribuzione e misura dell'energia sulla rete locale.</p>
        <p><b>Perché è utile prenderla in considerazione:</b> Sono costi regolati dallo Stato e <b>uguali per tutti i fornitori</b>, indipendentemente da chi scegli. Conoscerli aiuta a comprendere la struttura trasparente e non comprimibile della bolletta.</p>
    </div>

    <div class="legend-box">
        <h3>6. Oneri Generali di Sistema</h3>
        <p><b>Definizione:</b> Corrispettivi destinati alla copertura di costi legati ad attività di interesse generale per il sistema energetico (es. incentivi alle fonti rinnovabili, agevolazioni ferroviarie, ecc.).</p>
        <p><b>Perché è utile prenderla in considerazione:</b> Come per il trasporto, sono costi fissati per legge e uguali per qualsiasi gestore tu decida di sottoscrivere.</p>
    </div>
    """, unsafe_allow_html=True)
