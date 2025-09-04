from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

with open("requirements.txt") as arq:
    requirements = arq.read().splitlines()

setup(
    name='flavim_image_processing',
    version='0.0.1',
    license='MIT License',
    author='FlaviodosSantos',
    author_email='flaviovorthrox@yahoo.com.br',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/FlaviodosSantos/image-processing-package/tree/meu_package',
    description=u'Processar imagens usando scikit-image',
    packages=find_packages(),
    install_requires=requirements,
)