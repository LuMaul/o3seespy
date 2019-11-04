import openseespy.opensees as opy
from collections import OrderedDict


class OpenseesInstance(object):
    n_node = 0
    n_con = 0
    n_ele = 0
    n_mat = 0
    n_sect = 0
    n_tseries = 0
    n_pat = 0
    n_fix = 0
    n_integ = 0
    n_transformation = 0

    def __init__(self, dimensions: int, node_dofs=3, state=0):
        self.dimensions = dimensions
        self._state = state  # 0=execute line by line, 1=export to raw openseespy, 2=export reloadable json
        opy.wipe()
        opy.model('basic', '-ndm', dimensions, '-ndf', node_dofs)  # 2 dimensions, 3 dof per node
        self.commands = []
        self.dict = OrderedDict()
        if state == 1:
            self.commands.append('opy.wipe()')
            self.commands.append("opy.model('basic', '-ndm', {0}, '-ndf', {1})".format(dimensions, node_dofs))
        if state == 2:
            self.dict['ndm'] = dimensions
            self.dict['ndf'] = node_dofs
            # base_types = ['node', 'element', 'section', 'uniaxial_material']
        elif state == 3:
            self.commands.append('opy.wipe()')
            self.commands.append("opy.model('basic', '-ndm', {0}, '-ndf', {1})".format(dimensions, node_dofs))

    def to_commands(self, os_command):
        self.commands.append(os_command)

    def to_dict(self, os_model):
        if os_model.op_type not in self.dict:
            self.dict[os_model.op_type] = OrderedDict()
        self.dict[os_model.op_type][os_model.tag] = os_model.to_dict()

    @property
    def state(self):
        return self._state

