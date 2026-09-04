# -*- coding: utf-8 -*-
"""Japanese -> English translation map for index.html -> en/index.html.

This is a one-shot, hand-authored translation (2026-09-04). It exists as a
plain Python dict (not prose) so a future automated re-translation pass
can diff against it, and so re-running the apply script is deterministic.
"""

TRANSLATIONS = {
    # --- meta / nav ---
    "佐藤和彦｜Software Engineer / Research Prototyping": "Kaz Sato | Software Engineer / Research Prototyping",
    "本文へスキップ": "Skip to content",
    "佐藤 和彦": "Kaz Sato",
    "相談できること": "What I Can Help With",
    "代表的な仕事": "Selected Work",
    "調べ方": "How I Debug",
    "出版・監修": "Publications",
    "経歴と関心": "About",
    "年表": "Timeline",
    "連絡先": "Contact",

    # --- hero ---
    "アイデアを、": "Turning ideas",
    "動くもの": "into working",
    "にする。": " systems.",
    "AI・組み込み・デバイス・Webを横断し、研究アイデアや技術構想を、検証できるソフトウェアと試作機へ落とし込みます。うまく動かないものの調査や、技術検証の途中からでも対応できます。":
        "Working across AI, embedded systems, devices, and the web, I turn research ideas and technical concepts into testable software and working prototypes. I can also join mid-project — investigating why something isn't working, or picking up a technical evaluation already in progress.",
    "研究・試作・不具合調査の途中段階からでも相談できます。": "Feel free to reach out even mid-way through research, prototyping, or debugging.",
    "技術の変化を追い続ける": "Following technology as it changes",
    "AI / 組み込み / デバイス / Web": "AI / Embedded / Devices / Web",
    "設計・実装・実機検証・運用": "Design, implementation, hardware verification, operation",
    "技術書の監訳・監修・編集": "Technical book translation, supervision, and editing",

    # --- ASK section ---
    "技術名の一覧ではなく、持ち込める課題の形で整理しています。研究の本筋ではないけれど必要になる道具や、まだ原因が分からない不具合も含みます。":
        "Organized by the kind of problem you can bring me, not a list of technologies. This includes tools that fall outside your core research but still need building, and bugs whose cause isn't known yet.",
    "研究用ソフトウェア・検証ツールをつくる": "Build research software and verification tools",
    "実験・計測、センサーデータの可視化、性能比較、複数OSでの動作検証など。研究目的に合わせた道具を設計・実装します。":
        "Experiment and measurement tools, sensor data visualization, performance comparison, cross-OS verification — designed and built around your specific research goal.",
    "AIを機器・OS・センサーにつなぐ": "Connect AI to devices, the OS, and sensors",
    "MCPサーバーなどを介して、AIクライアントからBLEデバイス、画面、シリアルログ、業務システムを扱えるようにします。":
        "Using MCP servers and similar bridges, let an AI client operate BLE devices, capture the screen, monitor serial logs, or reach into a business system.",
    "AI・LLMを使ったツールを試作する": "Prototype AI / LLM-powered tools",
    "マルチエージェント、構造化出力、認証・DB・ストリーミングを含む試作まで。クラウドへの依存を減らすオンデバイス推論も扱います。":
        "From multi-agent systems and structured output to full prototypes with auth, a database, and streaming. On-device inference that reduces cloud dependence is also in scope.",
    "センサー・マイコン・IoTの実機をつくる": "Build sensor / microcontroller / IoT hardware",
    "複数マイコンの協調、無線通信、省電力、クラウド連携、スマートフォンアプリまで。実機動作と引き継ぎ文書を成果物にします。":
        "Multi-MCU coordination, wireless communication, low-power design, cloud integration, and companion phone apps. Delivered as working hardware plus handoff documentation.",
    "動かない技術・性能問題を切り分ける": "Isolate why something doesn't work, or runs slowly",
    "ライブラリのソース、OS設定、通信、ハードウェアの境界まで含めて、計測と仮説検証で原因を切り分けます。":
        "I isolate root causes by measuring and testing hypotheses — reading library source, checking OS settings, tracing communication, right down to the hardware boundary.",

    # --- WORK section ---
    "構想・試作・実機検証・本番運用を区別し、到達点を明記しています。公開できない受託案件は、社名と機密情報を伏せています。":
        "Each entry states clearly whether it's a concept, a prototype, hardware-verified, or in production. For client work that can't be disclosed, the company name and confidential details are withheld.",
    "AIを物理世界と接続させるMCPサーバーを用途毎に開発": "Building MCP servers, one per use case, to connect AI to the physical world",
    "MCPサーバー群": "MCP server suite",
    "AIクライアントからBLE機器、画面キャプチャ、複数デバイスのシリアルログ監視を呼び出せるようにするI/Oアダプタ。":
        "I/O adapters that let an AI client reach BLE devices, capture the screen, or monitor serial logs across multiple devices.",
    "実装範囲": "Implementation scope",
    "BLEのread/write/notify、画面・ウィンドウ取得、複数シリアルログの監視・要約、Web UI、stdio/HTTPの両トランスポートを実装。":
        "Implemented BLE read/write/notify, screen and window capture, multi-device serial log monitoring and summarization, a web UI, and both stdio and HTTP transports.",
    "● 日常的に使用中": "● In daily use",
    "AIエージェント向けTTS×リップシンク基盤": "TTS x lip-sync framework for AI agents",
    "Claude CodeなどのAI開発支援ツールに、MCP経由で声と3Dアバターの姿を与える。開発作業の進捗をTTS音声で読み上げる用途で日常的に使用。":
        "Gives AI dev-support tools like Claude Code a voice and a 3D avatar body, via MCP. Used daily to have TTS read out the progress of dev work.",
    "Tauri内蔵のMCPサーバー（音声一覧・発話・VRMAアニメーション再生など）、Azure Speech ServiceによるTTS、VRMアバターのリップシンク、Windows/macOS/Linux対応。":
        "An MCP server built into the Tauri app (list voices, speak, play VRMA animations, and more), TTS via Azure Speech Service, VRM avatar lip-sync, and Windows/macOS/Linux support.",
    "実機でEnd-to-End通信を確認": "End-to-end communication verified on real hardware",
    "Bluetooth PAN・低消費電力IoT通信": "Bluetooth PAN / low-power IoT communication",
    "標準スタックにないBNEP・PANを実装し、スマートフォン経由のインターネット接続を確立。周期補正と電流測定方法まで設計。":
        "Implemented BNEP/PAN, which isn't in the standard stack, to get internet access via a smartphone. Also designed the wake-cycle correction and current-measurement methodology.",
    "SDP、SSPペアリング、BNEP、DHCP、HTTPS通信を実機確認。deep sleep復帰周期のばらつきをEWMAで予測補正。":
        "Verified SDP, SSP pairing, BNEP, DHCP, and HTTPS communication on real hardware. Corrected deep-sleep wake-cycle jitter using EWMA prediction.",
    "サーバー／クライアント実装済み（統合検証前）": "Server and client implemented (integration testing pending)",
    "VRヘッドセットからのPC操作": "PC control from a VR headset",
    "Windowsアプリの画面をHEVCで送り、VR空間のパネルとして表示・操作するリモートデスクトップシステム。":
        "A remote-desktop system that streams a Windows app's screen over HEVC and displays it as a manipulable panel in VR space.",
    "GPU上のゼロコピーエンコード、UDP映像配信、入力注入、OpenXRレンダリング、6DoF操作、ハンドトラッキングまでを実装。":
        "Implemented zero-copy GPU encoding, UDP video delivery, input injection, OpenXR rendering, 6DoF manipulation, and hand tracking.",
    "● 本番稼働中": "● In production",
    "LINE用AIチャットボット": "AI chatbot for LINE",
    "自前サーバーで常時稼働。複数LLMの切替、Web検索・画像生成、管理画面を備え、実運用で起きた停止や表示崩れにも対応。":
        "Runs continuously on a self-hosted server. Supports switching between multiple LLMs, web search and image generation, and an admin panel — hardened against stalls and rendering glitches hit in real operation.",
    "Webhook、認証済み管理画面、OpenAI・xAI・Googleの切替、グループ内での選択的応答、Flex Messageとフォールバックを実装。":
        "Implemented the webhook, an authenticated admin panel, switching between OpenAI/xAI/Google, selective replies in group chats, and Flex Message rendering with a plain-text fallback.",
    "納品済み（受託・社名非公開）": "Delivered (client project, company name withheld)",
    "製造管理システムのデモ用生産ライン模型": "Production-line model for demoing a manufacturing management system",
    "製造管理システムのデモンストレーション用に、搬送・加工・組立・検査・良否判定・仕分けを卓上で再現した生産ライン模型。複数マイコンの役割分担と画像・色判定を統合。":
        "A tabletop production-line model built to demonstrate a manufacturing management system — reproducing conveyance, processing, assembly, inspection, pass/fail judgment, and sorting. Integrates role-split coordination across multiple MCUs with image- and color-based judgment.",
    "モーターPWM、PLCリレー通信、光電センサー、カメラ、カラーセンサー、サーボ制御、共通ライブラリ、引き継ぎ文書まで整備。":
        "Built out motor PWM control, PLC relay communication, photoelectric sensors, camera and color-sensor integration, servo control, a shared library, and handoff documentation.",

    # --- DEBUG / method section ---
    "成果物だけでなく、原因へたどり着く過程も技術支援の品質だと考えています。":
        "I consider the process of getting to a root cause — not just the deliverable — part of what makes technical support good.",
    "思い込みで直さず、": "Don't fix on a hunch —",
    "観測してから決める。": "observe first, then decide.",
    "遅いのはGPUではなかった": "It wasn't the GPU that was slow",
    "物体検出のカクつきを分離計測し、原因がカメラの自動露出だと特定。":
        "Isolated and measured stuttering in object detection, and traced the cause to the camera's auto-exposure.",
    "症状": "Symptom",
    "リアルタイム物体検出の映像がカクつく。": "Real-time object detection video was stuttering.",
    "判断": "Approach",
    "「モデル推論が重いはず」と決めず、GPU推論とカメラ供給を独立に実測。":
        "Instead of assuming \"the model inference must be heavy,\" measured GPU inference and camera frame delivery independently.",
    "計測": "Measurement",
    "USB帯域、センサー読み出し、ウォームアップ、ドライバ設定、レンズ汚れの仮説を個別に検証。":
        "Tested each hypothesis separately: USB bandwidth, sensor readout, warm-up time, driver settings, and a dirty lens.",
    "結論": "Conclusion",
    "GPUは推論能力の1/22しか使われておらず、必要なのはモデル最適化ではなく照明環境の改善だった。":
        "The GPU was using only 1/22 of its inference capacity — the fix needed wasn't model optimization, it was better lighting.",
    "サーボの不調はOS設定だった": "The servo problem was an OS setting",
    "配線やコードだけでなくPWMクロック管理まで調べて解消。": "Traced the issue past the wiring and code, into PWM clock management, and resolved it there.",
    "Raspberry Piにつないだサーボが指定角度どおりに動かない。": "A servo connected to a Raspberry Pi wasn't moving to the commanded angle.",
    "配線とコードに限定せず、OS側のPWMクロック管理まで調査。": "Instead of stopping at wiring and code, investigated the OS's PWM clock management as well.",
    "既定設定を切り分け、オーディオドライバとのハードウェアクロック競合を特定。": "Isolated the default settings and found a hardware clock conflict with the audio driver.",
    "設定変更で解消し、再発防止のため原因と対処をREADMEへ記録。": "Resolved with a configuration change, and documented the cause and fix in the README to prevent recurrence.",
    "同じパニック、毎回ちがう原因": "Same panic, a different cause each time",
    "ESP32のクラッシュを一括りにせず、独立した複数バグとして切り分け。": "Refused to treat the ESP32 crashes as one bug, and separated them into several independent ones.",
    "HTTPS通信中に同じパニック表示で繰り返しクラッシュ。": "Repeated crashes during HTTPS communication, always showing the same panic message.",
    "スタックサイズを増やす前に、残量ログとバックトレースを取る方針へ変更。": "Before just increasing the stack size, switched to logging remaining stack space and capturing backtraces.",
    "スタック監視、不要機能停止、ヒープ確保、バックトレース解析を順番に実施。": "Worked through stack monitoring, disabling unneeded features, freeing heap, and backtrace analysis in sequence.",
    "スタック圧迫、オブジェクト寿命、切断処理による不正解放を個別に特定・修正。": "Identified and fixed stack pressure, an object-lifetime issue, and an invalid free during disconnect handling — each a separate bug.",

    # --- Publications section ---
    "タイトル": "titles",
    "技術書の監訳・監修・編集（法人名義）": "Technical book translation, supervision, and editing (under the company's name)",
    "1990年代後半から2000年代初頭、PC・プログラミング関連書籍の監訳・監修・編集・執筆に携わりました。海外の複雑な技術を、日本の技術者が使える形へ翻訳・編集した経験は、現在の設計と開発にもつながっています。":
        "From the late 1990s to the early 2000s, I worked on translation supervision, technical supervision, editing, and writing for PC and programming books. Translating and editing complex technology from abroad into something Japanese engineers could actually use still shapes how I design and build today.",
    "このほか、個人名義で『Windows 95 バイブル』などの監修・監訳実績があります。": "In addition, under my own name, I supervised or translated titles including \"Windows 95 Bible.\"",
    "Windows 98 バイブル": "Windows 98 Bible",
    "監訳": "Supervising Translator",
    "インプレス": "Impress",
    "Windows 2000 Professional バイブル": "Windows 2000 Professional Bible",
    "詳説 Active Directory": "Active Directory (in depth)",
    "オライリー・ジャパン": "O'Reilly Japan",
    "ゲームクリエーターズバイブル": "Game Creators' Bible",
    "プロフェッショナル Java（上・下）": "Professional Java (Vol. 1 & 2)",
    "Java Studio 入門": "Introduction to Java Studio",
    "著": "Author",
    "ソフトバンク": "SoftBank Publishing",
    "法人名義29タイトルを表示": "Show all 29 titles under the company name",
    "Windows95ゲームプログラミング：DirectX入門（監訳、1997）": "Windows 95 Game Programming: Intro to DirectX (Supervising Translator, 1997)",
    "ゲームクリエーターズバイブル（監訳、2001）": "Game Creators' Bible (Supervising Translator, 2001)",
    "CGIパワフルテクニック大全集（監訳、1997）": "The Complete Guide to Powerful CGI Techniques (Supervising Translator, 1997)",
    "詳説Active Directory（監訳、2001）": "Active Directory (in depth) (Supervising Translator, 2001)",
    "Javaパワフルテクニック大全集（監訳、1997）": "The Complete Guide to Powerful Java Techniques (Supervising Translator, 1997)",
    "できる自作パソコン：Windows 98対応（編、1999）": "Build Your Own PC: Windows 98 Edition (Editor, 1999)",
    "できる自作パソコン：Windows Me/2000対応（編、2000）": "Build Your Own PC: Windows Me/2000 Edition (Editor, 2000)",
    "Perl 5パワフルテクニック大全集（監訳、1998）": "The Complete Guide to Powerful Perl 5 Techniques (Supervising Translator, 1998)",
    "Visual Basic 4パワフルテクニック大全集 v.2（監訳、1996）": "The Complete Guide to Powerful Visual Basic 4 Techniques, Vol. 2 (Supervising Translator, 1996)",
    "Windows 95/98/NTのための高速3Dグラフィックス（訳、1999）": "High-Speed 3D Graphics for Windows 95/98/NT (Translator, 1999)",
    "プロフェッショナルJava 上（監訳、2001）": "Professional Java, Vol. 1 (Supervising Translator, 2001)",
    "プロフェッショナルJava 下（監訳、2001）": "Professional Java, Vol. 2 (Supervising Translator, 2001)",
    "C#言語リファレンスblack book（監修、2002）": "C# Language Reference Black Book (Supervising Editor, 2002)",
    "C#実践プログラミング（監修、2001）": "Practical C# Programming (Supervising Editor, 2001)",
    "C++パワフルテクニック大全集（監訳、1999）": "The Complete Guide to Powerful C++ Techniques (Supervising Translator, 1999)",
    "C++ MIDIプログラミング（監訳、1999）": "C++ MIDI Programming (Supervising Translator, 1999)",
    "DirectX 3Dゲームプログラミング入門（監訳、2000）": "Introduction to DirectX 3D Game Programming (Supervising Translator, 2000)",
    "DirectX 5ゲームプログラミング入門（監訳、1998）": "Introduction to DirectX 5 Game Programming (Supervising Translator, 1998)",
    "Java Studio入門（著、1998）": "Introduction to Java Studio (Author, 1998)",
    "Linux全書（監訳、2000）": "The Complete Book of Linux (Supervising Translator, 2000)",
    "Webページサウンドテクニック（監訳、1998）": "Web Page Sound Techniques (Supervising Translator, 1998)",
    "Windows 2000 Professionalバイブル（監訳、2000）": "Windows 2000 Professional Bible (Supervising Translator, 2000)",
    "Windows 2000 Professionalネットワーキングバイブル（監訳、2000）": "Windows 2000 Professional Networking Bible (Supervising Translator, 2000)",
    "Windows 98シークレット（監修、1998）": "Windows 98 Secrets (Supervising Editor, 1998)",
    "Windows 98チューニングblack book（監修、1999）": "Windows 98 Tuning Black Book (Supervising Editor, 1999)",
    "Windows 98バイブル（監訳、1998）": "Windows 98 Bible (Supervising Translator, 1998)",
    "Windows 98バイブルプロフェッショナル（監訳、1998）": "Windows 98 Bible, Professional Edition (Supervising Translator, 1998)",
    "Windows 98レジストリblack book（監修、1999）": "Windows 98 Registry Black Book (Supervising Editor, 1999)",
    "Windows NT server 4ネットワークバイブル（1997）": "Windows NT Server 4 Network Bible (1997)",

    # --- About section ---
    "経歴と、いまの関心": "Background & Current Interests",
    "最初期には、Apple II向けアニメーションソフト「Fantavision」のPC-9801移植で、アセンブリ言語によるアニメーション生成エンジンを手がけました。そこから技術書の監訳・監修、組み込み、産業設備の実証機、モバイルアプリ、AIエージェントまで。領域を限定するより、複雑な技術を理解し、検証し、他者が使える形へ変換する仕事を続けてきました。現在は特に、AIをチャット画面の中に閉じず、OS・デバイス・センサー・開発環境へ接続することに関心があります。":
        "My earliest technical work was porting Fantavision — an Apple II animation program — to the PC-9801, building the assembly-language animation-generation engine. From there: translation-supervising and technical-supervising books, embedded systems, industrial demonstrator hardware, mobile apps, and AI agents. Rather than stay in one domain, I've kept doing the same underlying work — understanding complex technology, verifying it, and turning it into something other people can use. Right now I'm especially interested in connecting AI to the OS, devices, and sensors, instead of leaving it confined to a chat window.",
    "AIエージェントと実世界の接続": "Connecting AI agents to the physical world",
    "MCPなどを介し、AIに機器・OS機能・業務システムを操作させる仕組み。": "Mechanisms — MCP and similar — that let AI operate devices, OS functions, and business systems.",
    "クラウドに依存しない推論": "Cloud-independent inference",
    "端末内で完結するLLM実行。通信・アカウント・外部APIへの依存を減らす設計。": "Running LLMs entirely on-device, designed to reduce dependence on connectivity, accounts, and external APIs.",
    "実測にもとづく低消費電力通信": "Low-power communication grounded in real measurement",
    "省電力モードの実挙動を測り、カタログ値ではなく実測から設計すること。": "Measuring how power-saving modes actually behave, and designing from those measurements rather than datasheet numbers.",

    # --- Timeline section ---
    "開発活動の年表": "Development Activity Timeline",
    "2024年10月から現在まで、macOS/Windows両方の作業環境に残る記録（gitコミット履歴・README・作業ログ）に加え、GitHub上の個人・cami org（自社チーム）リポジトリの活動を突き合わせて時系列に並べたものです。書籍の監修・監訳からAI・組み込みへ続く関心の流れが、直近2年で密度を増していることがわかります。":
        "From October 2024 to the present, cross-referencing records left in both macOS and Windows working environments (git commit history, READMEs, work logs) with activity on GitHub — personal repos and the cami org (my own team's repos) — laid out chronologically. It shows a throughline from book supervision/translation to AI and embedded work, growing markedly denser over the last two years.",
    "Kaz Sato — ソフトウェア開発アクティビティ年表": "Kaz Sato — Software Development Activity Timeline",
    "~/Work ディレクトリ（macOS/Windows）+ GitHub（個人・cami org）の解析結果より作成（2024年10月 〜 2026年9月）":
        "Built from ~/Work directories (macOS/Windows) + GitHub (personal + cami org) (October 2024 – September 2026)",
    "カテゴリ:": "Category:",
    "AI協働基盤 / MCP": "AI Collaboration / MCP",
    "VR・3D・フォトグラメトリ": "VR / 3D / Photogrammetry",
    "組み込み / IoT": "Embedded / IoT",
    "デスクトップ/モバイルアプリ": "Desktop / Mobile Apps",
    "音声・音楽・ゲーム": "Audio / Music / Games",
    "その他": "Other",
    "2024年": "2024",
    "検出処理を試作するNode.jsツール": "Node.js tool prototyping a detection process",
    "sIoTamago ボード開発": "sIoTamago board bring-up",
    "nRF52840カスタムボード「sIoTamago」のZephyr/Arduinoボード定義一式を作成": "Built a full set of Zephyr/Arduino board definitions for the nRF52840-based \"sIoTamago\" custom board",
    "2025年": "2025",
    "モータ制御試作（BLE）": "Motor control prototype (BLE)",
    "Flutter+BLE特性経由でモータ/バイブレータの制御パラメータを送信": "Sending motor/vibration control parameters over a Flutter app via BLE characteristics",
    "暗号化ストレージ付きの安全なURL管理デスクトップアプリ": "A secure URL-management desktop app with encrypted storage",
    "WebSocketによるリアルタイム音声配信 + AIチャット": "Real-time audio streaming over WebSocket + AI chat",
    "配管内カメラ・BLE転送試作": "In-pipe camera / BLE transfer prototype",
    "ESP32でJPEG撮影しBLE経由でスマホへ転送する仕組みと専用アプリ": "An ESP32 setup that captures JPEG images and transfers them to a phone over BLE, plus a companion app",
    "Pico4 VR実験": "Pico 4 VR experiments",
    "WaylandTerm・guacaspaceなどPico4上でのVR UI検証": "VR UI experiments on the Pico 4 — WaylandTerm, guacaspace, and others",
    "WaterWars 水位監視プロトタイプ": "WaterWars water-level monitoring prototype",
    "SX1262 LoRa+超音波水位センサーによる長距離無線水位監視システムの初期プロトタイプ": "An early prototype of a long-range wireless water-level monitoring system using SX1262 LoRa and an ultrasonic sensor",
    "超音波センサー": "ultrasonic sensor",
    "ESP32 / LoRa (SX1262) / 超音波センサー": "ESP32 / LoRa (SX1262) / Ultrasonic sensor",
    "Python / VRM・glTF / Blender": "Python / VRM & glTF / Blender",
    "配管内フォトグラメトリ基盤": "In-pipe photogrammetry pipeline",
    "ESP32魚眼カメラ撮影 + OpenGL/GLFWによる可視化ツール群": "ESP32 fisheye camera capture plus an OpenGL/GLFW visualization toolset",
    "OAuth2認証+PIN暗号化によるセキュアURL共有システム": "A secure URL-sharing system with OAuth2 auth and PIN encryption",
    "VS Code拡張機能としてのAIコーディング支援・vibe-coding用チャットツール試作": "Prototyping an AI coding-assist / vibe-coding chat tool as a VS Code extension",
    "自律水中機（AUV）向けのBlenderベースチェックツール": "A Blender-based check tool for an autonomous underwater vehicle (AUV)",
    "組み込みボード開発（Mira Station）": "Embedded board bring-up (Mira Station)",
    "nRF5340/nRF7002カスタムボードのデバイスツリー調整、WiFi接続不良の原因特定": "Device-tree tuning for an nRF5340/nRF7002 custom board; tracked down the cause of a WiFi connectivity fault",
    "2026年": "2026",
    "VRM 3Dエージェントが伴走するADHD支援ボディダブリングアプリ": "An ADHD body-doubling app with a companion VRM 3D agent",
    "AI生成+TTSによる英語⇄日本語リスニング学習プラットフォーム": "An English↔Japanese listening-practice platform using AI generation + TTS",
    "tmux上で複数のClaude Codeインスタンスを階層構造で並列稼働させるオーケストレーション基盤": "An orchestration framework running multiple Claude Code instances in a hierarchy, in parallel, inside tmux",
    "MCPサーバー基盤 第1弾": "MCP server suite, first wave",
    "serial-monitor・web-search — AIに物理I/Fを与えるMCPサーバー": "serial-monitor and web-search — MCP servers giving AI a physical interface",
    "GPSテレメトリを送るLoRa P2Pセンサー⇄ゲートウェイ通信の実装、Webダッシュボードサーバー": "Implemented LoRa point-to-point sensor↔gateway communication carrying GPS telemetry, plus a web dashboard server",
    "3Dボードゲーム試作": "3D board game prototype",
    "Tank/Archer/Healer/Casterのアイソメトリック3Dボードゲーム": "An isometric 3D board game with Tank/Archer/Healer/Caster roles",
    "MCPサーバー基盤 第2弾": "MCP server suite, second wave",
    "bluetooth-helper・screen-capture — BLEと画面をAIに開放": "bluetooth-helper and screen-capture — opening up BLE and the screen to AI",
    "組み込みハード拡張": "Embedded hardware, expanded",
    "BLE HIDフットスイッチ、nRF52 BSP、Rust製Windows IME切替": "A BLE HID foot switch, an nRF52 BSP, and a Rust-based Windows IME switcher",
    "TTS×リップシンク基盤": "TTS × lip-sync framework",
    "AIが操作するTTS発話+3Dアバターのリップシンク実験（継続開発）": "Experiments in AI-driven TTS speech with 3D avatar lip-sync (ongoing)",
    "vrws（VR Window Stream）": "vrws (VR Window Stream)",
    "Windows画面をH.265でVRヘッドセットへストリーミングし操作するシステム": "A system that streams a Windows screen over H.265 to a VR headset and allows controlling it there",
    "photogramet": "photogramet",
    "配管内部フォトグラメトリ用COLMAP連携C++ GUIアプリ": "A C++ GUI app integrating COLMAP for in-pipe photogrammetry",
    "soundvisualizer": "soundvisualizer",
    "システム音声をFFT解析するプラグイン対応デスクトップビジュアライザ": "A plugin-capable desktop visualizer that runs FFT analysis on system audio",
    "WaterWars×Meshtastic統合": "WaterWars × Meshtastic integration",
    "オープンソースLoRaメッシュ通信ファームウェアをフォークし、位置情報を水位監視スキーマでゲートウェイ送信するww-gateway-nodeを追加。多層的に絡み合ったクラッシュ原因を段階的に切り分け":
        "Forked an open-source LoRa mesh firmware and added ww-gateway-node, which relays position data to the gateway as water-level-monitoring schema. Untangled a multi-layered crash by isolating its causes one at a time.",
    "sIoTamago ベアメタルアセンブリ検証": "sIoTamago bare-metal assembly experiments",
    "ブートローダーを使わずアセンブリ言語のみでLED点滅・RAM/Flashメモリテストを実装": "LED blink and RAM/flash memory tests written entirely in assembly, with no bootloader",
    "Kintone REST API連携の工数集計・請求書自動生成デスクトップアプリ": "A desktop app that tallies work hours via the Kintone REST API and auto-generates invoices",
    "産業ライン実証設備開発": "Industrial-line demonstrator hardware",
    "複数マイコン協調によるコンベア搬送〜検査〜仕分けの卓上実証設備": "A tabletop demonstrator, coordinated across multiple MCUs, covering conveyor transport through inspection and sorting",
    "RSS記事フィルタリング処理の不具合修正、ニュースキャッシュ基盤の整備": "Fixed a bug in RSS article filtering; built out a news-caching layer",
    "ニュース記事を起点にAIが話しかけてくるパーソナルニュースチャット": "A personal news chat where the AI opens the conversation, prompted by the day's articles",
    "複数のClaude Codeセッションの状態・進捗・ツール実行履歴をブラウザからリアルタイム監視するダッシュボード": "A dashboard for watching multiple Claude Code sessions' status, progress, and tool-call history in real time from a browser",
    "4役割のLLMエージェントがweb検索しながら討論するプラットフォーム": "A platform where four LLM agents, each with a distinct role, debate while searching the web",
    "2Dアイソメトリック・リアルタイム戦闘のアクションRPGテンプレート": "A 2D isometric action-RPG template with real-time combat",
    "Claude Codeのフックイベントを発光球体アニメーションとして可視化するデスクトップアプリ": "A desktop app that visualizes Claude Code hook events as a glowing, animated sphere",
    "LINE Messaging APIでAIが個人・グループチャットに応答する本番稼働ボット": "A bot in production, using the LINE Messaging API, where AI responds in both 1:1 and group chats",
    "ESP32 Bluetooth PAN / QSPI液晶 / テザリング": "ESP32 Bluetooth PAN / QSPI display / tethering",
    "BTstack採用のBluetooth PAN実装、QSPI液晶ネイティブドライバ、マルチボードWi-Fiテザリング": "A Bluetooth PAN implementation built on BTstack, a native QSPI-display driver, and multi-board WiFi tethering",
    "LLMに骨格のみ生成させメッシュ/リギングは決定的処理で行うVRM生成パイプライン": "A VRM-generation pipeline where the LLM only generates the skeleton, and mesh/rigging are handled deterministically",
    "YOLO物体検出・姿勢推定のLinux/macOS実機性能比較検証": "Comparing real-hardware performance of YOLO object detection and pose estimation on Linux vs. macOS",
    "bandbox（継続中）": "bandbox (ongoing)",
    "演奏テーマを解析しリアルタイム伴奏を生成するシステム": "A system that analyzes a musical theme and generates real-time accompaniment",
    "ボタン押下でnRF52840がiBeaconアドバタイズし、Flutterアプリがバックグラウンド検知するmonorepo": "A monorepo where a button press makes an nRF52840 advertise as an iBeacon, detected in the background by a Flutter app",
    "bandbox用USB HIDフットスイッチコントローラー、音楽生成マルチエージェント実験のRustアプリ化": "A USB HID foot-switch controller for bandbox, and turning a multi-agent music-generation experiment into a Rust app",
    "小規模プロトタイプ群": "Small prototypes",
    "技術書監修支援アプリ、rPPG心拍・表情推定の設計検討、Rust製テキストエディタなど": "A technical-book-supervision support app, a design study on rPPG heart-rate/expression estimation, a Rust text editor, and more",
    "植物・草食動物・肉食動物からなる3D生態系シミュレーション（土壌栄養循環・水・捕食関係）": "A 3D ecosystem simulation of plants, herbivores, and carnivores (soil nutrient cycling, water, predation)",
    "戦争・海運チョークポイント・金価格・暗号資産・為替データを組み合わせた為替レート予測プロトタイプ（現時点で実売買は未実装）":
        "An FX-rate prediction prototype combining war, shipping-chokepoint, gold-price, crypto, and exchange-rate data (does not execute real trades yet)",

    # --- Contact section ---
    "研究・構想の段階から": "From the research-and-concept stage",
    "ご相談いただけます。": "onward — feel free to reach out.",
    "「まだ何を頼めばよいか分からない」「検証方法から相談したい」という段階でも構いません。":
        "It's fine if you're still at the \"I'm not sure what to even ask for\" stage, or want to talk through how to verify something before starting.",

    # --- meta/aria attributes (not visible body text, but translatable) ---
    "メインナビゲーション": "Main navigation",
    "モバイルナビゲーション": "Mobile navigation",
    "プロフィール概要": "Profile summary",
    "AI、組み込み、デバイス、Webを横断し、研究アイデアや技術構想を検証できるソフトウェアと試作機へ落とし込みます。":
        "Working across AI, embedded systems, devices, and the web, turning research ideas and technical concepts into testable software and working prototypes.",
    "研究アイデアや技術構想を、検証できるソフトウェアと試作機へ。": "Turning research ideas and technical concepts into testable software and working prototypes.",

    # language-switcher option labels: language names are shown in their own
    # script on both pages, so this is an intentional identity mapping.
    "日本語": "日本語",
    "Language / 言語": "Language / 言語",
}

ALT_TRANSLATIONS = {
    "MCPサーバー群のビジュアル": "Illustration of the MCP server suite",
    "AIエージェント向けTTS×リップシンクアバターのビジュアル": "Illustration of the TTS x lip-sync avatar framework for AI agents",
    "Bluetooth PAN・低消費電力IoT通信のビジュアル": "Illustration of Bluetooth PAN / low-power IoT communication",
    "VRヘッドセットからのPC操作のビジュアル": "Illustration of PC control from a VR headset",
    "LINE用AIチャットボットのビジュアル": "Illustration of an AI chatbot for LINE",
    "製造管理システムのデモ用生産ライン模型のビジュアル": "Illustration of the production-line model for demoing a manufacturing management system",
    "技術書・翻訳・編集実績を表す出版ビジュアル": "Illustration representing technical book translation and editing work",
}
