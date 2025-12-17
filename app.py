import streamlit as st
import random
import datetime

# ==========================================
# 1. 跨越黑潮：WOLF 教案生成引擎 (Render Engine)
# ==========================================

def render_wolf_lesson(grade, topic_data, version_key):
    """
    WOLF 引擎核心：動態生成對應五個不同素養的五階段教案。
    """
    
    # 1. 取得該版本的特定資料 (這裡會用修正後的 Key 進行查找)
    if version_key in topic_data["versions"]:
        v_data = topic_data["versions"][version_key]
    else:
        return "⚠️ Error: 資料庫索引錯誤，請聯繫開發者。"
    
    # 2. 定義風格標題與教學模式
    if "Ver. A" in version_key:
        style_title = "標準探究版 (Scientific Inquiry)"
        methodology = "WOLF x POE (預測-觀察-解釋)"
        role = "物理學家 (Physicist)"
    elif "Ver. B" in version_key:
        style_title = "硬派實作版 (Engineering Design)"
        methodology = "WOLF x EDP (工程設計流程)"
        role = "造船工程師 (Engineer)"
    elif "Ver. C" in version_key:
        style_title = "深度文化版 (Cultural Immersion)"
        methodology = "WOLF x CRT (文化回應教學)"
        role = "文化人類學家 (Anthropologist)"
    elif "Ver. D" in version_key:
        style_title = "數學幾何版 (Mathematical Modeling)"
        methodology = "WOLF x PBL (問題導向學習)"
        role = "幾何分析師 (Mathematician)"
    else: # Ver. E
        style_title = "仿生美學版 (Biomimicry & Art)"
        methodology = "WOLF x Design Thinking (設計思考)"
        role = "仿生設計師 (Designer)"

    # 3. 組合 Markdown 文本
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

## 壹、 設計理念與素養矩陣 (Competency Matrix)

本課程將 WOLF 的五個教學階段，分別對應至不同領域的核心素養，以達成跨領域的深度學習。

### 一、 階段素養對照表
| WOLF 階段 | 教學重點 | 對應核心素養 |
| :--- | :--- | :--- |
| **1. 傳承** | 生活文化世界觀的傳承 | **{v_data['phase1_comp']}** |
| **2. 表達** | 自我世界觀的表達 | **{v_data['phase2_comp']}** |
| **3. 探索** | 生活文化世界觀的探索 | **{v_data['phase3_comp']}** |
| **4. 形成** | 學科概念世界觀的形成 | **{v_data['phase4_comp']}** |
| **5. 連結** | 對話與連結 | **{v_data['phase5_comp']}** |

### 二、 學習目標
1.  **[認知]** {v_data['obj_cognitive']}
2.  **[技能]** {v_data['obj_skill']}
3.  **[情意]** {v_data['obj_affective']}

---

## 貳、 WOLF 五階段教學活動詳案 (Detailed Procedure)

### 第一階段：生活文化世界觀的傳承 (Transmission)
> **對應素養**：{v_data['phase1_comp']}
> **教學重點**：引起動機，連結舊經驗，傳遞文化記憶。

* **活動設計**：
    1. **{v_data['phase1_title']}**：
       {v_data['phase1_content']}
    2. **文化傳承者 (耆老/專家) 的話**：
       > *「{v_data['phase1_elder_quote']}」*

### 第二階段：自我世界觀的表達 (Expression)
> **對應素養**：{v_data['phase2_comp']}
> **教學重點**：學生提問、發表自己對該物品原本的想法（直覺模型）。

* **活動設計**：
    1. **關鍵提問**：
       「{v_data['phase2_question']}」
    2. **學生觀點發表**：
       {v_data['phase2_student_view']}

### 第三階段：生活文化世界觀的探索 (Exploration)
> **對應素養**：{v_data['phase3_comp']}
> **教學重點**：學生實際操作，用舊經驗去嘗試解釋現象，產生**認知衝突**。

* **活動設計**：
    1. **實作挑戰**：{v_data['phase3_task']}
    2. **探索過程**：
       {v_data['phase3_process']}
    3. **認知衝突 (The Conflict)**：
       {v_data['phase3_conflict']}

### 第四階段：學科概念世界觀的形成 (Formation)
> **對應素養**：{v_data['phase4_comp']}
> **教學重點**：教師介入，引入科學/學科知識，解釋現象背後的原理。

