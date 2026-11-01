import pymupdf

doc = pymupdf.open("test_page.pdf")
page = doc[0]

# Convert page to SVG
svg_content = page.get_svg_image()

# Save to file
with open("output.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

doc.close()