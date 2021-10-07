from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration


class ConanConfiguration(ConanFile):
    name = "glm"
    version = "0.9.9.8"
    settings = {
        "arch": ["x86_64", "x86"],
        "os": ["Windows"],
        "compiler": {
            "Visual Studio": {
                "version": ["16"]
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
            and self.settings.build_type == "Release"
            and self.options.type == "interface"
        ):
            self.copy(src="glm/glm", pattern="*.*", dst="include/glm")
        elif (
            self.settings.arch == "x86_64"
            and self.settings.os == "Windows"
            and self.settings.compiler == "Visual Studio"
            and self.settings.compiler.version == 16
            and self.settings.build_type == "Release"
            and self.options.type == "interface"
        ):
            self.copy(src="glm/glm", pattern="*.*", dst="include/glm")
        else:
            raise ConanInvalidConfiguration(
                "Unsupported"
                + " 'self.settings.arch' = '" + str(self.settings.arch) + "'"
                + " 'self.settings.os' = '" + str(self.settings.os) + "'"
                + " 'self.settings.compiler' = '" + str(self.settings.compiler) + "'"
                + " 'self.settings.compiler.version' = '" + str(self.settings.compiler.version) + "'"
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
