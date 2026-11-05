#!/usr/bin/env python3
"""Generate static SVG assets for the Korumisa profile README (Korumisa profile README)."""
from pathlib import Path
from xml.sax.saxutils import escape as esc

from svgkit import (
    BG, BLUE, BORDER, GREEN, MONO, MUTED, PANEL, TEXT, VIOLET, ORANGE, RED, wipe, terminal
)

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"


def header():
    # Typing animation for the code window — typing animation
    lines = [
        [("const ", RED), ("segara", ORANGE), (" = {", TEXT)],
        [("  name", BLUE), (": ", TEXT), ('"I Made Gede Segara"', "#A5D6FF"), (",", TEXT)],
        [("  role", BLUE), (": ", TEXT), ('"Web Developer"', "#A5D6FF"), (",", TEXT)],
        [("  school", BLUE), (": ", TEXT), ('"Undiksha, Bali"', "#A5D6FF"), (",", TEXT)],
        [("  stack", BLUE), (": [", TEXT), ('"TypeScript"', "#A5D6FF"), (", ", TEXT),
         ('"React"', "#A5D6FF"), (", ", TEXT), ('"Laravel"', "#A5D6FF"), ("],", TEXT)],
        [("  status", BLUE), (": ", TEXT), ('"Mahasiswa aktif"', "#A5D6FF"), (",", TEXT)],
        [("};", TEXT)],
    ]
    y, t, body = 98, 0.6, []
    for i, segs in enumerate(lines, 1):
        ln = (f'<text x="62" y="{y}" font-family="{MONO}" font-size="13" fill="#484F58" '
              f'text-anchor="end">{i}</text>')
        el, t = wipe(78, y, segs, t, size=15, cw=9.0)
        body.append(ln + el)
        t += 0.2
        y += 26
    cursor_x = 99.0
    cursor = (f'<rect x="{cursor_x}" y="239" width="9" height="19" fill="{BLUE}" opacity="0">'
              f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" '
              f'dur="1s" begin="{t:.2f}s" repeatCount="indefinite"/></rect>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="300" viewBox="0 0 900 300" role="img" aria-label="I Made Gede Segara, Web Developer">
<defs>
  <clipPath id="r"><rect width="900" height="300" rx="16"/></clipPath>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="38"/></filter>
  <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
</defs>
<g clip-path="url(#r)">
  <rect width="900" height="300" fill="{BG}"/>
  <circle cx="780" cy="40" r="130" fill="{BLUE}" opacity="0.22" filter="url(#blur)">
    <animate attributeName="cx" values="780;700;780" dur="14s" repeatCount="indefinite"/>
  </circle>
  <circle cx="90" cy="290" r="120" fill="{VIOLET}" opacity="0.22" filter="url(#blur)">
    <animate attributeName="cy" values="290;240;290" dur="11s" repeatCount="indefinite"/>
  </circle>
  <rect x="32" y="30" width="540" height="244" rx="12" fill="{PANEL}" stroke="{BORDER}"/>
  <path d="M32 42a12 12 0 0 1 12-12h516a12 12 0 0 1 12 12v18H32z" fill="#161B22"/>
  <line x1="32" y1="60" x2="572" y2="60" stroke="{BORDER}"/>
  <circle cx="54" cy="45" r="5.5" fill="#FF5F56"/><circle cx="74" cy="45" r="5.5" fill="#FFBD2E"/><circle cx="94" cy="45" r="5.5" fill="{GREEN}"/>
  <text x="120" y="49" font-family="{MONO}" font-size="12" fill="{MUTED}">segara.ts</text>
  {''.join(body)}
  {cursor}
  <g transform="translate(735,152)">
    <circle r="46" fill="{BLUE}" opacity="0.10"><animate attributeName="opacity" values="0.06;0.22;0.06" dur="4s" repeatCount="indefinite"/></circle>
    <g><circle r="66" fill="none" stroke="url(#ring)" stroke-width="1.5" stroke-dasharray="3 7" opacity="0.9"/>
      <circle cx="66" cy="0" r="4.5" fill="{BLUE}"/>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="22s" repeatCount="indefinite"/></g>
    <g><circle r="98" fill="none" stroke="{VIOLET}" stroke-width="1" stroke-dasharray="2 9" opacity="0.7"/>
      <circle cx="-98" cy="0" r="3.5" fill="{VIOLET}"/>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="34s" repeatCount="indefinite"/></g>
    <text y="12" text-anchor="middle" font-family="{MONO}" font-size="34" font-weight="700" fill="{BLUE}">&lt;/&gt;</text>
  </g>
  <text x="735" y="272" text-anchor="middle" font-family="{SANS}" font-size="12" letter-spacing="3" fill="{MUTED}">BALI · INDONESIA</text>
</g>
<rect x="0.5" y="0.5" width="899" height="299" rx="16" fill="none" stroke="{BORDER}"/>
</svg>
'''


def about():
    blocks = [
        ("whoami", [
            [("I Made Gede Segara", BLUE), (" — web developer", MUTED)],
        ]),
        ("cat education.txt", [
            [("Mahasiswa aktif, Universitas Pendidikan Ganesha (Undiksha), Bali", TEXT)],
        ]),
        ("cat focus.txt", [
            [("Frontend & full-stack dengan TypeScript dan Laravel.", TEXT),
             (" Suka detail kecil:", MUTED)],
        ]),
        ("echo $NOW", [
            [("TypeScript", BLUE), (" · ", MUTED), ("Vite", VIOLET), (" · ", MUTED),
             ("Supabase", GREEN), (" · ", MUTED), ("Laravel", ORANGE)],
        ]),
    ]
    # Build via terminal helper but custom title
    term_blocks = []
    for cmd, lines in blocks:
        term_blocks.append((cmd, lines))
    return terminal("~/korumisa — about", term_blocks,
                    "Mahasiswa aktif Universitas Pendidikan Ganesha (Undiksha), Bali. Fokus frontend dan full-stack dengan TypeScript.")


def btn(label_top, label_bot, aria, icon_paths):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="54" viewBox="0 0 220 54" role="img" aria-label="{esc(aria)}">
<defs>
  <linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="220" y2="0">
    <stop offset="0" stop-color="{BLUE}"/><stop offset="0.5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{BLUE}"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-220 0;220 0;-220 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="ic" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
</defs>
<rect x="1" y="1" width="218" height="52" rx="26.0" fill="{BG}" stroke="url(#g)" stroke-width="1.6"/>
<rect x="8" y="8" width="38" height="38" rx="19" fill="url(#ic)"/>
<g transform="translate(15,15)">{icon_paths}</g>
<text x="58" y="23" font-family="{SANS}" font-size="10" letter-spacing="2" fill="{MUTED}">{esc(label_top)}</text>
<text x="58" y="40" font-family="{SANS}" font-size="15" font-weight="700" fill="{TEXT}">{esc(label_bot)}</text>
</svg>
'''


def card(title, line1, line2, tags, accent, cta="Live demo ↗"):
    tag_els = []
    x = 20.0
    for tag in tags:
        w = max(len(tag) * 7.4 + 24, 40)
        tag_els.append(
            f'<g transform="translate({x},{118})">'
            f'<rect width="{w:.1f}" height="24" rx="12" fill="{accent}" opacity="0.14"/>'
            f'<text x="{w/2:.1f}" y="16" text-anchor="middle" font-family="{MONO}" '
            f'font-size="11" fill="{accent}">{esc(tag)}</text></g>'
        )
        x += w + 8
    folder = (
        f'<path d="M20 28h6l2 3h8a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H20a2 2 0 0 1-2-2V30a2 2 0 0 1 2-2z" '
        f'fill="none" stroke="{accent}" stroke-width="1.6" stroke-linejoin="round" transform="translate(0,2)"/>'
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="280" height="176" viewBox="0 0 280 176" role="img" aria-label="{esc(title)}: {esc(line1)} {esc(line2)}">
<defs>
  <clipPath id="c"><rect width="280" height="176" rx="14"/></clipPath>
  <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
  <radialGradient id="glow" cx="1" cy="0" r="1"><stop offset="0" stop-color="{accent}" stop-opacity="0.28"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
</defs>
<g clip-path="url(#c)">
  <rect width="280" height="176" fill="{BG}"/>
  <circle cx="280" cy="0" r="120" fill="url(#glow)"><animate attributeName="r" values="100;140;100" dur="6s" repeatCount="indefinite"/></circle>
  <rect width="280" height="3" fill="url(#bar)"/>
</g>
<rect x="0.5" y="0.5" width="279" height="175" rx="14" fill="none" stroke="{BORDER}"/>
{folder}
<text x="52" y="47" font-family="{SANS}" font-size="18" font-weight="700" fill="{TEXT}">{esc(title)}</text>
<text x="20" y="80" font-family="{SANS}" font-size="13" fill="{MUTED}">{esc(line1)}</text>
<text x="20" y="98" font-family="{SANS}" font-size="13" fill="{MUTED}">{esc(line2)}</text>
{''.join(tag_els)}
<text x="20" y="165" font-family="{SANS}" font-size="12" font-weight="600" fill="{accent}">{esc(cta)}</text>
</svg>
'''


def stack_svg(items):
    colors = [BLUE, VIOLET, GREEN, ORANGE, "#79C0FF", RED]
    pills = []
    x = 20.0
    for i, name in enumerate(items):
        w = max(len(name) * 8.2 + 42, 68)
        c = colors[i % len(colors)]
        pills.append(
            f'<g transform="translate({x:.1f},14)">'
            f'<rect width="{w:.1f}" height="32" rx="16" fill="#161B22" stroke="{BORDER}"/>'
            f'<circle cx="17" cy="16" r="4" fill="{c}"/>'
            f'<text x="30" y="21" font-family="{SANS}" font-size="13" font-weight="600" fill="#C9D1D9">{esc(name)}</text></g>'
        )
        x += w + 12
    total = x + 20
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="60" viewBox="0 0 900 60" role="img" aria-label="Tech stack: {esc(', '.join(items))}">
<defs>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000"/><stop offset="0.08" stop-color="#fff"/><stop offset="0.92" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
  <mask id="m"><rect width="900" height="60" fill="url(#fade)"/></mask>
</defs>
<rect width="900" height="60" rx="12" fill="{BG}" stroke="{BORDER}"/>
<g mask="url(#m)">
  <g>
    <g>{''.join(pills)}</g>
    <g transform="translate({total:.1f},0)"><g>{''.join(pills)}</g></g>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="{-total:.1f} 0" dur="32s" repeatCount="indefinite"/>
  </g>
</g>
</svg>
'''


def main():
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "header.svg").write_text(header(), encoding="utf-8")
    (ASSETS / "about.svg").write_text(about(), encoding="utf-8")

    globe = ('<circle cx="12" cy="12" r="9" fill="none" stroke="#fff" stroke-width="1.8"/>'
             '<ellipse cx="12" cy="12" rx="4" ry="9" fill="none" stroke="#fff" stroke-width="1.6"/>'
             '<path d="M3 12h18" stroke="#fff" stroke-width="1.6"/>')
    mail = ('<rect x="3" y="5" width="18" height="14" rx="2.5" fill="none" stroke="#fff" stroke-width="1.8"/>'
            '<path d="m4 7.5 8 6 8-6" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/>')
    gh = ('<g transform="scale(1.5)"><path fill="#fff" d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"/></g>')
    pen = ('<path d="M4 20l4.2-1L19 8.2 15.8 5 5 15.8z" fill="none" stroke="#fff" stroke-width="1.8" stroke-linejoin="round"/>'
           '<path d="M13.5 7.3l3.2 3.2" stroke="#fff" stroke-width="1.8"/>')

    (ASSETS / "btn-portfolio.svg").write_text(
        btn("PORTFOLIO", "Lihat Portofolio", "Lihat Portofolio", globe), encoding="utf-8")
    (ASSETS / "btn-email.svg").write_text(
        btn("EMAIL", "Hubungi saya", "Hubungi saya", mail), encoding="utf-8")
    (ASSETS / "btn-github.svg").write_text(
        btn("GITHUB", "@Korumisa", "@Korumisa", gh), encoding="utf-8")
    (ASSETS / "btn-guestbook.svg").write_text(
        btn("GUESTBOOK", "Tulis pesan", "Tulis pesan", pen), encoding="utf-8")

    (ASSETS / "card-egabah.svg").write_text(card(
        "E-Gabah",
        "ERP penggilingan padi: pembelian,",
        "produksi, stok, penjualan, absensi, HR.",
        ["TypeScript", "Supabase"],
        BLUE,
    ), encoding="utf-8")
    (ASSETS / "card-absenyura.svg").write_text(card(
        "absenyura",
        "Absensi kampus: QR dinamis, GPS,",
        "sidik perangkat, dan foto selfie.",
        ["Vite", "TypeScript"],
        VIOLET,
    ), encoding="utf-8")
    (ASSETS / "card-baliticket.svg").write_text(card(
        "Baliticketchain",
        "Pemesanan tiket Bali dengan",
        "Laravel (admin + pengguna).",
        ["PHP", "Laravel"],
        GREEN,
        cta="Repo ↗",
    ), encoding="utf-8")

    # Remove legacy card filenames
    for old in ("card-catatku.svg", "card-attendance.svg", "card-portofolio.svg"):
        p = ASSETS / old
        if p.exists():
            p.unlink()

    (ASSETS / "stack.svg").write_text(stack_svg([
        "HTML", "CSS", "TypeScript", "React", "Vite", "Tailwind CSS",
        "Node.js", "Supabase", "PHP", "Laravel", "Git", "GitHub", "Vercel", "Figma",
    ]), encoding="utf-8")

    # Empty guestbook + empty activity placeholders
    from guestbook import render as gb_render
    gb_render([])
    import update_activity as act
    (ASSETS / "activity.svg").write_text(act.render([]), encoding="utf-8")

    print("static assets written")


if __name__ == "__main__":
    main()
