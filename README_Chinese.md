# GISphereKG-ChatBot
[[GISphere 官网]](https://www.gisphere.info/) 

## 摘要

本文的研究背景是GIS学科在全球范围内的重要性日益提升。GIS技术已广泛应用于城市规划、环境检测、灾害管理等领域，这种多学科应用吸引了越来越多的学生选择相关研究生项目。然而，目前申请人面临以下几个主要问题：
1.	信息过载：全球超过600个GIS项目和2000多名教授的数据分布在不同的资源中，导致信息查找困难。
2.	缺乏个性化指导：现有工具无法根据申请人的研究兴趣或职业目标提供精准推荐。
3.	难以理解研究领域动态：学生难以深入了解教授的研究兴趣和领域趋势，影响其选择决策。

为了解决上述问题，本文提出了 GISphere-KG 平台。该平台通过知识图谱 (KG) 整合和组织异构数据，并借助大语言模型 (LLMs) 的自然语言处理能力，实现智能化的搜索、匹配和推荐。核心研究问题包括：

- 如何更高效、直观地获取与个人兴趣相符的项目资源？
- 如何发现研究方向相近的教授？
- 如何基于申请者的兴趣提供个性化的 GIS 项目推荐？

## 架构
<div align=center>
  <img width="1000" alt="image" src="https://github.com/user-attachments/assets/c51d834e-ca07-454c-855e-a2e2e4bebc05">
  <p><b>GISphereKG 架构图</b></p>
</div>

### 1. 数据收集与预处理
- 从 97 个国家和地区收集超过 600 个 GIS 项目和 2000 名教授的信息，数据包括国家、城市、大学、教授研究兴趣等
- 对数据进行清理和标准化，确保其准确性和一致性
### 2. 知识图谱构建
- 设计了包括“教授-研究兴趣-大学-地理位置”等关系在内的七类实体结构，并通过 Neo4j 实现可视化
- 定义语义关系（如教授的研究兴趣相似性）以支持复杂的语义查询
### 3. 语义相似度计算
- 使用 state-of-the-art 嵌入模型（如 text-embedding-ada-002）将研究兴趣转化为语义向量，利用余弦相似度计算兴趣间的相似性
- 建立“教授研究兴趣相似性”关系以支持相关教授的快速发现

### 4. 基于LLM的图搜索
- 显式图搜索：直接查询图数据库中的实体及其关系（如教授的研究兴趣或大学的地理位置）
- 隐式图搜索：基于申请人输入的研究兴趣，推导语义相似的项目和相关教授

## 使用说明

### 方法1：在线网页应用（推荐）

访问在线应用：https://gispherekg.streamlit.app/

### 方法2：本地安装

要在本地运行该应用，请按照以下步骤操作：

1. **Neo4j 设置：**

   - 创建一个 Neo4j 实例。
   - 进入“备份与恢复”，选择“从备份文件恢复”。
   - 上传位于 `data/` 文件夹中的备份文件。

2. **配置环境变量：**
    设置以下环境变量：

   - **数据库相关：** `NEO4J_URI`、`NEO4J_USERNAME` 和 `NEO4J_PASSWORD`
   - **OpenAI LLM：** `OPENAI_API_KEY` 和 `OPENAI_MODEL`

3. **安装依赖库：**
    在项目目录下运行以下命令：

   ```
   cd llm-chatbot-python
   pip install -r requirements.txt
   ```

4. **启动应用：**
    通过以下命令启动应用，默认访问地址为 http://localhost:8501/：

   ```
   streamlit run bot.py
   ```

## 相关教程

本项目基于 Streamlit 框架构建。更多资源请参考：

- [Streamlit 官方文档](https://docs.streamlit.io/)
- [GitHub 仓库：使用 Python 构建 Neo4j 驱动的聊天机器人](https://github.com/neo4j-graphacademy/llm-chatbot-python)
- [教程：使用 Python 构建 Neo4j 驱动的聊天机器人](https://graphacademy.neo4j.com/courses/llm-chatbot-python/1-project-setup/2-setup/)

## 引用

Gu, Z., Li, W., Zhou, B., Wang, Y., Chen, Y., Ye, S., Wang, K., Gu, H. and Kang, Y. (2025), *GISphere Knowledge Graph for Geography Education: Recommending Graduate Geographic Information System/Science Programs*. Transactions in GIS, 29: e13283. https://doi.org/10.1111/tgis.13283
