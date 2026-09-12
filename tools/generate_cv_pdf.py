"""Generate the downloadable CV from the same Markdown used by the website.

Run from the gh-pages checkout: python tools/generate_cv_pdf.py
Requires reportlab (see requirements-pdf.txt).
"""
from pathlib import Path
from datetime import date
import re
from html import escape
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, CondPageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#102d46')
TEAL = colors.HexColor('#006d77')
TEXT = colors.HexColor('#334a5c')

def inline(text):
    text = text.replace('—', '-').replace('–', '-').replace('→', 'to')
    text = escape(text)
    text = re.sub(r'\[([^]]+)\]\(([^)]+)\)', lambda m: '<a href="'+(m[2] if ':' in m[2] else 'https://richardgong1987.github.io/resume/'+m[2])+'" color="#006d77">'+m[1]+'</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', text)
    return text

def blocks(source):
    paragraph=[]
    for line in source.splitlines()+['']:
        if not line.strip():
            if paragraph:
                yield 'p',' '.join(paragraph)
                paragraph=[]
        elif line.startswith('#') or line.startswith('- ') or line.strip()=='---':
            if paragraph:
                yield 'p',' '.join(paragraph)
                paragraph=[]
            if line.startswith('#'):
                prefix,body=line.split(' ',1)
                yield prefix,body
            elif line.startswith('- '):
                yield 'li',line[2:]
            else: yield 'hr',''
        else: paragraph.append(line.strip())

def build():
    # Embed fonts to keep PDF rendering consistent across platforms.
    # CV_FONT_DIR wins; otherwise search the usual spots on Linux, macOS (Homebrew
    # font casks land in ~/Library/Fonts) and the Codex runtime image.
    candidates=[Path(p).expanduser() for p in [
        os.environ.get('CV_FONT_DIR'),
        '/usr/share/fonts/truetype/dejavu',
        '~/Library/Fonts',
        '/Library/Fonts',
        '/opt/homebrew/share/fonts',
        '/opt/codex/runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/share/fonts/truetype',
    ] if p]
    fontdir=next((p for p in candidates if all((p/f).exists() for f in ['DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSans-Oblique.ttf','DejaVuSans-BoldOblique.ttf'])),None)
    if fontdir is None:
        searched=', '.join(str(p) for p in candidates)
        raise RuntimeError('DejaVu Sans not found in: '+searched+'\nInstall it (macOS: brew install --cask font-dejavu) or set CV_FONT_DIR.')
    for name,file in [('CVSans','DejaVuSans.ttf'),('CVSans-Bold','DejaVuSans-Bold.ttf'),('CVSans-Oblique','DejaVuSans-Oblique.ttf'),('CVSans-BoldOblique','DejaVuSans-BoldOblique.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
    pdfmetrics.registerFontFamily('CVSans',normal='CVSans',bold='CVSans-Bold',italic='CVSans-Oblique',boldItalic='CVSans-BoldOblique')
    source=(ROOT/'gong_hanjin_english.md').read_text().split('---',2)[2]
    start=int(re.search(r'^career_start_year:\s*(\d+)',(ROOT/'_config.yml').read_text(),re.M)[1])
    source=source.replace('{% include years.html %}',str(date.today().year-start))
    source=source.replace(' · [Download PDF](gong_hanjin_english.pdf)','')
    base=dict(fontName='CVSans',fontSize=9,leading=12.8,textColor=TEXT,spaceAfter=6)
    styles={
      'p':ParagraphStyle('body',**base),
      'li':ParagraphStyle('bullet',**(base|dict(leftIndent=10,firstLineIndent=-8,spaceAfter=6))),
      '#':ParagraphStyle('name',fontName='CVSans-Bold',fontSize=27,leading=32,textColor=NAVY,spaceAfter=8,keepWithNext=True),
      '##':ParagraphStyle('section',fontName='CVSans-Bold',fontSize=13,leading=17,textColor=TEAL,spaceBefore=16,spaceAfter=8,keepWithNext=True),
      '###':ParagraphStyle('role',fontName='CVSans-Bold',fontSize=11,leading=15,textColor=NAVY,spaceBefore=12,spaceAfter=7,keepWithNext=True),
    }
    story=[]
    for kind,body in blocks(source):
        if kind=='hr': continue
        if kind=='###': story.append(CondPageBreak(105))
        story.append(Paragraph(('• ' if kind=='li' else '')+inline(body),styles.get(kind,styles['p'])))
    def page(canvas,doc):
        canvas.setStrokeColor(colors.HexColor('#dce5e9'))
        canvas.line(44,34,A4[0]-44,34)
        canvas.setFont('CVSans',8)
        canvas.setFillColor(TEXT)
        canvas.drawString(44,22,'Hanjin Gong | Financial Systems & Software Engineering')
        canvas.drawRightString(A4[0]-44,22,str(doc.page))
    out=ROOT/'gong_hanjin_english.pdf'
    doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=38,bottomMargin=47,title='Hanjin Gong - Software Engineering CV',author='Hanjin Gong')
    doc.build(story,onFirstPage=page,onLaterPages=page)
    print(out)

if __name__=='__main__':
    build()
