from pathlib import Path
import struct, random, json
random.seed(9010)
OUT=Path('/Users/roylyl/Desktop/晚渡 - FL Studio 原创工程')
PPQ=480
END=384
# Original score. MIDI program numbers are zero-based General MIDI.
def vlq(n):
    b=[n&127]; n>>=7
    while n: b.insert(0,(n&127)|128); n>>=7
    return bytes(b)
def meta(k,s):
    s=s.encode() if isinstance(s,str) else s
    return bytes([255,k])+vlq(len(s))+s
class Part:
    def __init__(self,name,ch,program,vol,pan,reverb):
        self.name=name; self.ch=ch; self.events=[]; self.notes=[]
        self.events += [(0,0,meta(3,name)),(0,1,bytes([0xc0+ch,program]))]
        for cc,v in [(7,vol),(10,pan),(91,reverb),(93,0)]: self.events.append((0,2,bytes([0xb0+ch,cc,v])))
    def note(self,t,n,d,v):
        if t<0 or t>=END: return
        t=max(0,round(t*PPQ)); d=max(25,round(d*PPQ)); v=max(1,min(120,round(v)))
        d=min(d,END*PPQ-t)
        self.events.extend([(t,4,bytes([0x90+self.ch,n,v])),(t+d,3,bytes([0x80+self.ch,n,0]))]); self.notes.append([t,n,d,v])
    def cc(self,t,num,v): self.events.append((round(t*PPQ),2,bytes([0xb0+self.ch,num,v])))
    def data(self): return pack(self.events)
def pack(events):
    data=b''; last=0
    for t,p,b in sorted(events,key=lambda x:(x[0],x[1])): data+=vlq(t-last)+b; last=t
    data+=vlq(max(0,END*PPQ-last))+meta(47,b'')
    return b'MTrk'+struct.pack('>I',len(data))+data
