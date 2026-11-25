# news-image-20261124 — NUMBERS angle: 38 stories, 13 panels, 8-number strip.
# Template: winning front page (BEDAH-PRIZE-ZONE-19-22.md section 3).
# Facts: KANON-20261124.md only. Deterministic PIL rendering, 1024x1024.
# Hero trio: Riyadh PIF tower / Shanghai Chen Jining / Huawei 10 of 12.
# Map: real lat/lon, equirectangular; pins 1-13 with leader-line offsets.
import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024; OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png'); BG=(250,246,236); INK=(20,20,20); RED=(178,34,34); NAVY=(18,42,84); GOLD=(201,162,39); TEAL=(0,110,110)
def F(p,s):
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
SERIF=lambda s:F('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',s); SANS=lambda s:F('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',s); BOLD=lambda s:F('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
def wrap(t,f,mw):
    ws=[]
    for w in t.split():
        if ws and d.textlength(ws[-1]+' '+w,font=f)<=mw: ws[-1]+=' '+w
        else: ws.append(w)
    return ws
def txt(x,y,ls,f,fill=INK,lh=None):
    lh=lh or int(f.size*1.25)
    for i,l in enumerate(ls): d.text((x,y+i*lh),l,font=f,fill=fill)
    return y+len(ls)*lh
def chip(x,y,t,c):
    f=BOLD(8); w=int(d.textlength(t,font=f))+10; d.rounded_rectangle([x,y,x+w,y+14],3,fill=c); d.text((x+5,y+2),t,font=f,fill=(255,255,255)); return x+w+4
def scene(x,y,w,h,k):
    d.rectangle([x,y,x+w,y+h],fill=(30,45,80) if k in (1,4,6) else (210,225,235) if k in (7,13) else (245,220,180) if k==5 else (40,60,50) if k in (3,8) else (235,225,200))
    if k==1:
        d.rectangle([x+w*0.42,y+h*0.15,x+w*0.58,y+h],fill=(90,110,140)); d.polygon([(x+w*0.42,y+h*0.15),(x+w*0.5,y),(x+w*0.58,y+h*0.15)],fill=(200,170,60)); d.ellipse([x+w*0.68,y+h*0.12,x+w*0.78,y+h*0.22],fill=(255,120,40)); d.rectangle([x+w*0.1,y+h*0.7,x+w*0.35,y+h],fill=(50,60,80)); d.rectangle([x+w*0.65,y+h*0.6,x+w*0.9,y+h],fill=(50,60,80))
    elif k==2:
        d.rectangle([x+w*0.15,y+h*0.35,x+w*0.85,y+h],fill=(150,40,40)); d.rectangle([x+w*0.42,y+h*0.55,x+w*0.58,y+h],fill=(60,20,20)); d.rectangle([x+w*0.2,y+h*0.2,x+w*0.8,y+h*0.35],fill=(201,162,39)); d.rectangle([x+w*0.3,y+h*0.45,x+w*0.38,y+h*0.55],fill=(255,255,255)); d.rectangle([x+w*0.62,y+h*0.45,x+w*0.7,y+h*0.55],fill=(255,255,255))
    elif k==3:
        d.rectangle([x+w*0.2,y+h*0.3,x+w*0.8,y+h],fill=(220,220,210)); d.polygon([(x+w*0.15,y+h*0.3),(x+w*0.5,y+h*0.08),(x+w*0.85,y+h*0.3)],fill=(120,30,30)); d.rectangle([x+w*0.44,y+h*0.5,x+w*0.48,y+h],fill=(60,60,60)); d.rectangle([x+w*0.52,y+h*0.5,x+w*0.56,y+h],fill=(60,60,60)); d.ellipse([x+w*0.68,y+h*0.15,x+w*0.82,y+h*0.3],fill=(201,162,39))
    elif k==7:
        d.line([(x+5,y+h-10),(x+w*0.3,y+h*0.45),(x+w*0.55,y+h*0.55),(x+w-5,y+10)],fill=(178,34,34),width=4,joint='curve'); d.line([x,y+h*0.3,x+w,y+h*0.3],fill=(178,34,34),width=2); d.rectangle([x+w*0.05,y+h*0.75,x+w*0.95,y+h],fill=(18,42,84))
    elif k==13:
        d.polygon([(x+w*0.48,y+h*0.05),(x+w*0.55,y+h*0.55),(x+w*0.45,y+h*0.55)],fill=(220,220,220)); d.polygon([(x+w*0.45,y+h*0.35),(x+w*0.3,y+h*0.6),(x+w*0.45,y+h*0.55)],fill=(178,34,34)); d.ellipse([x+w*0.7,y+h*0.15,x+w*0.85,y+h*0.3],fill=(201,162,39)); d.rectangle([x,y+h*0.85,x+w,y+h],fill=(60,80,60))
    elif k==5:
        d.polygon([(x+w*0.4,y+h*0.15),(x+w*0.6,y+h*0.15),(x+w*0.5,y+h*0.45)],fill=(201,162,39)); d.rectangle([x+w*0.46,y+h*0.45,x+w*0.54,y+h*0.75],fill=(150,120,30)); d.rectangle([x+w*0.1,y+h*0.7,x+w*0.35,y+h],fill=(0,110,60)); d.rectangle([x+w*0.65,y+h*0.7,x+w*0.9,y+h],fill=(178,34,34))
    elif k==6:
        d.rectangle([x+w*0.1,y+h*0.55,x+w*0.9,y+h*0.7],fill=(120,60,30)); d.rectangle([x+w*0.15,y+h*0.35,x+w*0.85,y+h*0.55],fill=(40,80,120)); d.rectangle([x+w*0.2,y+h*0.15,x+w*0.3,y+h*0.35],fill=(200,200,200)); d.rectangle([x,y+h*0.7,x+w,y+h],fill=(30,90,140))
    elif k==8:
        d.rectangle([x+w*0.15,y+h*0.3,x+w*0.85,y+h*0.85],fill=(30,30,40)); d.rectangle([x+w*0.2,y+h*0.4,x+w*0.4,y+h*0.6],fill=(255,60,60)); d.rectangle([x+w*0.45,y+h*0.4,x+w*0.65,y+h*0.6],fill=(255,180,0)); d.rectangle([x+w*0.7,y+h*0.4,x+w*0.8,y+h*0.6],fill=(0,200,200))
    else:
        d.ellipse([x+w*0.7,y+h*0.12,x+w*0.85,y+h*0.27],fill=(255,220,120)); d.rectangle([x+w*0.1,y+h*0.55,x+w*0.9,y+h],fill=(90,110,90)); d.polygon([(x+w*0.2,y+h*0.55),(x+w*0.5,y+h*0.2),(x+w*0.8,y+h*0.55)],fill=(70,90,70))
# DATA: (num, place, field, chip, colour, headline, deck, source, lat, lon, scene-kind)
HERO=[(1,'RIYADH','MIDDLE EAST','CONFIRMED',(0,120,60),'Houthi drone hits Riyadh tallest tower again, 11 hurt','A Houthi drone struck the PIF tower, the tallest in Riyadh, for the second time in a week, injuring 11 people, including 2 Saudis, 2 Indians, 3 Nepalis and 4 Egyptians.','Saudi officials · wires',24.7,46.7,1),(2,'SHANGHAI','ASIA','OFFICIAL',(0,80,160),'China probes Shanghai party chief Chen Jining','Chen Jining, 62, the Shanghai party chief, is under investigation for serious violations, the fourth Politburo member to fall in a probe this year.','CCDI · wires',31.2,121.5,2),(3,'NEW YORK','US / TECH','CONFIRMED',(0,120,60),'Huawei guilty on 10 of 12 counts','A US federal jury found Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud, and cleared it of racketeering, with sentencing in Sep 2027.','US court · wires',40.7,-74.0,3)]
CARDS=[(4,'ZAPORIZHZHIA','EUROPE / WAR','REPORTED',(90,90,90),'Russian attacks kill 9 across Ukraine in a day','Russia launched 96 drones at Ukraine and 73 were shot down or jammed, while 9 people were killed and 81 injured in a day.','Ukraine officials · Kyiv',47.8,35.1,4),(5,'DAKAR','AFRICA / SPORT','OFFICIAL',(0,80,160),'CAS hands Senegal back the AFCON title','CAS restored the Africa Cup title to Senegal after Morocco forfeited 3-0, confirming a 1-0 win for Senegal.','CAS · wires',14.7,-17.4,5),(6,'HORMUZ','MIDDLE EAST','REPORTED',(90,90,90),'IRGC attacks container ship in Hormuz','An IRGC attack hit a container ship in Hormuz at 18:58 UTC, disabling navigation near Khasab, Oman.','UKMTO · wires',26.5,56.3,6),(7,'NEW YORK','WORLD / MARKETS','CONFIRMED',(0,120,60),'Dow closes above 50,000 for the first time','The Dow closed at 50,018, its first close above 50,000, while the Taiex set a record with a gain of 8.99 percent.','Market close · wires',40.7,-74.0,7),(8,'REDMOND','WORLD / TECH','REPORTED',(90,90,90),'Microsoft declares Code Red after historic outage','After a 24-hour outage, the worst in Exchange Online history, Microsoft declared Code Red and set a one-hour global recovery target.','Reuters',47.67,-122.12,8),(9,'ESKISEHIR','EUROPE','REPORTED',(90,90,90),'Turkish military helicopter crash kills 5','A Turkish military AS-532 helicopter crashed in Eskisehir, killing all 5 people on board.','Turkish officials',39.78,30.52,4),(10,'CARTAGENA','AMERICAS','REPORTED',(90,90,90),'Supermarket hostages: 25 held in Cartagena','Gunmen held 25 hostages in a Cartagena supermarket, freed 5 elderly women, and halted airport landings for about 45 minutes.','Colombia officials',10.39,-75.51,4),(11,'ADEN','MIDDLE EAST','REPORTED',(90,90,90),'Houthis advance within 60 km of Aden','Houthi forces advanced to within 60 km of Aden in Yemen, pressing south towards the port city.','Wires',12.79,45.03,4),(12,'LAHJ','MIDDLE EAST','REPORTED',(90,90,90),'Saudi strikes kill 25, wound 6 in Yemen','Saudi strikes on a bus and trucks in Wadi Maabaq, Lahj, killed or left missing 25 people and wounded 6.','Yemen officials',13.05,44.88,4),(13,'JIUQUAN','WORLD / SPACE','OFFICIAL',(0,80,160),'China names first foreign astronaut for Tiangong','China named Muhammad Zeeshan Ali of Pakistan to the Shenzhou-24 crew, the first foreign astronaut on Tiangong.','CMSA · wires',39.7,98.5,13)]
ALSO=[(14,'Ankara','Haftar visits Turkey for the first time','REPORTED'),(15,'London','UK sanctions Houthis + 4 officials','OFFICIAL'),(16,'Villavicencio','Car bomb injures 23','REPORTED'),(17,'Gaza','Israel kills Hamas internal security chief','REPORTED'),(18,'Baghdad','Iraq orders federal control of Kurdish oilfields','OFFICIAL'),(19,'Gaza','Meningitis epidemic alert: 272 cases in Oct','OFFICIAL'),(20,'DR Congo','Missing Cessna 208; rebels claim shootdown','CLAIM'),(21,'Hanoi','Hot-pot explosion kills at least 6','REPORTED'),(22,'Gulf of Finland','Ukraine hits Russian ship Sparta II','REPORTED'),(23,'Kuala Lumpur','Malaysia to return thousands of migrants','OFFICIAL'),(24,'Ulleungdo','S. Korea shelter order as jets enter ADIZ','OFFICIAL'),(25,'Dhaka','Hasina plans return on 16 Dec','REPORTED'),(26,'The Hague','14 nations endorse ICJ Myanmar ruling','REPORTED'),(27,'Jakarta','Indonesia nominates 2 VP candidates','OFFICIAL'),(28,'Beijing','China sentences official Ma to death for spying','OFFICIAL'),(29,'Brussels','NATO vows defence against space threat','OFFICIAL'),(30,'Mexico City','El Chapo Isidro: US drone aided weekend capture','REPORTED'),(31,'San Salvador','Bukele names 3 soldiers killed in Haiti','OFFICIAL'),(32,'Ottawa','Pentagon rebukes Canada: only 41.9% of air fleet ready','REPORTED'),(33,'Washington','US adds Megaspeed to trade blacklist','OFFICIAL'),(34,'Kyiv','Zelensky urges Ukraine-Russia-US-Europe talks','REPORTED'),(35,'Ras Al Khaimah','UAE bus-truck crash kills 13','REPORTED'),(36,'London','England record 5,258 heat deaths, summer 2026','OFFICIAL'),(37,'Kourou','Ariane 6 lofts 36 Amazon satellites','OFFICIAL'),(38,'Cikande','Factory-fire toll rises to 26','REPORTED')]
UTC=[('02:15','NATO vows space defence'),('08:16','Hanoi hot-pot blast'),('10:42','Saudi strikes Yemen'),('14:27','Riyadh tower hit'),('16:51','Houthis 60 km from Aden'),('18:58','Hormuz ship attack'),('20:41','Huawei guilty')]
NUMS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow close'),('+8.99%','Taiex record'),('25','killed in Yemen'),('26','Cikande toll'),('10/12','Huawei guilty'),('96','drones at Ukraine')]
REG=[('Europe',9,(178,34,34)),('Middle East',8,(220,120,0)),('Asia',8,(0,110,110)),('Africa',2,(0,120,60)),('Americas',7,(18,42,84)),('World/Space',4,(110,60,140))]
# HEADER + MASTHEAD
d.text((12,6),'THE WORLD ON ONE PAGE',font=BOLD(10),fill=RED); d.text((1024-12-int(d.textlength('38 STORIES · 6 REGIONS · 13 FIELDS',font=BOLD(10))),6),'38 STORIES · 6 REGIONS · 13 FIELDS',font=BOLD(10),fill=INK)
d.text((12,20),'Tuesday 24 November 2026',font=SERIF(30),fill=INK); d.line([12,54,1012,54],fill=RED,width=2)
d.text((12,58),'Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts.',font=SERIF(12),fill=RED)
# REGION BAR
x=12
for n,c,col in REG:
    w=int(1000*c/38); d.rectangle([x,76,x+w,94],fill=col); d.text((x+4,80),f'{n} {c}',font=BOLD(9),fill=(255,255,255)); x+=w
# NUMBERS STRIP
d.text((12,100),'THE DAY IN NUMBERS',font=BOLD(10),fill=RED)
for i,(v,l) in enumerate(NUMS):
    cx=12+i*125; d.text((cx,112),v,font=SERIF(17),fill=NAVY); d.text((cx,132),l,font=SANS(8),fill=INK)
d.line([12,148,1012,148],fill=(180,180,180),width=1)
# UTC STRIP
d.text((12,152),'THE DAY IN UTC',font=BOLD(9),fill=RED)
for i,(t,e) in enumerate(UTC):
    cx=140+i*126; d.text((cx,152),t,font=BOLD(9),fill=NAVY); d.text((cx,163),e,font=SANS(8),fill=INK)
# HEROES (3 across)
for i,(n,pl,fi,ch,col,hl,dk,src,la,lo,sk) in enumerate(HERO):
    x=12+i*334; d.rectangle([x,178,x+326,368],outline=(150,150,150),width=1); scene(x+1,179,x+324,71,sk); d.text((x+6,254),f'{n}  {pl} · {fi}',font=BOLD(9),fill=RED); w=chip(x+6,267,ch,col); d.text((x+6+w,269),src,font=SANS(8),fill=(90,90,90)); txt(x+6,284,wrap(hl,BOLD(12),314),BOLD(12),lh=14); txt(x+6,314,wrap(dk,SANS(9),314),SANS(9),lh=11)
# CARDS (5+5)
for i,(n,pl,fi,ch,col,hl,dk,src,la,lo,sk) in enumerate(CARDS):
    r,c=i//5,i%5; x=12+c*201; y=374+r*132; d.rectangle([x,y,x+195,y+126],outline=(150,150,150),width=1); scene(x+1,y+1,x+193,38,sk); d.text((x+5,y+42),f'{n}  {pl} · {fi}',font=BOLD(8),fill=RED); chip(x+5,y+55,ch,col); txt(x+5,y+70,wrap(hl,BOLD(10),185),BOLD(10),lh=11); txt(x+5,y+93,wrap(dk,SANS(8),185),SANS(8),lh=10)
# MAP (tall) + LEGEND
d.text((12,642),'THE WORLD · 13 STORIES PINNED',font=BOLD(10),fill=RED)
mx,my,mw,mh=12,658,690,168
d.rectangle([mx,my,mx+mw,my+mh],fill=(205,225,235),outline=(120,120,120))
# continents from real lat/lon boxes (equirectangular, simplified outlines)
def LL(lat,lon): return mx+(lon+180)/360*mw, my+(90-lat)/180*mh
CONT=[[(58, -168),(58,-125),(49,-125),(49,-95),(30,-95),(30,-82),(25,-80),(15,-92),(10,-85),(5,-78),(-5,-80),(-10,-75),(-20,-70),(-35,-70),(-55,-68),(-35,-58),(-20,-40),(-10,-35),(0,-50),(5,-52),(10,-60),(15,-70),(20,-87),(25,-97),(30,-115),(40,-125),(50,-130),(58,-155)],[(70,-20),(70,10),(60,20),(55,30),(50,20),(45,10),(40,-5),(36,0),(36,10),(40,20),(45,28),(55,35),(60,30),(68,25),(70,10)],[(70,30),(70,60),(68,90),(72,120),(70,170),(65,180),(60,160),(55,140),(50,130),(45,120),(40,110),(35,100),(30,90),(25,80),(20,75),(10,75),(8,85),(15,95),(20,105),(30,120),(40,122),(50,130),(55,140),(60,155),(65,170)],[(35,10),(30,20),(20,30),(15,35),(10,40),(5,45),(0,40),(-10,35),(-20,30),(-30,25),(-35,20),(-30,15),(-20,12),(-10,13),(0,10),(10,0),(20,-5),(30,-5),(35,5)],[( -10,115),(-20,120),(-30,130),(-40,145),(-35,150),(-25,150),(-15,140),(-10,130)]]
for poly in CONT:
    d.polygon([LL(la,lo) for la,lo in poly],fill=(120,170,110),outline=(80,120,80))
PINS=HERO+CARDS; OFF={3:(14,2),7:(2,14),11:(12,10),12:(-16,12),1:(0,0),2:(0,0),4:(0,0),5:(0,0),6:(0,0),8:(0,0),9:(0,0),10:(0,0),13:(0,0)}
for (n,pl,fi,ch,col,hl,dk,src,la,lo,sk) in PINS:
    px,py=LL(la,lo); dx,dy=OFF.get(n,(0,0)); cx,cy=px+dx,py+dy
    if (dx,dy)!=(0,0): d.line([px,py,cx,cy],fill=RED,width=1)
    d.ellipse([cx-9,cy-9,cx+9,cy+9],fill=RED,outline=(255,255,255),width=1); d.text((cx-3 if n<10 else cx-6,cy-6),str(n),font=BOLD(9),fill=(255,255,255))
# LEGEND beside map
lx=714; d.text((lx,658),'LEGEND · 1-13',font=BOLD(10),fill=RED)
for i,(n,pl,fi,ch,col,hl,dk,src,la,lo,sk) in enumerate(PINS):
    yy=674+i*11; d.ellipse([lx,yy,lx+9,yy+9],fill=RED); d.text((lx+12,yy-1),f'{n} {pl} — {hl[:34]}',font=SANS(8),fill=INK)
# ALSO (25 more, 3 columns, chip label on every item)
d.text((12,832),'ALSO ON TUESDAY 24 NOVEMBER — 25 MORE STORIES',font=BOLD(10),fill=RED); d.line([12,846,1012,846],fill=RED,width=1)
for i,(n,pl,hl,ch) in enumerate(ALSO):
    c,r=i//9,i%9; x=12+c*338; y=850+r*11; d.text((x,y),f'{n} {pl}: {hl} [{ch}]',font=SANS(7),fill=INK)
# DATE CHECK
d.rectangle([12,950,1012,1002],fill=(255,235,235),outline=RED,width=1)
d.text((18,954),'DATE CHECK',font=BOLD(9),fill=RED); txt(18,966,wrap('Every story above happened or was first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC. LEFT OUT (not 24 Nov): Hormuz mine claims (23 Nov); Nvidia Huang returns as CEO (23 Nov); EU 22nd sanctions package (23 Nov); COP31 ends with no deal (22 Nov); Merkury corvette sunk (22 Nov); El Chapo Isidro arrested (Fri 20 Nov); Cikande factory fire started (Sat 21 Nov); Trump hush-money appeal ruling (23 Nov); ATP Finals (22 Nov); Las Vegas GP (21 Nov). NOT YET: Shenzhou-24 launch (Wed 25 Nov 00:18 UTC); MPR session to pick VP (11 Dec); Huawei sentencing (Sep 2027); Hasina returns to Bangladesh (16 Dec).',SANS(8),980),SANS(8),lh=10)
d.text((12,1006),'Sources: dailysummaryof.com · Astrova · Horizon · WSOC/AP · Reuters · UKMTO · CAS · CMSA.  CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side only.  Scenes are drawn illustrations, not photographs.',font=SANS(7),fill=(90,90,90))
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True); im.save(OUT)
print('saved',OUT)