* **活動設計**：
    1. **教師引導 (專家觀點)**：{v_data['phase4_teacher']}
    2. **核心概念解碼**：
       > **{topic_data['concept']}**
       >
       > {v_data['phase4_science']}
    3. **概念應用與修正**：{v_data['phase4_application']}

### 第五階段：對話與連結 (Dialogue & Linkage)
> **對應素養**：{v_data['phase5_comp']}
> **教學重點**：學生用新學到的原理，重新解釋文化現象，完成文化與科學的整合。

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
# [FIX]: 這裡的 Key 必須跟 st.radio 的選項完全一致

topics_db = {
    "國中九年級 (力與運動/力矩)": [
        {
            "name": "誰能活著渡過黑潮？",
            "concept": "力矩 (Torque) 與 向量分解",
            "versions": {
                "Ver. A 標準探究版 (Science)": {
                    "obj_cognitive": "能運用向量分解解釋風對帆的作用力。",
                    "obj_skill": "能操作控制變因實驗，比較不同帆型的受力差異。",
                    "obj_affective": "體會科學原理如何驗證傳統智慧。",
                    "phase1_comp": "社會 [Sc-IV-2] 探究人類生活與環境的互動關係。",
                    "phase2_comp": "自科 [tr-IV-1] 能將所習得的知識正確的連結到所觀察到的自然現象。",
                    "phase3_comp": "自科 [pe-IV-2] 能正確安全操作適合學習階段的物品、器材儀器、科技設備與資源。",
                    "phase4_comp": "自科 [Sa-IV-2] 能以圖像與模型說明力與運動現象，提出解釋。",
                    "phase5_comp": "原民 [原-J-A2] 以原住民族文化主體性的觀點，對部落文化差異有初步了解。",
                    
                    "phase1_title": "黑潮傳說：海上的高速公路",
                    "phase1_content": "教師播放黑潮洶湧影片。講述 4000 年前南島祖先必須帶著全家大小，跨越這條流速極快（每秒 1.5 公尺）的『海上高速公路』。這是一場生死賭注，也是文明擴散的起點。",
                    "phase1_elder_quote": "帆要像螃蟹的手一樣，才能抓住風的脾氣。如果不順著風，海浪會把你的船吞掉。",
                    "phase2_question": "如果你是古代的船長，為了全家人的安全，你會選看起來四四方方、穩重的方形帆，還是看起來頭重腳輕、形狀怪異的倒三角帆（蟹爪帆）？",
                    "phase2_student_view": "學生分組討論並畫出預測圖。大多數學生依據直覺（自我世界觀），認為方形帆受風面積大、形狀規則，應該比較有力且穩定。",
                    "phase3_task": "風洞模擬實驗 (POE策略)",
                    "phase3_process": "學生製作相同面積的『方形帆』與『倒三角形帆』紙板模型，固定在滑車上，放入風洞（強力電風扇前）進行側風測試。記錄傾斜角度。",
                    "phase3_conflict": "【認知衝突】：學生驚訝地發現，他們認為『最穩』的方形帆，在強風下反而劇烈搖晃、嚴重側傾；而原本不看好的『怪異』倒三角帆，卻異常平穩。",
                    "phase4_teacher": "教師介入，引入物理學視角。這不是魔術，是力學。",
                    "phase4_science": "畫出受力圖。方形帆的『受風中心』過高，導致力臂 ($d$) 很長，產生巨大的翻船力矩 ($Torque = F \\times d$)。倒三角帆降低了重心，縮短力臂。",
                    "phase4_application": "學生修正之前的預測圖，在圖上標出『受風中心』與『力臂長度』，並計算兩者的力矩差異。",
                    "phase5_reinterpretation": "學生用『力矩』的概念，重新解釋耆老說的『抓住風的脾氣』其實就是『控制力矩平衡』。",
                    "phase5_reflection": "科學證明了祖先的設計不是落後，而是對抗黑潮環境的最佳化工程解。我們以為的『直覺』在極端環境下可能是錯誤的。",
                    "rubric_c": "無法解釋為何方形帆會翻。",
                    "rubric_b": "能指出重心高低影響穩定度。",
                    "rubric_a": "能精確繪製向量分解圖並計算力矩，以此解釋蟹爪帆優勢。"
                },
                "Ver. B 硬派實作版 (Engineering)": {
                    "obj_cognitive": "理解結構重心對載具穩定性的影響。",
                    "obj_skill": "能利用簡易材料設計並製作抗風船模。",
                    "obj_affective": "培養『試誤』與『反脆弱』的工程師精神。",
                    "phase1_comp": "科技 [議t-IV-1] 了解科技與社會議題的關係。",
                    "phase2_comp": "科技 [a-IV-2] 針對日常問題，提出多元的解決方案。",
                    "phase3_comp": "科技 [Sb-V-3] 能運用探究與實作方式，設計並測試簡易裝置。",
                    "phase4_comp": "自科 [tp-IV-2] 能依據實驗結果，解釋變因之間的關係。",
                    "phase5_comp": "原民 [原-J-A3] 能以原住民族文化主體性的觀點吸收文化新知，激發創新應變之潛能。",

                    "phase1_title": "造船者任務：黑潮求生",
                    "phase1_content": "發布任務書：『部落長老指派你們為首席工程師，部落需要一艘能抵抗 10 級強烈側風的船。』現場展示有限的材料包（竹籤、紙、膠帶）。",
                    "phase1_elder_quote": "海浪不會因為你的船好看就對你仁慈，它只尊重站得穩的船。",
                    "phase2_question": "在材料有限的情況下，憑你的直覺，怎樣的形狀跑得最快又不會翻？請畫出設計草圖。",
                    "phase2_student_view": "學生繪製設計草圖。許多組別傾向設計巨大的方形帆或高大的三角帆，認為帆越大動力越強（追求速度的直覺）。",
                    "phase3_task": "殘酷測試 (Crash Test)",
                    "phase3_process": "第一代模型上場。開啟工業扇最強檔，直接進行破壞性測試。學生親眼目睹自己的設計在水槽中翻船、解體。",
                    "phase3_conflict": "【實作衝突】：『為什麼我想像中完美的船，一秒鐘就翻了？』學生面臨挫折，發現直覺設計在極端環境下完全失效。",
                    "phase4_teacher": "工程診斷。教師扮演『工程總監』，引導學生分析『死因』。",
                    "phase4_science": "引入『力矩』概念作為診斷工具。翻船是因為側向力矩大於回復力矩。解決方案：改變帆的幾何形狀以降低重心。",
                    "phase4_application": "學生進行『迭代設計 (Iteration)』，將帆修改為蟹爪形或降低高度，進行第二代模型製作。",
                    "phase5_reinterpretation": "第二代模型成功通過強風測試。學生領悟：蟹爪帆是祖先經過無數次『翻船』後留下的終極演算法。",
                    "phase5_reflection": "工程師的智慧是跨越時空的。失敗不是終點，而是通往最佳設計的必經之路。",
                    "rubric_c": "模型無法通過測試。",
                    "rubric_b": "能透過嘗試錯誤修改模型，提升穩定性。",
                    "rubric_a": "能運用物理原理進行結構優化，成功渡過黑潮。"
                },
                "Ver. C 深度文化版 (Culture)": {
                    "obj_cognitive": "認識南島語族的航海科技與價值觀。",
                    "obj_skill": "能製作具有文化象徵意義的模型。",
                    "obj_affective": "認同並尊重原住民族『順應自然』的生態智慧。",
                    "phase1_comp": "原民 [原-J-C3] 探索不同文化的內涵，尊重並欣賞差異。",
                    "phase2_comp": "社會 [2a-IV-1] 敏覺居住地方的社會、經濟、文化及環境的變遷。",
                    "phase3_comp": "原民 [原-J-B3] 藉由族語的學習，賞析文化中美學的傳達。",
                    "phase4_comp": "社會 [1a-IV-2] 說明自然環境與人類活動的交互關係。",
                    "phase5_comp": "社會 [C3] 認識台灣原住民族的海洋世界觀與全球南島連結。",

                    "phase1_title": "聽見風的聲音",
                    "phase1_content": "教室佈置成海洋情境，播放阿美族海洋古調。教師帶領學生學習關鍵族語單字：Fayan (帆船)、Kuroshio (黑潮)。展示南島語族擴散地圖。",
                    "phase1_elder_quote": "船的眼睛看得到風的形狀。我們不征服海，我們是海的一部份。",
                    "phase2_question": "在你的想像中，西方大航海時代與南島祖先的航海，對於『風』和『海』的態度有什麼不同？是對抗還是合作？",
                    "phase2_student_view": "學生分享觀點。部分學生可能受現代觀點影響，認為科技就是要『征服』自然，船越大越好。",
                    "phase3_task": "儀式感手作與下水",
                    "phase3_process": "學生使用自然素材（落葉、麻繩、竹片）編織小帆。在下水測試前，教師引導學生進行模擬的『祈福儀式』。",
                    "phase3_conflict": "【文化衝突】：『為什麼要祈福？』『為什麼帆要做成這種像葉子的形狀？』學生在實作中感受到傳統工藝與現代工業的差異。",
                    "phase4_teacher": "文化轉譯者。連結『順應自然』的哲學與『流體力學』的科學。",
                    "phase4_science": "解釋『蟹爪帆』的空氣動力學優勢。祖先不與強風硬碰硬（對抗），而是設計出能讓風順利流過的形狀（合作/順應）。這就像太極拳，借力使力。",
                    "phase4_application": "學生重新審視自己的模型，調整帆的角度以『順應』風向，而非『擋住』風。",
                    "phase5_reinterpretation": "學生理解：祈福不是迷信，而是對自然的敬畏與風險管理；蟹爪帆是這份敬畏的具體科技展現。",
                    "phase5_reflection": "西方科學教我們計算風，南島智慧教我們感受風。兩者都是真理。",
                    "rubric_c": "僅完成模型製作，無法連結文化意涵。",
                    "rubric_b": "能說出蟹爪帆的文化故事與象徵意義。",
                    "rubric_a": "能深度比較西方與南島航海觀的哲學差異。"
                },
                "Ver. D 數學幾何版 (Math)": {
                    "obj_cognitive": "能計算不同幾何形狀的重心位置。",
                    "obj_skill": "能運用幾何作圖法找到不規則圖形的重心。",
                    "obj_affective": "欣賞數學在解決實際生存問題中的應用價值。",
                    "phase1_comp": "數學 [n-IV-9] 理解比與比例的應用。",
                    "phase2_comp": "數學 [s-IV-4] 理解幾何圖形的性質。",
                    "phase3_comp": "自科 [pa-IV-1] 能運用測量工具進行精確測量。",
                    "phase4_comp": "數學 [S-IV-10] 理解幾何圖形的重心性質。",
                    "phase5_comp": "原民 [原-J-A2] 能以原住民族文化主體性的觀點，運用基本邏輯思考策略。",

                    "phase1_title": "幾何的生存法則",
                    "phase1_content": "展示各種幾何形狀的帆（正方形、長方形、正三角形、倒三角形）。提問：『在數學家的眼裡，哪一種形狀最適合在海上保持平衡？』",
                    "phase1_elder_quote": "老人家不懂 $y=ax+b$，但他們知道怎樣的形狀才『正』，才不會『歪』。",
                    "phase2_question": "如果有兩塊面積相同的帆，一塊是長方形，一塊是倒三角形，你覺得哪一塊的『幾何中心（重心）』比較低？",
                    "phase2_student_view": "學生進行幾何直覺猜測。部分學生認為長方形比較穩，因為它看起來比較『正』。",
                    "phase3_task": "尋找重心 (Finding Centroid)",
                    "phase3_process": "學生剪下相同面積的紙板（方型 vs 蟹爪型）。利用『懸吊法』或『平衡法』（放在筆尖上）找出這兩塊紙板的真實重心位置。",
                    "phase3_conflict": "【數據衝突】：測量結果顯示，雖然蟹爪帆看起來頭重腳輕，但其幾何重心的高度，竟然比同面積的長方形帆還要低。",
                    "phase4_teacher": "數學家介入。引入幾何重心的計算公式。",
                    "phase4_science": "講解三角形重心位於中線 2:1 處的性質。透過計算證明，在底邊固定的情況下，特定的倒三角幾何配置能有效壓低『受力中心』。",
                    "phase4_application": "學生計算不同尺寸帆的力矩大小，並繪製『穩定性 vs 形狀』的關係圖。",
                    "phase5_reinterpretation": "學生用數學語言重新詮釋蟹爪帆：它是一個『最佳化幾何解』，在最大化面積（動力）的同時，最小化重心高度（力矩）。",
                    "phase5_reflection": "數學不只是紙上的公式，它是描述自然規律的語言。南島祖先是天生的幾何學家。",
                    "rubric_c": "無法找出幾何圖形的重心。",
                    "rubric_b": "能透過實驗找到重心，並比較高低。",
                    "rubric_a": "能運用重心性質與力矩公式，以數學邏輯證明蟹爪帆的穩定性。"
                },
                "Ver. E 仿生美學版 (Art)": {
                    "obj_cognitive": "認識仿生學 (Biomimicry) 的概念與應用。",
                    "obj_skill": "能運用自然造型元素進行帆船外觀設計。",
                    "obj_affective": "體會機能美學 (Form follows function) 的深層意義。",
                    "phase1_comp": "藝術 [視1-IV-1] 能運用藝術詞彙與概念，描述藝術作品。",
                    "phase2_comp": "藝術 [視1-IV-2] 能表達對藝術作品的直觀感受與聯想。",
                    "phase3_comp": "科技 [設a-IV-1] 能運用設計思考，解決日常生活問題。",
                    "phase4_comp": "自科 [Im-IV-2] 觀察生物的形態與構造。",
                    "phase5_comp": "原民 [原-J-B3] 藉由族語的學習，賞析文化中美學的傳達。",

                    "phase1_title": "向大自然學設計",
                    "phase1_content": "展示一系列自然界的流線型設計：鳥的翅膀、魚的鰭、螃蟹的螯。並展示現代科技（跑車、飛機）如何模仿這些造型。",
                    "phase1_elder_quote": "山有山的樣子，海有海的樣子。做的東西如果不像海裡的生物，海是不會接受的。",
                    "phase2_question": "蟹爪帆為什麼長得像螃蟹的螯？這僅僅是為了好看，還是有其他原因？",
                    "phase2_student_view": "學生發揮想像力，繪製各種仿生帆。他們開始思考『造型』與『功能』的關係。",
                    "phase3_task": "造型與風的對話",
                    "phase3_process": "學生使用柔軟的紙張或布料，模仿蟹爪帆的『弧度』與『立體結構』。用電風扇吹拂，觀察布料的線條變化。",
                    "phase3_conflict": "【美學衝突】：學生發現，平面死板的設計在風中會劇烈拍打，而模仿生物的弧形設計，風會順著線條流動，呈現『動態美』。",
                    "phase4_teacher": "設計師介入。引入『流體力學美學』與『仿生學』。",
                    "phase4_science": "解釋『型隨機能』。蟹爪帆的曲線類似飛機的機翼，能產生『氣動升力』。這種美，是經過演化篩選出來的『機能美』。",
                    "phase4_application": "學生優化自己的設計，在美感與功能之間取得平衡，並設計獨特的部落圖騰。",
                    "phase5_reinterpretation": "學生重新詮釋祖先的工藝：那不只是工具，那是藝術品。每一道弧線都有它的理由。",
                    "phase5_reflection": "真正的設計，是與自然和諧共處。我們從祖先的設計中學到，最美的線條，往往也是最有效率的線條。",
                    "rubric_c": "設計缺乏仿生概念。",
                    "rubric_b": "能模仿生物特徵進行設計，具備基本美感。",
                    "rubric_a": "能融合仿生概念與機能美學，設計出既美觀又具備空氣動力優勢的作品。"
                }
            }
        }
    ]
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
    .reportview-container .main .block-container{ max-width: 1000px; }
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
    
    # 3. 選擇風格 (擴充為 5 種)
    st.markdown("### 3. 選擇風格")
    version_select = st.radio(
        "Style", 
        [
            "Ver. A 標準探究版 (Science)", 
            "Ver. B 硬派實作版 (Engineering)", 
            "Ver. C 深度文化版 (Culture)",
            "Ver. D 數學幾何版 (Math)",
            "Ver. E 仿生美學版 (Art)"
        ]
    )
    
    st.markdown("---")
    st.caption("Engine: **跨越黑潮 v14.1 (Fix Key)**")

# 主畫面
st.markdown(f"# 🌊 跨越黑潮：{grade_select.split(' ')[0]} WOLF 教案")
st.markdown(f"### 🎯 {current_topic['name']}")

# 資訊儀表板
col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"**核心概念**\n\n{current_topic['concept']}")
with col2:
    st.warning(f"**教學模式**\n\n{version_select}") 
with col3:
    if "Ver. A" in version_select:
        st.metric("科學含量", "⭐⭐⭐⭐⭐")
    elif "Ver. B" in version_select:
        st.metric("實作強度", "🔥🔥🔥🔥🔥")
    elif "Ver. C" in version_select:
        st.metric("文化深度", "🌏🌏🌏🌏🌏")
    elif "Ver. D" in version_select:
        st.metric("邏輯思維", "📐📐📐📐📐")
    else:
        st.metric("藝術美感", "🎨🎨🎨🎨🎨")

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
