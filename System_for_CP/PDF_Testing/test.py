import pymupdf
import pathlib

doc = pymupdf.open("/home/limbo/Desktop/Coding fun/Side (& fun) Projects/Project XKS8/Project XKS8/CLRS_GOLDEN_BIBLE.pdf")
page = doc[569]

svg_content = page.get_svg_image()

with open("output.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

doc.close()



#md_text = doc.to_markdown()
#print(md_text)
#
#pathlib.Path("output.md").write_bytes(md_text.encode())