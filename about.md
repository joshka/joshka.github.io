---
layout: page
title: About
permalink: /about/
---

{% capture my_include %}{% include about.md %}{% endcapture %}
{{ my_include | markdownify }}
