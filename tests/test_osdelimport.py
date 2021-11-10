
from pytest import raises
from osdelimport.main import osdelimportTest

def test_osdelimport():
    # test osdelimport without any subcommands or arguments
    with osdelimportTest() as app:
        app.run()
        assert app.exit_code == 0


def test_osdelimport_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with osdelimportTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_command1():
    # test command1 without arguments
    argv = ['command1']
    with osdelimportTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'bar'
        assert output.find('Foo => bar')


    # test command1 with arguments
    argv = ['command1', '--foo', 'not-bar']
    with osdelimportTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
        assert data['foo'] == 'not-bar'
        assert output.find('Foo => not-bar')
