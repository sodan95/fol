import os
from datetime import datetime

INPUT_FILE = "list.txt"
OUTPUT_FILE = "sitemap.xml"

MAX_URLS = 50000

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

urls = urls[:MAX_URLS]

today = datetime.utcnow().strftime("%Y-%m-%d")

xml = []

xml.append('<?xml version="1.0" encoding="UTF-8"?>')
xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url in urls:
    xml.append("  <url>")
    xml.append(f"    <loc>{url}</loc>")
    xml.append(f"    <lastmod>{today}</lastmod>")
    xml.append("    <changefreq>daily</changefreq>")
    xml.append("    <priority>0.8</priority>")
    xml.append("  </url>")

xml.append("</urlset>")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(xml))

print(f"[DONE] Sitemap Created: {OUTPUT_FILE}")
print(f"[TOTAL URLS] {len(urls)}")