from traceback import format_exc
from logging import error
from conans import ConanFile, tools


class ConanConfiguration(ConanFile):
    name = "gtest"
    version = "1.11.0"
    settings = "arch", "os", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    def package_info(self):
        try:
            self.cpp_info.names["cmake_find_package"] = "GTest"
            self.cpp_info.libs = tools.collect_libs(self)
        except Exception as e:
            error(format_exc())
            raise e


if __name__ == "__main__":
    pass
