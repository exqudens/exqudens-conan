from os import path
from traceback import format_exc
from logging import error
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class ConanConfiguration(ConanFile):
    settings = {
        "arch": ["x86_64", "x86"],
        "os": ["Windows"],
        "compiler": {
            "Visual Studio": {
                "version": ["15", "16", "17"],
                "runtime": ["MD", "MT"]
            }
        },
        "build_type": ["Release"]
    }
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    def set_name(self):
        try:
            self.name = path.basename(path.dirname(path.dirname(path.abspath(__file__))))
        except Exception as e:
            error(format_exc())
            raise e

    def set_version(self):
        try:
            self.version = tools.load(path.join(path.dirname(path.abspath(__file__)), "version.txt")).strip()
        except Exception as e:
            error(format_exc())
            raise e

    def package(self):
        try:
            if (
                self.settings.arch == "x86"
                and self.settings.os == "Windows"
                and self.settings.compiler == "Visual Studio"
                and (
                        self.settings.compiler.version == 15
                        or self.settings.compiler.version == 16
                        or self.settings.compiler.version == 17
                )
                and self.settings.compiler.runtime == "MD"
                and self.settings.build_type == "Release"
                and self.options.shared
            ):
                self.copy(src="glfw-3.3.4.bin.WIN32/include", pattern="*.*", dst="include")
                self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3dll.lib", dst="lib")
                self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3.dll", dst="bin")
            elif (
                self.settings.arch == "x86"
                and self.settings.os == "Windows"
                and self.settings.compiler == "Visual Studio"
                and (
                        self.settings.compiler.version == 15
                        or self.settings.compiler.version == 16
                        or self.settings.compiler.version == 17
                )
                and self.settings.compiler.runtime == "MT"
                and self.settings.build_type == "Release"
                and not self.options.shared
            ):
                self.copy(src="glfw-3.3.4.bin.WIN32/include", pattern="*.*", dst="include")
                self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3_mt.lib", dst="lib")
            elif (
                self.settings.arch == "x86_64"
                and self.settings.os == "Windows"
                and self.settings.compiler == "Visual Studio"
                and (
                        self.settings.compiler.version == 15
                        or self.settings.compiler.version == 16
                        or self.settings.compiler.version == 17
                )
                and self.settings.compiler.runtime == "MD"
                and self.settings.build_type == "Release"
                and self.options.shared
            ):
                self.copy(src="glfw-3.3.4.bin.WIN64/include", pattern="*.*", dst="include")
                self.copy(src="glfw-3.3.4.bin.WIN64/lib-vc2019", pattern="glfw3dll.lib", dst="lib")
                self.copy(src="glfw-3.3.4.bin.WIN64/lib-vc2019", pattern="glfw3.dll", dst="bin")
            elif (
                self.settings.arch == "x86_64"
                and self.settings.os == "Windows"
                and self.settings.compiler == "Visual Studio"
                and (
                        self.settings.compiler.version == 15
                        or self.settings.compiler.version == 16
                        or self.settings.compiler.version == 17
                )
                and self.settings.compiler.runtime == "MT"
                and self.settings.build_type == "Release"
                and not self.options.shared
            ):
                self.copy(src="glfw-3.3.4.bin.WIN64/include", pattern="*.*", dst="include")
                self.copy(src="glfw-3.3.4.bin.WIN64/lib-vc2019", pattern="glfw3_mt.lib", dst="lib")
            else:
                raise ConanInvalidConfiguration(
                    "Unsupported"
                    + " 'self.settings.arch' = '" + str(self.settings.arch) + "'"
                    + " 'self.settings.os' = '" + str(self.settings.os) + "'"
                    + " 'self.settings.compiler' = '" + str(self.settings.compiler) + "'"
                    + " 'self.settings.compiler.version' = '" + str(self.settings.compiler.version) + "'"
                    + " 'self.settings.compiler.runtime' = '" + str(self.settings.compiler.runtime) + "'"
                    + " 'self.settings.build_type' = '" + str(self.settings.build_type) + "'"
                    + " 'self.options.type' = '" + str(self.options.shared) + "'"
                )
        except Exception as e:
            error(format_exc())
            raise e

    def package_info(self):
        try:
            self.cpp_info.libs = tools.collect_libs(self)
        except Exception as e:
            error(format_exc())
            raise e


if __name__ == "__main__":
    pass
