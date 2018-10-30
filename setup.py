from distutils.core import setup

setup(
    name='lrplots',
    version='0.4.1',
    author='Andy Hauser',
    author_email='Andreas.Hauser@LMU.de',
    scripts=['bin/lrplot'],
    url='https://github.com/ahcm/longread_plots',
    license='LICENSE',
    description='Plot collection for Long Read Sequencing',
    long_description='Plot collection for Long Read Sequencing like Oxford Nanopores',
    install_requires=[
        "matplotlib >= 2.2.0",
        "pandas >= 0.23.4",
        "seaborn >= 0.9.0",
    ],
)
