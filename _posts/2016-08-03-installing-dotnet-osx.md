---
layout: post
title:  "Installing .NET Core on OSX"
date:   2016-08-03 19:31:00 -0500
categories:
---

The easiest way to install [.NET Core](https://www.microsoft.com/net/core#macos)
on OSX is a little different than the way currently suggested on the official site. I suggest using [Homebrew](http://brew.sh), and [Homebrew Cask](http://caskroom.io).

## Instructions

If you have not already installed Homebrew, install it.
```console
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install dotnet using caskroom. This will also automatically install openssl if it's not already installed.
```console
$ brew update
$ brew tap caskroom/cask
$ brew cask install dotnet
```

By default, the installation of .NET Core links the crypto library to a folder location other than the Homebrew default. To fix the link to the openssl libraries run the following.
```console
$ sudo install_name_tool -add_rpath \
    $(brew --prefix openssl)/lib \
    /usr/local/share/dotnet/shared/Microsoft.NETCore.App/1.0.0/System.Security.Cryptography.Native.dylib
```

## Rationale

The [current installation instructions](https://www.microsoft.com/net/core#macos) suggest symlinking openssl libraries installed by Homebrew to `/usr/local/lib`. This approach is not the best, as it has the potential to cause security issues or cause software that's installed outside the Homebrew ecosystem to break. Previous instructions called on users to run `brew link openssl --force`, which Homebrew recently disabled specifically to avoid these issues.
