import streamlit as st
import random
import datetime

# ==========================================
# 1. 跨越黑潮：WOLF 教案生成引擎 (Render Engine)
# ==========================================

def render_wolf_lesson(grade, topic_data, version_key):
    """
    WOLF 引擎核心：將資料庫中的參數，精確映射到 WOLF 五階段架構中。
    """
    
    # 1. 取得該版本的特定資料
    v_data = topic_data["versions"][version_key]
    
    # 2. 定義風格標題與教學模式
    if "Ver. A" in version_key:
        style_title = "標準探究版 (Balanced Protocol)"
        methodology = "WOLF 模組 x POE (預測-觀察-解釋)"
        role = "科學探究者"
    elif "Ver. B" in version_key:
        style_title = "硬派實作版 (Maker Protocol)"
        methodology = "WOLF 模組 x EDP (工程設計流程)"
        role = "部落工程師"
    else: # Ver. C
        style_title = "深度文化版 (Cultural Immersion)"
        methodology = "WOLF 模組 x CRT (文化回應教學)"
        role = "文化傳承者"

    # 3. 組合 Markdown 文本 (嚴格遵循 WOLF 五階段)
    markdown_content = f"""
# 【跨越黑潮】WOLF 教學模組設計：{topic_data['name']}

| 項目 | 內容說明 |
| :--- | :--- |
| **單元名稱** | {topic_data['name']} —— {style_title} |
| **設計架構** | **WOLF (Worldview-Oriented Learning Framework)** |
| **適用對象** | {grade} |
| **教學時間** | 90 分鐘 (兩節課連排) |
| **教學模式** | {methodology} |
| **學生角色** | {role} |

---

## 壹、 核心素養與學習目標 (Competencies)

### 一、 核心素養 (本版本專屬)
* **主要素養**：**{v_data['competency_main']}**
* **次要素養**：{v_data['competency_sub']}

### 二、 學習目標
1.  **[認知]** {v_data['obj_cognitive']}
2.  **[技能]** {v_data['obj_skill']}
3.  **[情意]** {v_data['obj_affective']}

---

## 貳、 WOLF 五階段教學活動設計 (Five Phases)

本課程依據 WOLF 模組之五大階段進行設計，強調生活文化世界觀與學科概念世界觀的對話。

### 第一階段：生活文化世界觀的傳承 (Transmission)
> **教學重點 (引起動機)**：邀請耆老或家長分享、展示童玩/器具，做經驗傳承。

* **活動設計**：
    1. **{v_data['phase1_title']}**：
       {v_data['phase1_content']}
    2. **文化傳承者 (耆老/專家) 的話**：
       > *「{v_data['phase1_elder_quote']}」*

### 第二階段：自我世界觀的表達 (Expression)
> **教學重點 (發展活動 1)**：學生提問、發表自己對該物品原本的想法。

* **活動設計**：
    1. **關鍵提問**：
       「{v_data['phase2_question']}」
    2. **學生觀點發表 (自我世界觀)**：
       {v_data['phase2_student_view']}

### 第三階段：生活文化世界觀的探索 (Exploration)
> **教學重點 (發展活動 2)**：學生實際操作，用舊經驗去嘗試解釋現象（產生認知衝突）。

* **活動設計**：
    1. **實作挑戰**：{v_data['phase3_task']}
    2. **探索過程**：
       {v_data['phase3_process']}
    3. **認知衝突 (The Conflict)**：
       {v_data['phase3_conflict']}

### 第四階段：學科概念世界觀的形成 (Formation)
> **教學重點 (發展活動 3)**：教師介入，引入課本知識/實驗，解釋現象背後的原理。

* **活動設計**：
    1. **教師引導 (科學介入)**：{v_data['phase4_teacher']}
    2. **核心概念解碼**：
       > **{topic_data['concept']}**
       >
       > {v_data['phase4_science']}
    3. **概念應用與修正**：{v_data['phase4_application']}

### 第五階段：對話與連結 (Dialogue & Linkage)
> **教學重點 (綜合活動)**：學生用新學到的原理，重新解釋文化現象，完成文化與科學的整合。

* **活動設計**：
    1. **重新詮釋 (連結)**：{v_data['phase5_reinterpretation']}
    2. **文化反思 (對話)**：
       {v_data['phase5_reflection']}

---

## 參、 評量規準 (Assessment)

| 評量向度 | C (待加強) | B (基礎) | A (精熟) |
| :--- | :--- | :--- | :--- |
| **WOLF 歷程** | 僅參與聽講，未表達自我觀點。 | 能完成 Phase 3 的實作探索，並察覺與舊經驗的衝突。 | 能在 Phase 5 運用科學概念精確解釋文化現象，達成世界觀連結。 |
| **核心素養** | {v_data['rubric_c']} | {v_data['rubric_b']} | {v_data['rubric_a']} |

---
*本教案由【跨越黑潮】引擎依據 WOLF 教學模組規格自動生成*
"""
    return markdown_content

