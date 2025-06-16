# AGENTS.md — Project Codex Guidance

## 🧠 Project Name: Momentum

A full-stack AI-powered lifestyle app designed to help creators, devs, and wellness seekers build momentum through daily movement, creativity, and frictionless content sharing.

This app is intentionally personal — it exists to help the developer (Chris) regain confidence, build social visibility, and create movement habits like paddleboarding while continuing to grow technically.

---

## 🧰 Stack

| Layer       | Tech                                                        |
| ----------- | ----------------------------------------------------------- |
| Backend     | Django 5 + Django REST Framework                            |
| Database    | Postgres                                                    |
| Frontend    | Flutter                                                     |
| AI Tools    | OpenAI or Replicate (image gen)                             |
| Dev Tooling | Codex + GitHub                                              |
| Optional    | HealthKit / Google Fit, geolocation, image upload, Firebase |

---

## 📦 Django Apps

- `core`: User profiles, habit tracking, lockout logic
- `prompts`: Daily creative challenges + responses
- `movement`: Tracks physical sessions (walk, paddle, etc.)
- `content`: AI-generated media + auto-share logs

---

## 🔒 Lockout System

The app enforces a **daily physical movement minimum** before allowing the developer to:

- Access image generation tools
- Push code via Codex (optional)
- Post content or complete creative prompts

This uses:

- `DailyLockout` model (linked to movement sessions)
- Optional GPS or camera check-ins
- Unlocks when daily movement minimum is met

---

## 🌊 Special Behavior — Paddleboard Incentive

When paddleboarding is logged:

- App triggers a **confidence reward loop** (special badge/sticker/meme)
- Unlocks premium AI tools for the day (e.g., animation gen)
- Option to auto-generate a “Paddle Day” social post with scenic AI imagery

---

## 🧪 Dev Notes

- All models must be API-ready with DRF serializers and route wiring
- Codex should avoid hardcoding timestamps or user IDs
- Codex is allowed to scaffold admin views and seeders where helpful

---

## 🎯 Project Mission

Chris is using this tool to:

- Lose ~15 pounds
- Get out of the house more consistently
- Build quiet confidence in showing up in the world
- Generate content that _feels authentic_ without being glued to social media
- Learn, ship, and heal through full-stack dev

---

## 🧙‍♂️ Codex Behavior

Codex should:

- Scaffold with best practices
- Prioritize Chris’ goals over generic app polish
- Encourage self-reflection and creative reuse
- Suggest new prompts, challenges, or visual art based on usage patterns

---

## ✅ Next Milestones

1. Complete model + API scaffold via Codex
2. Implement movement lockout system
3. Add AI image generation + share flow
4. Add paddleboard tracking + incentive logic
5. Build frontend screens and state
6. Launch private MVP and begin personal use

---

_This app is about showing up: to the code, to the world, and to the water._
