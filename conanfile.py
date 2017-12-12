#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class OpenALConan(ConanFile):
    name = "openal"
    version = "1.18.2"
    url = "https://github.com/kcat/openal-soft.git"
    description = "A software implementation of the OpenAL 3D audio API."
    license = "https://github.com/kcat/openal-soft/blob/master/COPYING"
    exports_sources = ["CMakeLists.txt", "LICENSE"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        source_url = "https://github.com/kcat/openal-soft/archive"
        tools.get("{}/openal-soft-{}.tar.gz".format(source_url, self.version))
        os.system("ls")
        extracted_dir = "openal-soft-openal-soft-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include", src="sources/include")
        self.copy(pattern="*.hh", dst="include", src="sources/include")
        self.copy(pattern="*.hpp", dst="include", src="sources/include")
        with tools.chdir("sources"):
            self.copy(pattern="LICENSE")
            self.copy(pattern="*.dll", dst="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", keep_path=False)
            self.copy(pattern="*.a", dst="lib", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", keep_path=False)
            self.copy(pattern="*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if not self.options.shared:
            self.cpp_info.defines = ["FLAC__NO_DLL"]