# ==========================================
# 2. 教案資料庫 (Topics Database)
# ==========================================
# 這裡針對每個版本，設定了「完全不同」的素養與五階段內容

topics_db = {
    "國中九年級 (力與運動/力矩)": [
        {
            "name": "誰能活著渡過黑潮？",
            "concept": "力矩 (Torque) 與 向量分解",
            "versions": {
                "Ver. A 標準探究版": {
                    "competency_main": "自然科學 [Sa-V-2] 能以圖像與模型說明力與運動現象。",
                    "competency_sub": "原住民族 [原-J-A1] 展現原住民族文化主體性。",
                    "obj_cognitive": "能運用向量分解解釋風對帆的作用力。",
                    "obj_skill": "能操作控制變因實驗，比較不同帆型的受力。",
                    "obj_affective": "體會科學原理如何驗證傳統智慧。",
                    "phase1_title": "黑潮傳說",
                    "phase1_content": "播放黑潮洶湧的影片。講述 4000 年前南島祖先必須帶著全家大小，跨越這條『海上的高速公路』。",
                    "phase1_elder_quote": "帆要像螃蟹的手一樣，才能抓住風的脾氣。",
                    "phase2_question": "如果你是船長，為了安全，你會選看起來穩重的方形帆，還是頭重腳輕的倒三角帆？",
                    "phase2_student_view": "學生分組討論並畫出預測圖。大多數學生依據直覺（自我世界觀），認為方形帆受風面積大，應該比較有力且穩定。",
                    "phase3_task": "風洞模擬實驗 (POE策略)",
                    "phase3_process": "學生製作方形與倒三角形的紙板模型，放入風洞（電風扇前）進行側風測試。",
                    "phase3_conflict": "認知衝突產生：學生驚訝地發現，他們認為『最穩』的方形帆，在強風下反而劇烈搖晃甚至翻倒；而『怪異』的倒三角帆卻異常平穩。",
                    "phase4_teacher": "教師介入，引入物理學視角。這不是魔術，是力學。",
                    "phase4_science": "畫出受力圖。方形帆的『受風中心 (Center of Effort)』過高，導致力臂 ($d$) 很長，產生巨大的翻船力矩 ($Torque = F \\times d$)。倒三角帆降低了重心，縮短力臂。",
                    "phase4_application": "學生修正之前的預測圖，標出力臂長度。",
                    "phase5_reinterpretation": "學生用『力矩』的概念，重新解釋耆老說的『抓住風的脾氣』其實就是『控制力矩平衡』。",
                    "phase5_reflection": "科學證明了祖先的設計不是落後，而是對抗黑潮環境的最佳化工程解。",
                    "rubric_c": "無法解釋為何方形帆會翻。",
                    "rubric_b": "能指出重心高低影響穩定度。",
                    "rubric_a": "能繪製向量圖並計算力矩，精確解釋蟹爪帆優勢。"
                },
                "Ver. B 硬派實作版": {
                    "competency_main": "科技領域 [Sb-V-3] 能運用探究與實作方式，設計並測試簡易裝置。",
                    "competency_sub": "原住民族 [原-J-A2] 理解傳統工藝是解決生存問題的工程演算法。",
                    "obj_cognitive": "理解結構重心對載具穩定性的影響。",
                    "obj_skill": "能利用簡易材料設計抗風船模。",
                    "obj_affective": "培養從失敗中學習的工程師精神。",
                    "phase1_title": "造船者任務",
                    "phase1_content": "發布任務書：部落需要一艘能抵抗 10 級強風的船。展示材料包（竹籤、紙、膠帶）。",
                    "phase1_elder_quote": "海浪不會因為你的船好看就對你仁慈，它只尊重站得穩的船。",
                    "phase2_question": "憑你的直覺，怎樣的形狀跑得最快又不會翻？",
                    "phase2_student_view": "學生繪製設計草圖。許多組別傾向設計巨大的方形帆以追求速度。",
                    "phase3_task": "殘酷測試 (Crash Test)",
                    "phase3_process": "第一代模型上場。開啟工業扇最強檔。學生親眼目睹自己的設計翻船、解體。",
                    "phase3_conflict": "實作衝突：為什麼我想像中『完美』的船，一秒鐘就翻了？問題出在哪裡？",
                    "phase4_teacher": "工程診斷。引導學生分析『死因』。",
                    "phase4_science": "引入『力矩』概念作為診斷工具。翻船是因為側向力矩大於回復力矩。解決方案：(1)加重船底 (2)降低帆的幾何中心。",
                    "phase4_application": "學生進行『迭代設計 (Iteration)』，將帆修改為蟹爪形（方案2）。",
                    "phase5_reinterpretation": "第二代模型成功通過測試。學生領悟：蟹爪帆是祖先經過無數次『翻船』後留下的終極演算法。",
                    "phase5_reflection": "工程師的智慧是跨越時空的。我們用竹籤做的事，祖先用林投葉也做到了。",
                    "rubric_c": "模型無法通過測試且不知原因。",
                    "rubric_b": "能透過修改模型提升穩定性。",
                    "rubric_a": "能運用物理原理進行結構優化，並成功渡過黑潮。"
                },
                "Ver. C 深度文化版": {
                    "competency_main": "社會領域 [C3] 認識台灣原住民族的海洋世界觀。",
                    "competency_sub": "原住民族 [原-J-C3] 探索不同文化的內涵，尊重並欣賞差異。",
                    "obj_cognitive": "認識南島語族的航海科技與價值觀。",
                    "obj_skill": "能製作具有文化象徵意義的模型。",
                    "obj_affective": "認同並尊重原住民族的自然智慧。",
                    "phase1_title": "聽見風的聲音",
                    "phase1_content": "學習族語單字：Fayan (帆船)、Kuroshio (黑潮)。播放阿美族海洋古調。",
                    "phase1_elder_quote": "船的眼睛看得到風的形狀。",
                    "phase2_question": "在你的想像中，祖先是如何看待『風』和『海』的？是對抗還是合作？",
                    "phase2_student_view": "學生分享觀點。部分學生可能受現代觀點影響，認為要『征服』海洋。",
                    "phase3_task": "儀式感手作",
                    "phase3_process": "使用自然素材（落葉、麻繩）編織小帆。在下水前進行模擬的祈福儀式。",
                    "phase3_conflict": "文化衝突：為什麼要祈福？為什麼不把帆做大一點？現代科技不是更厲害嗎？",
                    "phase4_teacher": "文化轉譯者。連結『順應自然』與『物理效率』。",
                    "phase4_science": "解釋『蟹爪帆』的空氣動力學優勢（渦流升力）。祖先不與強風硬碰硬（對抗），而是設計出能讓風順利流過的形狀（合作/順應）。",
                    "phase4_application": "學生重新審視自己的模型，調整帆的角度以『順應』風向。",
                    "phase5_reinterpretation": "學生理解：祈福是對自然的敬畏，蟹爪帆是這份敬畏的具體科技展現。",
                    "phase5_reflection": "西方科學教我們計算風，南島智慧教我們感受風。兩者都是真理。",
                    "rubric_c": "僅完成模型製作。",
                    "rubric_b": "能說出蟹爪帆的文化意涵。",
                    "rubric_a": "能深度比較西方與南島航海觀的哲學差異。"
                }
            }
        }
    ]
    # 為了節省篇幅，其他年級的 WOLF 詳細內容可依此格式繼續擴充
}

