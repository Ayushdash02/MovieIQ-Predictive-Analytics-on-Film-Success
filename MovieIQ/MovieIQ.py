# ============================================================
# MovieIQ — Film Success Intelligence
# Professional Data Analyst / BI Analyst Portfolio Project
# VERSION 8.0 — HTML-SAFE / NATIVE STREAMLIT UI
# ============================================================

from pathlib import Path
import ast
import warnings

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

warnings.filterwarnings("ignore")

# ============================================================
# OPTIONAL LIBRARIES
# ============================================================

try:
    from scipy.stats import ttest_ind, chi2_contingency, pearsonr
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

try:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import (
        accuracy_score,
        precision_score,
        recall_score,
        f1_score,
        roc_auc_score,
        confusion_matrix,
        classification_report,
        roc_curve,
    )
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


# ============================================================
# 1. CONFIGURATION
# ============================================================

APP_NAME = "MovieIQ"
APP_SUBTITLE = "Film Success Intelligence"
APP_VERSION = "8.0"

BASE_DIR = Path(__file__).resolve().parent
ROOT_DATA_FILE = BASE_DIR / "movies.csv"
DATA_FILE = BASE_DIR / "data" / "movies.csv"

ASSETS_DIR = BASE_DIR / "assets"
LOGO_FILE = ASSETS_DIR / "movieiq_logo.png"
FAVICON_FILE = ASSETS_DIR / "favicon.png"

