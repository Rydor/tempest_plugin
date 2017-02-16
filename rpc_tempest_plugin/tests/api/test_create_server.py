from tempest.api.compute import base
from tempest import config
from tempest import test


class ComputeResouces(base.BaseV2ComputeTest):

    @test.attr(type='compute-create')
    def test_create_serv(self):
        server = self.create_test_server(validatable=True,
                                         wait_until='ACTIVE')
        self.assertTrue(server['id'])