# ==========================================
# 3. Streamlit 介面邏輯 (UI)
# ==========================================
st.set_page_config(page_title="跨越黑潮 WOLF 教案實驗室", page_icon="🌊", layout="wide")

# CSS 優化：讓標題更明顯
st.markdown("""
<style>
    .stButton>button { border-radius: 20px; border: 2px solid #2E86C1; width: 100%; }
    h1 { color: #154360; }
    h3 { border-left: 5px solid #F39C12; padding-left: 10px; color: #E67E22; }
    .stSuccess { background-color: #D4E6F1; }
</style>
""", unsafe_allow_html=True)

# Session State
if 'topic_index' not in st.session_state:
    st.session_state.topic_index = 0

def randomize_topic():
    st.session_state.topic_index = random.randint(0, 100)

# 側邊欄
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2922/2922037.png", width=80)
    st.title("⚙️ 課程控制台")
    st.markdown("---")
    
    # 1. 選擇年級
    grade_options = list(topics_db.keys())
    grade_select = st.selectbox("1. 選擇教學對象", grade_options)
    
    # 2. 隨機主題
    st.markdown("### 2. 生成主題")
    if st.button("🎲 隨機運算新主題 (Reroll)"):
        randomize_topic()
    
    current_grade_topics = topics_db[grade_select]
    current_topic = current_grade_topics[st.session_state.topic_index % len(current_grade_topics)]
    
    st.success(f"已鎖定：{current_topic['name']}")
    
    # 3. 選擇風格
    st.markdown("### 3. 選擇風格")
    version_select = st.radio("Style", ["Ver. A 標準探究版", "Ver. B 硬派實作版", "Ver. C 深度文化版"])
    
    st.markdown("---")
    st.caption("Engine: **跨越黑潮 v12.0 (WOLF-Certified)**")

