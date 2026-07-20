# Research Proposal: A Pipeline from Paper 1 — Deepening the Mechanism, then Modelling the Trajectory

*Qingyun Lyu — research proposal / follow-up programme for supervision*
*Builds on Paper 1 ("Value Co-Creation and Attenuation in a Social Virtual World") and on Prof. Yansong Hu's lecture, "Unlocking Service Provider Excellence: Expanding the TCQ Framework" (Journal of Service Research).*

---

> **中文导读**
> 这是一份"接着 Paper 1 往下走"的研究规划。它要解决一个我自己材料里没有讲透的张力：**Hu 的讲座把"用 HMM 把价值共创轨迹量化"变得极其诱人，但会议 mentor 明确提醒"下一篇先别急着做量化，把质性做深"。** 我的结论是——两者都对，关键在**排序**。所以我把后续拆成两篇、并明确先后：
> **Paper 2（近期，质性做深）**：不是换平台、换方法，而是把 Paper 1 只"描述"出来的**机制/过程**真正讲透——具身性如何"构成"（而非放大）共创与衰减、衰减的"慢侵蚀 vs. 快崩溃"两种模式、生态位互赖如何让衰减扩散。这直接回应会议意见，也为量化打好地基（构念、词典、编码都出自这里）。
> **Paper 3（中期，量化建模，接 Hu）**：在 Paper 2 打好的机制之上，才上 HMM——把共创建成隐状态+转移的动态轨迹，区分"促进机制 vs. 预防机制"，并用 **LV/奢侈品悖论**作为理论上最新颖的调节变量。
> 这样三篇共用一个田野（Light World，可加一个对照案例）、一条构念线（co-creation ↔ attenuation），是"强三篇博士论文"的结构。文末还评估了导师从 AI 拿到的"Plan C"（好直觉、坏执行，已被 Paper 3 吸收并修正），并给出与 Hu 合作的建议。

---

## 1. The through-line

The programme has one spine and I want to protect it: **co-creation in embodied virtual worlds
is a dynamic trajectory — value is built through interaction, crystallises into interdependent
roles, and then erodes when the conditions sustaining those roles are withdrawn.** Paper 1 maps
that trajectory qualitatively. The follow-up work does two further things to it — *explains* the
mechanism that drives it (Paper 2), then *measures and predicts* it at scale (Paper 3) — while
staying on one field site (Light World, plus one comparative case) and one construct family
(co-creation ↔ attenuation ↔ co-destruction). Compounding a single site and a single construct
across papers is what makes a coherent PhD rather than three unrelated studies, and it is the
main reason I am wary of proposals that restart on a new platform (see §6).

```
   Paper 1  ──────────▶  Paper 2  ──────────▶  Paper 3
  (revising)            (near-term)           (medium-term)
  QUALITATIVE           QUALITATIVE,          QUANTITATIVE /
  FOUNDATION            DEEP & PROCESSUAL     MIXED, DYNAMIC MODEL
  "here is the map"     "here is the engine   "here is the trajectory
                         and the clock"        at scale, and its levers"
  constructs, roles,    embodiment-as-        HMM latent states +
  barriers, the arc     mechanism; slow vs.   promotion/prevention
                        crash modes; inter-   mechanisms; LV/brand
                        dependence            heterogeneity moderator
        └── codes / dictionary / validated constructs flow rightward ──▶
```

## 2. The sequencing decision (the heart of this proposal)

My earlier notes jumped straight from Hu's lecture to an HMM study as "Paper 2." Having sat with
the conference feedback, I think that ordering is wrong, and correcting it is the single most
important judgement in this document.

**Why deepen the qualitative mechanism first, and only then model it:**

1. **The conference said so, and it was right.** The explicit advice was: *do not rush the next
   paper into quantitative method; make the qualitative work deep.* This was not conservatism —
   it was a diagnosis that my constructs are still described more than explained (see the Paper 1
   reflection).
2. **An HMM is only as good as the constructs it operationalises.** Hu's power comes from a
   *validated* set of building blocks and a *disciplined* dictionary behind the text-mining. If I
   run an HMM over a mechanism I have only sketched, I reproduce Paper 1's weakness in a more
   expensive, less forgiving form — a precise model of a vague construct. Paper 2 is what produces
   the building-block dictionary and the state definitions that Paper 3 needs as *inputs*.
3. **The two questions are genuinely different.** "How and why does co-creation turn into
   attenuation, and what is specific to embodiment?" is a *theory/mechanism* question best
   answered qualitatively. "Can this trajectory be represented as latent states with identifiable
   transitions and leverage points, at scale?" is a *measurement/prediction* question suited to
   HMM. Trying to answer both in one paper is what makes each shallow.

So the tension between Hu's method-pull and the conference's caution is not a contradiction to
resolve by picking a side; it is resolved by **ordering**. Paper 2 honours the caution; Paper 3
cashes in the method. Below I specify each.

## 3. Paper 2 (near-term): the processual mechanism of co-creation attenuation

**Working title.** "From Building to Leaving: A Processual Account of Co-Creation Attenuation in
an Embodied Social Virtual World."

