# 2025 Jun
# Use this script to 
# save time
# by converting a CV in markdown (result of manual edits) to a CV in pdf (ready to submit) instantly
# Why markdown, because its easy to paste from external/advanced text processing sources.
# and markdown documents are structured, without superflous content like .docx file could accumualte.
# therefore good for Ats.

# %%
pathfile = "/"
pathroot = pathfile.rsplit('/',1)[0]
markfile = pathroot+ "input.md"

with open(markfile, 'r') as file:
    text = file.read()
with open(pathroot+ "css1.txt", 'r') as file:
    css = file.read()

from markdown_pdf import Section
from markdown_pdf import MarkdownPdf


# %%
k2text = r"""# Name Sname
__Data Engineer__

Info | 01234 342543 | Town Post code | [anemail@outlook\.com](mailto:anemail@outlook.com) | [LinkedIn](https://www.linkedin.com/in/) 
 
<br>
""" + text
k2text = k2text.replace('something_that_I_want_to_delete', '#')

text = r"""# MYREALNAME SURNAME
__Data Engineer__

USA\-Citizen | 01234 567891 | Place PostalCode | [email@outlook\.com](mailto:email@outlook.com) | [LinkedIn](https://www.linkedin.com/in/abcd) 
 
<br>
""" + text
# %%
text
# %%

import datetime
import re

def tstampfname(name='CV_as_pdf', kind='.pdf', pref='_'):
    ct = datetime.datetime.now()
    return name+pref+str(ct)[:16]+kind

pdf = MarkdownPdf(toc_level=2, optimize=True)
pdf.add_section(Section(text), user_css=css)
pdf.save(pathroot + tstampfname())


pdf = MarkdownPdf(toc_level=2, optimize=True)
pdf.add_section(Section(k2text), user_css=css)
pdf.save(pathroot +'Safe_to_share_Headless_'+ tstampfname())

# %%
