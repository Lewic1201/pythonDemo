from setuptools import setup, find_packages


setup(
    name='msgboard',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    author='lewic',
    author_email='lpf1201@qq.com',
    entry_points="""
[console_scripts]
msgboard = messageboard.flasks:main
    """,
)
