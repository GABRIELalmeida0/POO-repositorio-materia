import os

# Define the VM names
vm1_name = "VM1"
vm2_name = "VM2"

# Define the VM specifications
vm_memory = "1024"
vm_storage = "15"

# Create and configure the VMs using Vagrant
os.system(f"vagrant init ubuntu/bionic64")
os.system(f"vagrant box update")
os.system(f"vagrant up --provider virtualbox")

# Configure the VMs with the specified settings
os.system(f"vagrant ssh {vm1_name} -c 'sudo VBoxManage modifyvm {vm1_name} --memory {vm_memory}'")
os.system(f"vagrant ssh {vm1_name} -c 'sudo VBoxManage modifyvm {vm1_name} --hda {vm_storage}'")
os.system(f"vagrant ssh {vm2_name} -c 'sudo VBoxManage modifyvm {vm2_name} --memory {vm_memory}'")
os.system(f"vagrant ssh {vm2_name} -c 'sudo VBoxManage modifyvm {vm2_name} --hda {vm_storage}'")
