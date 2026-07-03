# Roadmap and Demonstration

## Roadmap

| Phase | Goal | Infrastructure | Exit criteria |
|---|---|---|---|
| MVP / demo | demonstrate a working system and core scenarios | VPS + Docker Compose | demo flow, backup, basic observability |
| Pilot | load real data and collect feedback | VPS + regular backup procedures; migrate to external S3 as media grows | import of a real collection, list of UX/data issues |
| First customers | ensure predictable operations | separate DB, external S3-compatible object storage, monitoring | paying organization, recovery procedure, support |
| Growth | prepare scaling and regional contours | separate DB, external S3-compatible object storage, separate workers (import), read optimization, regional strategy | tenant count growth, SLA expectations, regional tenant distribution |

## Screenshots and Demo

### Global map

<figure markdown>
![UI_1](/portfolio/assets/botanical/map.png)
<figcaption>Global map</figcaption>
</figure>

### Plant management

<figure markdown>
![UI_2](/portfolio/assets/botanical/plants.png)
<figcaption>Plant management</figcaption>
</figure>

### Places and boundaries management

<figure markdown>
![UI_3](/portfolio/assets/botanical/places.png)
<figcaption>Places and boundaries management</figcaption>
</figure>

### AI-assisted plant import

<figure markdown>
![UI_4](/portfolio/assets/botanical/import.png)
<figcaption>AI-assisted plant import</figcaption>
</figure>

## What this project demonstrates

This project demonstrates my ability to:

* work at the intersection of system analysis, backend design, implementation, and deployment.
* take an idea through to a running system with multiple availability zones and a scaling roadmap
* strategically plan implementation of a small-to-medium-scale SaaS
* safely and in a controlled way apply LLM code generation for feature implementation
