import os

style_path = os.path.join(os.getcwd(), 'assets', 'css', 'style.css')

with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Expand max-width to 1320px
css = css.replace('max-width: 960px;', 'max-width: 1320px;')

# 2. Add inline code styling if not exists
code_style = """
code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
  font-size: 0.88em;
  background: var(--gy);
  color: var(--tx);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid var(--bd);
  word-break: break-word;
}
"""

if 'code {' not in css:
    css = css.replace('body {', code_style.strip() + '\n\nbody {')

# 3. Enhance .cols, .col, .colt, .pi and add specialized cheat sheet styling
old_pi_block = """.pi {
  font-size: 12px;
  padding: 6px 10px;
  border-radius: 6px;
  margin-bottom: 6px;
  border: 1px solid var(--bd);
  background: var(--sub);
}

.pi b {
  display: block;
  font-weight: 600;
  margin-bottom: 2px;
}

.pi span {
  color: var(--mu);
  font-size: 11px;
  line-height: 1.5;
}"""

# Also handle CRLF if needed
new_pi_block = """.cols {
  display: flex;
  gap: 16px;
  align-items: stretch;
}

.col {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.colt {
  font-size: 12px;
  font-weight: 700;
  color: var(--tx);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 2px solid var(--bd);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.pi {
  font-size: 13px;
  padding: 12px 14px;
  border-radius: 8px;
  margin-bottom: 10px;
  border: 1px solid var(--bd);
  background: var(--card);
  line-height: 1.6;
  transition: all 0.15s ease;
}

.pi:hover {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}

/* Fix text breaking bug: ONLY the direct first-child label is a block, all inner <b> are inline */
.pi > b:first-child,
.pi-title {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}

.pi span b,
.pi span code,
.pi li b,
.pi li code {
  display: inline !important;
}

.pi span {
  color: var(--tx);
  font-size: 13px;
  line-height: 1.6;
  display: block;
}

/* 4 distinct visual tiers for Service Cheat Sheet */
.pi.pi-def,
.pi:nth-child(2) {
  border-left: 4px solid var(--bl);
}
.pi.pi-def > b:first-child,
.pi:nth-child(2) > b:first-child {
  color: var(--bl);
}

.pi.pi-use,
.pi:nth-child(3) {
  border-left: 4px solid var(--gr);
}
.pi.pi-use > b:first-child,
.pi:nth-child(3) > b:first-child {
  color: var(--gr);
}

.pi.pi-diff,
.pi:nth-child(4) {
  border-left: 4px solid var(--or);
}
.pi.pi-diff > b:first-child,
.pi:nth-child(4) > b:first-child {
  color: var(--or);
}

.pi.pi-exam,
.pi:nth-child(5) {
  border-left: 4px solid var(--rd);
  background: var(--rdb);
  border-color: rgba(229, 100, 88, 0.3);
}
.pi.pi-exam > b:first-child,
.pi:nth-child(5) > b:first-child {
  color: var(--rd);
}

/* Structured point list (.pts) */
.pts {
  list-style: none;
  padding: 0;
  margin: 6px 0 0 0;
}

.pts li {
  padding: 4px 0 4px 16px;
  position: relative;
  line-height: 1.6;
  font-size: 13px;
}

.pts li::before {
  content: "";
  position: absolute;
  left: 2px;
  top: 0.7em;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--mu);
}

/* Exam Keywords Chips & Focus styles */
.kw-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--card);
  border: 1px solid var(--bd);
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 12px;
  margin: 3px 4px 3px 0;
  box-shadow: 0 1px 2px rgba(0,0,0,0.03);
}

.kw-chip .kw-target {
  color: var(--bl);
  font-weight: 700;
}

/* Mini comparison table */
.diff-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 8px;
  font-size: 12.5px;
}

.diff-table th, .diff-table td {
  padding: 7px 10px;
  border: 1px solid var(--bd);
  text-align: left;
  vertical-align: top;
}

.diff-table th {
  background: var(--sub);
  font-weight: 700;
  color: var(--tx);
  font-size: 11.5px;
  text-transform: uppercase;
}

.diff-table td {
  background: var(--card);
}

/* Study mode interactive controls */
.study-toolbar {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 10px 0 16px;
  flex-wrap: wrap;
}

.study-btn {
  background: var(--card);
  border: 1px solid var(--bd);
  color: var(--tx);
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s ease;
}

.study-btn:hover {
  border-color: var(--bl);
  color: var(--bl);
}

.study-btn.active {
  background: var(--bl);
  border-color: var(--bl);
  color: #fff;
}

body.study-focus-exam .pi:not(.pi-exam) {
  display: none !important;
}

body.study-hide-answers .kw-target,
body.study-hide-answers .ans-blur {
  filter: blur(5px);
  user-select: none;
  transition: filter 0.15s ease;
  cursor: pointer;
}

body.study-hide-answers .kw-target:hover,
body.study-hide-answers .ans-blur:hover {
  filter: none;
}"""

# Replace normalized
css_norm = css.replace('\r\n', '\n')
old_pi_norm = old_pi_block.replace('\r\n', '\n')

if old_pi_norm in css_norm:
    css_norm = css_norm.replace(old_pi_norm, new_pi_block)
    # Write back matching system
    with open(style_path, 'w', encoding='utf-8') as f:
        f.write(css_norm.replace('\n', '\r\n'))
    print("SUCCESS: style.css updated.")
else:
    print("ERROR: old_pi_block not found in css")