parts=[Part('01 Fingerpicked Acoustic',0,25,89,39,25),Part('02 Acoustic Piano',1,0,75,74,36),Part('03 Finger Bass',2,33,94,64,8),Part('04 Trumpet - Vocal Melody',3,56,85,64,38),Part('05 Clean Electric',4,27,68,91,42),Part('06 String Ensemble',5,48,62,52,45),Part('07 Trombone Harmony',6,57,66,76,34),Part('08 Acoustic Drums',9,0,91,64,16),Part('09 Warm Electric Piano',7,4,63,30,32)]
guit,piano,bass,lead,elec,strings,trom,drum,rhodes=parts
sections=[(0,8,'Intro',.48),(8,16,'Verse A',.61),(24,8,'Pre-Chorus',.70),(32,16,'Chorus A',.84),(48,8,'Interlude',.65),(56,8,'Verse B',.64),(64,8,'Bridge',.55),(72,16,'Final Chorus',.94),(88,8,'Outro',.48)]
# Voice-led chords: root, guitar/piano voicing. B7 resolves to Em.
chords={'Em':(40,[52,59,64,67,71]),'Cmaj7':(36,[48,55,59,64,67]),'G':(43,[50,55,59,62,67]),'D':(38,[50,57,62,66,69]),'Am7':(33,[45,52,55,60,64]),'B7':(35,[47,54,57,63,66]),'EmD':(38,[50,55,59,64,67]),'C':(36,[48,55,60,64,67])}
progressions={'Intro':['Em','Cmaj7','G','D'],'Verse A':['Em','EmD','Cmaj7','G','Am7','Em','Cmaj7','B7'],'Verse B':['Em','EmD','Cmaj7','G','Am7','Em','Cmaj7','B7'],'Pre-Chorus':['Am7','Cmaj7','G','D','Am7','Cmaj7','B7','B7'],'Chorus A':['C','G','D','Em','C','G','Am7','B7'],'Final Chorus':['C','G','D','Em','C','G','Am7','B7'],'Interlude':['Em','Cmaj7','G','D','Am7','Cmaj7','B7','B7'],'Bridge':['Am7','Em','Cmaj7','G','Am7','Cmaj7','B7','B7'],'Outro':['Cmaj7','G','Am7','B7','Em','Cmaj7','Em','Em']}
barinfo={}
for start,count,section,energy in sections:
    prog=progressions[section]
    for i in range(count):
        b=start+i; chord=prog[i%len(prog)]; root,vo=chords[chord]; barinfo[b]=(chord,section)
        t=b*4; en=energy
        if section=='Outro': en*=max(.28,1-i*.1)
        # Fingerstyle eighth notes, alternating bass and upper voices; gentle natural timing.
        order=[0,2,3,1,4,2,3,2] if i%2==0 else [0,2,4,3,1,2,3,4]
        for j,idx in enumerate(order):
            if section=='Outro' and i>=6 and j>3: continue
            guit.note(t+j*.5+random.uniform(0,.022),vo[idx],.70 if idx else .92,(62 if j%2==0 else 51)*(.65+en*.5)+random.randint(-5,5))
        # Broad strums in choruses still retain individual MIDI voicing.
        if 'Chorus' in section:
            for beat in [0,1.5,2.5,3.5]:
                for k,n in enumerate(vo[1:]): guit.note(t+beat+k*.019,n,.38,48+en*15+random.randint(-5,4))
        # Piano: sparse replies before chorus, full but voice-led chords in chorus.
        if b>=4:
            beats=[0,2] if 'Chorus' in section else ([.25] if i%2==0 else [2.25])
            if section=='Bridge': beats=[0]
            if section=='Outro' and i>=6: beats=[0]
            for bt in beats:
                for k,n in enumerate(vo[1:4]): piano.note(t+bt+k*.023,n,1.7 if 'Chorus' in section else 2.8,42+en*18+random.randint(-4,4))
            if i%4==3 and section not in ['Outro','Bridge']:
                for j,n in enumerate([vo[3]+12,vo[2]+12,vo[1]+12]): piano.note(t+3+j*.25,n,.3,48-j*4)
        if b>=8 and not(section=='Outro' and i>=6):
            # melodic bass: root, fifth, octave and restrained approaches.
            pattern=[(0,root,1.65),(2,root+7,.8),(3,root+12,.65)] if 'Chorus' in section else [(0,root,2.7),(3,root+7,.75)]
            if section=='Bridge' or section=='Outro': pattern=[(0,root,3.5)]
            for bt,n,d in pattern: bass.note(t+bt,n,d,58+en*24+random.randint(-4,4))
            if 'Chorus' in section and i%2: bass.note(t+3.75,root+11,.20,62)
        # Clean guitar answers in the gaps, widens the chorus.
        if 'Chorus' in section or section=='Interlude':
            for bt,idx in [(0.5,1),(1.5,2),(2.5,3),(3.25,2)]: elec.note(t+bt,vo[idx]+12,.55,44+en*13)
        elif section=='Verse B' and i%2:
            for j,n in enumerate(vo[1:4]): elec.note(t+2.5+j*.4,n+12,.7,44)
        # Strings deliberately absent from the early verse.
        if section in ['Pre-Chorus','Chorus A','Final Chorus','Bridge']:
            for n in [vo[1]+12,vo[2]+12,vo[3]+12]: strings.note(t+.04,n,3.92,40+en*20)
            strings.cc(t,11,round(58+en*36+(i%4)*2))
        if section in ['Verse B','Bridge','Final Chorus']:
            for k,n in enumerate(vo[1:4]): rhodes.note(t+.1+k*.025,n,3.4,41+en*10)
        # Acoustic drums: cross-stick verse, snare chorus, fills at phrase boundaries.
        if b>=8 and b<92 and section!='Bridge':
            loud='Chorus' in section
            for j in range(8):
                if section=='Outro' and j%2: continue
                drum.note(t+j*.5+(.018 if j%2 else 0),42,.09,(46 if j%2==0 else 32)+en*12+random.randint(-5,4))
            for bt in ([0,1.5,2,2.75] if loud else [0,2.5]): drum.note(t+bt,36,.12,65+en*26)
            for bt in [1,3]: drum.note(t+bt+.018,38 if loud else 37,.12,60+en*25)
            if loud and i%2==1: drum.note(t+2.75,38,.1,34)
            if i==0 and section in ['Chorus A','Final Chorus','Interlude']: drum.note(t,49,.8,82 if loud else 65)
            if i%8==7 and section!='Outro':
                for j,n in enumerate([38,38,45,47,50,45]): drum.note(t+2.5+j*.25,n,.13,54+j*5)
                drum.note(t+3.5,46,.2,52)
        elif section=='Bridge' and i>=4:
            drum.note(t,36,.1,60)
            for j in range(4): drum.note(t+j,51,.25,37+i*2)
