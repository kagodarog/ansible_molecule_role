import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('pkg', [
  'nginx',
  'mariadb-server',
  'php-fpm'
])
def test_pkg(host, pkg):
    package = host.package(pkg)

    assert package.is_installed

@pytest.mark.parametrize('svc', [
  'nginx',
  'mariadb',
  'php8.1-fpm'
])
def test_svc(host, svc):
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled