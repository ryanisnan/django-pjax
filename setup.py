try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='dj-pjax',
    version='1.0',
    description='An improvement of Django-PJAX: The Django helper for jQuery-PJAX.',
    license='BSD',
    url='https://github.com/eventials/django-pjax',
    author='Jacob Kaplan-Moss',
    author_email='jacob@jacobian.org',
    maintainer='Alexandre Vicenzi',
    maintainer_email='vicenzi.alexandre@gmail.com',
    py_modules=['djpjax'],
    install_requires=['django>=1.3'],
    keywords='django, PJAX',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
    ),
)
