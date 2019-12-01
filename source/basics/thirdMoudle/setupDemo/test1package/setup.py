from setuptools import setup, find_packages

# # 切到当前目录下,执行 python setup.py sdist
# setup(name='test_myDemo')


setup(
    name='msgboard',
    version='1.0.0',
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