# 主畫面
st.markdown(f"# 🌊 跨越黑潮：{grade_select.split(' ')[0]} WOLF 教案")
st.markdown(f"### 🎯 {current_topic['name']}")

# 資訊儀表板
col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"**核心概念**\n\n{current_topic['concept']}")
with col2:
    # 動態顯示該版本的核心素養
    v_comp = current_topic['versions'][version_select]['competency_main']
    st.warning(f"**核心素養**\n\n{v_comp.split(']')[0]}]...") 
with col3:
    if "Ver. A" in version_select:
        st.metric("科學含量", "⭐⭐⭐⭐")
    elif "Ver. B" in version_select:
        st.metric("實作強度", "🔥🔥🔥🔥🔥")
    else:
        st.metric("文化深度", "🌏🌏🌏🌏")

st.markdown("---")

# 動態生成完整教案文本
full_lesson_plan = render_wolf_lesson(grade_select, current_topic, version_select)

# 顯示與下載
tab1, tab2 = st.tabs(["📄 WOLF 教案預覽", "📥 下載正式文件"])

with tab1:
    st.markdown(full_lesson_plan)

with tab2:
    st.success("✅ 已為您生成符合 WOLF 教學模組規格的正式詳案。")
    st.download_button(
        label=f"📥 下載 {current_topic['name']} ({version_select[:6]}).md",
        data=full_lesson_plan,
        file_name=f"WOLF_Lesson_{current_topic['name']}_{version_select[:6]}.md",
        mime="text/markdown",
        type="primary"
    )