# Original melody motifs, in absolute pitch; rests between phrases allow brass breathing.
verse=[[(.5,64,.75),(1.5,67,.5),(2.25,66,.5),(3,64,.7)],[(0,62,1.5),(2,59,.65)],[(.5,64,.75),(1.5,67,.7),(2.5,71,1.0)],[(0,69,.7),(1,67,1.75)],[(.5,64,.5),(1.25,67,.5),(2,69,1.25)],[(0,67,.75),(1.25,66,.5),(2,64,1.35)],[(.5,62,.75),(1.5,64,.75),(2.5,67,.65)],[(0,66,1),(1.5,63,1.25)]]
pre=[[(.5,69,.75),(1.5,67,.5),(2.5,64,1)],[(0,67,1.25),(2,71,1.1)],[(.5,71,.75),(1.5,69,.5),(2.5,67,.9)],[(0,69,2.7)],[(.5,69,.7),(1.5,71,.7),(2.5,72,.75)],[(0,71,.75),(1,67,.6),(2,64,1.2)],[(0,66,1),(1.5,69,1.1)],[(0,66,1.2),(2,63,.65)]]
chorus=[[(0,67,.7),(1,71,.7),(2,72,1.45)],[(0,71,1),(1.5,69,.5),(2.25,67,1.1)],[(.5,66,.5),(1.25,69,.75),(2.5,74,1.0)],[(0,71,2.3),(3,67,.45)],[(0,67,.6),(1,72,.7),(2,76,1.25)],[(0,74,.75),(1,71,.7),(2,67,1.15)],[(.5,69,.75),(1.5,72,.75),(2.5,71,.65)],[(0,69,.75),(1,66,.7),(2,63,1.1)]]
bridge=[[(.5,64,1.25),(2,60,1)],[(0,59,2.5)],[(1,64,.75),(2,67,1)],[(0,62,2.5)],[(.5,64,.75),(1.5,67,.75),(2.5,69,.75)],[(0,71,1.2),(2,72,1.2)],[(0,69,.75),(1,66,.75),(2,63,1.2)],[(.5,66,1.5)]]
for start,count,section,en in sections:
    if section in ['Verse A','Verse B']: motif=verse
    elif section=='Pre-Chorus': motif=pre
    elif 'Chorus' in section: motif=chorus
    elif section=='Bridge': motif=bridge
    else: continue
    for i in range(count):
        notes=motif[i%8]
        for j,(bt,n,d) in enumerate(notes):
            if i>=8 and j==0 and i%4==0: bt+=.25; d=max(.3,d-.2)
            if section=='Final Chorus' and i==15: n=64 if j==2 else n; d=1.5 if j==2 else d
            lead.note((start+i)*4+bt+.016,n,d*.93,round(65+en*21)+random.randint(-5,4))
        if section=='Final Chorus' and i>=8:
            root,vo=chords[barinfo[start+i][0]]
            for bt,n,d in notes:
                candidates=[x for x in range(48,65) if x%12 in [q%12 for q in vo]]
                h=min(candidates,key=lambda x:abs(x-(n-7)))
                trom.note((start+i)*4+bt+.035,h,d*.88,63+random.randint(-3,3))
# Instrumental interlude is a distinct low register trumpet development.
for i in range(8):
    root,vo=chords[barinfo[48+i][0]]
    for j,idx in enumerate([2,3,4,3]): lead.note((48+i)*4+.5+j*.65,vo[idx],.48 if j<3 else .9,65+j*2)
# Intro/outro signature and ending cadence.
for b in [4,6,88,90]:
    for bt,n,d in [(.5,71,.75),(1.5,67,.65),(2.5,66,.5),(3.25,64,.6)]: elec.note(b*4+bt,n,d,48 if b<88 else 42)
for n in [52,59,64,67]: piano.note(94*4+(n%3)*.025,n,7.5,43)
lead.note(92*4+.5,67,1.1,65); lead.note(92*4+2,66,.7,59); lead.note(93*4,64,3.2,57)
for p in parts:
    for b,v in [(88,104),(90,91),(92,73),(94,52),(95,34)]: p.cc(b*4,11,v)
conductor=[(0,0,meta(3,'WANDU - Original composition / 88 BPM / E minor')),(0,1,meta(81,(round(60000000/88)).to_bytes(3,'big'))),(0,1,meta(88,bytes([4,2,24,8]))),(0,1,meta(89,bytes([1,1])))]
for b,c,name,en in sections: conductor.append((b*4*PPQ,1,meta(6,name)))
header=b'MThd'+struct.pack('>IHHH',6,1,len(parts)+1,PPQ)
(OUT/'MIDI'/'Wandu_Full_Arrangement.mid').write_bytes(header+pack(conductor)+b''.join(p.data() for p in parts))
for p in parts:
    (OUT/'MIDI'/(p.name+'.mid')).write_bytes(b'MThd'+struct.pack('>IHHH',6,1,2,PPQ)+pack(conductor)+p.data())
report={'bpm':88,'bars':96,'duration_seconds':END*60/88,'tracks':{p.name:len(p.notes) for p in parts},'sections':[{'bar':b+1,'bars':c,'name':n} for b,c,n,e in sections]}
(OUT/'score_manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,indent=2))
