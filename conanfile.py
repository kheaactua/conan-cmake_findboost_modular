#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile


class CMakeFindboostModularConan(ConanFile):
    name = "cmake_findboost_modular"
    version = "0.1.1"
    url = "https://github.com/bincrafters/cmake_findboost_modular"
    description = "Enables use of Boost Modular Packages with traditional CMake FindBoost"
    license = "MIT"
    exports_sources = ["FindBoost.cmake", "LICENSE"]
        
    def package(self):
        self.copy("FindBoost.cmake")
