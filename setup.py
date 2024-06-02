from setuptools import setup, find_packages

setup(
        name='wallpaper-reddit',
        version='3.1.2',
        packages=find_packages(),
        url='https://www.github.com/markubiak/wallpaper-reddit',
        author='Mark Kubiak',
        author_email='mkubiak.dev@gmail.com',
        description='A utility that downloads wallpapers from reddit',
        install_requires=['Pillow>=10.0.0'],
        package_data={
            'wpreddit': ['fonts/*.otf', 'conf_files/*.conf', 'conf_files/*.desktop']
        },
        entry_points={
            'console_scripts': [
                'wallpaper-reddit = wpreddit.main:run'
            ]
        }
)
