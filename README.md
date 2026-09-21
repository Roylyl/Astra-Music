<div align="center">

# 晚渡 · WANDU

### 原创叙事民谣 / 独立摇滚器乐编曲工程

完整 FL Studio 工程、九声部 MIDI、可复现的 MIDI 生成源文件与立体声试听。

<img src="assets/screenshots/02-arrangement.png" alt="《晚渡》在 FL Studio 中的完整播放列表排列" width="760">

[![Release](https://img.shields.io/github/v/release/Roylyl/Astra-Music?display_name=tag&include_prereleases&style=flat-square&label=release)](https://github.com/Roylyl/Astra-Music/releases)
[![Downloads](https://img.shields.io/github/downloads/Roylyl/Astra-Music/total?style=flat-square&label=downloads)](https://github.com/Roylyl/Astra-Music/releases)
[![Stars](https://img.shields.io/github/stars/Roylyl/Astra-Music?style=flat-square)](https://github.com/Roylyl/Astra-Music/stargazers)
[![Forks](https://img.shields.io/github/forks/Roylyl/Astra-Music?style=flat-square)](https://github.com/Roylyl/Astra-Music/forks)
[![Open Issues](https://img.shields.io/github/issues/Roylyl/Astra-Music?style=flat-square)](https://github.com/Roylyl/Astra-Music/issues)
[![Last Commit](https://img.shields.io/github/last-commit/Roylyl/Astra-Music?style=flat-square)](https://github.com/Roylyl/Astra-Music/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/Roylyl/Astra-Music?style=flat-square)](https://github.com/Roylyl/Astra-Music)

[试听与下载](#试听与下载) · [作品说明](#关于作品) · [配器](#配器) · [曲式](#曲式) · [快速开始](#快速开始) · [可复现-midi](#可复现-midi) · [工程核验](#工程与轨道核验) · [许可说明](#许可与第三方依赖)

</div>

## 项目概览

《晚渡》是一首以叙事民谣与独立摇滚为方向的原创器乐编曲。原声吉他铺开和声，小号承担原本人声的位置，弦乐与长号在后半段逐渐加入。

项目使用 FL Studio 制作，仓库保留完整工程、九个声部的钢琴卷帘 MIDI、完整多轨 MIDI、立体声试听、曲目清单，以及可复现 MIDI 的 Python 源文件。仓库中的 FL Studio 工程、MIDI、清单与试听共同构成当前公开版本；Python 脚本只负责生成 MIDI 与清单，不会生成配置好音源的 FLP 或渲染音频。

**88 BPM · E 小调 · 4/4 拍 · 96 小节 · 约 4 分 28 秒（含尾音）**

## 试听与下载

- [在线试听 / 下载 M4A](试听/晚渡.m4a)
- [下载 FL Studio 工程](晚渡.flp)
- [下载完整多轨 MIDI](MIDI/Wandu_Full_Arrangement.mid)
- [浏览九个独立声部 MIDI](MIDI/)

> M4A 为当前仓库提供的试听版本。96 kHz / 24-bit WAV 是本地导出与核验文件，未包含在仓库中。

## 核心内容

- **可编辑工程：** 根目录提供完整的 `晚渡.flp`，保留播放列表、九个乐器通道、混音器路由及时间标记。
- **可迁移编曲：** 提供一个完整多轨 MIDI 和九个独立声部 MIDI，可导入其他 DAW 后重新分配音源。
- **可复现素材：** `制作源文件/compose_wandu.py` 使用 Python 标准库和固定随机种子生成 MIDI 与 `score_manifest.json`。
- **制作记录：** 三张截图记录需求、工程排列与右侧钢琴复核过程；最终状态以本 README 和根目录工程为准。
- **明确的验证范围：** 仓库记录工程、MIDI、路由和波形核验结果，但不将这些技术检查表述为人工听音母带审定。

## 关于作品

作品完成于 **2026 年 9 月 10 日**。创作方向参考 Apple Music「鹿」歌单中的宋冬野《郭源潮（2026 Version）》、声音玩具《你的城市》《没有人能够比我们更接近对方》、谢天笑《向阳花》，以及李志、五条人等艺人的音乐。由这些收藏所呈现的叙事感与乐队编制，确定了克制的主歌、逐渐展开的副歌，以及回落的尾奏。参考用于确定风格与配器，旋律和 MIDI 为本项目重新创作。

本曲没有人声录音。小号演奏主旋律，乐句之间保留呼吸空隙；最终副歌加入长号和声，形成铜管之间的呼应。吉他、贝斯、键盘与鼓组均由 MIDI 驱动音源演奏。

本项目由作者提出审美方向与制作要求，结合 Codex 辅助完成作曲、MIDI 编排、工程整理与文件核验。

## 配器

全部声部使用 **FLEX / General MIDI Library**，各自对应独立的样式、钢琴卷帘和混音器轨。

| 轨道 | 实际音色 | 编曲作用 |
| --- | --- | --- |
| 01 原声吉他 | Steel Guitar | 分解和弦，副歌增加扫弦；起音和力度保留细微变化 |
| 02 原声钢琴 | Acoustic Piano | 主歌回应与副歌和弦，声像略偏右 |
| 03 指弹贝斯 | Electric Finger Bass | 主歌延音支撑，副歌增加五度与八度行进 |
| 04 小号 | Trumpet | 代替人声的主旋律 |
| 05 清音电吉他 | Electric Guitar Clean | 高音回应与节奏补充 |
| 06 弦乐 | Strings 1 | 预副歌、桥段与副歌的持续和声 |
| 07 长号 | Trombone | 最终副歌的铜管和声 |
| 08 原声鼓组 | Drum Standard Kit | 主歌边击、副歌军鼓，句末通鼓加花 |
| 09 电钢琴 | Electric Piano 1 | 第二主歌、桥段与最终副歌的和声铺底 |

## 曲式

时间按 88 BPM 计算并取近似值。

| 段落 | 小节 | 起始时间 |
| --- | --- | --- |
| 前奏 | 1–8 | 0:00 |
| 主歌 A | 9–24 | 0:22 |
| 预副歌 | 25–32 | 1:05 |
| 副歌 A | 33–48 | 1:27 |
| 间奏 | 49–56 | 2:11 |
| 主歌 B | 57–64 | 2:33 |
| 桥段 | 65–72 | 2:55 |
| 最终副歌 | 73–88 | 3:16 |
| 尾奏 | 89–96 | 4:00 |

乐谱长度约 4:22，完整混音保留混响尾音后约为 4:28。

## 快速开始

### 在 FL Studio 中打开完整工程

1. 使用 FL Studio 打开根目录的 [`晚渡.flp`](晚渡.flp)。本项目在 **macOS / Apple Silicon 的 FL Studio 2026（26.1.3）** 中完成打开、播放、保存和导出验证；其他版本尚未验证。
2. 确认 FLEX 中可以加载 **General MIDI Library**。音色库需由使用者通过自己的 FL Studio 安装获取，项目文件不包含音色库本体。
3. 切换到 **SONG** 模式，从第 1 小节播放完整编曲。
4. 在对应样式的钢琴卷帘中编辑音符。播放列表中的时间标记对应上表曲式，混音器轨 1–9 与配器表一一对应。

### 在其他 DAW 中使用 MIDI

也可以将 [`Wandu_Full_Arrangement.mid`](MIDI/Wandu_Full_Arrangement.mid) 导入其他 DAW，并按配器表重新分配音源。MIDI 不包含音色与完整混音设置，替换音源后声音会有所不同。

## 文件结构

```text
.
├── README.md
├── 晚渡.flp                         # 完整 FL Studio 工程
├── MIDI/
│   ├── Wandu_Full_Arrangement.mid    # 完整多轨 MIDI
│   └── ...                          # 九个独立声部 MIDI
├── 试听/
│   └── 晚渡.m4a                     # AAC 立体声试听
├── assets/
│   └── screenshots/                 # 制作过程截图
├── 制作源文件/
│   └── compose_wandu.py             # MIDI 生成源文件
└── score_manifest.json              # 速度、曲式与音符数量
```

本地制作目录另有 `备份/`，用于保存历史版本和隔离核验工程；主工程入口是根目录的 `晚渡.flp`。

96 kHz / 24-bit WAV 是本地导出与核验文件，当前仓库提供 M4A 试听，未包含 WAV。

## 仓库维护

正式提交包括根目录的 FL Studio 工程、`MIDI/`、`试听/`、制作源文件、`score_manifest.json`、截图与文档。更新编曲后应同步核对工程、MIDI、清单和试听，避免版本不一致；新增正式 WAV 等交付文件时也应保持可跟踪。

历史工程、自动备份和隔离核验副本放在根目录的 `备份/` 或 `Backup/`；临时工程可使用 `.flp.bak`、`.flp.tmp` 后缀。这些文件、Python 字节码／虚拟环境、系统及编辑器缓存由仓库的 `.gitignore` 排除，不提交；规则不会统一忽略 `.flp`、`.mid` 或音频文件。

提交前在仓库根目录检查：

```sh
git status --short
git diff --check
git diff --cached --stat
# 禁用个人全局规则，检查仓库自身的忽略配置。
git -c core.excludesFile=/dev/null check-ignore -v .DS_Store 制作源文件/__pycache__/compose_wandu.pyc 备份/晚渡.flp
# 正常应无输出：不能让正式的已跟踪文件落入忽略规则。
git -c core.excludesFile=/dev/null ls-files --cached --ignored --exclude-standard
```

## 可复现 MIDI

[`compose_wandu.py`](制作源文件/compose_wandu.py) 使用 Python 标准库生成 MIDI，并固定随机种子以复现力度与起音的微小变化。

### 生成步骤

运行前，将脚本顶部的 `OUT` 改为自己的输出目录。该变量当前包含作者本机的绝对路径，因此必须先修改；建议指向一个新建的空目录，并预先创建其中的 `MIDI` 子目录，再执行：

```bash
python3 制作源文件/compose_wandu.py
```

脚本输出 MIDI 及曲目清单，不会自动生成配置好 FLEX 音源的 FLP，也不会渲染音频；需要继续编辑最终编曲时，直接打开已有工程即可。

### 产物关系

```text
compose_wandu.py
├── MIDI/Wandu_Full_Arrangement.mid   # 10 轨：指挥轨 + 9 个声部
├── MIDI/01...09 *.mid                 # 每个声部的独立 MIDI
└── score_manifest.json                # 速度、曲式与音符数量

上述 MIDI ──手动导入与配置音源──> 晚渡.flp ──FL Studio 导出──> 试听/晚渡.m4a
```

这里的“可复现”仅指脚本生成的 MIDI 数据与清单。FL Studio 工程内的 FLEX 音源选择、路由、播放列表编排和混音设置需要在 DAW 中维护，不由脚本自动创建。

## 工程与轨道核验

核验于 2026 年 9 月 10 日完成。最终工程已在 FL Studio 中重新打开并原生保存，九个乐器均处于启用状态。

### MIDI 与路由

九个声部共 **3,867 个音符**。最终工程的音高、力度，以及换算到工程 PPQ 96 后的起音位置，与源 MIDI 对应。九个样式分别且仅引用自己的乐器通道，播放列表片段均从第 1 小节对齐，各声部依照曲式进入和退出，完整编曲覆盖 96 小节。

| 声部 | 混音器轨 | 通道声像约 | 音符数 |
| --- | --- | --- | --- |
| 原声吉他 | 1 | 左 39.1% | 1,400 |
| 原声钢琴 | 2 | 右 15.6% | 457 |
| 指弹贝斯 | 3 | 中央 | 218 |
| 小号 | 4 | 中央 | 227 |
| 清音电吉他 | 5 | 右 42.2% | 220 |
| 弦乐 | 6 | 左 18.8% | 144 |
| 长号 | 7 | 右 18.8% | 23 |
| 原声鼓组 | 8 | 中央 | 1,082 |
| 电钢琴 | 9 | 左 53.1% | 96 |

所有音符自身的声像均为中央，上表位置来自乐器通道的声像设置。百分比表示旋钮位置，不等于左右声道的音量比例。

### 右侧钢琴核验

第 2 声部使用 **Acoustic Piano**，第 9 声部使用 **Electric Piano 1**。原声钢琴的 457 个音符全部对应第 2 乐器通道及第 2 混音器轨，没有分配给电钢琴或其他乐器。

原声钢琴通道声像值为 7400，中央值为 6400，即约偏右 15.6%；第 2 混音器轨的额外声像保持中央。在 FL Studio 中隔离该声部并原生导出后：

- 左右声道均有声音输出，整段 RMS 右声道比左声道高约 **4.30 dB**。
- 左右声道的线性采样峰值分别约为 **0.1373 / 0.2306**，未检测到满刻度削波。
- 旧工作名称 `Felt Piano` 已修正为 `Acoustic Piano`，并同步到通道名、样式名、MIDI 轨道名与源文件。此次修正只涉及命名，完整混音仍与当前工程对应。

核验时曾截取第 **33–40 小节**的钢琴独奏，保留原声像，约 22 秒，对应完整混音的 **1:27–1:49**；该临时片段未包含在当前文件目录中。本地 `备份/Wandu_Piano_Audit.flp` 为隔离钢琴的核验副本；完整编曲使用根目录的 `晚渡.flp`。

### 音频输出与制作范围

完整 WAV 由 FL Studio 原生导出，规格为 **96 kHz / 24-bit / 立体声**。乐谱长度为 **261.818 秒**，保留混响尾音后的音频长度为 **267.557 秒**。各曲式段落均有声音输出，整曲采样峰值约 **−3.25 dBFS**，未检测到满刻度削波。

项目完成了原创作曲、完整 MIDI 编排、现有音源分配以及基础电平和声像设置。前奏、主歌、桥段、最终副歌和尾奏保留不同动态；声音表现以 FLEX / General MIDI Library 为基础，没有录制真实乐手或人声。

以上为文件、路由与波形核验结果，不代表经过人工听音母带审定，听感以实际播放为准。

## 制作过程截图

以下截图按制作顺序记录了需求提出、工程排列和钢琴复核。截图中的“尚未完成”、临时文件名及独立说明文档链接属于当时状态；最终工程与合并后的说明以本 README 为准。

### 1. 创作需求与首轮 MIDI 编排

从收藏歌单确定风格，完成九个声部的 MIDI，并将音源载入 FL Studio。

<p align="center">
  <img src="assets/screenshots/01-composition.png" alt="创作需求与首轮 MIDI 编排记录" width="720">
</p>

### 2. 原生片段与播放列表排列

制作过程中通过手动放入并保存一个原生片段，继续完成当前 FL Studio 版本下的播放列表排列。

<p align="center">
  <img src="assets/screenshots/02-arrangement.png" alt="原生片段与播放列表排列过程" width="820">
</p>

### 3. 右侧钢琴与轨道对应复核

对钢琴的音色、MIDI、混音器路由及左右声道进行复核，并修正音色名称。

<p align="center">
  <img src="assets/screenshots/03-piano-review.png" alt="右侧钢琴与九轨对应关系复核结果" width="680">
</p>

## 项目状态

当前公开版本以 `main` 分支中的根目录工程、MIDI、试听、`score_manifest.json` 和本 README 为同一组交付物。最近一次记录的完整工程核验完成于 **2026 年 9 月 10 日**；验证环境为 **macOS / Apple Silicon、FL Studio 2026（26.1.3）**。其他操作系统、处理器架构与 FL Studio 版本尚未验证。

顶部 Release 与 Downloads 徽章读取 GitHub 的实时公开数据；下载量只统计 GitHub Release 附件，不包含源码 ZIP、克隆、M4A 的页面访问或本地文件复制。如果仓库尚未创建 Release，徽章会相应显示无版本或零下载。

如果只需要收听作品，可直接使用 M4A；如果需要编辑音符或迁移到其他 DAW，优先使用 MIDI；如果需要复现当前音源、播放列表和混音路由，应打开 FL Studio 工程并确保本机已安装 FLEX / General MIDI Library。

## 隐私与安全

- 仓库内容是本地音乐工程、MIDI、音频、图片、JSON 和一个 Python 生成脚本，不包含服务端组件、账号登录、遥测或数据上传逻辑。
- `compose_wandu.py` 使用 Python 标准库，并将产物写入脚本顶部 `OUT` 指定的本地目录。运行前应检查并修改该绝对路径，避免写入错误位置。
- FL Studio 工程和试听文件属于二进制资产。合并外部修改前，建议核对文件来源，并在 DAW 中重新打开、播放和导出验证。

## 许可与第三方依赖

本仓库目前**未提供开源许可证文件**。公开可访问不等于获得复制、修改、再发布或商业使用授权；如需超出 GitHub 正常浏览与个人评估范围使用本作品或工程，请先取得作者许可。

FLEX / General MIDI Library 不随仓库分发。使用 FL Studio 工程时，需由使用者通过自己的 FL Studio 安装和相应许可取得所需音色库。仓库内提及的音乐人和作品仅用于说明创作参考方向，不代表其参与、认可或授权本项目；本项目旋律和 MIDI 为重新创作。

## 贡献与问题反馈

欢迎通过 [Issues](https://github.com/Roylyl/Astra-Music/issues) 报告文件缺失、工程兼容性、MIDI 对应、路由或文档问题，也可以通过 Pull Request 提交可审阅的修正。涉及 `晚渡.flp`、MIDI、试听或 `score_manifest.json` 的修改，请说明变更范围，并同步更新所有受影响的交付物与核验记录。
