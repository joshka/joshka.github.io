+++
title = "app.config and Dev Prod Test databases"
date = "2006-09-05T17:19:00+10:00"
[taxonomies]
tags = ["Software"]
+++

In well designed enterprise apps, it is often the case that your application will run in multiple
environments, and against different databases (Development, Test, and Production). This can lead to
issues when it comes to storing connections strings.

<!-- more -->

Using Visual Studio 2003, there was an option to override your application config file as described
by [Stephen Chu's
post](http://stephenchu.blogspot.com/2005/05/dynamic-deployment-config-settings.html). I couldn't
get this setting to work in Visual Studio 2005, and I assume it is deprecated as MSDN the seems to
have very little documentation about the setting One way I managed to find around it is to add
something similar to the following in your .proj file (.csproj, .vbproj, ...)

```xml
<Project>
  ...
  <Import Project="$(MSBuildBinPath)\Microsoft.VisualBasic.targets" />
  <Target Name="BeforeBuild">
    <CreateProperty Value="app.debug.config" Condition=" ‘$(Configuration)|$(Platform)’ == ‘Dev|AnyCPU’ ">
      <Output TaskParameter="Value" PropertyName="AppConfig" />
    </CreateProperty>
    <CreateProperty Value="app.test.config" Condition="‘$(AppConfig)’==” and ‘$(Configuration)|$(Platform)’ == ‘Test|AnyCPU’ ">
      <Output TaskParameter="Value" PropertyName="AppConfig" />
    </CreateProperty>
    <CreateProperty Value="app.prod.config" Condition="‘$(AppConfig)’==” and ‘$(Configuration)|$(Platform)’ == ‘Prod|AnyCPU’ ">
      <Output TaskParameter="Value" PropertyName="AppConfig" />
    </CreateProperty>
    <CreateProperty Value="app.config" Condition="‘$(AppConfig)’==”">
      <Output TaskParameter="Value" PropertyName="AppConfig" />
    </CreateProperty>
  </Target>
</Project>
```

This basically sets the `$(AppConfig)` variable to something sane (depending on your chosen
configuration). When the `_CopyAppConfigFile` target (see Microsoft.Common.targets) runs it copies
this file to the output directory.

An alternative would be to write a new task to replace `_CopyAppConfigFile` and import it.
