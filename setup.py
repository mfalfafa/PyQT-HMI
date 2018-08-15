from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
setup( 
  options = {         
    'py2exe' : {
        'excludes': excludes
        }
        },                   
  zipfile=None, 
  console = ['main.py'],
)