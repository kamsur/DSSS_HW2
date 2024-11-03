from setuptools import setup

setup(
    name="math_quiz",
    version="0.0.1",
    author="Masudur Rahaman Kazi",
    license="Apache 2.0",
    url="https://github.com/kamsur/DSSS_HW2.git",
    packages=["math_quiz"],
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:math_quiz',
        ],
    },
)