**Motivation.** Paper 1 establishes *that* co-creation attenuates along a role trajectory. Paper 2
explains *how and why*, and pins down what embodiment specifically contributes — the two things
the conference found missing. It is the paper that turns "attenuation" from a labelled outcome
into a specified mechanism, which is also what best protects the construct from the "is it really
new?" objection.

**Research questions.**
- RQ1. Through what mechanism does embodied co-creation *constitute* (not merely intensify) both
  value creation and its erosion? (non-portability of built resources; removal of individual
  remedies so platform silence becomes structural; spatially-felt depopulation)
- RQ2. How do structural barriers emerge over time and *compound through role interdependence*,
  such that the withdrawal of one role's conditions erodes the value other roles can create
  (e.g., when creators leave, mentors have no one to mentor)?
- RQ3. Under what conditions does attenuation take a *slow, cumulative* form versus a *fast,
  rupture* form, and what distinguishes the two?

**Theory.** Service-dominant logic and the co-creation/co-destruction literature, but used to
build **process theory**: attenuation as the bridge that makes the bright and dark sides one
trajectory, positioned against Sahaym et al. (2023), Tuunanen's work, Plé and Chumpitaz Cáceres
(2010), and Echeverri and Skålén (2011, 2021). Embodiment (Belk, 2013) supplies the constitutive
properties in RQ1.

**Method (continuity, deepened — not a restart).** Stay on Light World and extend the *same*
qualitative apparatus toward a **longitudinal / process design**: follow a set of worlds and
users across time (revisits over several months), reconstruct individual arcs from entry through
contribution to disillusion and exit (process-tracing / critical-incident analysis), and — to
isolate what is specific to embodiment — add a *light comparative anchor*: a matched non-embodied
or screen-based community, used not as a full second case but as a contrast that lets me say
which properties are embodiment-specific. This directly answers the conference's "what is
different in virtual environments?" without abandoning the field site.

