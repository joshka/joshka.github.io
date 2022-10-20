---
layout: post
title:  Detecting and Preventing Corrupt Software Downloads
date:   2010-04-30 11:33:00 +1000
categories:
---

In the past I and several of my colleagues have run into problems when attempting to install software downloaded from the [MSDN Subscriber Downloads](http://msdn.microsoft.com/en-us/subscriptions/downloads/default.aspx) or elsewhere. One possible cause for this is file corruption either due to an incomplete download, or caused later when copying the file to another device (e.g. over a local network or via flaky USB drives). This problem is easy to detect and prevent.

1. Install the [HashCheck Shell Extension](http://code.kliu.org/hashcheck/) by [Kai Liu](http://www.kailiu.com/). There are other options for hash checking programs, but this one works well enough.

1. On the download page for the file, copy the SHA1 hash. For MSDN downloads this can be found by expanding the Details View link.

1. In Windows Explorer open the Properties dialog for the file that you downloaded. Click on the new **Checksums** tab. HashCheck will calculate the various checksums of the file.

1. Paste the hash into the text box on the **Checksums** tab and ensure that the SHA1 line is highlighted to indicate that the values match.

1. Click **Save** to create a new .sha1 file beside the downloaded file that contains this calculated and checked hash. You can double click this file to check whether the file has changed since you downloaded it. Do this whenever you transfer the file on to another device (e.g. network, DVD, USB) to prevent file corruption causing installation failures.
