#!/usr/bin/env python3
"""
gen.py - Visual refresh for Hermes API landing page
Changes vs current version:
- Feature cards: add colored left border accent (keep emoji icon too)
- Pricing: add "SAVE 20%" annual badge next to Pro price
- How It Works: update step labels to match spec (Get API Key / Make a POST Request / Get Structured Data)
- Stats bar: verify correct text (already correct, ensure formatting)
- Overall: increase padding/spacing for more breathing room
- Ensure dashboard card metrics match spec exactly
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ─────────────────────────────────────────────
# 1. Feature cards: add colored left border accent
#    Replace glass rounded-2xl p-8 card-hover  →  glass rounded-2xl p-8 card-hover border-l-4 border-<color>-500
# ─────────────────────────────────────────────

# Card 1 – orange (icon-gradient-1)
html = html.replace(
    '<!-- Card 1 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 1 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-orange-500">',
    1
)

# Card 2 – purple (icon-gradient-2)
html = html.replace(
    '<!-- Card 2 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 2 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-purple-500">',
    1
)

# Card 3 – cyan (icon-gradient-3)
html = html.replace(
    '<!-- Card 3 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 3 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-cyan-500">',
    1
)

# Card 4 – emerald (icon-gradient-4)
html = html.replace(
    '<!-- Card 4 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 4 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-emerald-500">',
    1
)

# Card 5 – pink (icon-gradient-5)
html = html.replace(
    '<!-- Card 5 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 5 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-pink-500">',
    1
)

# Card 6 – amber (icon-gradient-6)
html = html.replace(
    '<!-- Card 6 -->\n        <div class="glass rounded-2xl p-8 card-hover">',
    '<!-- Card 6 -->\n        <div class="glass rounded-2xl p-8 card-hover border-l-4 border-amber-500">',
    1
)

# ─────────────────────────────────────────────
# 2. Pricing: add "SAVE 20%" annual badge next to Pro price
# ─────────────────────────────────────────────
html = html.replace(
    '          <div class="text-5xl font-extrabold mb-6">$49<span class="text-lg text-slate-400 font-medium">/mo</span></div>',
    '''          <div class="flex items-end gap-3 mb-6">
            <div class="text-5xl font-extrabold">$49<span class="text-lg text-slate-400 font-medium">/mo</span></div>
            <span class="mb-2 text-xs font-bold bg-green-500/20 text-green-400 border border-green-500/30 px-2.5 py-1 rounded-full uppercase tracking-wide">SAVE 20% annual</span>
          </div>''',
    1
)

# ─────────────────────────────────────────────
# 3. How It Works: update step titles to match spec exactly
#    Step 1: "Get API Key" → "Get Your API Key" (already matches, but update H3 text)
#    Step 2: "Make Your First Request" → "Make a POST Request"
#    Step 3: "Build & Scale" → "Get Structured Data"
# ─────────────────────────────────────────────
html = html.replace(
    '          <h3 class="text-xl font-bold mb-3" data-en="Make Your First Request" data-zh="发起首次请求">Make Your First Request</h3>\n          <p class="text-slate-400 leading-relaxed" data-en="Send a simple POST request with your API key. Get structured JSON data in seconds." data-zh="发送简单的 POST 请求并携带 API Key。数秒内获取结构化 JSON 数据。">Send a simple POST request with your API key. Get structured JSON data in seconds.</p>',
    '          <h3 class="text-xl font-bold mb-3" data-en="Make a POST Request" data-zh="发起 POST 请求">Make a POST Request</h3>\n          <p class="text-slate-400 leading-relaxed" data-en="Send a simple POST request with your API key and get a response in milliseconds." data-zh="发送简单的 POST 请求并携带 API Key，毫秒级返回结果。">Send a simple POST request with your API key and get a response in milliseconds.</p>',
    1
)

html = html.replace(
    '          <h3 class="text-xl font-bold mb-3" data-en="Build &amp; Scale" data-zh="构建与扩展">Build &amp; Scale</h3>\n          <p class="text-slate-400 leading-relaxed" data-en="Integrate into your workflow. Scale up as your business grows with flexible pricing." data-zh="集成到您的工作流。随着业务增长灵活扩展，定价方案随需而变。">Integrate into your workflow. Scale up as your business grows with flexible pricing.</p>',
    '          <h3 class="text-xl font-bold mb-3" data-en="Get Structured Data" data-zh="获取结构化数据">Get Structured Data</h3>\n          <p class="text-slate-400 leading-relaxed" data-en="Receive clean, structured JSON data ready to power your analytics, dashboards, and automation." data-zh="接收清洗后的结构化 JSON 数据，直接驱动您的分析、仪表板和自动化流程。">Receive clean, structured JSON data ready to power your analytics, dashboards, and automation.</p>',
    1
)

# Handle the non-HTML-escaped version too (in case the & wasn't escaped)
html = html.replace(
    '          <h3 class="text-xl font-bold mb-3" data-en="Build & Scale" data-zh="构建与扩展">Build & Scale</h3>',
    '          <h3 class="text-xl font-bold mb-3" data-en="Get Structured Data" data-zh="获取结构化数据">Get Structured Data</h3>',
    1
)

# ─────────────────────────────────────────────
# 4. Increase overall padding/spacing:
#    - Section py-24 → py-32 for major sections
#    - Feature section cards: p-8 → p-10
#    - Hero pt-32 pb-16 → pt-40 pb-24
# ─────────────────────────────────────────────

# Hero section more breathing room
html = html.replace(
    '<section class="hero-gradient pt-32 pb-16 px-4 relative overflow-hidden">',
    '<section class="hero-gradient pt-40 pb-28 px-4 relative overflow-hidden">',
    1
)

# Features section
html = html.replace(
    '<section id="features" class="py-24 px-4 bg-slate-900/30">',
    '<section id="features" class="py-32 px-4 bg-slate-900/30">',
    1
)

# How it works section
html = html.replace(
    '<section id="how-it-works" class="py-24 px-4">',
    '<section id="how-it-works" class="py-32 px-4">',
    1
)

# API Reference section
html = html.replace(
    '<section id="docs" class="py-24 px-4 bg-slate-900/30">',
    '<section id="docs" class="py-32 px-4 bg-slate-900/30">',
    1
)

# Pricing section
html = html.replace(
    '<section id="pricing" class="py-24 px-4">',
    '<section id="pricing" class="py-32 px-4">',
    1
)

# Stats bar: more vertical padding
html = html.replace(
    '<section class="stats-bar py-6 px-4">',
    '<section class="stats-bar py-8 px-4">',
    1
)

# ─────────────────────────────────────────────
# 5. Verify dashboard card metrics match spec:
#    Avg Price $24.99 | Monthly Sales 8,420 | BSR #1,203 | Gross Margin 34%
#    (already in the current file, but let's ensure BSR label says "BSR" not "Avg BSR")
# ─────────────────────────────────────────────
html = html.replace(
    '              <div class="text-xs text-slate-500 mb-1">Avg BSR</div>\n              <div class="text-2xl font-bold text-white">1,203</div>',
    '              <div class="text-xs text-slate-500 mb-1">BSR</div>\n              <div class="text-2xl font-bold text-white">#1,203</div>',
    1
)

# ─────────────────────────────────────────────
# 6. Add a subtle gradient separator line between feature cards section header and grid
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
# Report changes
# ─────────────────────────────────────────────
if html == original:
    print("WARNING: No changes were made. Check string matching.")
else:
    changes = []
    if 'border-l-4 border-orange-500' in html:
        changes.append('✓ Feature cards: colored left border accents added')
    if 'SAVE 20% annual' in html:
        changes.append('✓ Pricing: SAVE 20% annual badge added to Pro plan')
    if 'Make a POST Request' in html:
        changes.append('✓ How It Works Step 2: updated to "Make a POST Request"')
    if 'Get Structured Data' in html:
        changes.append('✓ How It Works Step 3: updated to "Get Structured Data"')
    if 'pt-40 pb-28' in html:
        changes.append('✓ Hero section: increased padding')
    if 'py-32' in html:
        changes.append('✓ Major sections: increased vertical padding (py-24 → py-32)')
    if '#1,203' in html:
        changes.append('✓ Dashboard card: BSR label and value updated')
    
    for c in changes:
        print(c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\n✅ index.html written successfully ({len(html):,} bytes)')
