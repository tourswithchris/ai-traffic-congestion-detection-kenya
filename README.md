# Nairobi Smart Traffic AI (Prototype)
AI prototype that detects traffic congestion levels from roadway camera images using a CNN classifier.

**Use case:** congestion monitoring, incident awareness, and city traffic analytics.  
**Status:** prototype / proof-of-work (non-production).

---

## What this repo is (and isn’t)

### ✅ Included (public proof-of-work)
- Prototype CNN-based congestion classifier (image → congestion level)
- Demo workflow (notebook) using sample images
- Pilot brief (1-page PDF) for stakeholders
- Results & benchmark artifacts (screenshots/tables)
- High-level architecture (no deployment details)

### ❌ Not included (kept private)
- Camera ingest (RTSP/streaming), production API, infra & deployment
- Full training pipeline + operational configs
- Any keys/secrets or environment configuration

---

## High-level Architecture (Prototype)

```mermaid
flowchart LR
  A[Traffic Camera / Image Source] --> B[Frame Sampling]
  B --> C[CNN Inference]
  C --> D[Congestion Level: Low / Medium / High]
  D --> E[Alerts + Analytics Dashboard (future)]
