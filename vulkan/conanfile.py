from os import path
from traceback import format_exc
from logging import error
from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
from conans.model.version import Version


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
            self.version = tools.load(path.join(path.dirname(path.dirname(path.abspath(__file__))), "version.txt")).strip()
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
                self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
                self.copy(src="1.2.182.0/Lib32", pattern="*.*", dst="lib")
                self.copy(src="1.2.182.0/Bin32", pattern="*.*", dst="bin")
                self.copy(src="1.2.182.0/Config", pattern="*.*", dst="config")
                self.copy(src="1.2.182.0/Tools32", pattern="*.*", dst="tools")
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
                self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
                self.copy(src="1.2.182.0/Lib32", pattern="*.*", dst="lib")
                self.copy(src="1.2.182.0/Bin32", pattern="*.*", dst="bin")
                self.copy(src="1.2.182.0/Config", pattern="*.*", dst="config")
                self.copy(src="1.2.182.0/Tools32", pattern="*.*", dst="tools")
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
                self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
                self.copy(src="1.2.182.0/Lib", pattern="*.*", dst="lib")
                self.copy(src="1.2.182.0/Bin", pattern="*.*", dst="bin")
                self.copy(src="1.2.182.0/Config", pattern="*.*", dst="config")
                self.copy(src="1.2.182.0/Tools", pattern="*.*", dst="tools")
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
                self.copy(src="1.2.182.0/Include", pattern="*.*", dst="include")
                self.copy(src="1.2.182.0/Lib", pattern="*.*", dst="lib")
                self.copy(src="1.2.182.0/Bin", pattern="*.*", dst="bin")
                self.copy(src="1.2.182.0/Config", pattern="*.*", dst="config")
                self.copy(src="1.2.182.0/Tools", pattern="*.*", dst="tools")
            else:
                raise ConanInvalidConfiguration(
                    "Unsupported"
                    + " 'self.settings.arch' = '" + str(self.settings.arch) + "'"
                    + " 'self.settings.os' = '" + str(self.settings.os) + "'"
                    + " 'self.settings.compiler' = '" + str(self.settings.compiler) + "'"
                    + " 'self.settings.compiler.version' = '" + str(self.settings.compiler.version) + "'"
                    + " 'self.settings.compiler.runtime' = '" + str(self.settings.compiler.runtime) + "'"
                    + " 'self.settings.build_type' = '" + str(self.settings.build_type) + "'"
                    + " 'self.options.shared' = '" + str(self.options.shared) + "'"
                )
        except Exception as e:
            error(format_exc())
            raise e

    def package_info(self):
        try:
            self.cpp_info.libs = ["vulkan-1.lib"]
        except Exception as e:
            error(format_exc())
            raise e


if __name__ == "__main__":
    pass
