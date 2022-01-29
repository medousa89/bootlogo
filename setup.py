from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-extensions-bootlogo-all',
		version='1.0',
		author='new',
		package_dir={'Extensions.BootlogoALL': 'src'},
		packages=['Extensions.BootlogoALL'],
		package_data={'Extensions.BootlogoALL': ['logos/*.mvi', 'preview/*.png', 'images/*.png', '*.png', 'locale/*/LC_MESSAGES/*.mo']},
		description='bootlogo',
		cmdclass=setup_translate.cmdclass,
	)
