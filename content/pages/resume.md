+++
title = "Resume"
path = "resume"
template = "resume.html"
description = "Josh McKinney: software engineer for backend, platform, security, and developer tooling. OpenAI (Codex), Amazon/AWS security, Ratatui co-maintainer."

[extra]
og_image = "og/resume.png"
engagements = [
    { years = "2015–16", client = "State of Tennessee", work = "Led development of the budget system managing the State's $32B annual budget, integrated with PeopleSoft", stack = "C#, SQL Server, SSAS, BIDS" },
    { years = "2014–15", client = "Victorian Dept of Health and Human Services", work = "Shipped features and fixes for a government budget management system", stack = "ASP.NET, VB.NET, JavaScript" },
    { years = "2014", client = "Readify", work = "Replaced a legacy Dynamics CRM system with CRM Online integrated with billing and internal processes", stack = "ASP.NET MVC, Azure, MYOB API" },
    { years = "2014", client = "iCareHealth", work = "Built reporting for an aged care facility management system", stack = "SQL Server, SSAS, SSRS" },
    { years = "2013", client = "UniSuper", work = "Integrated Sitecore with internal systems, enabling the launch of the customer-facing website", stack = "ASP.NET, WCF, Sitecore" },
    { years = "2012–13", client = "VivaTags", work = "Built front and back end for a mobile payments platform; co-inventor on its patent application", stack = "ASP.NET MVC, Azure, JavaScript" },
    { years = "2012", client = "Webjet", work = "Built the UI for one of the first Australian Windows 8 Store apps", stack = "C#, XAML" },
    { years = "2011", client = "Fiserv / Westpac", work = "Built a mobile single-page banking application", stack = "ASP.NET MVC, KnockoutJS" },
    { years = "2010–11", client = "Australian Taxation Office", work = "Led TFS adoption and built tooling to fit it into enterprise configuration management", stack = "C#, Java, TFS, Build Forge" },
    { years = "2010", client = "Australian Fisheries Management Authority", work = "Diagnosed performance problems, mentored staff, and planned the TFS rollout", stack = "VB.NET, Oracle, TFS" },
    { years = "2010", client = "COIN / Macquarie Bank", work = "Cut brokerage tracking queries from 4+ hours to under 10 seconds", stack = "ASP.NET, SQL Server" },
    { years = "2009", client = "Government of Vanuatu", work = "Redesigned the national budget management system and trained the onsite team", stack = "BIDS, C#, SQL Server" },
    { years = "2008", client = "Institut d'émission des départements d'outre-mer (IEDOM)", work = "Migrated BIDS to Oracle Database, rolled out budget entry, and trained partner consultants", stack = "BIDS, C#, Oracle Database" },
    { years = "2006", client = "ANU School of Biology", work = "Built software monitoring a microphone array to detect cricket signalling patterns", stack = "C#, WinForms, hardware I/O" },
    { years = "2005", client = "Australian Customs Service", work = "Extended the anti-dumping and countervailing case database", stack = "Access, VBA, SQL" },
    { years = "2004–05", client = "National Occupational Health and Safety Commission", work = "Built the Dangerous Goods Ready Reckoner placarding app", stack = "JavaScript, HTML" },
    { years = "2004", client = "Fisheries Research and Development Corporation", work = "Fixed and deployed the FishBase grant management system", stack = "Access, VBA, SQL" },
]
+++