st.set_page_config(
    page_title="MovieIQ — Film Success Intelligence",
    page_icon=str(FAVICON_FILE) if FAVICON_FILE.exists() else "🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# 2. NATIVE STREAMLIT PROFESSIONAL THEME
# ============================================================
# IMPORTANT:
# This CSS is only styling. No HTML fragments are rendered into
# the dashboard. All visible UI is native Streamlit.
# ============================================================

st.markdown(
    """
    <style>
    :root {
        --bg: #070A0F;
        --panel: #0D141E;
        --panel2: #101923;
        --border: #223044;
        --text: #F8FAFC;
        --muted: #94A3B8;
        --soft: #64748B;
        --accent: #E50914;
        --success: #22C55E;
        --warning: #F59E0B;
    }

    .stApp {
        background:
            radial-gradient(circle at 85% -10%, rgba(229,9,20,.10), transparent 25%),
            radial-gradient(circle at 0% 20%, rgba(56,189,248,.04), transparent 22%),
            var(--bg);
        color: var(--text);
    }

    .main .block-container {
        max-width: 1500px;
        padding: 1.4rem 2.1rem 3.5rem;
    }

    section[data-testid="stSidebar"] {
        background: #0A0F16;
        border-right: 1px solid #1D2938;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }

    section[data-testid="stSidebar"] .stRadio label {
        border-radius: 10px;
        padding: .45rem .55rem;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        background: #111A25;
    }

    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #101923, #0B1119);
        border: 1px solid #26364A;
        border-radius: 14px;
        padding: 14px 15px;
        box-shadow: 0 10px 28px rgba(0,0,0,.14);
    }

    div[data-testid="stMetricLabel"] {
        color: #8291A5 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-weight: 850 !important;
    }

    .stTextInput input,
    .stNumberInput input,
    .stDateInput input {
        background: #0E151F !important;
        border-color: #27364A !important;
    }

    div[data-baseweb="select"] > div {
        background: #0E151F !important;
        border-color: #27364A !important;
    }

    .stButton > button,
    .stDownloadButton > button {
        border-radius: 10px;
        border: 1px solid #2A3A50;
        background: #111A25;
        color: #F8FAFC;
        font-weight: 750;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        border-color: rgba(229,9,20,.65);
        background: rgba(229,9,20,.10);
    }

    div[data-testid="stExpander"] {
        background: #0B1119;
        border: 1px solid #202E41;
        border-radius: 12px;
    }

    div[data-testid="stDataFrame"] {
        border: 1px solid #243246;
        border-radius: 12px;
        overflow: hidden;
    }

    h1, h2, h3 {
        letter-spacing: -.4px;
    }

    .mq-note {
        color: #94A3B8;
        font-size: 0.88rem;
        line-height: 1.65;
    }

    .mq-small {
        color: #64748B;
        font-size: 0.76rem;
    }

    .mq-divider {
        margin: 1.1rem 0 1.25rem;
        border-top: 1px solid #1F2C3E;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { background: transparent !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 3. HELPERS
# ============================================================

def money(value):
    if value is None or pd.isna(value):
        return "—"
    value = float(value)
    if abs(value) >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    if abs(value) >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    if abs(value) >= 1_000:
        return f"${value / 1_000:.1f}K"
    return f"${value:,.0f}"


def pct(value):
    if value is None or pd.isna(value):
        return "—"
    return f"{float(value) * 100:.1f}%"


def number(value):
    if value is None or pd.isna(value):
        return "—"
    return f"{float(value):,.0f}"


def safe_mean(series):
    if series is None:
        return np.nan
    s = pd.to_numeric(series, errors="coerce").dropna()
    return s.mean() if not s.empty else np.nan


def parse_genres(value):
    if value is None or pd.isna(value):
        return []

    if isinstance(value, list):
        raw = value
    else:
        try:
            raw = ast.literal_eval(str(value))
        except Exception:
            return []

    if not isinstance(raw, list):
        return []

    result = []
    for item in raw:
        if isinstance(item, dict) and item.get("name"):
            result.append(str(item["name"]))
        elif isinstance(item, str):
            result.append(item)

    return result


def page_header(title, subtitle=""):
    st.title(title)
    if subtitle:
        st.caption(subtitle)
    st.markdown('<div class="mq-divider"></div>', unsafe_allow_html=True)


def section(title, description=None):
    st.subheader(title)
    if description:
        st.caption(description)


def insight(title, text):
    with st.container(border=True):
        st.markdown(f"**{title}**")
        st.caption(text)


def style_chart(fig, height=None):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, Segoe UI, sans-serif",
            color="#DCE5EF",
            size=11,
        ),
        title=dict(
            font=dict(size=15, color="#F8FAFC"),
            x=0,
            xanchor="left",
        ),
        margin=dict(l=15, r=15, t=55, b=15),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=10, color="#A8B6C8"),
        ),
        hoverlabel=dict(
            bgcolor="#101722",
            bordercolor="#34465D",
            font=dict(color="#F8FAFC", size=11),
        ),
    )
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor="#26364A",
        tickfont=dict(color="#8291A5", size=10),
        title_font=dict(color="#9AA9BC", size=10),
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(93,111,135,.13)",
        zeroline=False,
        linecolor="#26364A",
        tickfont=dict(color="#8291A5", size=10),
        title_font=dict(color="#9AA9BC", size=10),
    )
    if height:
        fig.update_layout(height=height)
    return fig


# ============================================================
# 4. DATA LOADING
# ============================================================

@st.cache_data(show_spinner=False)
def load_data():
    candidates = [ROOT_DATA_FILE, DATA_FILE]

    for path in candidates:
        if path.exists():
            try:
                data = pd.read_csv(path)
                return data, path
            except Exception:
                continue

    return None, None


def prepare_data(data):
    df = data.copy()

    numeric_columns = [
        "budget",
        "revenue",
        "popularity",
        "runtime",
        "vote_average",
        "vote_count",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

    if "title" not in df.columns:
        df["title"] = "Untitled"

    # --------------------------------------------------------
    # Success definition: revenue > budget
    # --------------------------------------------------------

    if "budget" in df.columns and "revenue" in df.columns:
        valid_financial = (
            df["budget"].notna()
            & df["revenue"].notna()
            & (df["budget"] > 0)
        )

        df["success"] = np.where(
            valid_financial,
            (df["revenue"] > df["budget"]).astype(int),
            np.nan,
        )

        df["success_status"] = np.select(
            [
                df["success"].eq(1),
                df["success"].eq(0),
            ],
            [
                "Success",
                "Failure",
            ],
            default="Unknown",
        )

        df["profit"] = np.where(
            df["budget"].notna() & df["revenue"].notna(),
            df["revenue"] - df["budget"],
            np.nan,
        )

        df["roi"] = np.where(
            df["budget"].gt(0) & df["revenue"].notna(),
            (df["revenue"] - df["budget"]) / df["budget"],
            np.nan,
        )
    else:
        df["success"] = np.nan
        df["success_status"] = "Unknown"
        df["profit"] = np.nan
        df["roi"] = np.nan

    # --------------------------------------------------------
    # Genres
    # --------------------------------------------------------

    if "genres" in df.columns:
        df["genre_list"] = df["genres"].apply(parse_genres)
        df["genre_clean"] = df["genre_list"].apply(
            lambda x: ", ".join(x) if x else "Unknown"
        )
    elif "genre" in df.columns:
        df["genre_clean"] = (
            df["genre"]
            .fillna("Unknown")
            .astype(str)
        )
        df["genre_list"] = df["genre_clean"].apply(
            lambda x: [x] if x != "Unknown" else []
        )
    else:
        df["genre_clean"] = "Unknown"
        df["genre_list"] = [[] for _ in range(len(df))]

    df["primary_genre"] = (
        df["genre_clean"]
        .astype(str)
        .str.split(",")
        .str[0]
        .str.strip()
        .replace("", "Unknown")
        .fillna("Unknown")
    )

    # --------------------------------------------------------
    # Release year
    # --------------------------------------------------------

    if "release_date" in df.columns:
        release_dates = pd.to_datetime(
            df["release_date"],
            errors="coerce",
        )
        df["release_year"] = release_dates.dt.year
    elif "release_year" not in df.columns:
        df["release_year"] = np.nan

    # --------------------------------------------------------
    # Segments
    # --------------------------------------------------------

    if "budget" in df.columns:
        df["budget_segment"] = pd.cut(
            df["budget"],
            bins=[
                -np.inf,
                1_000_000,
                10_000_000,
                50_000_000,
                100_000_000,
                np.inf,
            ],
            labels=[
                "Micro",
                "Low",
                "Mid",
                "High",
                "Blockbuster",
            ],
        )

    if "vote_average" in df.columns:
        df["rating_segment"] = pd.cut(
            df["vote_average"],
            bins=[
                -np.inf,
                5,
                6,
                7,
                8,
                np.inf,
            ],
            labels=[
                "Very Low",
                "Low",
                "Average",
                "Good",
                "Excellent",
            ],
        )

    if "popularity" in df.columns:
        try:
            df["popularity_segment"] = pd.qcut(
                df["popularity"],
                q=4,
                labels=[
                    "Low",
                    "Medium",
                    "High",
                    "Very High",
                ],
                duplicates="drop",
            )
        except Exception:
            df["popularity_segment"] = "Unknown"

    if "revenue" in df.columns:
        try:
            df["revenue_segment"] = pd.qcut(
                df["revenue"],
                q=4,
                labels=[
                    "Low",
                    "Medium",
                    "High",
                    "Very High",
                ],
                duplicates="drop",
            )
        except Exception:
            df["revenue_segment"] = "Unknown"

    return df


raw_df, dataset_path = load_data()

if raw_df is None:
    st.error("Movie dataset not found.")
    st.info(
        "Place movies.csv in the MovieIQ root folder "
        "or inside the data folder."
    )
    st.stop()

df = prepare_data(raw_df)


def valid_financial_data(data):
    required = ["budget", "revenue"]

    if not all(c in data.columns for c in required):
        return pd.DataFrame()

    result = data.dropna(
        subset=required
    ).copy()

    return result[
        (result["budget"] > 0)
        & (result["revenue"] > 0)
    ]


financial = valid_financial_data(df)


# ============================================================
# 5. RANDOM FOREST MODEL
# ============================================================

@st.cache_resource(show_spinner="Training Random Forest model...")
def train_success_model(data):
    if not SKLEARN_AVAILABLE:
        return None

    required = [
        "success",
        "budget",
        "popularity",
        "runtime",
        "vote_average",
        "primary_genre",
    ]

    if not all(c in data.columns for c in required):
        return None

    model_df = data[required].copy()

    model_df = model_df.dropna(
        subset=[
            "success",
            "budget",
            "popularity",
            "runtime",
            "vote_average",
        ]
    )

    model_df = model_df[
        model_df["success"].isin([0, 1])
    ]

    if len(model_df) < 50:
        return None

    if model_df["success"].nunique() < 2:
        return None

    model_df["primary_genre"] = (
        model_df["primary_genre"]
        .fillna("Unknown")
        .astype(str)
    )

    X = pd.get_dummies(
        model_df[
            [
                "budget",
                "popularity",
                "runtime",
                "vote_average",
                "primary_genre",
            ]
        ],
        columns=["primary_genre"],
        dtype=float,
    )

    y = model_df["success"].astype(int)

    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.25,
            random_state=42,
            stratify=y,
        )
    except Exception:
        return None

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    try:
        roc_auc = roc_auc_score(
            y_test,
            probabilities,
        )
    except Exception:
        roc_auc = np.nan

    try:
        fpr, tpr, thresholds = roc_curve(
            y_test,
            probabilities,
        )
    except Exception:
        fpr = np.array([])
        tpr = np.array([])
        thresholds = np.array([])

    cm = confusion_matrix(
        y_test,
        predictions,
    )

    report = classification_report(
        y_test,
        predictions,
        target_names=["Failure", "Success"],
        output_dict=True,
        zero_division=0,
    )

    feature_importance = pd.DataFrame(
        {
            "Feature": X.columns,
            "Importance": model.feature_importances_,
        }
    ).sort_values(
        "Importance",
        ascending=False,
    )

    return {
        "model": model,
        "features": X.columns.tolist(),
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "recall": recall_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "f1": f1_score(
            y_test,
            predictions,
            zero_division=0,
        ),
        "roc_auc": roc_auc,
        "confusion_matrix": cm,
        "report": report,
        "fpr": fpr,
        "tpr": tpr,
        "thresholds": thresholds,
        "X_test": X_test,
        "y_test": y_test,
        "predictions": predictions,
        "probabilities": probabilities,
        "feature_importance": feature_importance,
        "training_rows": len(X_train),
        "test_rows": len(X_test),
    }


model_results = train_success_model(df)


# ============================================================
# 6. SIDEBAR
# ============================================================

with st.sidebar:
    if LOGO_FILE.exists():
        st.image(
            str(LOGO_FILE),
            use_container_width=True,
        )
    else:
        st.title("🎬 MovieIQ")
        st.caption("Film Success Intelligence")

    st.divider()

    st.caption("NAVIGATION")

    pages = [
        "🏠 Executive Overview",
        "🎬 Movie Explorer",
        "💰 Financial Performance",
        "🎭 Genre Intelligence",
        "👥 Audience Intelligence",
        "📈 Success Drivers",
        "🧪 Statistical Testing",
        "🤖 Predictive Analytics",
        "🎯 Model Performance",
        "💡 Business Insights",
        "📋 Data Quality",
    ]

    page = st.radio(
        "Navigation",
        pages,
        label_visibility="collapsed",
    )

    st.divider()

    st.caption("DATASET")

    st.write(f"📁 {dataset_path.name}")
    st.write(f"🎬 {len(df):,} movies")
    st.write(f"📊 {df.shape[1]:,} fields")
    st.write(
        f"💰 {len(financial):,} valid financial records"
    )

    st.divider()

    st.caption("INTELLIGENCE")

    if model_results is not None:
        st.success("🤖 Random Forest ready")
    elif not SKLEARN_AVAILABLE:
        st.warning("Install scikit-learn")
    else:
        st.warning("Model unavailable")

    if not SCIPY_AVAILABLE:
        st.warning("Install scipy for statistical tests")

    st.divider()
    st.caption(f"MovieIQ • v{APP_VERSION}")


# ============================================================
# 7. EXECUTIVE OVERVIEW
# ============================================================

if page == "🏠 Executive Overview":

    page_header(
        "🎬 MovieIQ — Film Success Intelligence",
        "Executive business intelligence for financial performance, audience response, statistical evidence and predictive screening.",
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Total Movies",
        f"{len(df):,}",
        "Records analysed",
    )

    c2.metric(
        "Total Revenue",
        money(financial["revenue"].sum() if not financial.empty else 0),
        "Valid financial records",
    )

    c3.metric(
        "Average Budget",
        money(financial["budget"].mean() if not financial.empty else np.nan),
        "Production investment",
    )

    c4.metric(
        "Average Revenue",
        money(financial["revenue"].mean() if not financial.empty else np.nan),
        "Commercial return",
    )

    c5.metric(
        "Success Rate",
        pct(financial["success"].mean() if not financial.empty else np.nan),
        "Revenue > budget",
    )

    section(
        "Portfolio Financial Performance",
        "Historical relationship between production investment and commercial revenue.",
    )

    if not financial.empty:
        chart_df = financial.copy()

        if len(chart_df) > 1500:
            chart_df = chart_df.sample(
                1500,
                random_state=42,
            )

        fig = px.scatter(
            chart_df,
            x="budget",
            y="revenue",
            color="success_status",
            hover_name="title",
            hover_data=[
                "primary_genre",
                "popularity",
                "vote_average",
            ],
            log_x=True,
            log_y=True,
            title="Budget vs Revenue — Log Scale",
        )

        st.plotly_chart(
            style_chart(fig, 500),
            use_container_width=True,
        )

    if not financial.empty:
        left, right = st.columns(2)

        genre_stats = (
            df.groupby("primary_genre", as_index=False)
            .agg(
                Movies=("title", "size"),
                Avg_Revenue=("revenue", "mean"),
                Success_Rate=("success", "mean"),
            )
        )

        genre_stats = genre_stats[
            genre_stats["Movies"] >= 5
        ]

        with left:
            top_rev = genre_stats.nlargest(
                10,
                "Avg_Revenue",
            ).sort_values("Avg_Revenue")

            fig = px.bar(
                top_rev,
                x="Avg_Revenue",
                y="primary_genre",
                orientation="h",
                title="Top Genres by Average Revenue",
            )

            st.plotly_chart(
                style_chart(fig, 430),
                use_container_width=True,
            )

        with right:
            top_success = genre_stats.nlargest(
                10,
                "Success_Rate",
            ).sort_values("Success_Rate")

            fig = px.bar(
                top_success,
                x="Success_Rate",
                y="primary_genre",
                orientation="h",
                title="Top Genres by Success Rate",
            )

            fig.update_xaxes(tickformat=".0%")

            st.plotly_chart(
                style_chart(fig, 430),
                use_container_width=True,
            )

    section("Executive Signals")

    if not financial.empty:
        correlation = financial[
            ["budget", "revenue"]
        ].corr().iloc[0, 1]

        best_genre = (
            df.groupby("primary_genre")["success"]
            .mean()
            .dropna()
            .sort_values(ascending=False)
        )

        if not best_genre.empty:
            best_name = best_genre.index[0]
            best_rate = best_genre.iloc[0]

            insight(
                "💡 Budget / Revenue",
                f"Budget and revenue show a correlation of {correlation:.2f} in the valid financial sample.",
            )

            insight(
                "🎭 Genre Signal",
                f"{best_name} has the highest observed success rate in the current dataset at {pct(best_rate)}.",
            )

    insight(
        "⚠️ Interpretation",
        "MovieIQ defines success as revenue greater than budget. This is a historical analytical definition, not a complete accounting-profit measure.",
    )


# ============================================================
# 8. MOVIE EXPLORER — NO RAW HTML
# ============================================================

elif page == "🎬 Movie Explorer":

    page_header(
        "🎬 Movie Explorer",
        "Search, segment and benchmark movies using business-friendly filters.",
    )

    explorer = df.copy()

    with st.container(border=True):
        st.markdown("### 🔎 Search & Catalogue Controls")

        search = st.text_input(
            "Search movie title",
            placeholder="Type a movie title...",
            key="explorer_search_v8",
        )

        f1, f2, f3, f4 = st.columns(4)

        with f1:
            genre_options = sorted(
                explorer["primary_genre"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            selected_genres = st.multiselect(
                "🎭 Genre",
                genre_options,
                placeholder="All genres",
                key="explorer_genres_v8",
            )

        with f2:
            status_filter = st.selectbox(
                "🎯 Success Status",
                [
                    "All",
                    "Success",
                    "Failure",
                    "Unknown",
                ],
                key="explorer_status_v8",
            )

        with f3:
            sort_option = st.selectbox(
                "↕ Sort By",
                [
                    "Revenue",
                    "Profit",
                    "ROI",
                    "Rating",
                    "Popularity",
                    "Budget",
                ],
                key="explorer_sort_v8",
            )

        with f4:
            display_limit = st.selectbox(
                "📋 Show",
                [25, 50, 100, 250, 500],
                index=1,
                key="explorer_limit_v8",
            )

        with st.expander(
            "⚙️ Advanced Filters",
            expanded=False,
        ):
            a1, a2, a3 = st.columns(3)

            with a1:
                rating_range = st.slider(
                    "⭐ Rating Range",
                    0.0,
                    10.0,
                    (0.0, 10.0),
                    0.1,
                    key="explorer_rating_v8",
                )

            with a2:
                max_popularity = (
                    float(
                        explorer["popularity"]
                        .dropna()
                        .max()
                    )
                    if "popularity" in explorer.columns
                    and explorer["popularity"].notna().any()
                    else 100.0
                )

                popularity_min = st.number_input(
                    "🔥 Minimum Popularity",
                    min_value=0.0,
                    max_value=max_popularity,
                    value=0.0,
                    step=max(
                        max_popularity / 100,
                        0.1,
                    ),
                    key="explorer_pop_v8",
                )

            with a3:
                if (
                    "release_year" in explorer.columns
                    and explorer["release_year"].notna().any()
                ):
                    min_year = int(
                        explorer["release_year"]
                        .dropna()
                        .min()
                    )
                    max_year = int(
                        explorer["release_year"]
                        .dropna()
                        .max()
                    )

                    year_range = st.slider(
                        "📅 Release Year",
                        min_year,
                        max_year,
                        (min_year, max_year),
                        key="explorer_year_v8",
                    )
                else:
                    year_range = None
                    st.caption(
                        "Release year is unavailable in this dataset."
                    )

    # --------------------------------------------------------
    # Apply filters
    # --------------------------------------------------------

    if search.strip():
        explorer = explorer[
            explorer["title"]
            .astype(str)
            .str.contains(
                search.strip(),
                case=False,
                na=False,
            )
        ]

    if selected_genres:
        explorer = explorer[
            explorer["primary_genre"]
            .isin(selected_genres)
        ]

    if status_filter != "All":
        explorer = explorer[
            explorer["success_status"]
            == status_filter
        ]

    if "vote_average" in explorer.columns:
        explorer = explorer[
            explorer["vote_average"]
            .fillna(-1)
            .between(
                rating_range[0],
                rating_range[1],
            )
        ]

    if "popularity" in explorer.columns:
        explorer = explorer[
            explorer["popularity"]
            .fillna(-1)
            >= popularity_min
        ]

    if (
        year_range is not None
        and "release_year" in explorer.columns
    ):
        explorer = explorer[
            explorer["release_year"]
            .fillna(-1)
            .between(
                year_range[0],
                year_range[1],
            )
        ]

    sort_map = {
        "Revenue": "revenue",
        "Profit": "profit",
        "ROI": "roi",
        "Rating": "vote_average",
        "Popularity": "popularity",
        "Budget": "budget",
    }

    sort_column = sort_map[sort_option]

    if sort_column in explorer.columns:
        explorer = explorer.sort_values(
            sort_column,
            ascending=False,
            na_position="last",
        )

    result_count = len(explorer)

    # --------------------------------------------------------
    # Result summary
    # --------------------------------------------------------

    st.markdown("### 📊 Filtered Universe")

    k1, k2, k3, k4 = st.columns(4)

    k1.metric(
        "Movies Found",
        f"{result_count:,}",
    )

    k2.metric(
        "Avg Revenue",
        money(
            explorer["revenue"].mean()
            if "revenue" in explorer.columns
            else np.nan
        ),
    )

    k3.metric(
        "Avg Rating",
        (
            f"{explorer['vote_average'].mean():.2f}/10"
            if "vote_average" in explorer.columns
            and explorer["vote_average"].notna().any()
            else "—"
        ),
    )

    k4.metric(
        "Success Rate",
        pct(
            explorer["success"].mean()
            if "success" in explorer.columns
            else np.nan
        ),
    )

    if explorer.empty:
        st.warning(
            "No movies match the current filters. "
            "Try clearing one or more filters."
        )
    else:
        # ----------------------------------------------------
        # Catalogue
        # ----------------------------------------------------

        st.markdown("### 🎞️ Movie Catalogue")

        display_df = explorer.head(
            display_limit
        ).copy()

        columns = [
            "title",
            "primary_genre",
            "release_year",
            "budget",
            "revenue",
            "profit",
            "roi",
            "popularity",
            "vote_average",
            "runtime",
            "success_status",
        ]

        columns = [
            c for c in columns
            if c in display_df.columns
        ]

        display_df = display_df[columns].copy()

        rename_map = {
            "title": "Movie",
            "primary_genre": "Genre",
            "release_year": "Year",
            "budget": "Budget",
            "revenue": "Revenue",
            "profit": "Profit",
            "roi": "ROI",
            "popularity": "Popularity",
            "vote_average": "Rating",
            "runtime": "Runtime",
            "success_status": "Status",
        }

        display_df = display_df.rename(
            columns=rename_map
        )

        for col in [
            "Budget",
            "Revenue",
            "Profit",
        ]:
            if col in display_df.columns:
                display_df[col] = display_df[col].apply(money)

        if "ROI" in display_df.columns:
            display_df["ROI"] = display_df["ROI"].apply(pct)

        if "Rating" in display_df.columns:
            display_df["Rating"] = display_df["Rating"].apply(
                lambda x: (
                    f"{float(x):.1f}/10"
                    if pd.notna(x)
                    else "—"
                )
            )

        if "Runtime" in display_df.columns:
            display_df["Runtime"] = display_df["Runtime"].apply(
                lambda x: (
                    f"{float(x):.0f} min"
                    if pd.notna(x)
                    else "—"
                )
            )

        if "Year" in display_df.columns:
            display_df["Year"] = display_df["Year"].apply(
                lambda x: (
                    str(int(x))
                    if pd.notna(x)
                    else "—"
                )
            )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            height=540,
        )

        # ----------------------------------------------------
        # Selected movie profile
        # ----------------------------------------------------

        st.markdown("### 🎯 Selected Movie Profile")

        title_options = (
            explorer["title"]
            .fillna("Untitled")
            .astype(str)
            .drop_duplicates()
            .tolist()
        )

        selected_title = st.selectbox(
            "Select a movie",
            title_options,
            key="selected_movie_v8",
        )

        selected_rows = explorer[
            explorer["title"].astype(str)
            == selected_title
        ]

        if not selected_rows.empty:
            movie = selected_rows.iloc[0]

            p1, p2, p3, p4, p5 = st.columns(5)

            p1.metric(
                "Revenue",
                money(movie.get("revenue")),
            )

            p2.metric(
                "Budget",
                money(movie.get("budget")),
            )

            p3.metric(
                "Profit",
                money(movie.get("profit")),
            )

            p4.metric(
                "ROI",
                pct(movie.get("roi")),
            )

            p5.metric(
                "Outcome",
                str(
                    movie.get(
                        "success_status",
                        "Unknown",
                    )
                ),
            )

            left, right = st.columns(
                [1.1, 1],
                gap="large",
            )

            with left:
                st.markdown(
                    f"**{selected_title}**"
                )

                st.write(
                    f"**Genre:** {movie.get('primary_genre', 'Unknown')}"
                )

                if pd.notna(movie.get("release_year")):
                    st.write(
                        f"**Release Year:** {int(movie['release_year'])}"
                    )

                if pd.notna(movie.get("vote_average")):
                    st.write(
                        f"**Rating:** {movie['vote_average']:.1f}/10"
                    )

                if pd.notna(movie.get("popularity")):
                    st.write(
                        f"**Popularity:** {movie['popularity']:.1f}"
                    )

                if pd.notna(movie.get("runtime")):
                    st.write(
                        f"**Runtime:** {movie['runtime']:.0f} minutes"
                    )

                st.info(
                    "MovieIQ success is defined as revenue greater than budget. "
                    "Use this profile for historical benchmarking, not guaranteed forecasting."
                )

            with right:
                profile_data = pd.DataFrame(
                    {
                        "Metric": [
                            "Budget",
                            "Revenue",
                            "Profit",
                        ],
                        "Value": [
                            max(
                                float(movie.get("budget", 0) or 0),
                                0,
                            ),
                            max(
                                float(movie.get("revenue", 0) or 0),
                                0,
                            ),
                            max(
                                float(movie.get("profit", 0) or 0),
                                0,
                            ),
                        ],
                    }
                )

                fig = px.bar(
                    profile_data,
                    x="Metric",
                    y="Value",
                    title="Financial Profile",
                    text="Value",
                )

                fig.update_traces(
                    texttemplate="$%{y:,.0f}",
                    textposition="outside",
                )

                st.plotly_chart(
                    style_chart(fig, 320),
                    use_container_width=True,
                )


# ============================================================
# 9. FINANCIAL PERFORMANCE
# ============================================================

elif page == "💰 Financial Performance":

    page_header(
        "💰 Financial Performance",
        "Analyse budget, revenue, profit and ROI across the movie portfolio.",
    )

    if financial.empty:
        st.warning("Valid budget/revenue records are unavailable.")
    else:
        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Total Revenue",
            money(financial["revenue"].sum()),
        )

        c2.metric(
            "Total Budget",
            money(financial["budget"].sum()),
        )

        c3.metric(
            "Total Profit",
            money(financial["profit"].sum()),
        )

        c4.metric(
            "Average ROI",
            pct(financial["roi"].mean()),
        )

        section(
            "Budget vs Revenue",
            "Log scale makes low- and high-budget movies easier to compare.",
        )

        sample = financial
        if len(sample) > 2000:
            sample = sample.sample(
                2000,
                random_state=42,
            )

        fig = px.scatter(
            sample,
            x="budget",
            y="revenue",
            color="success_status",
            hover_name="title",
            log_x=True,
            log_y=True,
            title="Budget vs Revenue",
        )

        st.plotly_chart(
            style_chart(fig, 520),
            use_container_width=True,
        )

        left, right = st.columns(2)

        with left:
            roi_data = financial[
                financial["roi"].notna()
            ].copy()

            if not roi_data.empty:
                fig = px.histogram(
                    roi_data,
                    x="roi",
                    nbins=40,
                    title="ROI Distribution",
                )

                fig.update_xaxes(tickformat=".0%")

                st.plotly_chart(
                    style_chart(fig, 400),
                    use_container_width=True,
                )

        with right:
            status_fin = (
                financial.groupby(
                    "success_status",
                    as_index=False,
                )
                .agg(
                    Movies=("title", "size"),
                    Avg_Revenue=("revenue", "mean"),
                )
            )

            fig = px.bar(
                status_fin,
                x="success_status",
                y="Avg_Revenue",
                title="Average Revenue by Outcome",
            )

            st.plotly_chart(
                style_chart(fig, 400),
                use_container_width=True,
            )


# ============================================================
# 10. GENRE INTELLIGENCE
# ============================================================

elif page == "🎭 Genre Intelligence":

    page_header(
        "🎭 Genre Intelligence",
        "Compare genre scale, revenue and observed success performance.",
    )

    genre_stats = (
        df.groupby("primary_genre", as_index=False)
        .agg(
            Movies=("title", "size"),
            Avg_Revenue=("revenue", "mean"),
            Avg_Budget=("budget", "mean"),
            Avg_ROI=("roi", "mean"),
            Success_Rate=("success", "mean"),
        )
    )

    genre_stats = genre_stats[
        genre_stats["Movies"] >= 5
    ].copy()

    if genre_stats.empty:
        st.warning("Not enough genre observations.")
    else:
        c1, c2 = st.columns(2)

        with c1:
            top = genre_stats.nlargest(
                12,
                "Avg_Revenue",
            ).sort_values("Avg_Revenue")

            fig = px.bar(
                top,
                x="Avg_Revenue",
                y="primary_genre",
                orientation="h",
                title="Genres by Average Revenue",
            )

            st.plotly_chart(
                style_chart(fig, 500),
                use_container_width=True,
            )

        with c2:
            top = genre_stats.nlargest(
                12,
                "Success_Rate",
            ).sort_values("Success_Rate")

            fig = px.bar(
                top,
                x="Success_Rate",
                y="primary_genre",
                orientation="h",
                title="Genres by Success Rate",
            )

            fig.update_xaxes(tickformat=".0%")

            st.plotly_chart(
                style_chart(fig, 500),
                use_container_width=True,
            )

        section("Genre Performance Table")

        table = genre_stats.sort_values(
            "Success_Rate",
            ascending=False,
        ).copy()

        table["Avg Revenue"] = table[
            "Avg_Revenue"
        ].apply(money)

        table["Avg Budget"] = table[
            "Avg_Budget"
        ].apply(money)

        table["Avg ROI"] = table[
            "Avg_ROI"
        ].apply(pct)

        table["Success Rate"] = table[
            "Success_Rate"
        ].apply(pct)

        table = table[
            [
                "primary_genre",
                "Movies",
                "Avg Revenue",
                "Avg Budget",
                "Avg ROI",
                "Success Rate",
            ]
        ].rename(
            columns={
                "primary_genre": "Genre",
            }
        )

        st.dataframe(
            table,
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# 11. AUDIENCE INTELLIGENCE
# ============================================================

elif page == "👥 Audience Intelligence":

    page_header(
        "👥 Audience Intelligence",
        "Understand how popularity, ratings and audience engagement relate to financial outcomes.",
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Average Rating",
        f"{safe_mean(df['vote_average']):.2f}/10"
        if "vote_average" in df.columns
        else "—",
    )

    c2.metric(
        "Average Popularity",
        f"{safe_mean(df['popularity']):.1f}"
        if "popularity" in df.columns
        else "—",
    )

    c3.metric(
        "Average Vote Count",
        number(safe_mean(df["vote_count"]))
        if "vote_count" in df.columns
        else "—",
    )

    left, right = st.columns(2)

    with left:
        if {
            "vote_average",
            "revenue",
        }.issubset(df.columns):
            chart_df = df[
                ["vote_average", "revenue", "title"]
            ].dropna()

            fig = px.scatter(
                chart_df,
                x="vote_average",
                y="revenue",
                hover_name="title",
                title="Rating vs Revenue",
            )

            st.plotly_chart(
                style_chart(fig, 450),
                use_container_width=True,
            )

    with right:
        if {
            "popularity",
            "revenue",
        }.issubset(df.columns):
            chart_df = df[
                ["popularity", "revenue", "title"]
            ].dropna()

            if len(chart_df) > 2000:
                chart_df = chart_df.sample(
                    2000,
                    random_state=42,
                )

            fig = px.scatter(
                chart_df,
                x="popularity",
                y="revenue",
                hover_name="title",
                log_y=True,
                title="Popularity vs Revenue",
            )

            st.plotly_chart(
                style_chart(fig, 450),
                use_container_width=True,
            )

    section("Audience Signals by Outcome")

    if {
        "success_status",
        "popularity",
        "vote_average",
    }.issubset(df.columns):
        audience = (
            df.groupby(
                "success_status",
                as_index=False,
            )
            .agg(
                Avg_Popularity=("popularity", "mean"),
                Avg_Rating=("vote_average", "mean"),
            )
        )

        st.dataframe(
            audience.round(2),
            use_container_width=True,
            hide_index=True,
        )


# ============================================================
# 12. SUCCESS DRIVERS
# ============================================================

elif page == "📈 Success Drivers":

    page_header(
        "📈 Success Drivers",
        "Explore observable relationships between movie characteristics and financial success.",
    )

    numeric_cols = [
        c for c in [
            "budget",
            "revenue",
            "profit",
            "roi",
            "popularity",
            "runtime",
            "vote_average",
            "vote_count",
            "success",
        ]
        if c in df.columns
    ]

    if len(numeric_cols) >= 2:
        corr = df[numeric_cols].corr()

        fig = px.imshow(
            corr,
            text_auto=".2f",
            aspect="auto",
            title="Correlation Matrix",
        )

        st.plotly_chart(
            style_chart(fig, 650),
            use_container_width=True,
        )

    section(
        "Success Group Comparison",
        "Compare central tendencies between successful and unsuccessful movies.",
    )

    compare_cols = [
        c for c in [
            "budget",
            "revenue",
            "popularity",
            "runtime",
            "vote_average",
        ]
        if c in df.columns
    ]

    if compare_cols:
        comparison = (
            df.groupby("success_status")[compare_cols]
            .mean()
            .T
        )

        st.dataframe(
            comparison.round(2),
            use_container_width=True,
        )

    if SCIPY_AVAILABLE:
        st.info(
            "Statistical significance testing is available on the Statistical Testing page."
        )


# ============================================================
# 13. STATISTICAL TESTING
# ============================================================

elif page == "🧪 Statistical Testing":

    page_header(
        "🧪 Statistical Testing",
        "Evaluate whether observed differences are statistically distinguishable under the selected tests.",
    )

    if not SCIPY_AVAILABLE:
        st.error(
            "SciPy is not installed. Run: pip install scipy"
        )
    else:
        section(
            "Independent T-Test — Popularity",
            "H0: mean popularity is equal between successful and unsuccessful movies.",
        )

        success_pop = df.loc[
            df["success"] == 1,
            "popularity",
        ].dropna()

        failure_pop = df.loc[
            df["success"] == 0,
            "popularity",
        ].dropna()

        if len(success_pop) >= 2 and len(failure_pop) >= 2:
            t_stat, p_value = ttest_ind(
                success_pop,
                failure_pop,
                equal_var=False,
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "T-Statistic",
                f"{t_stat:.3f}",
            )

            c2.metric(
                "P-Value",
                f"{p_value:.5f}",
            )

            c3.metric(
                "Decision",
                (
                    "Significant"
                    if p_value < 0.05
                    else "Not Significant"
                ),
            )

            if p_value < 0.05:
                st.success(
                    "The popularity difference is statistically significant at the 5% level."
                )
            else:
                st.info(
                    "The popularity difference is not statistically significant at the 5% level."
                )

        section(
            "Chi-Square Test — Genre vs Success",
            "H0: genre and financial success are independent.",
        )

        contingency = pd.crosstab(
            df["primary_genre"],
            df["success_status"],
        )

        if (
            contingency.shape[0] >= 2
            and contingency.shape[1] >= 2
        ):
            chi2, p, dof, expected = chi2_contingency(
                contingency
            )

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Chi-Square",
                f"{chi2:.3f}",
            )

            c2.metric(
                "P-Value",
                f"{p:.5f}",
            )

            c3.metric(
                "Degrees of Freedom",
                f"{dof}",
            )

            if p < 0.05:
                st.success(
                    "Genre and success show a statistically significant association at the 5% level."
                )
            else:
                st.info(
                    "Genre and success do not show a statistically significant association at the 5% level."
                )

        section(
            "Pearson Correlation — Budget vs Revenue",
        )

        valid_corr = df[
            ["budget", "revenue"]
        ].dropna()

        valid_corr = valid_corr[
            (valid_corr["budget"] > 0)
            & (valid_corr["revenue"] > 0)
        ]

        if len(valid_corr) >= 3:
            r, p = pearsonr(
                valid_corr["budget"],
                valid_corr["revenue"],
            )

            c1, c2 = st.columns(2)

            c1.metric(
                "Pearson r",
                f"{r:.3f}",
            )

            c2.metric(
                "P-Value",
                f"{p:.5f}",
            )


# ============================================================
# 14. PREDICTIVE ANALYTICS
# ============================================================

elif page == "🤖 Predictive Analytics":

    page_header(
        "🤖 Predictive Analytics",
        "Use the Random Forest classifier as a historical decision-support screening tool.",
    )

    if model_results is None:
        st.error(
            "The predictive model is unavailable. "
            "Check scikit-learn and dataset completeness."
        )
    else:
        st.info(
            "Target definition: revenue > budget. "
            "Prediction probabilities are historical model outputs and are not guaranteed box-office forecasts."
        )

        section(
            "Movie Scenario",
            "Adjust assumptions for a hypothetical movie project.",
        )

        c1, c2, c3 = st.columns(3)

        median_budget = (
            safe_mean(df["budget"])
            if "budget" in df.columns
            else 10_000_000
        )

        if not pd.notna(median_budget):
            median_budget = 10_000_000

        with c1:
            budget_input = st.number_input(
                "💰 Production Budget ($)",
                min_value=0.0,
                value=float(median_budget),
                step=1_000_000.0,
            )

        median_popularity = (
            safe_mean(df["popularity"])
            if "popularity" in df.columns
            else 20.0
        )

        if not pd.notna(median_popularity):
            median_popularity = 20.0

        with c2:
            popularity_input = st.number_input(
                "🔥 Popularity",
                min_value=0.0,
                value=float(median_popularity),
                step=1.0,
            )

        median_runtime = (
            safe_mean(df["runtime"])
            if "runtime" in df.columns
            else 110.0
        )

        if not pd.notna(median_runtime):
            median_runtime = 110.0

        with c3:
            runtime_input = st.number_input(
                "⏱️ Runtime (minutes)",
                min_value=1.0,
                value=float(median_runtime),
                step=5.0,
            )

        c4, c5 = st.columns(2)

        median_rating = (
            safe_mean(df["vote_average"])
            if "vote_average" in df.columns
            else 6.5
        )

        if not pd.notna(median_rating):
            median_rating = 6.5

        with c4:
            rating_input = st.slider(
                "⭐ Expected Rating",
                0.0,
                10.0,
                float(
                    np.clip(
                        median_rating,
                        0.0,
                        10.0,
                    )
                ),
                0.1,
            )

        genre_options = sorted(
            df["primary_genre"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if not genre_options:
            genre_options = ["Unknown"]

        with c5:
            genre_input = st.selectbox(
                "🎭 Primary Genre",
                genre_options,
            )

        input_df = pd.DataFrame(
            {
                "budget": [budget_input],
                "popularity": [popularity_input],
                "runtime": [runtime_input],
                "vote_average": [rating_input],
                "primary_genre": [genre_input],
            }
        )

        encoded = pd.get_dummies(
            input_df,
            columns=["primary_genre"],
            dtype=float,
        )

        encoded = encoded.reindex(
            columns=model_results["features"],
            fill_value=0,
        )

        probability = float(
            model_results["model"]
            .predict_proba(encoded)[0, 1]
        )

        prediction = int(
            model_results["model"]
            .predict(encoded)[0]
        )

        st.markdown("### 🎯 Screening Result")

        r1, r2, r3 = st.columns(3)

        r1.metric(
            "Predicted Outcome",
            "SUCCESS" if prediction == 1 else "FAILURE",
        )

        r2.metric(
            "Success Probability",
            pct(probability),
        )

        r3.metric(
            "Model",
            "Random Forest",
        )

        if probability >= 0.70:
            st.success(
                "High historical model probability. Use as a screening signal, not a guarantee."
            )
        elif probability >= 0.50:
            st.warning(
                "Moderate historical model probability. Additional commercial due diligence is recommended."
            )
        else:
            st.error(
                "Low historical model probability. Treat this scenario cautiously."
            )


# ============================================================
# 15. MODEL PERFORMANCE
# ============================================================

elif page == "🎯 Model Performance":

    page_header(
        "🎯 Model Performance",
        "Evaluate Random Forest classification performance on the held-out test sample.",
    )

    if model_results is None:
        st.error("Model evaluation unavailable.")
    else:
        c1, c2, c3, c4, c5 = st.columns(5)

        c1.metric(
            "Accuracy",
            pct(model_results["accuracy"]),
        )

        c2.metric(
            "Precision",
            pct(model_results["precision"]),
        )

        c3.metric(
            "Recall",
            pct(model_results["recall"]),
        )

        c4.metric(
            "F1 Score",
            pct(model_results["f1"]),
        )

        c5.metric(
            "ROC-AUC",
            (
                f"{model_results['roc_auc']:.3f}"
                if pd.notna(model_results["roc_auc"])
                else "—"
            ),
        )

        left, right = st.columns(2)

        with left:
            cm = pd.DataFrame(
                model_results["confusion_matrix"],
                index=[
                    "Actual Failure",
                    "Actual Success",
                ],
                columns=[
                    "Predicted Failure",
                    "Predicted Success",
                ],
            )

            fig = px.imshow(
                cm,
                text_auto=True,
                aspect="auto",
                title="Confusion Matrix",
            )

            st.plotly_chart(
                style_chart(fig, 430),
                use_container_width=True,
            )

        with right:
            report_df = (
                pd.DataFrame(
                    model_results["report"]
                )
                .T
                .reset_index()
                .rename(
                    columns={
                        "index": "Class"
                    }
                )
            )

            report_df = report_df[
                report_df["Class"].isin(
                    [
                        "Failure",
                        "Success",
                    ]
                )
            ]

            metrics_long = report_df.melt(
                id_vars="Class",
                value_vars=[
                    "precision",
                    "recall",
                    "f1-score",
                ],
                var_name="Metric",
                value_name="Score",
            )

            fig = px.bar(
                metrics_long,
                x="Class",
                y="Score",
                color="Metric",
                barmode="group",
                title="Classification Metrics",
            )

            fig.update_yaxes(
                range=[0, 1]
            )

            st.plotly_chart(
                style_chart(fig, 430),
                use_container_width=True,
            )

        if len(model_results["fpr"]) > 0:
            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=model_results["fpr"],
                    y=model_results["tpr"],
                    mode="lines",
                    name=(
                        "Random Forest"
                        f" (AUC={model_results['roc_auc']:.3f})"
                    ),
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=[0, 1],
                    y=[0, 1],
                    mode="lines",
                    name="Random baseline",
                    line=dict(dash="dash"),
                )
            )

            fig.update_layout(
                title="ROC Curve",
                xaxis_title="False Positive Rate",
                yaxis_title="True Positive Rate",
            )

            st.plotly_chart(
                style_chart(fig, 450),
                use_container_width=True,
            )

        section(
            "Feature Importance",
            "Relative importance within the fitted Random Forest model.",
        )

        importance = model_results[
            "feature_importance"
        ].head(15).sort_values(
            "Importance",
            ascending=True,
        )

        fig = px.bar(
            importance,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top Model Features",
        )

        st.plotly_chart(
            style_chart(fig, 500),
            use_container_width=True,
        )

        section("Classification Report")

        st.dataframe(
            pd.DataFrame(
                model_results["report"]
            ).T.round(3),
            use_container_width=True,
        )

        insight(
            "🤖 Model Governance",
            "The classifier is an exploratory screening model. It does not include marketing spend, release timing, cast, director, distributor, competition or other external commercial variables.",
        )


# ============================================================
# 16. BUSINESS INSIGHTS
# ============================================================

elif page == "💡 Business Insights":

    page_header(
        "💡 Business Insights",
        "Translate MovieIQ analysis into decision-support recommendations.",
    )

    genre_stats = (
        df.groupby("primary_genre", as_index=False)
        .agg(
            Movies=("title", "size"),
            Success_Rate=("success", "mean"),
            Avg_Revenue=("revenue", "mean"),
            Avg_Budget=("budget", "mean"),
            Avg_ROI=("roi", "mean"),
        )
    )

    genre_stats = genre_stats[
        genre_stats["Movies"] >= 5
    ]

    if not genre_stats.empty:
        best_success = genre_stats.loc[
            genre_stats["Success_Rate"].idxmax()
        ]

        best_revenue = genre_stats.loc[
            genre_stats["Avg_Revenue"].idxmax()
        ]

        best_roi = genre_stats.loc[
            genre_stats["Avg_ROI"].idxmax()
        ]

        insight(
            "📌 Portfolio Conclusion",
            f"Observed success rate is {pct(financial['success'].mean()) if not financial.empty else '—'}. "
            f"{best_success['primary_genre']} leads observed success rate, "
            f"{best_revenue['primary_genre']} leads average revenue, and "
            f"{best_roi['primary_genre']} leads average ROI among genres with at least five movies.",
        )

    left, right = st.columns(2)

    with left:
        insight(
            "🏢 Studios",
            "Use MovieIQ as an early-stage screening layer. Benchmark proposed projects against historical budget, genre, popularity and rating patterns.",
        )

        insight(
            "💼 Investors",
            "Treat model output as risk screening rather than a standalone investment decision. Combine it with ROI, downside exposure and external due diligence.",
        )

        insight(
            "🎥 Producers",
            "Use Movie Explorer to compare proposed projects with historical movies that have similar characteristics.",
        )

    with right:
        insight(
            "📣 Marketing Teams",
            "Audience-interest indicators such as popularity and rating can support campaign prioritisation, but should not be interpreted as causal guarantees.",
        )

        insight(
            "⚠️ Risk",
            "Historical relationships do not automatically establish causation. The dataset does not contain every commercial driver.",
        )

        insight(
            "🚀 Next Version",
            "Add marketing spend, release date, cast, director, distributor, production company and competition variables.",
        )

    section("Recommended Actions")

    actions = [
        "Benchmark every proposed movie against historical comparables.",
        "Separate revenue scale from ROI efficiency.",
        "Use model probability as an early screening signal.",
        "Introduce time-aware validation when reliable release dates are available.",
        "Compare Random Forest with Logistic Regression and Gradient Boosting.",
        "Tune classification thresholds based on business costs of false positives and false negatives.",
    ]

    for i, action in enumerate(actions, 1):
        st.write(f"**{i}.** {action}")


# ============================================================
# 17. DATA QUALITY
# ============================================================

elif page == "📋 Data Quality":

    page_header(
        "📋 Data Quality",
        "Audit missing values, duplicates, financial validity and the prepared analytical dataset.",
    )

    total_missing = int(
        df.isna().sum().sum()
    )

    # Hash-safe duplicate detection: prepared MovieIQ data contains
    # list-valued columns such as genre_list.
    duplicate_check = df.copy()
    for _column in duplicate_check.columns:
        if duplicate_check[_column].map(lambda _value: isinstance(_value, (list, dict, set))).any():
            duplicate_check[_column] = duplicate_check[_column].map(
                lambda _value: repr(_value) if isinstance(_value, (list, dict, set)) else _value
            )
    duplicate_count = int(duplicate_check.duplicated().sum())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Rows",
        f"{len(df):,}",
    )

    c2.metric(
        "Columns",
        f"{df.shape[1]:,}",
    )

    c3.metric(
        "Missing Cells",
        f"{total_missing:,}",
    )

    c4.metric(
        "Duplicate Rows",
        f"{duplicate_count:,}",
    )

    section("Missing Value Analysis")

    missing = (
        df.isna()
        .sum()
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing",
    ]

    missing["Missing %"] = (
        missing["Missing"]
        / len(df)
        * 100
    )

    missing = missing[
        missing["Missing"] > 0
    ].sort_values(
        "Missing",
        ascending=False,
    )

    if missing.empty:
        st.success(
            "No missing values were detected."
        )
    else:
        fig = px.bar(
            missing.head(20),
            x="Missing %",
            y="Column",
            orientation="h",
            title="Top Columns by Missing Percentage",
        )

        fig.update_xaxes(
            ticksuffix="%"
        )

        st.plotly_chart(
            style_chart(fig, 500),
            use_container_width=True,
        )

        st.dataframe(
            missing,
            use_container_width=True,
            hide_index=True,
        )

    section("Duplicate Analysis")

    if duplicate_count:
        st.warning(
            f"{duplicate_count:,} duplicate rows were detected."
        )
    else:
        st.success(
            "No duplicate rows were detected."
        )

    section("Financial Data Validation")

    if {
        "budget",
        "revenue",
    }.issubset(df.columns):

        negative_budget = int(
            df["budget"]
            .fillna(0)
            .lt(0)
            .sum()
        )

        zero_budget = int(
            df["budget"]
            .fillna(0)
            .eq(0)
            .sum()
        )

        zero_revenue = int(
            df["revenue"]
            .fillna(0)
            .eq(0)
            .sum()
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Negative Budgets",
            f"{negative_budget:,}",
        )

        c2.metric(
            "Zero Budgets",
            f"{zero_budget:,}",
        )

        c3.metric(
            "Zero Revenue",
            f"{zero_revenue:,}",
        )

    section("Prepared Data Preview")

    st.dataframe(
        df.head(100),
        use_container_width=True,
        hide_index=True,
    )

    section("Export")

    csv_data = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇️ Download Prepared MovieIQ Dataset",
        data=csv_data,
        file_name="movieiq_prepared_dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )


# ============================================================
# 18. SINGLE NATIVE FOOTER
# ============================================================

st.divider()

footer_left, footer_right = st.columns(
    [2, 1]
)

with footer_left:
    st.caption(
        "MovieIQ • Film Success Intelligence"
    )
    st.caption(
        "Professional Data Analyst / BI Analyst Portfolio Project"
    )

with footer_right:
    st.caption(
        f"Analytics • Statistics • Machine Learning • v{APP_VERSION}"
    )
    st.caption(
        "Decision support, not guaranteed box-office forecasting."
    )
