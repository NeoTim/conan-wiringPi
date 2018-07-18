from conans import ConanFile, tools


class WiringpiConan(ConanFile):
    name = "wiringPi"
    version = "2.46"
    license = "GNU LGPLv3"
    url = "https://git.drogon.net/?p=wiringPi;a=summary"
    author="Gordon Henderson <projects@drogon.net>"
    description = "WiringPi is a PIN based GPIO access library written in C. (for Raspberry Pi)"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [False]}
    default_options = "shared=False"
    generators = "compiler_args"

    def source(self):
        self.run("git clone git://git.drogon.net/wiringPi")
        self.run("cd wiringPi")


    def build(self):
        ### edit Makefile
        ## create Installation Dir
        self.run("mkdir -p %s/_install-tmp/include" % self.source_folder)
        self.run("mkdir -p %s/_install-tmp/lib" % self.source_folder)
        self.run("mkdir -p %s/_install-tmp/bin" % self.source_folder)
        self.run("mkdir -p %s/_install-tmp/src" % self.source_folder)

        ## change Destination Dir
        self.run("sed -i 's+PREFIX?=/local+PREFIX?=+g' %s" % (self.source_folder + "/wiringPi/wiringPi/Makefile"))
        self.run("sed -i 's+DESTDIR?=/usr+DESTDIR?=%s/_install-tmp+g' %s" % ((self.source_folder), (self.source_folder + "/wiringPi/wiringPi/Makefile")))

	## build wiringPi
        self.run("cd %s/wiringPi/wiringPi && make -j5 && make install" % self.source_folder)
	
    def package(self):
        self.copy("*.h", dst="include", src=self.source_folder+"/_install-tmp/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        ## License File
        self.copy("COPYING.LESSER", dst="license", ignore_case=True, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["wiringPi"]