Software engineer with 20+ years of experience across backend, platform, security, and developer
tooling. Built and operated authentication, authorization, and service-to-service security systems
at Amazon/AWS; shipped AI developer tooling on OpenAI's Codex; co-maintainer of
[Ratatui](https://ratatui.rs), the standard Rust terminal UI library. I
work best on systems other engineers depend on, where correctness, maintainability, and developer
experience all matter.

## Experience

### OpenAI (Codex)

<p class="resume-role">Member of Technical Staff · Oct 2025 – Mar 2026 · Seattle WA</p>

* Worked on Codex, OpenAI's AI coding agent, across the Rust terminal UI, auth/login, client
  connectivity, reliability, and developer workflow polish
* Owned major terminal UI improvements: transcript rendering, scrolling, copy/selection, paste
  handling, keyboard behavior, streaming performance, terminal compatibility, diagnostics, and
  multi-agent navigation
* Shipped custom CA support, logging, CI/Bazel reliability improvements, and snapshot-backed UI
  tests; regular issue triage, PR review, and technical interviewing

### Ratatui

<p class="resume-role">Open Source Maintainer · 2023 – Present · Seattle WA</p>

* Co-maintainer of Ratatui, the standard Rust terminal UI library: 23k+ GitHub stars, 70M+
  crates.io downloads, 6,900+ reverse dependencies, 15k+ dependent repositories (including OpenAI
  Codex)
* Day-to-day maintainer work: API design and review, contributor PR review, releases, issue
  triage, documentation and the ratatui.rs site, and community support
* Helped grow the contributor community and the maintainer team; maintain the crates Ratatui
  builds on (kasuari, instability, line-clipping)
* See [projects](/projects/) for the widgets, libraries, and tools around it

### Amazon and AWS

<p class="resume-role">Senior Software Development Engineer · 2017 – 2022 · Seattle WA</p>

* Tech lead for a new OAuth / OpenID Connect authentication and authorization service securing 80K+
  inter-service connections across 2.5M hosts at 15K TPS peak
* Maintained a rule-based access-control system governing 3M+ employees, 1M+ groups, and 2M+
  resources, plus a hierarchical resource-permissions service managing tens of millions of
  resources
* Provided critical feedback addressing security gaps in a draft IETF OAuth standard; performed
  security assessments of new and legacy systems
* 24/7 on-call and operations for three Tier-0 / Tier-1 internal systems; planned and executed
  peak-season operations to prevent overload and downtime
* Advised managers and directors on scoping, strategy, and risk; ran integration office hours,
  internal conference talks, and mentoring (2 intern conversions)

### Performa Software

<p class="resume-role">Senior Application Analyst · 2014 – 2016 · Nashville TN, Melbourne Australia</p>

* Lead developer delivering a budget entry, analysis, and reporting system
  (BEARS) managing the State of Tennessee's $32B annual budget;
  integrated with PeopleSoft commitment-control ledger APIs
* Bug fixes and features on a budget management system for the Victorian Department of Health and
  Human Services

### Readify

<p class="resume-role">Senior Developer · 2010 – 2014 · Canberra, Melbourne, Sydney Australia</p>

* Consulted on 30+ government and private projects: backend systems, enterprise integration
  (CRM/ERP/CMS/banking), performance work (cut a critical query from 4+ hours to <10s), and
  agile/devops training

### Earlier roles

<p class="resume-role">2001 – 2009 · Canberra Australia</p>

* Software development and consulting for Australian government and enterprise clients (Beacon IT,
  F1 Solutions, Pharmacy Guild of Australia)
* 24/7 managed security services operations: firewalls, VPNs, IDS (Citadel Securix)
* University IT class tutoring (University of Canberra)

## Skills

* **Languages:** Rust, Python, Java, C#/.NET, TypeScript/JavaScript, SQL, Shell
* **Security/Auth:** OAuth 2.x, OpenID Connect, JWT, TLS/mTLS, IAM, access control and
  authorization at scale, protocol/standards review
* **Platform:** AWS (IAM, DynamoDB, EC2, ECS, Lambda, S3), distributed systems, operations and
  on-call, CI/CD, Bazel, Docker, Linux
* **Developer tooling:** CLI/terminal applications, API design, documentation, OSS maintainership,
  contributor experience

## Education and recognition

* University of Canberra, 2000–2003: Bachelor of Engineering (Computer Engineering), incomplete;
  68 of 96 credit points, GPA 6.1/7.0
* Co-inventor, US patent application [US20140025512A1](https://patents.google.com/patent/US20140025512A1/en):
  Vendor portal and method of facilitating electronic commerce (VivaTags, 2014, abandoned)
* MCSD: Application Lifecycle Management (2014)
