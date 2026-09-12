---
title: Hanjin Gong — Full CV
redirect_from:
  - /english.resume.html
  - /gong.hanjin.english.html
description: >-
  Full curriculum vitae of Hanjin Gong (Richard Gong), senior full-stack and
  financial-software engineer in Tokyo, Japan. Nomura, HSBC, Ctrip. Fixed income,
  JGB portfolio optimisation, convex optimisation with CVXPY, algorithmic trading,
  Java, Python, TypeScript, Go, kdb+/q, Kubernetes, AWS.
layout: default
page_kind: cv
---
# Hanjin Gong

Richard Gong · Senior Software Engineer

**Financial Systems · Backend & Full-Stack Development**

Tokyo, Japan · Open to relocation to the UK or Canada

[Email](mailto:richardgong1988@gmail.com) · [LinkedIn](https://www.linkedin.com/in/hanjin-gong-algorithms/) · [GitHub](https://github.com/richardgong1987) · [Download PDF](gong_hanjin_english.pdf)

## Profile

Software engineer with {% include years.html %} years of experience across investment banking, retail banking, payments and consumer platforms. My work combines financial-domain understanding with hands-on backend, frontend and delivery engineering. At Nomura, my experience includes Java financial applications alongside JGB portfolio optimisation and risk analytics using Python and CVXPY.

I work across requirements, implementation, integration and deployment, and independently develop automated trading strategies in C# with cTrader Automate.

## Professional experience

### Senior Engineer | Nomura Securities

Contract assignment through Michael Page Japan

Tokyo, Japan · June 2022 – Present

Platform: Japan Government Bond (JGB) Portfolio Optimisation & Risk Analytics Platform — used by rates PMs, traders, and risk officers on the Tokyo desk.

- Develop and maintain financial applications in Java at Nomura, alongside Python and TypeScript development, delivering application features and maintaining existing code.
- Built the JGB optimisation engine in Python + CVXPY: formulated risk-adjusted carry/PnL objectives under duration, DV01, issuer-concentration, liquidity-bucket, and regulatory constraints. Tuned solver (ECOS / OSQP) selection by problem shape and achieved sub-second solve times on representative books.
- Designed low-latency risk APIs in Python (Flask/FastAPI) and Node.js (NestJS) exposing optimisation, scenario PnL, and exposure-decomposition endpoints; improved tail latency through response caching, lazy curve rebuilds, and vectorised pandas hot paths.
- Re-architected the legacy monolith into Dockerised microservices on AWS (EKS + ALB), with per-service SLOs, blue/green deploys, and deployment lead time reduced from days to minutes. Introduced structured logging, Datadog dashboards, and trace propagation across the optimisation → risk → UI chain.
- Owned risk decomposition logic — positions broken down by tenor bucket, issue, and sector; key-rate DV01 and shock-scenario PnL computed incrementally to support interactive what-if flows instead of full recomputation per click.
- Built the Next.js (App Router) trader-facing front end in TypeScript: server components for heavy data fetching, streaming SSR for first paint, Zustand for interactive optimisation state. Replaced an Angular legacy path for new modules while maintaining interop during migration.

- Develop GitLab CI build and packaging jobs and Jenkins pipelines that invoke Ansible; maintain deployment playbooks and Kubernetes manifests.

Stack: Java · Python (CVXPY, NumPy, pandas, FastAPI, Flask) · Node.js (NestJS) · TypeScript / Next.js 16 · Angular · Redis · kdb+/q (read-side) · Docker · Kubernetes · AWS (EKS, ALB, S3) · GitLab CI/CD · GitLab Runner · Jenkins · Ansible · Datadog

---

### Senior Software Engineer — Nisshin

Tokyo, Japan · Jan 2021 – Jun 2022

Platform: Talent Management System (HR SaaS)

- Built REST APIs on Java 17 + Javalin with a React / TypeScript front end for real-time HR analytics; enforced strict layering (handlers → services → repositories) to keep the codebase testable as the team grew.
- Introduced a Redis-backed caching strategy with TTL + cache-aside invalidation and rewrote N+1 MySQL queries into batched joins — cut median page-load time by ~30% and removed a recurring DB CPU spike during morning login peaks.
- Developed load and stress-testing scripts in Python and Go to evaluate application performance under concurrent workloads and support performance troubleshooting.
- Stood up GitLab CI/CD pipelines (build, test, container scan, staging deploy), mentored 5+ junior engineers on code review, branching model, and observability.

Stack: Java 17 · Javalin · Python · Go · React · TypeScript · MySQL · Redis · GitLab CI · Load & stress testing

---

### Technical Leader — HSBC Bank

Guangzhou, China · Jan 2019 – Jan 2021

Platform: Overseas Bank Account Opening (30+ jurisdictions)

- Led architecture for a Java + Node.js microservices estate handling cross-border KYC, document capture, and account provisioning across 30+ countries with per-region compliance rules.
- Drove workflow automation (orchestration + retries + dead-letter handling) that cut manual operational overhead by ~20% and shortened average account-opening turnaround meaningfully.
- Rolled out Datadog observability across services — SLOs, latency histograms, error-budget alerting — replacing ad-hoc log grepping with actionable dashboards for on-call engineers.

Stack: Java · Spring Boot · Node.js · Oracle · MySQL · Kafka · Docker · Datadog

---

### Technical Leader — SurLead

Manila, Philippines · Mar 2015 – Jan 2019

- Delivered FinTech and e-commerce client platforms in Java + TypeScript on Oracle / MySQL, owning architecture, delivery, and team leadership end-to-end.
- Migrated legacy deployments to Docker and split a monolith into NestJS / Express microservices — shortened release cycles by ~40% and enabled independent team ownership per service.

Stack: Java · TypeScript · NestJS · Express · Oracle · MySQL · Docker

---

### Full-Stack Engineer — Ctrip

Shanghai, China · Jun 2013 – Feb 2015

Platform: Ctrip Wireless (travel-booking platform, millions of DAU)

- Co-designed the frontend framework (Node.js · Backbone.js · jQuery) used across booking, payment, and loyalty modules — standardised component patterns across product lines.
- Shipped user-facing features on the booking and payment critical path, serving millions of daily users with tight SLAs during peak travel seasons.

Stack: Node.js · Backbone.js · jQuery · Java (backend integrations) · MySQL

---

### Front-End Engineer — Qunshuo

Shanghai, China · Aug 2010 – May 2013

- Built enterprise web apps on Java / Spring / Hibernate / MySQL with contemporary JS frameworks; delivered a SAP-integrated childcare module on schedule.

---


## Core technologies

- **Languages:** Java, Python, Go, TypeScript/JavaScript, Node.js and C#/.NET.
- **Applications:** Spring Boot, Javalin, FastAPI, Flask, NestJS, Express, React, Next.js and Angular.
- **Data and integration:** SQL, Oracle, MySQL, Redis, Kafka, RabbitMQ, kdb+/q, REST and gRPC.
- **Delivery:** GitLab CI/CD, Jenkins, Ansible, Docker, Kubernetes, GitHub Actions, AWS and Azure.
- **Quantitative development:** CVXPY, NumPy, pandas, portfolio optimisation, yield curves, DV01/key-rate duration and scenario PnL.

## Independent trading research

**Personal research and live trading | 2025–present**

- Develop automated cTrader strategies in C#, separating signal generation, execution, position management and diagnostics.
- Build reusable indicator components using ATR, Bollinger Bands, fractals, previous-day levels and volatility filters.
- Implement position sizing, stop-loss and take-profit rules, partial exits and broker-specific volume normalisation using OnTick and OnBar events.
- Evaluate strategies through backtesting, sensitivity checks and live observation, with explicit R-multiple risk controls, drawdown monitoring and transaction-cost assumptions.

## Education

**MSc Computer Science | University of Liverpool, UK**  
Expected 2027

**Associate Degree, Science & Technology | Shanghai College of Science & Technology**  
2007–2010

## Certifications and languages

- Cisco Certified Technician (CCT) — Routing & Switching.
- Microsoft Certified Professional & Specialist (2016).
- AI, Business & the Future of Work — Lund University (2023).
- English (fluent) · Chinese (native).

## Contact

Open to senior backend, full-stack and financial-software engineering opportunities, especially in trading, risk and market-data systems.

[richardgong1988@gmail.com](mailto:richardgong1988@gmail.com) · [LinkedIn](https://www.linkedin.com/in/hanjin-gong-algorithms/) · +81 80-7006-5858
