#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a clean, questions-and-answers-only Markdown file from the SAME content
as the board (imports MODULES from build_data.py), then pandoc -> docx -> pdf.

Run: python3 tools/build_doc.py   ->  writes build/PONGBOT_QA.md
"""
import re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_data import MODULES  # shared single source of truth

BULLET_RE = re.compile(r'^[\-•·–►▪]\s*')
TABLE_RE  = re.compile(r'^\|.*\|$')
HEADER_RE = re.compile(r'^【')

def is_label_only(line):
    return bool(re.match(r'^([^：:]{1,20})[：:]\s*$', line))

def transform_answer(answer):
    """Convert the card's mini-markup (【headers】, | tables |, - bullets, 要点：)
    into clean Markdown with correct blank-line separation for pandoc."""
    out, prev = [], None
    def ensure_blank():
        if out and out[-1] != '':
            out.append('')
    for raw in answer.split('\n'):
        line = raw.strip()
        if line == '':
            continue
        if TABLE_RE.match(line):
            if prev != 'table':
                ensure_blank()
            out.append(line); prev = 'table'; continue
        if BULLET_RE.match(line):
            if prev != 'bullet':
                ensure_blank()
            out.append('- ' + BULLET_RE.sub('', line)); prev = 'bullet'; continue
        ensure_blank()
        if line.startswith('要点') and ('：' in line or ':' in line):
            sep = '：' if '：' in line else ':'
            label, _, rest = line.partition(sep)
            out.append(f'> **{label}{sep}**{rest.strip()}')
        elif HEADER_RE.match(line):
            out.append(f'**{line}**')
        elif is_label_only(line):
            out.append(f'**{line}**')
        else:
            out.append(line)
        prev = 'other'
    return '\n'.join(out)

CN = '〇一二三四五六七八九十'
def cn_num(n):
    return CN[n] if 0 <= n < len(CN) else str(n)

def main():
    qa_mods = [m for m in MODULES if m['id'] != 'mod0']
    mod0 = next((m for m in MODULES if m['id'] == 'mod0'), None)
    n_qa = sum(len(m['cards']) for m in qa_mods)

    p = []
    p += ['# 庞伯特 PONGBOT｜北美销售负责人 · 终面问答集', '']
    p += ['*岗位：庞伯特 / PONGBOT（上海创屹科技）· 北美销售负责人 · 终面（CEO 张海波）　|　候选人：郑翔宇（Alex）*', '']
    p += [f'*正文 {n_qa} 道面试问答，覆盖：开场必答 / 公司·产品·赛道认知 / 竞争格局 / Foxx 经历 / PayPal 经历 / 销售能力与北美打法 / 行为 STAR / 战略·风险·收尾 / 反问环节；文末附「考前速查」。答案均为中文，可直接用于普通话终面。*', '']
    p += ['---', '']

    qn = 0
    for idx, mod in enumerate(qa_mods, start=1):
        p += [f"## {cn_num(idx)}、{mod['name']}", '']
        for card in mod['cards']:
            qn += 1
            p += [f"### Q{qn}. {card['title']}", '']
            p += [transform_answer(card['answer']), '']

    if mod0:
        p += ['---', '', '## 附录 · 考前速查（市场 / 产品 / 竞品）', '']
        for card in mod0['cards']:
            p += [f"### {card['title']}", '']
            p += [transform_answer(card['answer']), '']

    md = '\n'.join(p)
    out_md = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build', 'PONGBOT_QA.md'))
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Wrote {out_md}")
    print(f"Q&A questions: {qn} | appendix 速查 cards: {len(mod0['cards']) if mod0 else 0}")

if __name__ == '__main__':
    main()
