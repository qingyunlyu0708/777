import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.family"] = "DejaVu Sans"

fig, ax = plt.subplots(figsize=(14, 9.0), dpi=200)
ax.set_xlim(-3, 103); ax.set_ylim(-20, 108); ax.axis("off")

TEAL="#2a9d8f"; RED="#e76f51"; GOLD="#e9c46a"
BARFILL="#f4f1de"; BARED="#6c584c"; INFILL="#e9ecef"

base, amp, mu, sl, sr = 16.0, 60.0, 44.0, 20.0, 30.0
def curve(x):
    x=np.asarray(x,dtype=float)
    s=np.where(x<=mu, sl, sr)
    return base+amp*np.exp(-((x-mu)**2)/(2*s**2))

for xx in (33,70):
    ax.plot([xx,xx],[-13,100],ls=":",color="#cccccc",lw=1,zorder=1)

xr=np.linspace(4,44,200); xf=np.linspace(44,96,200)
ax.plot(xr,curve(xr),color=TEAL,lw=9,solid_capstyle="round",zorder=3)
ax.plot(xf,curve(xf),color=RED,lw=9,solid_capstyle="round",zorder=3)

ax.text(15,float(curve(15))+3.2,"Value co-creation",color=TEAL,fontsize=13,
        fontweight="bold",rotation=46,ha="center",va="bottom")
ax.text(79,float(curve(79))+6.2,"Co-creation attenuation path",color=RED,fontsize=13,
        fontweight="bold",rotation=-25,ha="center",va="bottom")

roles=[(8,"Experiential\nparticipant"),(20,"Creation-oriented\nprosumer"),
       (30,"Social\norganiser"),(39,"Knowledge\nmentor"),(62,"Critics /\nnegotiators")]
for x,lab in roles:
    y=float(curve(x))
    ax.scatter([x],[y],s=95,color="white",edgecolor="#333",zorder=5,linewidth=1.6)
    ax.text(x,y+7,lab,fontsize=9.3,ha="center",va="bottom",color="#222",fontweight="bold")

ax.scatter([44],[float(curve(44))],s=160,color=GOLD,edgecolor="#333",zorder=6,linewidth=1.6)
ax.text(44,float(curve(44))+12.0,"Co-creation vitality\n(peak value)",fontsize=10.5,
        ha="center",va="bottom",color="#1d3557",fontweight="bold")

ax.scatter([90],[float(curve(90))],s=95,color="white",edgecolor="#333",zorder=5,linewidth=1.6)
ax.annotate("Exit",xy=(90,float(curve(90))),xytext=(95,float(curve(90))-10),fontsize=10,
    fontweight="bold",ha="center",color=RED,
    arrowprops=dict(arrowstyle="-|>",color=RED,lw=1.6))

ib=FancyBboxPatch((-2,-2),26,9,boxstyle="round,pad=0.4,rounding_size=2",
    fc=INFILL,ec="#333",lw=1.3,zorder=4)
ax.add_patch(ib)
ax.text(11,2.5,"Platform affordances\n× User resources",fontsize=9,ha="center",
        va="center",fontweight="bold",zorder=7)
ax.annotate("",xy=(6,float(curve(6))-1),xytext=(11,7),
    arrowprops=dict(arrowstyle="-|>",color="#333",lw=1.6))

leg=("Interaction activities -> value co-created\n"
     "- Exploratory   -> experiential / aesthetic\n"
     "- Creative        -> content / symbolic\n"
     "- Social            -> relational / emotional\n"
     "- Governance  -> normative / institutional")
lb=FancyBboxPatch((57,81),44,22,boxstyle="round,pad=0.5,rounding_size=2",
    fc="white",ec=TEAL,lw=1.3,zorder=4)
ax.add_patch(lb)
ax.text(58.6,92,leg,fontsize=8.7,ha="left",va="center",color="#222",zorder=7)

barriers=[(13,"Access &\nparticipation\nconstraints"),
          (38,"Fragile\ninteraction\ninfrastructure"),
          (57,"Relational &\nemotional\nerosion"),
          (73,"Normative\nbreakdown"),
          (88,"Perceived platform\nunresponsiveness")]
for i,(x,lab) in enumerate(barriers):
    w=13.0
    bb=FancyBboxPatch((x-w/2,-10.2),w,8.8,boxstyle="round,pad=0.3,rounding_size=1.5",
        fc=BARFILL,ec=BARED,lw=1.2,zorder=4)
    ax.add_patch(bb)
    ax.text(x,-5.8,f"{i+1}. "+lab,fontsize=7.5,ha="center",va="center",color="#3a2e26",zorder=7)
    ax.annotate("",xy=(x,float(curve(x))-1.2),xytext=(x,-1.3),
        arrowprops=dict(arrowstyle="-|>",color=BARED,lw=1.05,ls="--",alpha=0.75))

ax.annotate("",xy=(88,-13.2),xytext=(13,-13.2),
    arrowprops=dict(arrowstyle="-|>",color=BARED,lw=1.3))
ax.text(50.5,-15.8,"recursive, cumulative barrier sequence",fontsize=8.4,style="italic",
        color=BARED,va="center",ha="center")

ph=[(16,"INITIAL ACCESS"),(51,"SUSTAINED INTERACTION & CO-CREATION"),
    (86,"DISENGAGEMENT & WITHDRAWAL")]
for x,lab in ph:
    ax.text(x,-18.6,lab,fontsize=9,ha="center",va="center",color="#1d3557",fontweight="bold")
ax.annotate("",xy=(101,-18.6),xytext=(2,-18.6),
    arrowprops=dict(arrowstyle="-|>",color="#1d3557",lw=1.4))

ax.text(-1.5,55,"Co-creation vitality (value)",rotation=90,fontsize=10.5,
        va="center",ha="center",color="#1d3557",fontweight="bold")

ax.set_title("A process model of value co-creation and attenuation in a social virtual world",
             fontsize=14.5,fontweight="bold",pad=14)

plt.tight_layout()
for ext in ("png","pdf","svg"):
    fig.savefig(f"figure_process_model.{ext}",dpi=200,bbox_inches="tight",facecolor="white")
print("saved png/pdf/svg")
