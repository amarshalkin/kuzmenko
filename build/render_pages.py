import fitz, io, os, json, time
from PIL import Image
SRC="/sessions/awesome-peaceful-babbage/mnt/uploads/e5e8a41e-79c6-4b79-a721-b59d2b631ba9-1780477733806_1клик — light.pdf"
PDIR="/sessions/awesome-peaceful-babbage/mnt/kuzmenko/pages"
W=1400; Q=72
doc=fitz.open(SRC); N=doc.page_count
ar=None; t0=time.time()
for i in range(N):
    p=doc[i]; r=p.rect; zoom=W/r.width
    pix=p.get_pixmap(matrix=fitz.Matrix(zoom,zoom),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im.save(os.path.join(PDIR,"page-%03d.webp"%(i+1)),'WEBP',quality=Q,method=5)
    if ar is None: ar=pix.height/pix.width
json.dump({"count":N,"ar":round(ar,5),"width":W},open(os.path.join(PDIR,"manifest.json"),"w"))
total=sum(os.path.getsize(os.path.join(PDIR,f)) for f in os.listdir(PDIR) if f.endswith('.webp'))
print("rendered",N,"pages in",round(time.time()-t0,1),"s  total",round(total/1048576,1),"MB  ar",round(ar,4))
