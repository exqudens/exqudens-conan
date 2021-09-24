from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class ConanConfiguration(ConanFile):
    name = "glfw"
    version = "3.3.4"
    settings = {
        "arch": ["x86_64", "x86"],
        "os": ["Windows"],
        "compiler": {
            "Visual Studio": {
                "version": ["16"],
                "runtime": ["MD", "MT"]
            }
        },
        "build_type": ["Release"]
    }
    options = {"type": ["interface", "static", "shared"]}

    def package(self):
        if (
            self.settings.arch == "x86"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "shared"
        ):
            self.copy(src="glfw-3.3.4.bin.WIN32/include", pattern="*.*", dst="include")
            self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3dll.lib", dst="lib")
            self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3.dll", dst="bin")
        elif (
            self.settings.arch == "x86"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MT"
            and self.settings.build_type == "Release"
            and self.options.type == "static"
        ):
            self.copy(src="glfw-3.3.4.bin.WIN32/include", pattern="*.*", dst="include")
            self.copy(src="glfw-3.3.4.bin.WIN32/lib-vc2019", pattern="glfw3_mt.lib", dst="lib")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MD"
            and self.settings.build_type == "Release"
            and self.options.type == "shared"
        ):
            self.copy(src="glfw-3.3.4.bin.WIN64/include", pattern="*.*", dst="include")
            self.copy(src="glfw-3.3.4.bin.WIN64/lib-vc2019", pattern="glfw3dll.lib", dst="lib")
            self.copy(src="glfw-3.3.4.bin.WIN64/lib-vc2019", pattern="glfw3.dll", dst="bin")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.compiler.runtime == "MT"
            and self.settings.build_type == "Release"
            and self.options.type == "static"
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
                + " 'self.options.type' = '" + str(self.options.type) + "'"
            )

    def package_info(self):
        if self.options.type == "interface":
            self.cpp_info.libs = []
        else:
            self.cpp_info.libs = tools.collect_libs(self)


if __name__ == "__main__":
    pass
