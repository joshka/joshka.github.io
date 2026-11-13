+++
title = "Projects"
path = "projects"
template = "projects.html"
description = "Rust and terminal tools I build and maintain, led by Ratatui (70M+ downloads): widgets, betamax, jk, ratatui-diff, and more."

[extra]
og_image = "og/projects.png"

[extra.ratatui]
name = "Ratatui"
url = "https://ratatui.rs"
repo = "https://github.com/ratatui/ratatui"
crate = "ratatui"
summary = "Co-maintainer of the standard Rust terminal UI library."
intro = "I've worked on Ratatui since the 2023 fork from tui-rs."
highlights = [
    "Day-to-day maintainer work: API design and review, contributor PR review, releases, triage, docs, and community support.",
    "Designed much of the everyday API: Layout::areas, the Text, Line, and Span ergonomics, and ratatui::run.",
    "Built much of [ratatui.rs](https://ratatui.rs), and maintain the crates underneath: kasuari, instability, line-clipping.",
    "Started [tui-widgets](https://github.com/ratatui/tui-widgets) and the other widgets below.",
]

[[extra.groups]]
title = "Tools"
columns = 2
cards = [
    { name = "betamax", url = "/betamax/", repo = "https://github.com/joshka/betamax", crate = "betamax", summary = "Rust-first terminal capture for GIFs, screenshots, videos, and terminal snapshots." },
    { name = "jk", image = "captures/jk.png", url = "/jk/", repo = "https://github.com/joshka/jk", crate = "jk", summary = "A jj-native terminal UI for Jujutsu, with change selection and inline descriptions." },
    { name = "girt", image = "captures/girt.png", url = "/girt/", repo = "https://github.com/joshka/girt", crate = "girt", wip = true, summary = "An experimental Rust library for reading and writing Git repositories." },
    { name = "qwertty", image = "captures/qwertty.png", url = "/qwertty/", repo = "https://github.com/joshka/qwertty", crate = "qwertty", wip = true, summary = "Terminal application building blocks, and a conformance reference for terminal control sequences." },
]

[[extra.groups]]
title = "Ratatui widgets"
intro = "Most of these live in [tui-widgets](https://github.com/ratatui/tui-widgets), a collection I started and maintain under the Ratatui org. Each one is a separate crate."
cards = [
    { name = "ratatui-diff", url = "/ratatui-diff/", repo = "https://github.com/joshka/ratatui-diff", image = "https://github.com/joshka/ratatui-diff/releases/download/media-v1/split.png", summary = "A navigable unified and split diff widget for Ratatui." },
    { name = "tui-popup", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-popup", image = "https://vhs.charm.sh/vhs-q5Kz0QP3zmrBlQ6dofjMh.gif", summary = "A popup for Ratatui: centred, titled, and draggable." },
    { name = "tui-scrollview", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-scrollview", image = "https://vhs.charm.sh/vhs-6PuT3pdwSTp4aTvKrCBx9F.gif", summary = "A scrollable view for content larger than the screen." },
    { name = "tui-scrollbar", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-scrollbar", image = "https://vhs.charm.sh/vhs-21HzyozMOar6SYjVDBrpOb.gif", summary = "A scrollbar with fractional thumb rendering for smooth movement." },
    { name = "tui-big-text", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-big-text", image = "https://vhs.charm.sh/vhs-7DFJFGwBEnUjjLCFSqwEm9.gif", summary = "Large text built from font8x8 glyphs." },
    { name = "tui-prompts", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-prompts", image = "https://vhs.charm.sh/vhs-7gLcGtWJWDlQZqcMlhrpRG.gif", summary = "Interactive text, password, and confirmation prompts." },
    { name = "tui-qrcode", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-qrcode", image = "https://vhs.charm.sh/vhs-nUpcmCP1igCcGoJ5iio07.gif", summary = "QR codes rendered in the terminal." },
    { name = "tui-bar-graph", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-bar-graph", image = "https://vhs.charm.sh/vhs-1sx9Ht6NzU6e28Cl51jJVv.gif", summary = "Pretty bar graphs with braille, block, and gradient styles." },
    { name = "tui-cards", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-cards", image = "https://vhs.charm.sh/vhs-34mhPM1Juk2XnnLTGpOtE9.gif", summary = "Playing cards for card games in the terminal." },
    { name = "tui-box-text", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-box-text", image = "https://vhs.charm.sh/vhs-6ldj2r9v3mIaSzk8H7Jp8t.gif", summary = "Large text drawn with box-drawing characters." },
    { name = "tui-equalizer", repo = "https://github.com/ratatui/tui-widgets", crate = "tui-equalizer", image = "https://vhs.charm.sh/vhs-FiRQkkDAUEnH2BrPbUx5i.gif", summary = "An audio equalizer with multiple frequency bands." },
    { name = "tui-markdown", image = "captures/tui-markdown.png", repo = "https://github.com/joshka/tui-markdown", crate = "tui-markdown", summary = "Converts Markdown into styled Ratatui Text." },
]

[[extra.groups]]
title = "Libraries"
chips = ["instability", "kasuari", "line-clipping", "webfinger-rs", "detect-terminal", "askama-derive-axum"]

[[extra.groups]]
title = "Writing and practice"
cards = [
    { name = "Software Practices", image = "captures/practice.png", url = "/practice/", repo = "https://github.com/joshka/practice", summary = "Durable software-development preferences for code, docs, tests, review, and coding agents." },
    { name = "TidySrc", image = "captures/tidysrc.png", url = "/tidysrc/", repo = "https://github.com/joshka/tidysrc", summary = "Names recurring source-change problems and the patterns that address them." },
    { name = "cargo-manifesto", url = "/cargo-manifesto/", repo = "https://github.com/joshka/cargo-manifesto", crate = "cargo-manifesto", summary = "A satirical Cargo subcommand that writes down the principles behind every decision you already made." },
]
+++

Things I build and maintain, mostly in Rust and mostly for the terminal. Consulting work from 2004 to
2016 is on my [resume](/resume/#consulting-engagements).
