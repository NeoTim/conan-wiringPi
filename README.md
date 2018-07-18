# Conan wiringPi

[ ![Download](https://api.bintray.com/packages/l0nax/3rd-party/wiringPi/images/download.svg) ](https://bintray.com/l0nax/3rd-party/wiringPi/_latestVersion)

This is only the [Conan](https://conan.io) Package for the WiringPi **Library**!

I'm **not** the Developer of the [wiringPi](http://wiringpi.com/) Library.

[WiringPi Homepage](http://wiringpi.com/) <br/>
[WiringPi Git Repository](https://git.drogon.net/?p=wiringPi;a=summary)

[Conan wiringPi GitHub Repository](https://github.com/l0nax/conan-wiringPi)

## Basic Setup

```
$ conan install wiringPi/2.43@l0nax/3rd
```

## Project setup

If you handle multiple dependencies in your project is better to add a _conanfile.txt_

```
[requires]
wiringPi/2.43@l0nax/3rd

[options]
wiringPi:shared=False

[generators]
cmake
```

Complete the installation of requirements for your project running:

```
conan install .
```
