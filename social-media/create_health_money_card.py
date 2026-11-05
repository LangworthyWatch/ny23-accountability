#!/usr/bin/env python3
"""Health-industry PAC money and the committee seat, entry 2026-11-05-health-industry-money-committee-seat (DOCUMENTED PATTERN).
Figures: FEC committee receipts classified with the FEC committee master (three cycles); NYS DOH Sept 2026 Medicaid
managed care enrollment; USAspending FY2023-26 family sums. Retained under research/sources/donor-contractors-2026-11-05/."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.card import (Card, NAVY, DARK, RED, GREEN, MUTED, BORDER, WHITE, LIGHTGRAY)

c = Card(scale=2)
c.brand_bar()
y = c.badge(58, "DOCUMENTED PATTERN  ·  NOV 5, 2026")
y = c.title(y, "$6,000.  $85,250.  $193,000.", size=40)
y = c.title(y - 2, "Health-Industry PAC Money to Him, by Election Cycle.", size=26)
y = c.subtitle(y + 4, "In between the second and third numbers: a seat on the Energy and Commerce Health Subcommittee, December 13, 2024.", size=13.5)
y = c.divider(y + 10)

# HERO: three bars with the appointment marker
h_h = 300
c.panel(44, y, c.w - 44, y + h_h, fill=WHITE, outline=BORDER)
c.text(66, y + 26, "HEALTH-INDUSTRY PACs: DRUG, DEVICE, INSURANCE AND PROVIDER GROUPS", size=14, bold=True, fill=NAVY, anchor="lm")
c.text(66, y + 46, "From his campaign and leadership PAC filings, one classification rule for all three cycles. Share of all PAC money in gray.", size=11.5, fill=MUTED, anchor="lm")
rows = [("2021-22", 6000, "3.0%", NAVY), ("2023-24", 85250, "9.5%", NAVY), ("2025-26", 193000, "15.1%", RED)]
x0 = 200; xmax = c.w - 250; unit = (xmax - x0) / 193000.0
ry = y + 92
for lab, v, sh, col in rows:
    c.text(66, ry, lab, size=18, bold=True, fill=col, anchor="lm")
    w = max(v * unit, 6)
    c.rect(x0, ry - 22, x0 + w, ry + 22, fill=col, outline=None, radius=4)
    c.text(x0 + w + 14, ry - 8, f"${v:,.0f}", size=26, impact=True, fill=col, anchor="lm")
    c.text(x0 + w + 14, ry + 16, f"{sh} of PAC money", size=12, fill=MUTED, anchor="lm")
    if lab == "2023-24":
        my = ry + 36
        c.rect(x0, my, xmax, my + 1, fill=RED, outline=None)
        c.text(x0 + 8, my + 10, "Dec. 13, 2024: named to Energy and Commerce; seated on its Health Subcommittee", size=11.5, bold=True, fill=RED, anchor="lt")
        ry += 24
    ry += 66
c.text(66, y + h_h - 20, "Drug and device company PACs alone went from $5,500 to $62,000. Twelve of them gave for the first time in 2025-26.", size=12.5, bold=True, fill=DARK, anchor="lm")
y += h_h + 12

# MEDICAID PLANS strip: 100% stacked bar outside Erie
m_h = 150
c.panel(44, y, c.w - 44, y + m_h, fill="#EDF2F7", outline=BORDER)
c.text(66, y + 24, "WHO RUNS MEDICAID IN HIS COUNTIES OUTSIDE ERIE: 87,512 ENROLLEES, SEPT. 2026", size=14, bold=True, fill=NAVY, anchor="lm")
c.text(66, y + 44, "Every one is in a plan whose parent company's PAC has given to him. The four parents gave $12,000 this cycle.", size=12, fill=MUTED, anchor="lm")
segs = [("Fidelis Care (Centene)", 68579, "#2C5282"), ("Highmark", 9893, "#4A5568"), ("Molina", 5546, "#718096"), ("UnitedHealthcare", 3494, "#A0AEC0")]
bx0, bx1 = 66, c.w - 66; bw = bx1 - bx0; tot = sum(s[1] for s in segs)
x = bx0; by = y + 66
for lab, v, col in segs:
    w = bw * v / tot
    c.rect(x, by, x + w, by + 30, fill=col, outline=None)
    if w > 120: c.text(x + w / 2, by + 15, f"{lab}  {v:,}", size=12, bold=True, fill=WHITE, anchor="mm")
    x += w
c.text(bx0, by + 46, "Then Highmark 9,893   ·   Molina 5,546   ·   UnitedHealthcare 3,494   (NYS Dept. of Health, Table IIa, Sept. 2026; Erie County plans not shown)", size=11, fill=MUTED, anchor="lm")
y += m_h + 12

# CONTRACTS strip
k_h = 104
c.panel(44, y, c.w - 44, y + k_h, fill=WHITE, outline=BORDER)
c.text(66, y + 24, "WHAT FOUR OF HIS HEALTH DONORS HOLD IN FEDERAL CONTRACTS, FY2023 TO FY2026", size=14, bold=True, fill=NAVY, anchor="lm")
cols = [("UnitedHealth / Optum", "$81.3B", "military health system"), ("McKesson", "$44.9B", "drug distribution"), ("Centene / Health Net", "$8.6B", "military health system"), ("Maximus", "$6.0B", "Medicare call centers")]
cw = (c.w - 88) / 4
for i, (n, a, d) in enumerate(cols):
    cx = 44 + cw * i + cw / 2
    c.text(cx, y + 54, a, size=24, impact=True, fill=NAVY, anchor="mm")
    c.text(cx, y + 76, n, size=12, bold=True, fill=DARK, anchor="mm")
    c.text(cx, y + 92, d, size=10.5, fill=MUTED, anchor="mm")
y += k_h + 12

# fair case
f_h = 70
c.panel(44, y, c.w - 44, y + f_h, fill="#F0FFF4", outline="#9AE6B4")
c.text(c.w / 2, y + 20, "WHAT CUTS HIS WAY", size=13, bold=True, fill=GREEN, anchor="mm")
c.text(c.w / 2, y + 40, "Every Health Subcommittee member gets this money. His Medicaid vote cut the plans' revenue. His three PBM votes ran against UnitedHealth.", size=12, fill=DARK, anchor="mm")
c.text(c.w / 2, y + 57, "All of it is lawful and disclosed. No contribution is tied to any vote.", size=12, fill=DARK, anchor="mm")
y += f_h + 10

kk_h = 60
c.panel(44, y, c.w - 44, y + kk_h, fill=NAVY, outline=None)
c.text(c.w / 2, y + 22, "The seat he called an \"unparalleled opportunity to influence\" health policy changed who funds him within one cycle.", size=13.5, bold=True, fill=WHITE, anchor="mm")
c.text(c.w / 2, y + 44, "Sources: FEC filings and committee master  ·  USAspending.gov  ·  NYS DOH Medicaid enrollment, Sept. 2026  ·  Clerk of the House", size=10.5, fill=LIGHTGRAY, anchor="mm")
y += kk_h + 10
c.text(c.w / 2, y, "langworthywatch.org/fact-checks/2026-11-05-health-industry-money-committee-seat/", size=11.5, bold=True, fill=NAVY, anchor="mm")
assert y < 1080 - 50 - 6, y
c.footer_bar()
c.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "health_money_card.png"), to_desktop=True)
