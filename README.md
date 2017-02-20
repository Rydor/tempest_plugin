**Description**

The purpose of these tests are to fill the gaps currently in RPC test coverage.

The resources to be validated include the following:
VMs

These tests are provided as a Tempest plugin, this way we can take advantage of all the features and capabilities of Tempest without having to merge these tests into the Tempest tree.


**Installation**

Install Tempest
Configure Tempest configuration file according to your OpenStack deployment
Clone the repository into the system where you installed Tempest: git clone https://github.com/Rydor/tempest_plugin.git
cd tempest_plugin
pip install -e .
To verify the installation was successfull, go to your tempest directory and run the following command:
ostestr --list | grep compute-create
You should see the list of tests from the plugin.


**Running the tests**

To create test resources run this command:
ostestr --regex compute-create
