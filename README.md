# GISphereKG-ChatBot
## 摘要
本文的研究背景是GIS学科在全球范围内的重要性日益提升。GIS技术已广泛应用于城市规划、环境检测、灾害管理等领域，这种多学科应用吸引了越来越多的学生选择相关研究生项目。然而，目前申请人面临以下几个主要问题：
1.	信息过载：全球超过600个GIS项目和2000多名教授的数据分布在不同的资源中，导致信息查找困难。
2.	缺乏个性化指导：现有工具无法根据申请人的研究兴趣或职业目标提供精准推荐。
3.	难以理解研究领域动态：学生难以深入了解教授的研究兴趣和领域趋势，影响其选择决策。
为了解决这些问题，本文提出 GISphere-KG 平台。它通过知识图谱（KG）整合和组织异构数据，并结合大语言模型（LLMs）的自然语言处理能力，为申请人提供智能化的搜索、匹配和推荐功能。其核心研究问题包括：
•	如何使申请人更高效、直观地获取与其兴趣一致的项目资源？
•	如何帮助申请人发现研究方向相近的教授？
•	如何根据申请人兴趣个性化推荐适合的 GIS 项目？

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




