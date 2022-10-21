---
title:  "Installing .NET Core on OSX"
date:   2016-08-03 19:31:00 -0500
categories: software
---

**Note:** this post contains  outdated instructions for a problem that occurred installing .NET core on OSX in 2016. <https://github.com/dotnet/sdk/issues/4600> suggests that you can now install dotnet core on macOS by running `brew install dotnet`. The instructions at <https://learn.microsoft.com/en-us/dotnet/core/install/macos> are also worth reading rather than this post.

---

The easiest way to install [.NET Core](https://www.microsoft.com/net/core#macos)
on OSX is a little different than the way currently suggested at the official site.
I suggest using [Homebrew](http://brew.sh), and [Homebrew Cask](http://caskroom.io).

## Instructions

If you have not already installed Homebrew, install it.

```console
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install dotnet using caskroom. This will also automatically install openssl if
it's not already installed.

```console
$ brew update
$ brew tap caskroom/cask
$ brew cask install dotnet
```

Note: this will work completely once
[homebrew-cask#23854](https://github.com/caskroom/homebrew-cask/pull/23854) is
merged. Until then, follow the part of instructions that link the 1.0.0 versions
of openssl to your `/usr/local/lib` folder.

```console
$ ln -s /usr/local/opt/openssl/lib/libcrypto.1.0.0.dylib /usr/local/lib/
$ ln -s /usr/local/opt/openssl/lib/libssl.1.0.0.dylib /usr/local/lib/
```

**Update 2016-08-18:** replaced rpath with linking method
([diff](https://github.com/joshka/joshka.github.io/commit/fed667f640251b74a4cbb92d446136d75e3fe95e))
