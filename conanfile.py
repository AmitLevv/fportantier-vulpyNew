from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps

class MyProjectConan(ConanFile):
    name = "MyProject"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"
    requires = [
    "boost/1.75.0",
    "fmt/7.1.3",  # Downgrade to 7.1.3
    "nlohmann_json/3.10.5",
    "spdlog/1.8.5"
]
    generators = "CMakeDeps", "CMakeToolchain"

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*my_project.lib", dst="lib", keep_path=False)