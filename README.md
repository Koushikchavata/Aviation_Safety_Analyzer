# ✈️ Aviation Safety Analyzer
### LLM-Based Aviation Safety Report Analytics and Automated Hazard Review Generation Using Semantic Clustering

## 📌 Project Overview

Aviation Safety Analyzer is an AI-powered application designed to analyze aviation safety reports, identify recurring safety hazards, and automatically generate structured hazard reviews.

The system uses Natural Language Processing (NLP), semantic embeddings, machine learning clustering algorithms, and Large Language Models (LLMs) to identify patterns in aviation incident reports.

It processes aviation safety narratives from the NASA Aviation Safety Reporting System (ASRS), groups semantically similar reports, and generates meaningful hazard summaries to support aviation safety analysts.

The application provides an interactive dashboard developed using Streamlit, allowing users to explore clusters, search reports, visualize incident patterns, and export hazard reports.

## 🎯 Project Objectives

- Analyze large volumes of aviation safety reports.
- Identify recurring aviation hazards using semantic clustering.
- Group similar incident narratives automatically.
- Generate AI-based hazard summaries and safety recommendations.
- Visualize aviation incident patterns through an interactive dashboard.
- Support aviation safety analysts in identifying potential risks.

## 🚀 Key Features

- **Semantic Analysis:** Understands the meaning of aviation safety narratives rather than relying only on keywords.
- **Text Embeddings:** Uses Sentence-BERT (all-MiniLM-L6-v2) to convert text into numerical representations.
- **Dimensionality Reduction:** Uses UMAP to reduce embedding dimensions.
- **Hazard Clustering:** Uses HDBSCAN to identify meaningful groups of aviation incidents.
- **AI-Based Hazard Reviews:** Uses Gemini 2.5 Flash to generate structured hazard reviews.
- **Interactive Dashboard:** Streamlit-based dashboard for exploring aviation safety data.
- **Data Visualization:** Uses Plotly to display cluster statistics, flight phases, and incident patterns.
- **PDF Generation:** Generates downloadable hazard reports using ReportLab.
- **Noise Detection:** Identifies reports that do not belong to meaningful clusters without forcing them into categories.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend / Dashboard | Streamlit |
| Data Processing | Pandas, NumPy, PyArrow |
| NLP | Sentence-BERT |
| Embedding Model | all-MiniLM-L6-v2 |
| Dimensionality Reduction | UMAP |
| Clustering Algorithm | HDBSCAN |
| Generative AI | Google Gemini 2.5 Flash |
| Visualization | Plotly |
| PDF Generation | ReportLab |
| Data Storage | JSON, Parquet |

## ⚙️ System Workflow

1. **Data Collection:** Collect aviation safety narratives from the ASRS dataset.
2. **Data Preprocessing:** Clean the text, remove unnecessary characters, and handle missing values.
3. **Text Embedding:** Convert narratives into 384-dimensional semantic embeddings.
4. **Dimensionality Reduction:** Apply UMAP to reduce the embeddings to 10 dimensions.
5. **Clustering:** Apply HDBSCAN to identify groups of semantically similar reports.
6. **Representative Report Selection:** Select representative narratives from each meaningful cluster.
7. **Hazard Review Generation:** Use Gemini 2.5 Flash to generate structured hazard reviews.
8. **Dashboard Visualization:** Display clusters, reports, statistics, and generated reviews through Streamlit.

## 📊 Project Results

The proposed system was evaluated using a sample of 20,000 aviation safety reports from an ASRS extract containing 212,322 reports.

| Evaluation Metric | Result |
|---|---:|
| Total Reports in Sample | 20,000 |
| Meaningful Clusters | 71 |
| Noise Reports | 10,320 |
| Noise Percentage | 51.60% |
| Clustered Reports | 9,680 |
| Largest Cluster Size | 1,098 |
| Mean Cluster Size | 136.3 |

The system successfully identified recurring aviation safety themes, including altitude deviations, ATC phraseology issues, and bird strikes.

## 📁 Project Structure

```text
Aviation_Safety_Analyzer/
│
├── app.py
├── utils.py
├── pdf_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── clustered_aviation_reports.parquet
├── hazard_reports.json
│
├── Cluster_0_Hazard_Report.pdf
├── Cluster_1_Hazard_Report.pdf
├── Cluster_3_Hazard_Report.pdf
├── Cluster_5_Hazard_Report.pdf
├── Cluster_10_Hazard_Report.pdf
├── Cluster_18_Hazard_Report.pdf
│
└── Other project files
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Koushikchavata/Aviation_Safety_Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd Aviation_Safety_Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API Credentials

If you are running the Gemini-powered hazard generation functionality, configure your Google Gemini API key according to the environment variable expected by the application.

Never upload API keys or other confidential credentials to GitHub.

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## 📈 Applications

- Aviation safety monitoring.
- Incident and hazard identification.
- Aviation risk analysis.
- Flight safety trend analysis.
- Air Traffic Control (ATC) incident analysis.
- Safety management and decision support.

## ⚠️ Limitations

- The current evaluation uses only the first 20,000 cleaned reports from the larger ASRS dataset.
- Clustering evaluation is qualitative and requires further expert validation.
- Some reports remain unclustered and are classified as noise.
- AI-generated hazard reviews may contain unsupported interpretations and require verification.

**Important:** This application is intended as an analytical support tool. AI-generated recommendations are not a replacement for qualified aviation safety professionals or formal safety investigations.

## 🔮 Future Enhancements

- Process the complete ASRS dataset.
- Improve clustering accuracy through parameter optimization.
- Explore aviation-specific embedding models.
- Integrate Retrieval-Augmented Generation (RAG).
- Add expert validation and human-in-the-loop review.
- Introduce real-time aviation safety report monitoring.
- Support multilingual aviation safety narratives.

## 👨‍💻 Author

**Chavata Yuva Sai Koushik**

Department of Electronics and Communication Engineering  
School of Engineering, Dayananda Sagar University  
Bengaluru, Karnataka, India.

## 📚 Research Publication

**Research Title:** LLM-Based Aviation Safety Report Analytics and Automated Hazard Review Generation Using Semantic Clustering.

## 📜 License

This project is intended for academic and research purposes.
