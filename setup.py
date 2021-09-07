import setuptools

setuptools.setup(
  name="jupyter-pycharm-server",
  # py_modules rather than packages, since we only have 1 file
  py_modules=['pycharm'],
  entry_points={
      'jupyter_serverproxy_servers': [
          # name = packagename:function_name
          'pycharm = pycharm:setup_pycharm',
      ]
  },
  packages=setuptools.find_packages(),
      keywords=['Jupyter'],
      classifiers=['Framework :: Jupyter'],
  install_requires=[
    'jupyter-server-proxy'
  ],
)