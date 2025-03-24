# GISphereKG ChatBot

## Abstract

The research background of this paper is the increasing global importance of the GIS discipline. GIS technology is widely applied in urban planning, environmental monitoring, disaster management, and other areas. This interdisciplinary application has attracted a growing number of students to pursue related graduate programs. However, applicants currently face the following key issues:

1. **Information overload:** Data on over 600 GIS projects and more than 2000 professors from around the world are dispersed across different sources, making information retrieval difficult.
2. **Lack of personalized guidance:** Existing tools cannot provide precise recommendations based on an applicant’s research interests or career goals.
3. **Difficulty understanding research dynamics:** Students find it challenging to gain in-depth insights into professors' research interests and trends in the field, which affects their decision-making.

To address these challenges, this paper proposes the GISphere-KG platform. By integrating and organizing heterogeneous data through a knowledge graph (KG) and leveraging the natural language processing capabilities of large language models (LLMs), the platform offers intelligent search, matching, and recommendation functionalities for applicants. The core research questions include:

- How can applicants more efficiently and intuitively access project resources that align with their interests?
- How can applicants discover professors with similar research directions?
- How can personalized recommendations for suitable GIS projects be provided based on an applicant’s interests?

## Architecture

<div align=center>
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/c51d834e-ca07-454c-855e-a2e2e4bebc05">
  <p><b>The workflow of the GISphere-KG</b></p>
</div>

### 1. Data Collection and Preprocessing

- Collected information from over 600 GIS projects and 2000 professors across 97 countries and regions, including details such as country, city, university, and professors' research interests.
- Data cleaning and standardization are performed to ensure accuracy and consistency.

### 2. Knowledge Graph Construction

- Designed a seven-category entity structure—including relationships such as "Professor - Research Interests - University - Geographic Location"—and visualized it using Neo4j.
- Defined semantic relationships (e.g., similarity between professors' research interests) to support complex semantic queries.

### 3. Semantic Similarity Calculation

- Utilized state-of-the-art embedding models (e.g., text-embedding-ada-002) to convert research interests into semantic vectors, with cosine similarity used to compute the similarity between interests.
- Established "Professor Research Interest Similarity" relationships to support rapid discovery of related professors.

### 4. LLM-based Graph Search

- **Explicit graph search:** Directly queries the entities and relationships within the graph database (e.g., professors' research interests or universities' geographic locations).
- **Implicit graph search:** Infers semantically similar projects and related professors based on the research interests provided by the applicant.

## Usage

### Option 1: Online Application (Recommended)

Access the live application at:
 https://gispherekg.streamlit.app/

### Option 2: Local Installation

To run the application locally, follow these steps:

1. **Neo4j Setup:**

   - Create a [Neo4j](https://neo4j.com/) instance (for free).
   - Navigate to 'Back up and restore' and select 'Restore from backup file.'
   - Upload the backup file located in the `llm-chatbot-python/data/` folder.

2. **Environment Variables:**
    Create a `secrets.toml` file in `llm-chatbot-python/.streamlit/` folder and configure the following environment variables:

   - **Neo4j Database:** `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`
   - **OpenAI LLM:** `OPENAI_API_KEY`, `OPENAI_MODEL`

3. **Install Dependencies:**
    In the project directory, run:

   ```bash
   cd llm-chatbot-python
   pip install -r requirements.txt
   ```

4. **Run the Application:**
    Launch the app on http://localhost:8501/ with:

   ```bash
   streamlit run bot.py
   ```

## Related Tutorials

This project is built upon the Streamlit framework. For additional resources, please refer to the following:

- [Streamlit Documentation](https://docs.streamlit.io/)
- [GitHub Repo: Build a Neo4j-backed Chatbot using Python](https://github.com/neo4j-graphacademy/llm-chatbot-python)
- [Tutorial: Build a Neo4j-backed Chatbot using Python](https://graphacademy.neo4j.com/courses/llm-chatbot-python/1-project-setup/2-setup/)

## Chinese Version

A Chinese version of the README is available here:
 [[中文版本\]](https://chatgpt.com/c/README_Chinese.md)

## Citation

Gu, Z., Li, W., Zhou, B., Wang, Y., Chen, Y., Ye, S., Wang, K., Gu, H. and Kang, Y. (2025), *GISphere Knowledge Graph for Geography Education: Recommending Graduate Geographic Information System/Science Programs*. Transactions in GIS, 29: e13283. https://doi.org/10.1111/tgis.13283