**Contribution & fit.** A processual, mechanism-level theory of how engagement-generated value
declines in embodied communities, with the slow-vs-rupture typology as a clean conceptual
addition. Because it is mechanism-deep and theory-forward, it can aim higher than a purely
descriptive paper — an IS/online-community or service outlet that rewards process theory (e.g.,
*Information Systems Journal*, *Journal of Service Research*, or *Internet Research*/*OIR* for
continuity). It also produces the coded, validated building blocks Paper 3 consumes.

## 4. Paper 3 (medium-term): modelling the trajectory at scale (the Hu bridge)

**Working title.** "Modelling Co-Creation as a Dynamic, Multi-State Trajectory in Branded Virtual
Worlds: An Extended-TCQ, HMM Approach."

**Motivation.** With a validated mechanism and dictionary from Papers 1–2, Hu's approach becomes
directly applicable — and now it has something rigorous to operationalise. Paper 3 makes the
trajectory *measurable, comparable and predictable*, and separates the levers that deepen
co-creation from those that arrest its decline.

**Research questions.**
- RQ1. Can users' co-creation in an SVW be represented as latent states with identifiable
  migration paths (co-creation ↔ attenuation)?
- RQ2. Which building-block interactions act as **promotion mechanisms** (deepen co-creation)
  versus **prevention mechanisms** (arrest attenuation)? — Hu's asymmetry, transferred.
- RQ3. How does **brand/space value-logic** — mass-market/accessibility vs.
  luxury/exclusivity — moderate these trajectories? (the LV puzzle)

**Theory — an Extended-TCQ adapted to virtual worlds.** I will carry Hu's nine building blocks
into the SVW setting rather than borrow them wholesale:

| Hu's TCQ building block | Virtual-world adaptation |
|---|---|
| Touchpoints | world / avatar / creation-toolkit touchpoints |
| (External) context | spatial, normative and governance context |
| Functional qualities | stability, latency, moderation, toolkit accessibility |
| Experiential qualities | immersion, belonging, aesthetic dwelling |
| CX dimensions (emotional/cognitive/social/physical) | + **embodiment** as a fifth dimension |

The moderator comes from brand-community and luxury-branding literature: brand value-logic
(accessibility vs. exclusivity) conditions whether openness and democratised co-creation help or
hurt.

**Method & data.** Mixed-method, continuous with Papers 1–2. Stage 1 (already done): qualitative
coding yields the building-block dictionary and barrier taxonomy. Stage 2: text-mine longitudinal
public chat / event and creation traces into weekly/monthly indicators; estimate an HMM of latent
co-creation states and transitions; read the qualities × elements interactions as promotion vs.
prevention mechanisms; test brand-type moderation. Keep Light World (existing access + ethics
approval) and add **one comparative branded space, including a luxury/exclusivity case**, to power
RQ3. HMM is the primary model (simple, interpretable, and — unlike optimal-matching sequence
analysis — natively suited to *early-warning*, i.e. predicting migration); a Transformer/LLM
variant is a robustness extension, not the headline.

**The LV / brand-heterogeneity hook (the theoretical novelty).** Reframe the Wharton observation
that luxury brands (e.g., LV) can fare *worse* in open online communities: "different brands,
different results" becomes **"the same mechanism, opposite valence depending on the brand's value
logic."** For exclusivity-based brands, the very openness and high interaction that act as a
*promotion* mechanism for mass brands can dilute scarcity and aura — tipping co-creation into
attenuation. That is a boundary condition, not a contradiction, and it is the most publishable
idea in the whole pipeline.

**Contribution & fit.** (a) first dynamic, state-based operationalisation of co-creation
attenuation; (b) extends TCQ from service firms into branded virtual worlds (answering Hu's own
suggestion); (c) the brand-value-logic moderator as a genuine theoretical boundary. Fit: *Journal
of Service Research*, *Information & Management*, *Journal of Business Research*, or *OIR* — chosen
by which framing (service vs. online-community) I lead with.

## 5. How the three papers compound

| | Paper 1 (revising) | Paper 2 (near) | Paper 3 (medium) |
|---|---|---|---|
| Question | *What* is the trajectory? | *How & why* does it work? | *How much / which levers*, at scale? |
| Method | Netnography + interviews | Longitudinal/process qualitative + light comparison | Text-mining + HMM (mixed) |
| Object | constructs, roles, barriers | embodiment mechanism; slow/crash modes; interdependence | latent states, transitions, moderators |
| Field site | Light World | Light World (+ contrast anchor) | Light World + comparative luxury case |
| Feeds forward | the arc | the dictionary + validated constructs | the model + boundary condition |

One site, one construct family, three escalating questions. Each paper is a legitimate standalone
contribution *and* a necessary input to the next.

## 6. Appraisal of the AI-generated "Plan C" (so we can close it out)

The "Plan C" you were given (Tencent Yuanbao: *Understanding Dynamics of Metaverse Value
Co-Creation*, TraMineR sequence analysis over Roblox/Decentraland logs, three states
Passive/Socializer/Creator, 8-month timeline) has **one sound instinct and several disqualifying
execution flaws**. I want to keep the instinct and discard the execution:

- **Right:** model co-creation as dynamic, multi-state trajectories with a prevention/early-
  warning purpose, combining behavioural + textual data. This instinct is convergent with Hu and
  with my own agenda — and it is fully absorbed by **Paper 3**.
- **Wrong / risky:** (1) *data infeasibility* — individual-level longitudinal logs from Roblox or
  Decentraland are not available at the needed granularity, whereas my real asset is Light World
  access via immersive netnography, interviews and ethics approval; (2) *discontinuity* —
  switching platform, method and construct focus severs Paper 1's thread and forfeits the
  compounding in §5; (3) *it drops my signature contribution* — a generic Passive/Socializer/
  Creator ladder has no attenuation, no critic/exit, no governance, i.e. it models the bright
  side and misses exactly what my work is about; (4) *under-justified method swap* — sequence
  analysis describes/clusters observed sequences, whereas HMM infers latent states + transitions
  and supports early-warning far more naturally; (5) *internal contradiction* — "track users
  6–12 months" cannot coexist with an "8-month data-to-submission" timeline unless the data are
  archival, which returns us to the feasibility problem.

**Verdict:** treat Plan C as a brainstorming spark, not a blueprint. Its defensible core is
subsumed by Paper 3, with feasibility (Light World, not Roblox/Decentraland), continuity (same
construct), and method (HMM, not sequence analysis) fixed — and the sequencing in §2 adds the
qualitative depth Plan C skips entirely.

## 7. Assets, feasibility, risks, and collaboration

- **Assets.** Live, ethically-approved Light World access; demonstrated immersive-netnography
  capability; a full Paper 1 coding scheme that seeds the Paper 3 dictionary; and a distinctive
  construct (committed-to-critic conversion) that no generic engagement study has.
- **Main risk — single platform.** Mitigated by adding a light comparative anchor in Paper 2 and
  a comparative luxury case in Paper 3, which also *creates* the theoretical payoff (embodiment-
  specificity; brand-value moderation) rather than merely hedging.
- **Data-capture risk for Paper 3.** Longitudinal public chat/event/creation traces on Light
  World need a documented, ethics-consistent capture protocol; scoping this is an early Paper 3
  task and a reason it is medium-, not near-term.
- **Collaboration with Prof. Hu.** He explicitly encouraged extending TCQ into virtual worlds and
  raised the LV puzzle himself. Paper 3 is the natural vehicle; I would like your view on
  inviting him as an advisor/collaborator on that paper specifically, given the method is his.

## 8. Decisions I'd like to settle with you

1. **Endorse the sequencing?** — qualitative-deep Paper 2 *before* quantitative Paper 3, rather
   than jumping straight to HMM. (My recommendation: yes.)
2. **Paper 2 scope** — is the longitudinal/process design on Light World, plus a light non-
   embodied contrast, the right shape, or would you prefer a single-site deep process study with
   no comparison?
3. **Paper 3 comparative case** — do we commit now to sourcing a luxury/exclusivity branded space
   for the LV hook, and start scoping data-capture feasibility in parallel?
4. **Hu collaboration** — approach him about co-authoring/advising Paper 3?
5. **Journal targeting** — lead Paper 2 as IS process theory or keep the OIR/online-community
   framing for track-record continuity?
